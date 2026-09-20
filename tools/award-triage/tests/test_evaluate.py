"""効果測定の計算のテスト。

取りこぼし率を過小に出す実装は、この仕組みで一番危険なバグなので
そこを重点的に押さえる。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from award_triage.config import Gates, load_rubric  # noqa: E402
from award_triage.evaluate import (  # noqa: E402
    GoldenRow, gate_stats, normalize_decision, pearson, spearman,
)
from award_triage.models import Assessment, Entry, SHORTLIST  # noqa: E402

RUBRIC = load_rubric()


def pair(eid: str, total: float, decision_ready: bool = True) -> tuple[Entry, Assessment]:
    a = Assessment(entry_id=eid)
    a.eligibility = {c.id: 0.99 for c in RUBRIC.eligibility}
    a.category = "still_image"
    a.category_confidence = 0.9
    conf = 0.9 if decision_ready else 0.1
    a.scores = {ax.id: total for ax in RUBRIC.scores}
    a.score_confidence = {ax.id: conf for ax in RUBRIC.scores}
    a.total = RUBRIC.weighted_total(a.scores)
    return Entry(entry_id=eid, fields={}), a


def test_spearman_is_rank_based():
    # 単調だが非線形な関係。順位相関は 1.0 になる。
    xs = [1.0, 2.0, 3.0, 4.0]
    ys = [1.0, 4.0, 9.0, 16.0]
    assert abs(spearman(xs, ys) - 1.0) < 1e-9
    assert pearson(xs, ys) < 1.0


def test_spearman_handles_ties_and_constants():
    assert spearman([1.0, 1.0, 1.0], [1.0, 2.0, 3.0]) is None  # 定数は相関なし
    assert spearman([1.0], [1.0]) is None


def test_false_reject_is_counted():
    """人間が通した作品を機械が自動で落としたら、取りこぼしとして数える。"""
    pairs = [pair("A", 0.2), pair("B", 0.3)]
    golden = {
        "A": GoldenRow("A", decision=SHORTLIST),   # 人間は通した
        "B": GoldenRow("B", decision="REJECT"),
    }
    g = Gates(**{**RUBRIC.gates.__dict__, "auto_reject_below": 1.0})
    st = gate_stats(pairs, golden, RUBRIC, g)
    assert st.automated == 2
    assert st.automated_checked == 2
    assert st.false_reject == 1
    assert abs(st.false_reject_rate - 0.5) < 1e-9


def test_review_entries_are_not_counted_as_errors():
    """人間に回したものは、人間の判定と違っても誤りではない。"""
    pairs = [pair("A", 3.0, decision_ready=False)]
    golden = {"A": GoldenRow("A", decision="REJECT")}
    st = gate_stats(pairs, golden, RUBRIC, RUBRIC.gates)
    assert st.review == 1
    assert st.automated_checked == 0
    assert st.false_reject_rate == 0.0
    assert st.automation_rate == 0.0


def test_unlabelled_entries_do_not_inflate_accuracy():
    pairs = [pair("A", 3.0), pair("B", 3.0)]
    golden = {"A": GoldenRow("A", decision=SHORTLIST)}  # B は人間未採点
    g = Gates(**{**RUBRIC.gates.__dict__, "shortlist_above": 2.0})
    st = gate_stats(pairs, golden, RUBRIC, g)
    assert st.automated == 2
    assert st.automated_checked == 1  # 突合できたのは1件だけ


def test_decision_aliases():
    assert normalize_decision("通過") == "SHORTLIST"
    assert normalize_decision("×") == "REJECT"
    assert normalize_decision("失格") == "INELIGIBLE"
    assert normalize_decision("") == ""
