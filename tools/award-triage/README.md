# award-triage — 一次審査アシスト

International AI Creator Award 2026 の一次審査を、**多言語で届く応募を審査員の言語に
正規化した上で、読む順番と読む量を減らす**ための道具。

判定を置き換えるものではない。既定値では機械は何も確定せず、全件が人間に回る。
自動化はゴールデンセットで取りこぼし率を測ってから、測った分だけ開ける。

```
応募CSV ──▶ 取り込み・正規化 ──▶ 翻訳(Claude) ──▶ 判定(TypeSafe) ──▶ 振り分け
              言語判定 / 匿名化      原文は保持      資格5 + 分類 + 採点4      │
                                                                              ├─▶ review.html（審査員が読む）
                                                                              └─▶ run.jsonl（監査記録）
                                        ┌──────────────────────────────────────┘
審査員が console で判定 ──▶ golden.csv ─┴─▶ calibrate ──▶ 取りこぼし率・自動化率・削減額
```

最後の輪が閉じているのが要点。審査員が普通に審査するだけでゴールデンセットが貯まり、
それが次の閾値を決める。効果測定のために別の作業を増やさない。

---

## なぜ Award に絞ったか

カスタマーサポート（aicu.ai / aicu.jp）ではなくこちらを先にする理由:

| | Award 一次審査 | CS |
|---|---|---|
| 締切 | **10/5 応募締切 → 中旬にノミネート発表。締切が動かない** | なし |
| 工数の山 | 締切直後に集中して発生し、人力だと確実に溢れる | 平準化されていて危機感が薄い |
| 多言語 | 7言語対応が要件そのもの | 実質 ja/en |
| 効果測定 | 審査員の判定が正解データになる。測れる | 「解決した」の定義から作る必要がある |
| 失敗のコスト | 全件人間に回すだけ。既存フローが壊れない | 顧客に直接届くので事故ると痛い |

CS は Award で確立したルーブリック → 閾値 → 測定の型をそのまま持ち込める。逆は成立しない。

---

## 48時間の進め方

AI が書く部分は数時間で終わる。**48時間のうち本当に必要なのは、審査委員の合意を
取る時間とゴールデンセットを作る時間**で、そこは短縮できない。

| 時間 | やること | 誰が | 成果物 |
|---|---|---|---|
| 0–4h | `config/rubric.yaml` の確定。公式10カテゴリへの差し替え、採点4軸の criteria を審査委員の言葉に直す | **審査委員** | rubric.yaml v1 |
| 4–6h | エントリーポータルの実カラムを `config/fields.yaml` に反映。`check` で取り込み確認 | 開発 | 取り込み通過 |
| 6–10h | 実データ30件で `run`。訳文と判定を目視。ルーブリックの言葉を直して2周回す | 開発+審査委員1名 | run.jsonl |
| 10–16h | **ゴールデンセット作成。審査員2名が独立に60件を console で判定** | **審査員2名** | golden.csv ×2 |
| 16–20h | `calibrate`。審査員2名の一致率を先に見る（人間同士が一致しない軸は機械にも無理） | 開発 | 効果測定レポート |
| 20–26h | 相関の低い軸の criteria を書き直して再測定 | 審査委員 | rubric.yaml v2 |
| 26–30h | 閾値を `calibrate` の推奨値に設定。取りこぼし率の上限は**審査委員会が決める** | 審査委員会 | gates 確定 |
| 30–38h | 全件 `run`。エラー件数と未判定を潰す | 開発 | 本番 run |
| 38–44h | 審査員へ console 配布、運用手順の説明 | 開発 | review.html |
| 44–48h | 審査規程への記載文面、異議申立てへの回答手順 | 事務局 | 規程差分 |

**この順番を崩さないこと。** ルーブリックが固まる前にコードを触ると全部やり直しになる。

---

## セットアップ

```bash
cd tools/award-triage
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

export ANTHROPIC_API_KEY=...      # 翻訳用
export TYPESAFE_API_KEY=...       # https://console.typesafe.ai/keys
```

鍵が無くても中身は見られる:

```bash
award-triage run --entries samples/entries.sample.csv --fake --no-translate \
  --out out/run.jsonl --report out/review.html
open out/review.html
```

`--fake` はダミー判定。審査には使えないが、審査委員に画面を見せて議論を始めるには十分。

## 使い方

```bash
# 1. 設定と入力の検証、コスト概算
award-triage check --entries entries.csv

# 2. 翻訳 + 判定（まず --limit 30 で試走する）
award-triage run --entries entries.csv --limit 30 \
  --out out/run.jsonl --report out/review.html

# 3. 審査員が out/review.html で判定 → 「判定をCSVで書き出す」で golden.csv

# 4. 効果測定
award-triage calibrate --run out/run.jsonl --golden golden.csv \
  --max-false-reject 0.02 > out/measurement.md
```

`calibrate` の出力はそのまま審査委員会に出せる Markdown。

## 効果測定の読み方

出る数字は4つだけ。見る順番も決まっている。

1. **取りこぼし率** — 機械が自動で落とした中に、人間なら通した作品が何%あったか。
   これが許容値を超えていたら、他の数字がどれだけ良くても自動化してはいけない。
   許容値（既定2%）は開発側が決める数字ではない。審査委員会が決める。
