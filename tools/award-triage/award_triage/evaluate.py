"""効果測定。

測るのは4つだけ。
  1. 取りこぼし率  : 機械が自動で落とした中に、人間なら通した作品が何%あったか
  2. 誤通過率      : 機械が自動で通した中に、人間なら落とした作品が何%あったか
  3. 自動化率      : 人間が読まずに済んだ割合
  4. 削減額        : 3 と実測の審査工数から出した金額

1 がこの仕組みの許容条件で、3 と 4 が導入する理由。1 を先に決めて、
それを満たす範囲でどこまで 3 を上げられるかを閾値スイープで探す。
"""

from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import Gates, Rubric
from .gate import decide
from .models import AUTOMATED, Assessment, Entry, INELIGIBLE, REJECT, REVIEW, SHORTLIST

#: 人間の判定として受理する表記ゆれ
_DECISION_ALIASES = {
    "shortlist": SHORTLIST, "pass": SHORTLIST, "通過": SHORTLIST, "○": SHORTLIST, "1": SHORTLIST,
    "reject": REJECT, "fail": REJECT, "不通過": REJECT, "×": REJECT, "0": REJECT,
    "ineligible": INELIGIBLE, "失格": INELIGIBLE, "対象外": INELIGIBLE,
    "review": REVIEW, "保留": REVIEW,
}


def normalize_decision(value: str) -> str:
    v = (value or "").strip().lower()
    return _DECISION_ALIASES.get(v, v.upper())


@dataclass
class GoldenRow:
    entry_id: str
    decision: str = ""
    category: str = ""
    scores: dict[str, float] = field(default_factory=dict)


def load_golden(path: str | Path, rubric: Rubric) -> dict[str, GoldenRow]:
    """人間が採点した正解セットを読む。

    列: entry_id, decision, category, <採点軸id> ...
    decision 以外は任意。空欄はその指標の集計から除外される。
    """
    out: dict[str, GoldenRow] = {}
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            eid = (row.get("entry_id") or "").strip()
            if not eid:
                continue
            g = GoldenRow(
                entry_id=eid,
                decision=normalize_decision(row.get("decision", "")),
                category=(row.get("category") or "").strip(),
            )
            for axis in rubric.scores:
                raw = (row.get(axis.id) or "").strip()
                if raw:
                    try:
                        g.scores[axis.id] = float(raw)
                    except ValueError:
                        pass
            out[eid] = g
    return out


# --- 統計 (scipy を持ち込まずに済ませる) ------------------------------------

def _rank(xs: list[float]) -> list[float]:
    """同順位は平均順位にする。"""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(xs: list[float], ys: list[float]) -> float | None:
    n = len(xs)
    if n < 2:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    if dx == 0 or dy == 0:
        return None  # 片方が定数。相関は定義されない
    return num / (dx * dy)


