---
layout: post
title: "GitHubを最強のToDo管理ツールにする"
date: "2021-11-14 23:59:59"
author: aki
description: エンジニア、もしくは非エンジニアにこそ親しんでほしいGitHubによる個人ToDo管理
preview: https://akihiko.shirai.as/{% link /assets/2021/ga.png %}
---

# ToDo 管理ツール、いろいろありますよね。

古くは [Remember the Milk](https://www.rememberthemilk.com/)、[Evernote](https://www.evernote.com/)、[Google Gmail の ToDo](https://support.google.com/tasks/answer/7675772?co=GENIE.Platform%3DDesktop&hl=ja)なども便利です。
しかし、たかだか ToDo を管理するのに有料のサービスを使いたくはありませんし、ToDo にはそこそこに個人的なセキュリティが求められる要素があります。

# Gmail ToDo だと管理が難しい例

Gmail の ToDo はメールに起因する ToDo には便利ですが、カンバン方式のワークフロー、メールに起因しない ToDo…例えば「**ああ〜、あのイベントの参加費を月末までに精算処理して領収書提出しなきゃ〜**」とか「**来月の LT での講演頼まれちゃったけど、上長伺いから広報チェックから事後記事公開まで ~~面倒くさい~~ たいへん～**」など、チェックボックス的な 1 段階の階層では片付かない ToDo にはあまり効率が良くありません。Gmail の ToDo は期限もメールそのものへのリンクも保持することができます。また子階層は 1 階層まで作れますが、だいたい 10〜20 の ToDo が常に存在している状態になると、期限付きの ToDo（多くは期限切れの ToDo）ばかりが上に行き、新規で作成される期限設定なしの ToDo が延々と下に連なって、画面外に行ってしまいます。

# エンジニア、もしくは非エンジニアにこそ親しんでほしい GitHub による個人 ToDo 管理

ソフトウェアエンジニアであれば GitHub の Issues は慣れ親しんでいるはずです。
このエントリーはその Issues と Projects の Automated Kanban ([カンバン方式](https://mba.globis.ac.jp/about_mba/glossary/detail-11756.html#:~:text=%E3%81%8B%E3%82%93%E3%81%B0%E3%82%93%E6%96%B9%E5%BC%8F%E3%81%A8%E3%81%AF%E3%80%81%E7%94%9F%E7%94%A3,%E5%BE%8C%E5%B7%A5%E7%A8%8B%E3%81%AB%E6%B8%A1%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82)) を非エンジニアでも ToDo として親しんでしまおう！というコンセプトで書いています。
(よって、プログラミングは一切行いません！)
個人の ToDo 管理で慣れてくれば、備忘録、読書リスト、クラブやサークル、家族内での ToDo 管理などに便利に使えるはずです。また GitHub 公式モバイルアプリもそこそこに使えます。
きっと GitHub の Wiki 機能なども便利になってくるはずです。
身近なところから DX を進めていきましょう！

# どうやってはじめるの？

必要なものはこちらのパブリックリポジトリに公開しておきました。
https://github.com/kaitas/ToDo

こちらは私自身が自分のリポジトリで[フォーク](https://qiita.com/o_ob/items/fd45fba2a9af0ce963c3#%E3%81%95%E3%81%8F%E3%81%A3%E3%81%A8%E5%AD%A6%E3%81%B3%E3%81%9F%E3%81%84%E4%BA%BA%E5%90%91%E3%81%91%E3%83%95%E3%82%A9%E3%83%BC%E3%82%AF%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)して使っている様子です。
![ToDoExample.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/dafa9cd6-2b45-fa3c-61eb-4f1807795d8e.png)

カンバン方式なので、左から ToDo が生まれ、右に行くにつれ終了に近づいていきます。
通常の Issue と同じく、Close すれば右に行きますし、私の場合は「今日中に終わらせたい」とか「処理中」とか「待ち！」といった中間のカンバン置き場(column)もあります。
完全に終了したものは「Archive」してアーカイブや「Remove」して削除します。

多くの ToDo は有機的に絡み合っていることがあります。細かな Task によって構成されている場合も多いですが、Issues の中でチェックボックス付きリスト `- []`で列挙することで見やすく管理することもできます。
![スクリーンショット 2021-11-14 午前1.32.46.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/8148fcd5-fa82-4929-17c1-dff9d78f9841.png)

他にも Issues や Projects の機能で期限や担当者などを割り当てたりすることもできますが、ここではよりシンプルで幅広い方々に使っていただけそうな使い方について解説していきます。
（面白い使い方がありましたらコメントやプルリクエストで教えてください）

## 準備(ふだん GitHub を使っている人向け)

準備作業は README にも記載してありますが、とってもシンプルなのです。

1. [このリポジトリ](https://github.com/kaitas/ToDo)をあなたのプライベートリポジトリにクローンします（パブリックリポジトリでテストしてからでいいです）。
2. `.github/ISSUE_TEMPLATE/config.yml` を編集して、ユーザー名とリポジトリ名を入力します。custom.md が実際のテンプレートとしてリンクされます。
3. Projects に「MyToDo」のような名前でプロジェクトを作成します。Automated Kanban を選ぶといいでしょう。
4. Issues で新しい課題を作成してみてください。custom.md を使ってクールな ToDo スタイルのフォームを作ってみましょう。
5. Project でオートメーションを設定し、課題のクローズを処理します。
6. これでもう余計な ToDo 管理アプリは不要！

ここまで読んでスルッと作業できる人は以下のセクションは読み飛ばして構いません。

## 非エンジニア向けに丁寧な解説

### 全体の流れ(初心者向け)

1. [このリポジトリ](https://github.com/kaitas/ToDo)をの[このあたり](https://github.com/kaitas/ToDo/blob/main/.github/ISSUE_TEMPLATE/config.yml)を見ながら進めます。新規リポジトリを「MyToDo」という名前で作成してください。
2. `.github/ISSUE_TEMPLATE/config.yml` を作成して、[このファイル](https://github.com/kaitas/ToDo/blob/main/.github/ISSUE_TEMPLATE/config.yml)を参考にしながらユーザー名とリポジトリ名だけ自分の情報を設定します。`.github/ISSUE_TEMPLATE/custom.md` が実際のテンプレートとして必要になりますので、こちらも[このファイル](https://github.com/kaitas/ToDo/blob/main/.github/ISSUE_TEMPLATE/custom.md)を参考にしながら同様に作成します。
3. Projects に「MyToDo」のような名前でプロジェクトを作成します。Automated Kanban を選ぶといいでしょう。
4. Issues で新しい課題を作成してみてください。custom.md を使ってクールな ToDo スタイルのフォームを作ってみましょう。
5. Project でオートメーションを設定し、課題のクローズを処理します。
6. これでもう余計な ToDo 管理アプリは不要！

### さくっと学びたい人向け「フォークについて」

（まずはじめに）GitHub には 公開（オープンソース）のリポジトリであるパブリックリポジトリと、非公開のプライベートリポジトリがあります。リポジトリの右上の「Fork」を使うと、この[ご用意したリポジトリ](https://github.com/kaitas/ToDo)をフォークして自分のものにできます。
![スクリーンショット 2021-11-14 午前1.21.09.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/40d05fdd-5044-5217-d89f-1b645aaf72a8.png)

フォークとは、食事で使う先の割れたフォークのことです。このオープンソースとして公開されているソースを自分の改造を施すために自分の公開リポジトリとしてコピーすることができます（クローンした上で公開）。
実験用途や公開で ToDo を管理したいのであればそれで構いませんが、多くの場合、ToDo は個人的な情報を管理することが多いと思いますので、内容を理解したらプライベートリポジトリで作り直すことをお勧めします。

なおリポジトリを後からパブリック → プライベートに変更することもできます。
![makeprivate.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/39d2fff2-da35-f002-09c3-3da1191c56aa.png)
最近の GitHub であれば無料プランでプライベートリポジトリを作れますので大丈夫です。ただ「破壊的な作業」であるので、最後に「ユーザ ID/リポジトリ名」を打って確認する必要があります。
※「大事な情報をパブリックリポジトリで管理して漏洩した！」といった事故にならないようにお気を付けて。

さて、以下の解説は、[新規リポジトリ作成](https://github.com/new)を行った流れで解説します。

### (1) [新規リポジトリ「MyToDo」作成](https://github.com/new)

![スクリーンショット 2021-11-14 午前1.39.46.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/8a84e65b-1c6b-9e8e-0ce8-6df613ad9f93.png)

`Repository name` と `Private` を選ぶところ以外は何も大事なところはありません。
`Initialize this repository with:` 以下は ReadMe やライセンスを設定するところですが、今回はチェックオフで問題ありません。
これでプライベートリポジトリができあがりました。
続いてコードの追加です。

### (2) config.yml と custom.md の作成

`.github/ISSUE_TEMPLATE/config.yml` の編集には特別なツールは不要です。テキストファイルはブラウザだけで追加編集することができます。
`[Add File]` からファイル名に `.github/ISSUE_TEMPLATE/config.yml` と打ってください。最初のドットを忘れずに。スラッシュ「/」を打つと深いディレクトリにファイルを作ることができます。`.github`ディレクトリは MacOS などでは 見えないディレクトリ扱い なので要注意です。 `.github/ISSUE_TEMPLATE` というディレクトリは GitHub 上の予約語で、ここに `config.yml` ファイルを作成して設定を書くことで GitHub 側が自動で処理をしてくれる約束になっています。もちろん無料で利用できます。

```config.yml:
blank_issues_enabled: true
contact_links:
  - name: Add new ToDo
    about: made by config.yml
    # edit {username} and {repo} for your environment
    url: https://github.com/kaitas/ToDo/issues/new?template=custom.md&projects=kaitas%2FToDo%2F1&labels=ToDo
```

最後の行の kaitas となっているところはご自身の GitHub ユーザ名 （https://github.com/ の後ろにある ID）、ToDo のところは先ほど作成したリポジトリ名に置き換えてください。= より後ろにも同じく 2 箇所あります。 %2F が / に置き換えられる URL 文字列になっています。

☆「わからない！」という質問をいただいたので画像で説明します！
![config.yml.note.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/33d000aa-bc2a-443d-4e5a-4b10657f1002.png)
↑ 最後の行の URL に注目です。

`name` や `about` の後ろの文字列は日本語可能です。また #　より後ろはコメント行ですので、好きにメモを書いておいて構いません。
編集が終わったら下の`[Commit Changes]`を押して保存しましょう。
☆ この作業は「コミット」といって保存よりも意味が大きいものですが、自分の個人的なリポジトリなので気にせずガンガンコミットしていきましょう。人生にコミットする ToDo です。

続いて、同じ `ISSUE_TEMPLATE` ディレクトリに `custom.md` というファイルを作成します。
中身はこちら(なくても動きます)

```custom.md:
---
name: ToDo template
about: See See .github/ISSUE_TEMPLATE/custom.md
title:  "[DATE]: [FEATURE NAME]"
labels: 'ToDo'
projects: 'kaitas/ToDo'
assignees: 'kaitas'
---


## Description

1. To
2. Do

- [ ]

```

これは旧来の GitHub Issues のテンプレートファイルの名残になっているものです。
適当に書き換えていただいて構いません！日本語も使えます
書き換えるためにもまずはコピペで貼り付けて、編集が終わったら下の`[Commit Changes]`を押して保存しましょう。

### (3) Projects に「MyToDo」を作成する

作成したリポジトリの上部に `Projects` というタブがあります。新規プロジェクトを作成し「MyToDo」という名前でプロジェクトを作成します。選択肢に `Automated Kanban`がありますので選んでください。これは、新しい Issue (課題, この場合は新しい ToDo)が終了した場合に次のカラムに自動移動してくれる処理が入る設定です。あとで変更もできます。

### (4) Issues で新しい課題を作成してみてください。

`[New Issue]` というボタンを押すと、見慣れない画面になったと思います。

![スクリーンショット 2021-11-14 午前2.00.46.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/5f708c07-ca27-f6e6-ed08-54b5f9d185b0.png)
上の `ToDo template` が旧来の custom.md によるカスタマイズの結果で、下の `Add new Todo` が今回のおすすめの方法です。 `[Open]`を押してみるとこんな感じに ToDo を作成できます。

例として「イベントの精算をする」という ToDo を作成してみます。

![スクリーンショット 2021-11-14 午前2.07.43.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/b047c2ec-ab0a-540f-2181-4dc951532622.png)

こんな感じの Issue が作成されました。
![スクリーンショット 2021-11-14 午前2.10.03.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/decbf2d7-fe23-7b29-562c-a273682f48b4.png)
GitHub の Issues に慣れた人であれば、アサインやラベル、マイルストーンの設定もしていいと思います。
ここで「Projects」がきっちり設定されていることに注目です。先程の `config.yml` の中で URL 文字列で設定したプロジェクト名が、自動で設定されるというところがとても嬉しい実装になっているので、慣れてきたら他のプロジェクト（例えば経理とか個人資産とか家族の備忘録とか）を同じリポジトリでプロジェクトを分けてどんどん作ってみるといいと思います。

### (5) Project ビュー

![スクリーンショット 2021-11-14 午前2.14.49.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/e4e33761-9b52-a3cb-2d74-af7e77cc0b00.png)
`[To Do]`のタブの一番下に先程追加した Issue があります。初期に存在するカードは読んだら「…」で Remove して消してしまって構いません。

チェックボックスを ON にすると、タスクが進行します。
![スクリーンショット 2021-11-14 午前2.16.45.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/3f9e7da6-01a0-ef49-c148-368f3a583720.png)
`[Close issue]` すると自動的にカードが `[Done]` のカラムに移動します。
![スクリーンショット 2021-11-14 午前2.16.56.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/9021e235-0875-f282-5881-7ea4372b7c85.png)
詳細を追記したり、編集したい時は `[Go to issue for full details]` を押せば、新しいタブで Issue の詳細が開きます。

オートメーションがうまく動いていない時は「Manage」を設定し、課題のクローズ時の処理を設定します。

これでもう余計な ToDo 管理アプリは不要です！
毎日の ToDo 管理で GitHub と慣れ親しみましょう！

## おまけ

ちなみに、毎日これで ToDo 管理していると GitHub のユーザトップページに「草」が生えます。
![スクリーンショット 2021-11-14 午前2.21.22.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/ee6467e2-fa71-1336-26a2-e2b8c1881dbd.png)
これで`つよつよエンジニア`を証明できるわけではありませんが、毎日の無味乾燥な ToDo 消化がちょっと楽しくなってくるのではないでしょうか？

ご感想や改造・機能追加などはぜひプルリクエストで教えてください！
（初心者向け解説なので、あまり複雑にはしないのが良いかもですが）
皆様のご感想もお待ちしております

## 祝！10,000 view ＆ 100 LGTM！

おかげさまで [10,000 view](https://twitter.com/o_ob/status/1465286252253806594) 、そして [100LGTM 突破](https://twitter.com/qiita_milestone/status/1463311535313506308) となりました！
せっかくなので、いくつか追加 Tips を紹介しておきます。

### Tips: チェックボックスを使いこなそう

Issues の Markdown を書くときに

```- []

```

と書くと、チェックボックスが作れます。チェックボックスは Kanban 上では `4 of 15 tasks` といった形で達成状況を表示できるので便利です。
![tasks.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/a514ccfb-1cff-a8aa-d65a-b717983a5407.png)

### Tips: ナイスな Issues を作ろう

上記のチェックボックス化することで、Issue の切り方も変わってくると思います。
多くの「やらなきゃならないこと」に押しつぶされるときは、ToDo が多岐に渡っている上に今すぐ処理できず、さらに複雑に絡まっていることが多いです。これをソフトウェア開発と同じツールで自分宛の Issue にしてみると、意外とナイスな Issue の切り方ができるし、何度も起きそうな案件はテンプレ化して、ちょうどいい時に進めていける感じがします。
自分の場合は、これに加えて Google Apps Script (GAS) をよく使用します。何度も起きる案件はスプレッドシートやスクリプトで処理することを考えましょう。特に自分ではなく他者がデータや判断を持っている案件はフォーム化することで解決することは多いです。

### Tips: 新しいテンプレを作ろう

`.github/ISSUE_TEMPLATE/` のディレクトリには Issues のテンプレを作ることができます。そして Issues 管理はモバイル版の GitHub でも操作がしやすいのです。
例えばこれはモバイル版 Github で見た「講演を依頼されてから資料公開まで」のテンプレです。

![FFXARataUAkj_U_.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/11b9ed7e-91fe-ddc8-a34b-057dcf585566.jpeg)
コードサンプルとしてはこんな感じです。

```.github/ISSUE_TEMPLATE/kouen.md:
---
name: 講演依頼
about: 講演依頼ワークフロー
title:  "講演準備 mm/dd"
labels: 'ToDo'
projects: '(your_id)/my-todo'
assignees: '(your_id)'

---
- [ ] 講演依頼
- [ ] タイトル決定
- [ ] Slack伺い
- [ ] JIRA起票
- [ ] 事前打ち合わせ
- [ ] ゴール設定
- [ ] [Slides準備]()
- [ ] 動画準備
- [ ] 講演当日
- [ ] PDFのSlideShare公開
- [ ] 動画の公開
- [ ] 字幕の修正
- [ ] note等公開

## 講演依頼を貼り付け
```

GitHub 上は[こちら](https://github.com/kaitas/ToDo/blob/main/.github/ISSUE_TEMPLATE/pitch.md)

質問などもお気軽にどうぞ！ハッピー ToDo 管理ライフ！
