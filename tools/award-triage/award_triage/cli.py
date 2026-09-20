"""コマンドラインインターフェース。"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__, evaluate, report as report_mod, store
from .config import load_fieldmap, load_rubric
from .ingest import load_entries
from .models import AUTOMATED
from .fake import FakeTypeSafeClient
from .screen import screen_all
from .translate import DEFAULT_MODEL as DEFAULT_TRANSLATE_MODEL, Translator
from .typesafe import TypeSafeClient, TypeSafeError


def _progress(label: str):
    def cb(i: int, n: int) -> None:
        end = "\n" if i == n else "\r"
        print(f"  {label}: {i}/{n}", end=end, file=sys.stderr, flush=True)

    return cb


def _load_configs(args) -> tuple:
    rubric = load_rubric(args.rubric)
    fieldmap = load_fieldmap(args.fields)
    for w in rubric.warnings:
        print(f"warning: {w}", file=sys.stderr)
    return rubric, fieldmap


# --------------------------------------------------------------------------- run
def cmd_run(args) -> int:
    rubric, fieldmap = _load_configs(args)
    entries = load_entries(args.entries, fieldmap)
    if args.limit:
        entries = entries[: args.limit]
    if not entries:
        print("応募が0件です。", file=sys.stderr)
        return 1
    print(f"{len(entries)} 件を読み込みました。", file=sys.stderr)

    claude_usage = None
    if not args.no_translate:
        translator = Translator(
            rubric, fieldmap, model=args.translate_model, max_workers=args.workers
        )
        claude_usage = translator.translate_all(entries, progress=_progress("翻訳"))

    try:
        if args.fake:
            print("*** --fake: ダミー判定です。審査には使えません。 ***", file=sys.stderr)
            client = FakeTypeSafeClient(rubric)
        else:
            client = TypeSafeClient(model=args.typesafe_model)
        with client:
            assessments, _ = screen_all(
                entries, rubric, fieldmap, client,
                max_workers=args.workers, progress=_progress("判定"),
            )
    except TypeSafeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    by_id = {a.entry_id: a for a in assessments}
    if claude_usage is not None and assessments:
        # 翻訳は件数で按分して1件あたりに割り付ける（請求突合用の概算）
        per = len(assessments)
        for a in assessments:
            a.claude_usage.input_tokens = claude_usage.input_tokens // per
            a.claude_usage.output_tokens = claude_usage.output_tokens // per

    pairs = [(e, by_id[e.entry_id]) for e in entries if e.entry_id in by_id]
    store.save_run(args.out, pairs)
    print(f"\n結果: {args.out}", file=sys.stderr)

    counts: dict[str, int] = {}
    for _, a in pairs:
        counts[a.decision] = counts.get(a.decision, 0) + 1
    for k in ("REVIEW", "SHORTLIST", "REJECT", "INELIGIBLE"):
        print(f"  {k:<11} {counts.get(k, 0)}", file=sys.stderr)
    automated = sum(counts.get(k, 0) for k in AUTOMATED)
    print(f"  自動化率      {automated / len(pairs):.1%}", file=sys.stderr)

    errs = [a.entry_id for _, a in pairs if a.error]
    if errs:
        print(f"  ! 判定エラー {len(errs)} 件: {', '.join(errs[:5])}", file=sys.stderr)

    if args.report:
        out = report_mod.render(pairs, rubric, fieldmap, args.report, run_label=Path(args.out).stem)
        print(f"レビューコンソール: {out}", file=sys.stderr)
    return 0


# ------------------------------------------------------------------------ report
def cmd_report(args) -> int:
    rubric, fieldmap = _load_configs(args)
    pairs = store.load_run(args.run)
    out = report_mod.render(pairs, rubric, fieldmap, args.out, run_label=Path(args.run).stem)
    print(f"レビューコンソール: {out}")
    return 0


# --------------------------------------------------------------------- calibrate
def _fmt(x, spec="+.3f", dash="—"):
    return dash if x is None else format(x, spec)


def cmd_calibrate(args) -> int:
    rubric, _ = _load_configs(args)
    pairs = store.load_run(args.run)
    golden = evaluate.load_golden(args.golden, rubric)

    matched = [p for p in pairs if p[1].entry_id in golden]
    print(f"# 効果測定 — {rubric.award}\n")
    print(f"実行結果 {len(pairs)} 件 / ゴールデンセット {len(golden)} 件 / 突合 {len(matched)} 件\n")
    if len(matched) < 20:
        print("> **注意**: 突合できた件数が少なすぎます。以下の数字は参考値です。")
        print("> 一次審査の閾値を決めるには 50 件以上、できれば 2 名以上の審査員による")
        print("> 採点を突き合わせてください。\n")

    st = evaluate.gate_stats(pairs, golden, rubric, rubric.gates)
    print("## 1. 現在の閾値での振り分け\n")
    print("| 指標 | 値 |")
    print("|---|---|")
    print(f"| 自動判定 | {st.automated} / {st.n} ({st.automation_rate:.1%}) |")
    print(f"| 人間が読む件数 | {st.review} |")
    print(f"| 人間と突合できた自動判定 | {st.automated_checked} |")
    print(f"| **取りこぼし率**（自動で落としたが人間は通した） | **{st.false_reject_rate:.1%}** ({st.false_reject}件) |")
    print(f"| 誤通過率（自動で通したが人間は落とした） | {st.false_shortlist_rate:.1%} ({st.false_shortlist}件) |")
    print(f"| 自動判定の人間との一致率 | {st.automated_accuracy:.1%} |\n")

    cs = evaluate.category_stats(pairs, golden)
    print("## 2. カテゴリ判定\n")
    if cs["checked"]:
        print(f"照合 {cs['checked']} 件 / 正解率 **{cs['accuracy']:.1%}**\n")
        wrong = sorted(
            ((k, v) for k, v in cs["confusion"].items() if k[0].lower() != k[1].lower()),
            key=lambda kv: -kv[1],
        )[:8]
        if wrong:
            print("よくある取り違え（人間 → 機械）:\n")
            for (h, m), n in wrong:
                print(f"- {h} → {m}: {n} 件")
            print()
    else:
        print("ゴールデンセットに category 列がないため測定できません。\n")

    print("## 3. 採点軸ごとの人間との一致\n")
    print("| 軸 | n | 順位相関 (Spearman) | 平均絶対誤差 | 人間平均 | 機械平均 |")
    print("|---|---|---|---|---|---|")
    axis_stats = evaluate.score_stats(pairs, golden, rubric)
    for axis in rubric.scores:
        s = axis_stats[axis.id]
        print(
            f"| {s['label']} | {s['n']} | {_fmt(s['spearman'])} | {_fmt(s['mae'], '.3f')} | "
            f"{_fmt(s['human_mean'], '.2f')} | {_fmt(s['machine_mean'], '.2f')} |"
        )
    print("\n順位相関が 0.5 を下回る軸は、ルーブリックの criteria が審査員の")
    print("見ているものを言語化できていない。閾値ではなく criteria を直すこと。\n")

    sw = evaluate.sweep(pairs, golden, rubric, max_false_reject_rate=args.max_false_reject)
    print(f"## 4. 閾値スイープ（取りこぼし率 {args.max_false_reject:.1%} 以下を条件）\n")
    rec = sw["recommended"]
    if rec:
        print("推奨設定 — `config/rubric.yaml` の `gates:` に書き込む値:\n")
        print("```yaml")
        print("gates:")
        print(f"  shortlist_above: {rec['shortlist_above']:.2f}"
              + ("   # 自動通過なし" if rec["shortlist_above"] < 0 else ""))
        print(f"  auto_reject_below: {rec['auto_reject_below']:.2f}"
              + ("   # 自動不通過なし" if rec["auto_reject_below"] < 0 else ""))
        print("```\n")
        print(f"この設定での自動化率 **{rec['automation_rate']:.1%}** / "
              f"取りこぼし率 {rec['false_reject_rate']:.1%} / "
              f"誤通過率 {rec['false_shortlist_rate']:.1%}\n")
    else:
        print(f"条件を満たす閾値がありませんでした。\n\n> {sw['note']}\n")

    cost = evaluate.cost_report(pairs, rubric, st)
    print("## 5. コストと削減\n")
    print("| 項目 | 値 |")
    print("|---|---|")
    print(f"| 機械コスト（翻訳+判定） | ¥{cost['machine_cost_jpy']:,.0f}"
          + ("" if cost["typesafe_priced"] else " ※TypeSafe 分は単価未設定のため未計上") + " |")
    print(f"| 人間が読まずに済んだ件数 | {cost['entries_not_read_by_human']} |")
    print(f"| 削減した審査工数 | {cost['human_hours_avoided']:.1f} 時間 |")
    print(f"| 回避できた人件費 | ¥{cost['human_cost_avoided_jpy']:,.0f} |")
    print(f"| **差引** | **¥{cost['net_saving_jpy']:,.0f}** |")
    print(f"\n単価は `config/rubric.yaml` の `pricing:` に書いた値を使っています"
          f"（1件あたり {rubric.pricing.human_minutes_per_entry} 分 / "
          f"時給 ¥{rubric.pricing.human_hourly_jpy:,.0f}）。実測値に直してください。")
    return 0


# ------------------------------------------------------------------------- check
def cmd_check(args) -> int:
    rubric, fieldmap = _load_configs(args)
    print(f"ルーブリック v{rubric.version}: {rubric.award}")
    print(f"  応募資格チェック {len(rubric.eligibility)} 件")
    print(f"  カテゴリ {len(rubric.categories)} 件")
    print(f"  採点軸 {len(rubric.scores)} 件 / 合計満点 {rubric.max_total:.2f}")
    g = rubric.gates
    auto = []
    if g.shortlist_above >= 0:
        auto.append(f"自動通過 >= {g.shortlist_above}")
    if g.auto_reject_below >= 0:
        auto.append(f"自動不通過 <= {g.auto_reject_below}")
    print(f"  自動判定: {', '.join(auto) if auto else '無効（全件が人間レビューに回る）'}")

    if args.entries:
        entries = load_entries(args.entries, fieldmap)
        print(f"\n{args.entries}: {len(entries)} 件")
        langs: dict[str, int] = {}
        problems = 0
        for e in entries:
            langs[e.source_language or "不明"] = langs.get(e.source_language or "不明", 0) + 1
            if e.ingest_warnings:
                problems += 1
                if problems <= 5:
                    print(f"  ! {e.entry_id}: {'; '.join(e.ingest_warnings)}")
        print(f"  言語分布: {', '.join(f'{k}={v}' for k, v in sorted(langs.items()))}")
        if problems:
            print(f"  取り込み警告のある応募: {problems} 件")

        # 1件あたりの概算。実測は run 後の calibrate で出る。
        chars = sum(len(e.text_for(rubric.canonical_language, fieldmap.judge_fields)) for e in entries)
        est_tokens = chars / 2.2  # 日英混在のざっくり値
        p = rubric.pricing
        translate_usd = (est_tokens * 2 / 1e6) * p.claude_input_per_mtok + (
            est_tokens * 2 / 1e6
        ) * p.claude_output_per_mtok
        print(f"\n  翻訳コスト概算: ¥{translate_usd * p.usd_jpy:,.0f}"
              f" (モデル {DEFAULT_TRANSLATE_MODEL} の単価で、判定言語 {len(rubric.judge_languages)} 言語分)")
        print("  ※ TypeSafe 側は単価が未公表のため概算に含めていません。")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="award-triage",
        description="International AI Creator Award — 多言語取り込みと一次審査アシスト",
    )
    p.add_argument("--version", action="version", version=__version__)
    p.add_argument("--rubric", help="ルーブリック YAML (既定: config/rubric.yaml)")
    p.add_argument("--fields", help="フィールドマッピング YAML (既定: config/fields.yaml)")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="設定と入力データを検証し、コストを概算する")
    c.add_argument("--entries", help="応募データ CSV/JSONL")
    c.set_defaults(func=cmd_check)

    r = sub.add_parser("run", help="翻訳して判定し、結果を書き出す")
    r.add_argument("--entries", required=True, help="応募データ CSV/JSONL")
    r.add_argument("--out", default="out/run.jsonl", help="結果 JSONL の出力先")
    r.add_argument("--report", help="同時に HTML レビューコンソールを書き出す")
    r.add_argument("--limit", type=int, help="先頭 N 件だけ処理する（試走用）")
    r.add_argument("--no-translate", action="store_true", help="翻訳を省く（原文のまま判定）")
    r.add_argument("--fake", action="store_true",
                   help="APIを呼ばずダミー判定で動かす（画面確認と動作確認用。審査不可）")
    r.add_argument("--translate-model", default=DEFAULT_TRANSLATE_MODEL,
                   help=f"翻訳に使う Claude モデル (既定: {DEFAULT_TRANSLATE_MODEL})")
    r.add_argument("--typesafe-model", default="jev-latest")
    r.add_argument("--workers", type=int, default=8, help="並列数")
    r.set_defaults(func=cmd_run)

    rep = sub.add_parser("report", help="既存の結果から HTML を作り直す")
    rep.add_argument("--run", required=True)
    rep.add_argument("--out", default="out/review.html")
    rep.set_defaults(func=cmd_report)

    cal = sub.add_parser("calibrate", help="人間の判定と突き合わせて効果を測る")
    cal.add_argument("--run", required=True, help="run が出した JSONL")
    cal.add_argument("--golden", required=True, help="人間の判定 CSV")
    cal.add_argument("--max-false-reject", type=float, default=0.02,
                     help="許容する取りこぼし率 (既定 0.02 = 2%%)")
    cal.set_defaults(func=cmd_calibrate)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
