"""パイプラインを流れるデータ構造。"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any

# 振り分け先
SHORTLIST = "SHORTLIST"        # 自動で通過（二次審査へ）
REJECT = "REJECT"              # 自動で不通過
INELIGIBLE = "INELIGIBLE"      # 応募資格を満たさない
REVIEW = "REVIEW"              # 人間が見る
DECISIONS = (SHORTLIST, REVIEW, REJECT, INELIGIBLE)

#: 機械が確定してよい判定（= 人間の手を離れるもの）
AUTOMATED = (SHORTLIST, REJECT, INELIGIBLE)


@dataclass
class Entry:
    """正規化された応募1件。"""

    entry_id: str
    fields: dict[str, str]                     # 原文
    source_language: str = ""
    translations: dict[str, dict[str, str]] = field(default_factory=dict)  # lang -> {field: text}
    ingest_warnings: list[str] = field(default_factory=list)

    def text_for(self, lang: str, judge_fields: list[str]) -> str:
        """審査に投入する本文を1つのテキストに組み立てる。

        judge_fields に無いフィールド（氏名・連絡先など）は決して含めない。
        """
        src = self.translations.get(lang, self.fields)
        lines = []
        for f in judge_fields:
            value = src.get(f) or self.fields.get(f, "")
            if value:
                lines.append(f"{f}: {value}")
        return "\n".join(lines)


@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0

    def add(self, other: "Usage") -> None:
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens


@dataclass
class Assessment:
    """1件分の機械判定の結果。監査できるよう全ての生値を残す。"""

    entry_id: str
    eligibility: dict[str, float] = field(default_factory=dict)          # id -> noul
    category: str = ""
    category_confidence: float = 0.0
    category_probabilities: dict[str, float] = field(default_factory=dict)
    scores: dict[str, float] = field(default_factory=dict)               # axis id -> score
    score_confidence: dict[str, float] = field(default_factory=dict)
    total: float = 0.0
    decision: str = REVIEW
    reasons: list[str] = field(default_factory=list)
    claude_usage: Usage = field(default_factory=Usage)
    typesafe_usage: Usage = field(default_factory=Usage)
    error: str = ""

    def to_json(self) -> dict[str, Any]:
        return asdict(self)