2. **採点軸ごとの順位相関** — 0.5 を下回る軸は、criteria が審査員の見ているものを
   言語化できていない。閾値をいじっても直らない。`rubric.yaml` の文章を直す。
3. **自動化率** — 1 を守った上でどこまで上げられるか。`calibrate` の閾値スイープが
   `gates:` にそのまま書ける値を出す。
4. **差引** — 3 と実測の審査工数から出る金額。`pricing:` の値を実測に直してから読む。

条件を満たす閾値が出ないのは正常な結果のひとつ。その場合は全件人間に回したまま、
翻訳と並べ替えの部分だけを使う。それでも審査員が読む労力はかなり下がる。

## 設計上の約束

- **既定では機械は何も確定しない。** `gates.shortlist_above` / `auto_reject_below` は
  ともに `-1`（無効）。負の閾値で全件自動通過する事故は `tests/test_gate.py` で押さえてある。
- **迷ったら人間に回す。** 確信度が閾値を下回る、資格判定がグレー、申告カテゴリと
  不一致、API エラー — どれも `REVIEW` に落ちる。
- **一次審査は氏名を伏せる。** `fields.yaml` の `judge_fields` に無いフィールドはモデルに
  渡らない。`creator` と `credits` は意図的に外してある。
- **原文を捨てない。** 訳は常に添えるだけ。console で原文と訳を切り替えて読める。
- **判定言語を1つに固定する。** 原文の言語ごとに判定が揺れると、公平性の説明ができない。
- **生値を全部残す。** `run.jsonl` に noul / probabilities / confidence をそのまま保存。
  「なぜ落ちたのか」の問い合わせに数字で答えられる。

## コスト

翻訳（Claude）の既定モデルは `claude-opus-5`。単価は 1M トークンあたり入力 $5 / 出力 $25。
コスト優先なら落とせる:

```bash
award-triage run --translate-model claude-sonnet-5 ...   # $2 / $10
award-triage run --translate-model claude-haiku-4-5 ...  # $1 / $5
```

どれを使うかは、30件を各モデルで訳して審査員が読み比べてから決めるのが速い。
TypeSafe(Jev) 側は単価表が公開されていないため `pricing.typesafe_*_per_mtok` は 0 に
してある。請求額が分かったら入れること。入れるまで `calibrate` の機械コストは
「TypeSafe 分未計上」と明記して出る。

第三者の公開事例では、1回の判定あたり **$0.00013〜$0.0006 程度**（904回で $0.12 /
1,260回で $0.78）という報告がある。本ツールは1応募につき1リクエストなので、
応募 1,000 件でも数百円規模に収まる見込み。ただしこれは他人のワークロードの数字で、
質問10個・本文800字という本ツールの形とは違う。**30件の試走で実費を確認してから
`pricing:` に入れること。**

支配的なコストは翻訳側。応募が 1,000 件・平均 800 字なら、ja+en の2言語で
おおむね数千円〜（モデルによる）。`check --entries` が実データでの概算を出す。

## 本番投入前のチェックリスト

- [ ] **このディレクトリを AICU の非公開リポジトリへ移す。** ここは公開リポジトリで、
      応募データには個人情報が含まれる。`.gitignore` で入力ファイルは弾いてあるが、
      運用を始める場所としては不適切。
- [ ] `config/rubric.yaml` の `categories` を公式10カテゴリに差し替えた
- [ ] `config/fields.yaml` をエントリーポータルの実カラムに合わせた
- [ ] 審査員2名の一致率を測り、人間同士が割れる軸を把握した
- [ ] 取りこぼし率の許容値を審査委員会が承認した
- [ ] 応募規約・審査規程に機械補助を使う旨を記載した
- [ ] 異議申立てがあったときに `run.jsonl` から説明する手順を決めた
- [ ] `pricing:` を実測値に直した

## 構成

| ファイル | 役割 |
|---|---|
| `config/rubric.yaml` | **審査基準の正本。** 審査委員が直接編集する |
| `config/fields.yaml` | 入力カラムのマッピングと、モデルに渡すフィールドの限定 |
| `award_triage/ingest.py` | CSV/JSONL 取り込み、言語判定、重複検出 |
| `award_triage/translate.py` | Claude による翻訳（原文は保持） |
| `award_triage/typesafe.py` | TypeSafe System One 呼び出し。1応募 = 1リクエスト |
| `award_triage/gate.py` | 振り分け。**迷ったら人間** |
| `award_triage/evaluate.py` | 効果測定と閾値スイープ |
| `award_triage/report.py` | 審査員向け単一HTMLコンソール |
| `award_triage/fake.py` | 鍵なしで動かすダミー判定 |

TypeSafe は公式 SDK ではなく文書化された HTTP エンドポイントを直接叩いている。
判定結果は審査記録として長く残るので、リクエストとレスポンスの形を自分のコードの
中で完全に把握できる状態を優先した。SDK に寄せる場合は `typesafe.py` だけ差し替える。

## テスト

```bash
pip install pytest && python3 -m pytest tests -q
```
