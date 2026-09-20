"""審査員向けの単一 HTML レビューコンソールを書き出す。

外部 CDN もサーバも使わない1ファイル。審査員にメール添付やファイル共有で
渡してブラウザで開けばよい。審査員がつけた判定は localStorage に残り、
CSV として書き出せる。その CSV はそのまま `award-triage calibrate` の
ゴールデンセットになる（人間の判断を測る材料が審査そのものから出る）。
"""

from __future__ import annotations

import html
import json
from pathlib import Path

from .config import FieldMap, Rubric
from .models import Assessment, Entry

_CSS = """
:root{--bg:#fbfbfa;--panel:#fff;--ink:#1a1a18;--muted:#6b6b66;--line:#e4e4e0;
--pass:#1f7a4d;--rev:#8a6d1f;--rej:#a13b2c;--inel:#5a5a55;--bar:#c9c9c4;--accent:#2f5fd0}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#17171a;--panel:#202024;
--ink:#ececea;--muted:#9a9a94;--line:#33333a;--pass:#63c898;--rev:#d6b45c;--rej:#e08272;
--inel:#8e8e88;--bar:#44444c;--accent:#8fb0ff}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 system-ui,"Hiragino Sans","Noto Sans JP",sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:24px 16px 96px}
h1{font-size:1.3rem;margin:0 0 4px}
.sub{color:var(--muted);font-size:.85rem;margin-bottom:20px}
.toolbar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);
padding:10px 0;margin-bottom:12px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
button,select,input[type=search]{font:inherit;color:var(--ink);background:var(--panel);
border:1px solid var(--line);border-radius:6px;padding:5px 10px;cursor:pointer}
input[type=search]{cursor:text;min-width:180px;flex:1}
button.on{border-color:var(--accent);color:var(--accent);font-weight:600}
.card{background:var(--panel);border:1px solid var(--line);border-radius:10px;margin-bottom:10px;overflow:hidden}
.head{display:flex;gap:12px;align-items:baseline;padding:12px 14px;cursor:pointer}
.head:hover{background:color-mix(in srgb,var(--accent) 6%,transparent)}
.badge{font-size:.72rem;font-weight:700;letter-spacing:.04em;padding:2px 7px;border-radius:4px;
border:1px solid currentColor;white-space:nowrap}
.SHORTLIST{color:var(--pass)}.REVIEW{color:var(--rev)}.REJECT{color:var(--rej)}.INELIGIBLE{color:var(--inel)}
.title{font-weight:600;flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tot{font-variant-numeric:tabular-nums;color:var(--muted);font-size:.85rem}
.body{display:none;padding:0 14px 16px;border-top:1px solid var(--line)}
.card.open .body{display:block}
h3{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);
margin:18px 0 6px;font-weight:600}
table{width:100%;border-collapse:collapse;font-size:.88rem}
td{padding:3px 0;vertical-align:top}
td.k{width:12em;color:var(--muted)}
td.n{width:5em;text-align:right;font-variant-numeric:tabular-nums}
.meter{height:6px;background:var(--bar);border-radius:3px;overflow:hidden;margin-top:6px}
.meter>i{display:block;height:100%;background:var(--accent)}
.txt{white-space:pre-wrap;font-size:.9rem;background:var(--bg);border:1px solid var(--line);
border-radius:6px;padding:10px;margin:0}
.tabs{display:flex;gap:6px;margin-bottom:6px}
.tabs button{padding:3px 9px;font-size:.8rem}
.why{font-size:.85rem;color:var(--muted);margin:4px 0 0}
.warn{color:var(--rej);font-size:.85rem}
.verdict{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px}
.verdict input[type=text]{flex:1;min-width:160px;font:inherit;padding:5px 8px;
border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--ink)}
.count{color:var(--muted);font-size:.85rem;margin-left:auto}
a{color:var(--accent)}
"""