def spearman(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2:
        return None
    return pearson(_rank(xs), _rank(ys))


# --- 集計 -------------------------------------------------------------------

@dataclass
class GateStats:
    n: int = 0
    automated: int = 0
    review: int = 0
    #: 自動で落としたが人間は通した（= 取りこぼし）
    false_reject: int = 0
    #: 自動で通したが人間は落とした
    false_shortlist: int = 0
    #: 自動判定のうち人間と一致したもの
    automated_checked: int = 0
    automated_agree: int = 0

    @property
    def automation_rate(self) -> float:
        return self.automated / self.n if self.n else 0.0

    @property
    def false_reject_rate(self) -> float:
        """自動判定した全体に対する取りこぼしの割合。"""
        return self.false_reject / self.automated_checked if self.automated_checked else 0.0

    @property
    def false_shortlist_rate(self) -> float:
        return self.false_shortlist / self.automated_checked if self.automated_checked else 0.0

    @property
    def automated_accuracy(self) -> float:
        return self.automated_agree / self.automated_checked if self.automated_checked else 0.0


def gate_stats(
    pairs: list[tuple[Entry, Assessment]],
    golden: dict[str, GoldenRow],
    rubric: Rubric,
    gates: Gates,
) -> GateStats:
    st = GateStats()
    for entry, a in pairs:
        decision, _ = decide(a, rubric, gates, entry.fields.get("category", ""))
        st.n += 1
        if decision in AUTOMATED:
            st.automated += 1
        else:
            st.review += 1

        g = golden.get(a.entry_id)
        if not g or not g.decision or decision not in AUTOMATED:
            continue
        st.automated_checked += 1
        human_pass = g.decision == SHORTLIST
        machine_pass = decision == SHORTLIST
        if human_pass and not machine_pass:
            st.false_reject += 1
        elif machine_pass and not human_pass:
            st.false_shortlist += 1
        else:
            st.automated_agree += 1
    return st


def category_stats(
    pairs: list[tuple[Entry, Assessment]], golden: dict[str, GoldenRow]
) -> dict[str, Any]:
    checked = 0
    correct = 0
    confusion: dict[tuple[str, str], int] = {}
    for _, a in pairs:
        g = golden.get(a.entry_id)
        if not g or not g.category or not a.category:
            continue
        checked += 1
        key = (g.category, a.category)
        confusion[key] = confusion.get(key, 0) + 1
        if g.category.strip().lower() == a.category.strip().lower():
            correct += 1
    return {
        "checked": checked,
        "accuracy": correct / checked if checked else None,
        "confusion": confusion,
    }


def score_stats(
    pairs: list[tuple[Entry, Assessment]], golden: dict[str, GoldenRow], rubric: Rubric
) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    by_id = {a.entry_id: a for _, a in pairs}
    for axis in rubric.scores:
        human: list[float] = []
        machine: list[float] = []
        for eid, g in golden.items():
            a = by_id.get(eid)
            if a is None or axis.id not in g.scores or axis.id not in a.scores:
                continue
            human.append(g.scores[axis.id])
            machine.append(a.scores[axis.id])
        out[axis.id] = {
            "label": axis.label,
            "n": len(human),
            "spearman": spearman(human, machine),
            "mae": (
                sum(abs(h - m) for h, m in zip(human, machine)) / len(human) if human else None
            ),
            "human_mean": sum(human) / len(human) if human else None,
            "machine_mean": sum(machine) / len(machine) if machine else None,
        }
    return out


def cost_report(
    pairs: list[tuple[Entry, Assessment]], rubric: Rubric, stats: GateStats
) -> dict[str, Any]:
    p = rubric.pricing
    c_in = sum(a.claude_usage.input_tokens for _, a in pairs)
    c_out = sum(a.claude_usage.output_tokens for _, a in pairs)
    t_in = sum(a.typesafe_usage.input_tokens for _, a in pairs)
    t_out = sum(a.typesafe_usage.output_tokens for _, a in pairs)

    claude_usd = (c_in / 1e6) * p.claude_input_per_mtok + (c_out / 1e6) * p.claude_output_per_mtok
    ts_usd = (t_in / 1e6) * p.typesafe_input_per_mtok + (t_out / 1e6) * p.typesafe_output_per_mtok

    machine_jpy = (claude_usd + ts_usd) * p.usd_jpy
    per_entry_jpy = p.human_hourly_jpy * (p.human_minutes_per_entry / 60.0)
    saved_entries = stats.automated
    human_saved_jpy = saved_entries * per_entry_jpy

    return {
        "claude_tokens": {"input": c_in, "output": c_out},
        "typesafe_tokens": {"input": t_in, "output": t_out},
        "typesafe_priced": p.typesafe_priced,
        "machine_cost_jpy": machine_jpy,
        "human_cost_per_entry_jpy": per_entry_jpy,
        "entries_not_read_by_human": saved_entries,
        "human_cost_avoided_jpy": human_saved_jpy,
        "net_saving_jpy": human_saved_jpy - machine_jpy,
        "human_hours_avoided": saved_entries * p.human_minutes_per_entry / 60.0,
    }


def sweep(
    pairs: list[tuple[Entry, Assessment]],
    golden: dict[str, GoldenRow],
    rubric: Rubric,
    *,
    max_false_reject_rate: float = 0.02,
    steps: int = 12,
) -> dict[str, Any]:
    """閾値を振って「取りこぼし率の上限を守れる範囲で最大の自動化率」を探す。

    max_false_reject_rate は審査委員会が決める数字であって、こちらが
    決めるものではない。既定の 2% は議論の出発点にすぎない。
    """
    top = rubric.max_total
    base = rubric.gates
    candidates: list[dict[str, Any]] = []

    shortlist_opts = [-1.0] + [top * (0.5 + 0.5 * i / steps) for i in range(steps + 1)]
    reject_opts = [-1.0] + [top * (0.5 * i / steps) for i in range(steps + 1)]

    for s in shortlist_opts:
        for r in reject_opts:
            if s >= 0 and r >= 0 and r >= s:
                continue  # 落とす線が通す線より上、は意味を成さない
            g = Gates(**{**base.__dict__, "shortlist_above": s, "auto_reject_below": r})
            st = gate_stats(pairs, golden, rubric, g)
            candidates.append(
                {
                    "shortlist_above": s,
                    "auto_reject_below": r,
                    "automation_rate": st.automation_rate,
                    "false_reject_rate": st.false_reject_rate,
                    "false_shortlist_rate": st.false_shortlist_rate,
                    "automated_checked": st.automated_checked,
                    "n_automated": st.automated,
                }
            )

    safe = [
        c
        for c in candidates
        if c["false_reject_rate"] <= max_false_reject_rate and c["automated_checked"] >= 5
    ]
    best = max(safe, key=lambda c: c["automation_rate"]) if safe else None
    return {
        "max_false_reject_rate": max_false_reject_rate,
        "recommended": best,
        "candidates": sorted(candidates, key=lambda c: -c["automation_rate"])[:40],
        "note": (
            "推奨が出ない場合、ゴールデンセットが小さすぎるか、"
            "採点が人間の判断を再現できていない。閾値ではなくルーブリックを直すこと。"
        ),
    }
