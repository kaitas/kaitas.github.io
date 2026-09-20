"""振り分けロジックのテスト。ここが壊れると審査結果が壊れる。"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from award_triage.config import Gates, load_rubric  # noqa: E402
from award_triage.gate import decide  # noqa: E402
from award_triage.models import Assessment, INELIGIBLE, REJECT, REVIEW, SHORTLIST  # noqa: E402

RUBRIC = load_rubric()


def good(**over) -> Assessment:
    """すべての条件を満たす、満点に近い判定結果。"""
    a = Assessment(entry_id="X")
    a.eligibility = {c.id: 0.98 for c in RUBRIC.eligibility}
    a.category = "still_image"
    a.category_confidence = 0.9
    a.scores = {ax.id: 3.0 for ax in RUBRIC.scores}
    a.score_confidence = {ax.id: 0.9 for ax in RUBRIC.scores}
    a.total = RUBRIC.weighted_total(a.scores)
    for k, v in over.items():
        setattr(a, k, v)
    return a


def gates(**over) -> Gates:
    return Gates(**{**RUBRIC.gates.__dict__, **over})


def test_default_config_automates_nothing():
    """初期設定は「全件人間」。ここが緩んでいたら事故る。"""
    d, why = decide(good(), RUBRIC, RUBRIC.gates)
    assert d == REVIEW, why


def test_negative_threshold_never_auto_passes():
    """閾値 -1 は無効化の意味。total >= -1 で全件通過してはいけない。"""
    g = gates(shortlist_above=-1.0, auto_reject_below=-1.0)
    for total in (0.0, 1.5, 3.0):
        d, _ = decide(good(total=total), RUBRIC, g)
        assert d == REVIEW


def test_shortlist_when_enabled():
    g = gates(shortlist_above=2.3)
    assert decide(good(), RUBRIC, g)[0] == SHORTLIST


def test_auto_reject_when_enabled():
    g = gates(auto_reject_below=0.8)
    a = good(total=0.5, scores={ax.id: 0.5 for ax in RUBRIC.scores})
    assert decide(a, RUBRIC, g)[0] == REJECT


def test_clear_eligibility_failure_is_ineligible():
    a = good()
    a.eligibility["publicly_viewable"] = 0.02
    d, why = decide(a, RUBRIC, gates(shortlist_above=2.3))
    assert d == INELIGIBLE
    assert "第三者閲覧可能" in why[0]


def test_grey_eligibility_goes_to_human():
    a = good()
    a.eligibility["public_window"] = 0.5
    assert decide(a, RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW


def test_low_score_confidence_goes_to_human():
    a = good()
    a.score_confidence["originality"] = 0.2
    assert decide(a, RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW


def test_low_category_confidence_goes_to_human():
    a = good(category_confidence=0.1)
    assert decide(a, RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW


def test_category_mismatch_goes_to_human():
    a = good()
    d, why = decide(a, RUBRIC, gates(shortlist_above=2.3), declared_category="music_sound")
    assert d == REVIEW
    assert "不一致" in why[0]


def test_matching_declared_category_is_fine():
    a = good()
    assert decide(a, RUBRIC, gates(shortlist_above=2.3), declared_category="still_image")[0] == SHORTLIST


def test_missing_answers_go_to_human():
    a = good()
    del a.scores["impact"]
    assert decide(a, RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW

    b = good()
    del b.eligibility["genuine_entry"]
    assert decide(b, RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW


def test_api_error_goes_to_human():
    assert decide(good(error="HTTP 500"), RUBRIC, gates(shortlist_above=2.3))[0] == REVIEW