_JS = """
const S = JSON.parse(localStorage.getItem(KEY) || '{}');
const save = () => { try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} };

document.querySelectorAll('.head').forEach(h =>
  h.onclick = () => h.parentElement.classList.toggle('open'));

// 原文/訳文の切り替え
document.querySelectorAll('.tabs').forEach(t => t.onclick = e => {
  if (e.target.tagName !== 'BUTTON') return;
  const box = t.parentElement;
  t.querySelectorAll('button').forEach(b => b.classList.toggle('on', b === e.target));
  box.querySelectorAll('pre.txt').forEach(p =>
    p.style.display = p.dataset.lang === e.target.dataset.lang ? '' : 'none');
});

// 審査員の判定
function paint(id){
  const row = document.querySelector(`[data-verdict="${id}"]`);
  if(!row) return;
  row.querySelectorAll('button[data-v]').forEach(b =>
    b.classList.toggle('on', S[id] && S[id].decision === b.dataset.v));
  const memo = row.querySelector('input[type=text]');
  if (S[id] && memo) memo.value = S[id].memo || '';
}
document.querySelectorAll('[data-verdict]').forEach(row => {
  const id = row.dataset.verdict;
  row.querySelectorAll('button[data-v]').forEach(b => b.onclick = () => {
    S[id] = S[id] || {}; S[id].decision = S[id].decision === b.dataset.v ? '' : b.dataset.v;
    save(); paint(id); tally();
  });
  const memo = row.querySelector('input[type=text]');
  if (memo) memo.oninput = () => { S[id] = S[id] || {}; S[id].memo = memo.value; save(); };
  paint(id);
});

function tally(){
  const n = Object.values(S).filter(v => v && v.decision).length;
  document.getElementById('tally').textContent = `審査済み ${n} / ${ALL.length}`;
}
tally();

// フィルタ
let filter = 'ALL', q = '';
function apply(){
  let shown = 0;
  document.querySelectorAll('.card').forEach(c => {
    const okF = filter === 'ALL' || c.dataset.decision === filter
      || (filter === 'UNDONE' && !(S[c.dataset.id] && S[c.dataset.id].decision));
    const okQ = !q || c.dataset.search.includes(q);
    c.style.display = (okF && okQ) ? '' : 'none';
    if (okF && okQ) shown++;
  });
  document.getElementById('shown').textContent = `${shown} 件表示`;
}
document.querySelectorAll('[data-filter]').forEach(b => b.onclick = () => {
  filter = b.dataset.filter;
  document.querySelectorAll('[data-filter]').forEach(x => x.classList.toggle('on', x === b));
  apply();
});
document.getElementById('q').oninput = e => { q = e.target.value.toLowerCase(); apply(); };
apply();

// CSV 書き出し: そのまま calibrate のゴールデンセットになる形
document.getElementById('export').onclick = () => {
  const esc = s => `"${String(s == null ? '' : s).replace(/"/g, '""')}"`;
  const rows = [['entry_id','decision','category','memo'].join(',')];
  ALL.forEach(e => {
    const v = S[e.id];
    if (!v || !v.decision) return;
    rows.push([e.id, v.decision, e.category, v.memo || ''].map(esc).join(','));
  });
  if (rows.length === 1) { alert('まだ判定が1件も入っていません'); return; }
  const blob = new Blob(['\\ufeff' + rows.join('\\n')], {type:'text/csv;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'golden.csv';
  a.click();
  URL.revokeObjectURL(a.href);
};
"""


def _bar(value: float, maximum: float) -> str:
    pct = 0.0 if maximum <= 0 else max(0.0, min(1.0, value / maximum)) * 100
    return f'<div class="meter"><i style="width:{pct:.1f}%"></i></div>'


def _esc(s: object) -> str:
    return html.escape(str(s if s is not None else ""))


