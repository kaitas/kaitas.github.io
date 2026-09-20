"""取り込み -> 翻訳 -> 判定 -> 振り分け の一本のパイプライン。"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from typing import Callable

from .config import FieldMap, Rubric
from .gate import decide
from .models import Assessment, Entry, Usage
from .typesafe import TypeSafeClient, TypeSafeError, build_questions, parse_answers


def assess_entry(
    entry: Entry,
    rubric: Rubric,
    fieldmap: FieldMap,
    client: TypeSafeClient,
    questions: dict,
) -> Assessment:
    a = Assessment(entry_id=entry.entry_id)

    state = entry.text_for(rubric.canonical_language, fieldmap.judge_fields)
    if not state.strip():
        a.error = "審査に渡せる本文が空"
        a.decision, a.reasons = "REVIEW", [a.error]
        return a

    try:
        answers, usage = client.ask(state, questions)
    except TypeSafeError as exc:
        a.error = str(exc)
        a.decision, a.reasons = "REVIEW", [f"判定に失敗: {exc}"]
        return a

    a.typesafe_usage = usage
    parsed = parse_answers(answers, rubric)
    a.eligibility = parsed["eligibility"]
    a.category = parsed["category"]
    a.category_confidence = parsed["category_confidence"]
    a.category_probabilities = parsed["category_probabilities"]
    a.scores = parsed["scores"]
    a.score_confidence = parsed["score_confidence"]
    a.total = rubric.weighted_total(a.scores)

    if parsed["missing"]:
        a.error = f"回答が欠落: {', '.join(parsed['missing'])}"

    a.decision, a.reasons = decide(a, rubric, rubric.gates, entry.fields.get("category", ""))
    return a


def screen_all(
    entries: list[Entry],
    rubric: Rubric,
    fieldmap: FieldMap,
    client: TypeSafeClient,
    *,
    max_workers: int = 8,
    progress: Callable[[int, int], None] | None = None,
) -> tuple[list[Assessment], Usage]:
    questions = build_questions(rubric)
    total_usage = Usage()

    def run(entry: Entry) -> Assessment:
        return assess_entry(entry, rubric, fieldmap, client, questions)

    results: list[Assessment] = []
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        for i, a in enumerate(pool.map(run, entries), 1):
            results.append(a)
            total_usage.add(a.typesafe_usage)
            if progress:
                progress(i, len(entries))
    return results, total_usage
