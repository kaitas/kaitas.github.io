"""応募データの取り込みと正規化。

エントリーポータルの出力形式が確定していないので、CSV / JSONL のどちらでも
受け、カラム名は config/fields.yaml のマッピングで吸収する。
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

from .config import FieldMap
from .models import Entry

# 言語判定：Unicode ブロックで十分に分かるものだけ機械判定し、
# ラテン文字圏（en/fr/es/pt）は区別せず "latin" として翻訳モデルに委ねる。
_HIRAGANA_KATAKANA = re.compile(r"[぀-ヿ]")
_HANGUL = re.compile(r"[가-힯ᄀ-ᇿ]")
_CJK = re.compile(r"[一-鿿]")


def detect_language(text: str) -> str:
    """ざっくりした言語判定。確信が持てなければ空文字を返す。"""
    if not text.strip():
        return ""
    if _HANGUL.search(text):
        return "ko"
    if _HIRAGANA_KATAKANA.search(text):
        return "ja"
    if _CJK.search(text):
        # ひらがな・カタカナが無い漢字のみのテキストは中国語とみなす。
        return "zh"
    if re.search(r"[A-Za-z]", text):
        return "latin"  # en/fr/es/pt の区別は翻訳側で行う
    return ""


def _read_rows(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() in (".jsonl", ".ndjson"):
        rows = []
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{i}: JSON として読めません: {exc}") from exc
        return rows
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError(f"{path}: トップレベルが配列ではありません")
        return data
    # CSV。BOM 付き Excel 出力を想定して utf-8-sig で開く。
    with path.open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def load_entries(path: str | Path, fieldmap: FieldMap) -> list[Entry]:
    path = Path(path)
    rows = _read_rows(path)
    entries: list[Entry] = []
    seen: dict[str, int] = {}

    for i, row in enumerate(rows, 1):
        warnings: list[str] = []
        fields = {name: fieldmap.pick(row, name) for name in fieldmap.mapping}

        entry_id = fields.get("entry_id") or ""
        if not entry_id:
            entry_id = f"row-{i}"
            warnings.append("entry_id が空だったので行番号を割り当てた")
        if entry_id in seen:
            warnings.append(f"entry_id が重複（{seen[entry_id]} 行目と同じ）")
            entry_id = f"{entry_id}#{i}"
        seen[entry_id] = i

        lang = fields.get("language") or ""
        if lang not in (None, ""):
            lang = lang.strip().lower()[:2]
        if not lang:
            lang = detect_language(
                " ".join(fields.get(f, "") for f in ("title", "description", "ai_usage"))
            )
            if not lang:
                warnings.append("言語を判定できなかった")

        for required in ("title", "description", "url"):
            if not fields.get(required):
                warnings.append(f"{required} が空")

        entries.append(
            Entry(entry_id=entry_id, fields=fields, source_language=lang, ingest_warnings=warnings)
        )

    if not entries:
        print(f"警告: {path} から応募が1件も読めませんでした", file=sys.stderr)
    return entries
