"""実行結果の保存・読み出し。

1行1応募の JSONL。応募の原文・訳文・判定の生値をすべて残す。
「なぜこの作品が一次で落ちたのか」を後から説明できる必要があるため、
要約した形では保存しない。
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Iterator

from .models import Assessment, Entry, Usage


def _assessment_from_json(d: dict[str, Any]) -> Assessment:
    a = Assessment(entry_id=d.get("entry_id", ""))
    a.eligibility = {k: float(v) for k, v in (d.get("eligibility") or {}).items()}
    a.category = d.get("category", "")
    a.category_confidence = float(d.get("category_confidence", 0.0))
    a.category_probabilities = {
        k: float(v) for k, v in (d.get("category_probabilities") or {}).items()
    }
    a.scores = {k: float(v) for k, v in (d.get("scores") or {}).items()}
    a.score_confidence = {k: float(v) for k, v in (d.get("score_confidence") or {}).items()}
    a.total = float(d.get("total", 0.0))
    a.decision = d.get("decision", "REVIEW")
    a.reasons = list(d.get("reasons") or [])
    a.error = d.get("error", "")
    for key, attr in (("claude_usage", "claude_usage"), ("typesafe_usage", "typesafe_usage")):
        u = d.get(key) or {}
        setattr(a, attr, Usage(int(u.get("input_tokens", 0)), int(u.get("output_tokens", 0))))
    return a


def _entry_from_json(d: dict[str, Any]) -> Entry:
    return Entry(
        entry_id=d.get("entry_id", ""),
        fields={k: str(v) for k, v in (d.get("fields") or {}).items()},
        source_language=d.get("source_language", ""),
        translations={
            lang: {k: str(v) for k, v in fields.items()}
            for lang, fields in (d.get("translations") or {}).items()
        },
        ingest_warnings=list(d.get("ingest_warnings") or []),
    )


def save_run(path: str | Path, pairs: list[tuple[Entry, Assessment]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for entry, a in pairs:
            fh.write(
                json.dumps(
                    {"entry": asdict(entry), "assessment": a.to_json()}, ensure_ascii=False
                )
                + "\n"
            )


def load_run(path: str | Path) -> list[tuple[Entry, Assessment]]:
    out: list[tuple[Entry, Assessment]] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        out.append((_entry_from_json(rec["entry"]), _assessment_from_json(rec["assessment"])))
    return out


def iter_run(path: str | Path) -> Iterator[tuple[Entry, Assessment]]:
    yield from load_run(path)
