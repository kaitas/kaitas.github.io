"""国際言語サポート：応募を審査員の言語へ正規化する。

方針:
  * 原文は決して捨てない。翻訳は常に「添える」もの。
  * 判定 (TypeSafe) に渡すのは canonical 言語の1本に固定する。原文の言語ごとに
    判定の当たり外れが変わると、公平性の説明ができなくなるため。
  * 固有名詞・ツール名・モデル名は訳さない。審査員はそこを手掛かりに読む。
"""

from __future__ import annotations

import json
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable

import anthropic

from .config import FieldMap, Rubric
from .models import Entry, Usage

# 既定は最上位モデル。コストを優先するなら CLI の --translate-model で
# claude-sonnet-5 / claude-haiku-4-5 に落とせる（README のコスト表を参照）。
DEFAULT_MODEL = "claude-opus-5"

LANG_NAMES = {
    "ja": "Japanese",
    "en": "English",
    "ko": "Korean",
    "zh": "Chinese",
    "fr": "French",
    "es": "Spanish",
    "pt": "Portuguese",
    "latin": "a Latin-script language (English, French, Spanish or Portuguese)",
}

SYSTEM = """\
You translate award entry submissions for a panel of judges.

Rules:
- Translate meaning, not words. The judges decide on the substance of the work.
- Do NOT translate: proper nouns, work titles' original forms, artist names,
  AI tool and model names, URLs, hashtags, or code.
- Do NOT summarise, improve, or editorialise. If the original is vague, the
  translation is vague. If a claim is unsupported, keep it unsupported.
- Do NOT add anything not in the original.
- If a field is already in the target language, return it unchanged.
- Return the source language you detected as a two-letter ISO 639-1 code.
"""

_TOOL = {
    "name": "emit_translation",
    "description": "Return the detected source language and the translated fields.",
    "strict": True,
    "input_schema": {
        "type": "object",
        "properties": {
            "source_language": {
                "type": "string",
                "description": "ISO 639-1 code of the original text, e.g. 'ja', 'ko', 'pt'.",
            },
            "fields": {
                "type": "object",
                "description": "Translated text, keyed by the same field names as the input.",
                "additionalProperties": {"type": "string"},
            },
        },
        "required": ["source_language", "fields"],
        "additionalProperties": False,
    },
}


class Translator:
    def __init__(
        self,
        rubric: Rubric,
        fieldmap: FieldMap,
        *,
        model: str = DEFAULT_MODEL,
        api_key: str | None = None,
        max_workers: int = 8,
    ) -> None:
        self.rubric = rubric
        self.fieldmap = fieldmap
        self.model = model
        self.max_workers = max_workers
        # api_key を渡さない場合、SDK が環境変数と `ant auth login` の
        # プロファイルを順に見る。ここで空チェックはしない。
        self.client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()

    def _targets(self, entry: Entry) -> list[str]:
        """この応募に対して生成すべき訳の言語。"""
        wanted = set(self.rubric.judge_languages) | {self.rubric.canonical_language}
        # 原文と同じ言語は訳さない（原文をそのまま使う）
        return sorted(w for w in wanted if w != entry.source_language)

    def translate_entry(self, entry: Entry) -> Usage:
        usage = Usage()
        payload = {
            f: entry.fields.get(f, "")
            for f in self.fieldmap.translate_fields
            if entry.fields.get(f)
        }
        if not payload:
            return usage

        for target in self._targets(entry):
            src = LANG_NAMES.get(entry.source_language, "an unknown language")
            dst = LANG_NAMES.get(target, target)
            try:
                resp = self.client.messages.create(
                    model=self.model,
                    max_tokens=8000,
                    system=SYSTEM,
                    # 翻訳は思考を深める仕事ではない。thinking は既定のまま
                    # (adaptive) にして effort を下げるのが推奨される形。
                    output_config={"effort": "low"},
                    tools=[_TOOL],
                    tool_choice={"type": "tool", "name": "emit_translation"},
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Source language: {src}. Target language: {dst}.\n"
                                "Translate every value in this JSON object.\n\n"
                                + json.dumps(payload, ensure_ascii=False, indent=2)
                            ),
                        }
                    ],
                )
            except anthropic.APIError as exc:
                entry.ingest_warnings.append(f"{target} への翻訳に失敗: {exc}")
                continue

            usage.add(Usage(resp.usage.input_tokens, resp.usage.output_tokens))

            if resp.stop_reason == "refusal":
                entry.ingest_warnings.append(f"{target} への翻訳が拒否された（要目視）")
                continue

            block = next((b for b in resp.content if b.type == "tool_use"), None)
            if block is None:
                entry.ingest_warnings.append(f"{target} への翻訳結果が空だった")
                continue

            data = block.input if isinstance(block.input, dict) else {}
            translated = data.get("fields") or {}
            if not entry.source_language or entry.source_language == "latin":
                detected = str(data.get("source_language", "")).lower()[:2]
                if detected:
                    entry.source_language = detected
            # 訳されなかったフィールドは原文で埋める（審査員に空欄を見せない）
            merged = dict(entry.fields)
            merged.update({k: str(v) for k, v in translated.items() if v})
            entry.translations[target] = merged

        return usage

    def translate_all(self, entries: Iterable[Entry], progress=None) -> Usage:
        total = Usage()
        entries = list(entries)
        with ThreadPoolExecutor(max_workers=self.max_workers) as pool:
            for i, usage in enumerate(pool.map(self.translate_entry, entries), 1):
                total.add(usage)
                if progress:
                    progress(i, len(entries))
        return total
