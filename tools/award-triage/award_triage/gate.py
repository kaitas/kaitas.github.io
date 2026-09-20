"""振り分けロジック。

設計方針は1つだけ:「迷ったら人間に回す」。
機械が SHORTLIST / REJECT / INELIGIBLE を出すのは、閾値が明示的に
有効化されていて、かつ確信度が足りている場合に限る。閾値の初期値
(-1) は「自動判定しない」を意味し、全件が REVIEW になる。
まずそこから始めて、calibrate で取りこぼし率を測ってから緩めること。
"""

from __future__ import annotations

from .config import Gates, Rubric
from .models import Assessment, INELIGIBLE, REJECT, REVIEW, SHORTLIST


def decide(a: Assessment, rubric: Rubric, gates: Gates, declared_category: str = "") -> tuple[str, list[str]]:
    """判定と、その理由（日本語）を返す。"""
    reasons: list[str] = []

    if a.error:
        return REVIEW, [f"判定に失敗: {a.error}"]

    # --- 応募資格 -----------------------------------------------------------
    missing_checks = [c.id for c in rubric.eligibility if c.id not in a.eligibility]
    if missing_checks:
        return REVIEW, [f"応募資格の判定が欠落: {', '.join(missing_checks)}"]

    grey: list[str] = []
    for check in rubric.eligibility:
        noul = a.eligibility[check.id]
        if noul < gates.eligibility_fail_below:
            reasons.append(f"応募資格「{check.label}」を満たさない (noul={noul:.3f})")
            return INELIGIBLE, reasons
        if noul <= gates.eligibility_pass_above:
            grey.append(f"{check.label} (noul={noul:.3f})")

    if grey:
        return REVIEW, [f"応募資格がグレー: {', '.join(grey)}"]

    # --- カテゴリ -----------------------------------------------------------
    if not a.category:
        return REVIEW, ["カテゴリ判定が欠落"]
    if a.category_confidence < gates.min_category_confidence:
        return REVIEW, [
            f"カテゴリの確信度が低い ({a.category_confidence:.3f} < {gates.min_category_confidence})"
        ]
    if gates.flag_category_mismatch and declared_category:
        if declared_category.strip().lower() != a.category.strip().lower():
            return REVIEW, [f"申告カテゴリ({declared_category})と判定({a.category})が不一致"]

    # --- 採点 ---------------------------------------------------------------
    missing_axes = [ax.id for ax in rubric.scores if ax.id not in a.scores]
    if missing_axes:
        return REVIEW, [f"採点が欠落: {', '.join(missing_axes)}"]

    weak = [
        f"{ax.label}={a.score_confidence.get(ax.id, 0.0):.3f}"
        for ax in rubric.scores
        if a.score_confidence.get(ax.id, 0.0) < gates.min_score_confidence
    ]
    if weak:
        return REVIEW, [f"採点の確信度が低い: {', '.join(weak)}"]

    # --- 合計点によるカット -------------------------------------------------
    # 負の閾値は「この自動判定を使わない」の意味。total は常に 0 以上なので
    # ここで弾かないと全件が自動通過してしまう。
    if gates.shortlist_above >= 0 and a.total >= gates.shortlist_above:
        return SHORTLIST, [f"合計 {a.total:.3f} >= {gates.shortlist_above}"]
    if gates.auto_reject_below >= 0 and a.total <= gates.auto_reject_below:
        return REJECT, [f"合計 {a.total:.3f} <= {gates.auto_reject_below}"]

    return REVIEW, [f"合計 {a.total:.3f} は自動判定の範囲外"]
