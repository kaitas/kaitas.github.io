"""ルーブリックとフィールドマッピングの読み込み。"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

DEFAULT_CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


@dataclass
class ScoreAxis:
    id: str
    label: str
    weight: float
    instructions: str
    criteria: list[str]

    @property
    def max_score(self) -> float:
        return float(len(self.criteria) - 1)


@dataclass
class EligibilityCheck:
    id: str
    label: str
    instructions: str


@dataclass
class Gates:
    eligibility_fail_below: float = 0.15
    eligibility_pass_above: float = 0.85
    min_score_confidence: float = 0.55
    min_category_confidence: float = 0.50
    flag_category_mismatch: bool = True
    shortlist_above: float = -1.0
    auto_reject_below: float = -1.0


@dataclass
class Pricing:
    usd_jpy: float = 155.0
    claude_input_per_mtok: float = 2.0
    claude_output_per_mtok: float = 10.0
    typesafe_input_per_mtok: float = 0.0
    typesafe_output_per_mtok: float = 0.0
    human_minutes_per_entry: float = 6.0
    human_hourly_jpy: float = 5000.0

    @property
    def typesafe_priced(self) -> bool:
        return self.typesafe_input_per_mtok > 0 or self.typesafe_output_per_mtok > 0


@dataclass
class Rubric:
    version: int
    award: str
    accepted_languages: list[str]
    judge_languages: list[str]
    canonical_language: str
    eligibility: list[EligibilityCheck]
    categories: dict[str, str]
    scores: list[ScoreAxis]
    gates: Gates
    pricing: Pricing
    warnings: list[str] = field(default_factory=list)

    @property
    def max_total(self) -> float:
        """重み付き合計の理論最大値。"""
        return sum(a.weight * a.max_score for a in self.scores)

    def weighted_total(self, per_axis: dict[str, float]) -> float:
        return sum(a.weight * per_axis.get(a.id, 0.0) for a in self.scores)


def _require(d: dict[str, Any], key: str, where: str) -> Any:
    if key not in d:
        raise ValueError(f"{where}: 必須キー '{key}' がありません")
    return d[key]


def load_rubric(path: str | os.PathLike[str] | None = None) -> Rubric:
    p = Path(path) if path else DEFAULT_CONFIG_DIR / "rubric.yaml"
    raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    warnings: list[str] = []

    langs = raw.get("languages", {})
    axes: list[ScoreAxis] = []
    for a in _require(raw, "scores", str(p)):
        criteria = list(_require(a, "criteria", "scores[]"))
        if len(criteria) < 2:
            raise ValueError(f"scores[{a.get('id')}]: criteria は2段階以上必要です")
        axes.append(
            ScoreAxis(
                id=_require(a, "id", "scores[]"),
                label=a.get("label", a["id"]),
                weight=float(a.get("weight", 1.0)),
                instructions=_require(a, "instructions", "scores[]"),
                criteria=criteria,
            )
        )

    total_weight = sum(a.weight for a in axes)
    if total_weight <= 0:
        raise ValueError("scores[].weight の合計が 0 です")
    if abs(total_weight - 1.0) > 1e-6:
        warnings.append(
            f"scores[].weight の合計が {total_weight:.3f} でした。1.0 に正規化して計算します。"
        )
        for a in axes:
            a.weight /= total_weight

    categories = dict(_require(raw, "categories", str(p)))
    if len(categories) < 2:
        raise ValueError("categories は2件以上必要です")

    return Rubric(
        version=int(raw.get("version", 0)),
        award=raw.get("award", ""),
        accepted_languages=list(langs.get("accepted", ["ja", "en"])),
        judge_languages=list(langs.get("judge", ["ja", "en"])),
        canonical_language=str(langs.get("canonical", "en")),
        eligibility=[
            EligibilityCheck(
                id=_require(e, "id", "eligibility[]"),
                label=e.get("label", e["id"]),
                instructions=_require(e, "instructions", "eligibility[]"),
            )
            for e in raw.get("eligibility", [])
        ],
        categories=categories,
        scores=axes,
        gates=Gates(**(raw.get("gates") or {})),
        pricing=Pricing(**(raw.get("pricing") or {})),
        warnings=warnings,
    )


@dataclass
class FieldMap:
    mapping: dict[str, list[str]]
    judge_fields: list[str]
    translate_fields: list[str]

    def pick(self, row: dict[str, Any], internal: str) -> str:
        """入力行から内部フィールド名に対応する値を取り出す。"""
        for candidate in self.mapping.get(internal, []):
            if candidate in row and row[candidate] not in (None, ""):
                return str(row[candidate]).strip()
        return ""


def load_fieldmap(path: str | os.PathLike[str] | None = None) -> FieldMap:
    p = Path(path) if path else DEFAULT_CONFIG_DIR / "fields.yaml"
    raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    mapping = {k: (v if isinstance(v, list) else [v]) for k, v in raw["mapping"].items()}
    return FieldMap(
        mapping=mapping,
        judge_fields=list(raw.get("judge_fields", list(mapping))),
        translate_fields=list(raw.get("translate_fields", [])),
    )