def render(
    pairs: list[tuple[Entry, Assessment]],
    rubric: Rubric,
    fieldmap: FieldMap,
    out_path: str | Path,
    *,
    run_label: str = "",
) -> Path:
    counts: dict[str, int] = {}
    for _, a in pairs:
        counts[a.decision] = counts.get(a.decision, 0) + 1

    # 見るべき順: REVIEW を上に、その中で点の高い順
    order = {"REVIEW": 0, "SHORTLIST": 1, "REJECT": 2, "INELIGIBLE": 3}
    pairs = sorted(pairs, key=lambda p: (order.get(p[1].decision, 9), -p[1].total))

    langs = [l for l in dict.fromkeys(rubric.judge_languages)]
    cards: list[str] = []
    index: list[dict[str, str]] = []

    for entry, a in pairs:
        eid = entry.entry_id
        title = entry.fields.get("title") or "(無題)"
        index.append({"id": eid, "category": a.category})

        # --- 本文タブ（原文 + 各訳） ---
        views = [("原文", entry.fields, entry.source_language or "src")]
        for lang in langs:
            if lang in entry.translations:
                views.append((lang.upper(), entry.translations[lang], lang))
        tabs = "".join(
            f'<button data-lang="{_esc(code)}"{" class=on" if i == 0 else ""}>{_esc(label)}</button>'
            for i, (label, _, code) in enumerate(views)
        )
        texts = "".join(
            '<pre class="txt" data-lang="{c}"{hide}>{t}</pre>'.format(
                c=_esc(code),
                hide="" if i == 0 else ' style="display:none"',
                t=_esc(
                    "\n".join(
                        f"{f}: {src.get(f, '')}" for f in fieldmap.judge_fields if src.get(f)
                    )
                ),
            )
            for i, (_, src, code) in enumerate(views)
        )

        elig = "".join(
            '<tr><td class="k">{l}</td><td class="n">{v:.3f}</td><td>{b}</td></tr>'.format(
                l=_esc(c.label), v=a.eligibility.get(c.id, 0.0),
                b=_bar(a.eligibility.get(c.id, 0.0), 1.0),
            )
            for c in rubric.eligibility
        )
        scores = "".join(
            '<tr><td class="k">{l}<br><small style="color:var(--muted)">重み {w:.2f}</small></td>'
            '<td class="n">{v:.2f}<br><small style="color:var(--muted)">確信 {c:.2f}</small></td>'
            "<td>{b}</td></tr>".format(
                l=_esc(ax.label), w=ax.weight,
                v=a.scores.get(ax.id, 0.0), c=a.score_confidence.get(ax.id, 0.0),
                b=_bar(a.scores.get(ax.id, 0.0), ax.max_score),
            )
            for ax in rubric.scores
        )
        top_cats = sorted(a.category_probabilities.items(), key=lambda kv: -kv[1])[:3]
        cat_line = " / ".join(f"{_esc(k)} {v:.2f}" for k, v in top_cats) or "—"

        url = entry.fields.get("url", "")
        url_html = f'<a href="{_esc(url)}" target="_blank" rel="noopener">{_esc(url)}</a>' if url else "—"
        warns = entry.ingest_warnings + ([a.error] if a.error else [])

        search = " ".join(
            [eid, title, a.category, entry.fields.get("description", "")]
            + [t.get("description", "") for t in entry.translations.values()]
        ).lower()

        cards.append(f"""
<div class="card" data-id="{_esc(eid)}" data-decision="{_esc(a.decision)}" data-search="{_esc(search)}">
  <div class="head">
    <span class="badge {_esc(a.decision)}">{_esc(a.decision)}</span>
    <span class="title">{_esc(title)}</span>
    <span class="tot">{a.total:.2f} / {rubric.max_total:.2f}</span>
    <span class="tot">{_esc(a.category or "—")}</span>
  </div>
  <div class="body">
    <p class="why">{_esc(" / ".join(a.reasons))}</p>
    {'<p class="warn">⚠ ' + _esc(" / ".join(warns)) + "</p>" if warns else ""}
    <h3>作品</h3>
    <table><tr><td class="k">応募ID</td><td>{_esc(eid)}</td></tr>
    <tr><td class="k">URL</td><td>{url_html}</td></tr>
    <tr><td class="k">原文言語</td><td>{_esc(entry.source_language or "不明")}</td></tr>
    <tr><td class="k">カテゴリ候補</td><td>{cat_line}（確信 {a.category_confidence:.2f}）</td></tr></table>
    <h3>本文</h3>
    <div><div class="tabs">{tabs}</div>{texts}</div>
    <h3>応募資格</h3><table>{elig}</table>
    <h3>採点</h3><table>{scores}</table>
    <h3>審査員の判定</h3>
    <div class="verdict" data-verdict="{_esc(eid)}">
      <button data-v="SHORTLIST">通過</button>
      <button data-v="REVIEW">保留</button>
      <button data-v="REJECT">不通過</button>
      <button data-v="INELIGIBLE">失格</button>
      <input type="text" placeholder="メモ（任意）">
    </div>
  </div>
</div>""")

    summary = " · ".join(
        f"{k} {counts.get(k, 0)}" for k in ("REVIEW", "SHORTLIST", "REJECT", "INELIGIBLE")
    )
    filters = "".join(
        f'<button data-filter="{k}"{" class=on" if k == "ALL" else ""}>{label}</button>'
        for k, label in (
            ("ALL", "すべて"), ("REVIEW", "要審査"), ("UNDONE", "未判定"),
            ("SHORTLIST", "自動通過"), ("REJECT", "自動不通過"), ("INELIGIBLE", "失格"),
        )
    )

    doc = f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>一次審査コンソール</title><style>{_CSS}</style></head><body>
<div class="wrap">
<h1>{_esc(rubric.award)} — 一次審査コンソール</h1>
<p class="sub">{_esc(run_label)}　{len(pairs)} 件　{_esc(summary)}<br>
機械の判定は読む順番を決めるためのもので、審査結果ではありません。</p>
<div class="toolbar">
  {filters}
  <input type="search" id="q" placeholder="作品名・本文で検索">
  <button id="export">判定をCSVで書き出す</button>
  <span class="count"><span id="tally"></span>　<span id="shown"></span></span>
</div>
{''.join(cards)}
</div>
<script>
const KEY = {json.dumps("award-triage:" + (run_label or "run"))};
const ALL = {json.dumps(index, ensure_ascii=False)};
{_JS}
</script></body></html>"""

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return out
