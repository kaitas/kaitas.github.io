---
layout: post
title: "TwitterやFacebookで表示されるOGPイメージをGithubPagesで簡単に実装する"
date: '2020-12-27 23:52:00'
author: aki
description: Github Pages で Twitter や Facebook で表示できるOGPを設定する話。 Github Pages, Jekyll 
preview: https://github.githubassets.com/images/modules/logos_page/Octocat.png
---

# OGP とは

OGPとは [Open Graph Protocol](https://ogp.me/) の略で、Webサイトのメタデータを記述する枠組みです。
ページのHEADセクションに決まった形式でHTMLを記述することにより、Twitterでリンク先のプレビューとして表示されるTwitterカードや、Facebookでのプレビューとして利用できます。

## Twitterカードでの表示例

[こんな感じに表示できます](https://twitter.com/o_ob/status/1342952856710627328)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/aad09d67-85fa-ebe1-9b27-af23420ba631.png)

## Facebookでのプレビュー表示の例
投稿やコメントなどでこんな感じに表示されます。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/3fea699c-c10e-e1ad-845c-7aeaa3639696.png)

## Twitter公式の説明
[Twitter公式のドキュメント](https://developer.twitter.com/ja/docs/tweets/optimize-with-cards/guides/getting-started)によると、TwitterのカードタグはOpen Graphのタグと似ており、タグやデータを複製することなくTwitterカードを簡単に生成できます。
Twitter側のカードプロセッサがページのタグを探す場合、最初にTwitter固有のプロパティがチェックされ、存在しない場合は、サポートされているOpen Graphのプロパティに移行します。そのため、両方を独立してページで定義することができるとともに、コンテンツやエクスペリエンスを記述するために必要なマークアップの重複を最小限に抑えることができます。

```html:Twitter公式にあるOGPの記述例
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@nytimesbits" />
<meta name="twitter:creator" content="@nickbilton" />
<meta property="og:url" content="http://bits.blogs.nytimes.com/2011/12/08/a-twitter-for-my-sister/" />
<meta property="og:title" content="A Twitter for My Sister" />
<meta property="og:description" content="In the early days, Twitter grew so quickly that it was almost impossible to add new features because engineers spent their time trying to keep the rocket ship from stalling." />
<meta property="og:image" content="http://graphics8.nytimes.com/images/2011/12/08/technology/bits-newtwitter/bits-newtwitter-tmagArticle.jpg" />
```

# Github Pages で 楽して OGP を使いたい

## このドキュメントの対象
このドキュメントでは Github Pages を使ったブログスタイルのサイトで、楽して OGP を使う方法を解説します。
読者としては HTMLと簡単なスクリプティングはわかるけれども「Wordpress 等でコンテンツ以外の部分をお任せにしてきてしまった書き手」が、そろそろ Wordpress に限界を感じて、Github Pagesで静的サイトに移行して（もしくはそれを検討しており）Markdown でブログを書こう、という方を対象にしています。

またこのドキュメントの想定する環境として、Github Environments に実装された Jekyll を利用します。
特殊なプラグインや外部のビルド環境は使用しません。
メンテナンス性を考えて、基本的にレイアウトファイルと Markdown 側だけで勝負します。
以下のサンプルでは、デフォルトの Github Pages のテーマの一つである [jekyll-theme-cayman](https://pages-themes.github.io/cayman/) を使用しています（お使いのテーマで動かない場合も読み替えて実装できるはずです）。
 


Github Pages の リポジトリの設定
- https://github.com/(username)/(repoName))/settings
ここの `Social Preview` でもサムネイル画像を設定できますし、[テンプレート](https://github.com/kaitas/aki.shirai.as/settings/og-template)があって 640×320px (最大は1280×640px) の画像で作成しろとあります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/990068cd-d41f-501a-30ef-1ab4a39705f6.png)

ここでプレビュー画像を設定して解決するような用途であれば、このドキュメントを読む必要はありません。
すべてのページで不細工なプレビュー画像が統一して表示されます。
ブログサイトの場合は、何を投稿しても同じように表示されてしまい、映えがありません。
各投稿にあわせてプレビュー画像を設定したいと思いました。

# テンプレのHTMLを操作する
まず `/_layouts` にある `default.html` を編集していきます（[オリジナルファイル](https://github.com/pages-themes/cayman/blob/master/_layouts/default.html)）。

Open Graphは `<html prefix="og: http://ogp.me/ns#">` を介して “og” RDFa Core 1.1 CURIEプレフィックスマッピングを指定することを推奨しています。
このように宣言は `html要素` に含めることができるようですので、

これを

`<html lang="{{ site.lang | default: "en-US" }}">`

こんな感じに

`<html lang="{{ site.lang | default: "en-US" }}" prefix="og: http://ogp.me/ns#">`

修正すれば、OGPをサポートすることを宣言できます。

続くヘッダ部分を修正していきます。
もともとのソースは Google Analytics へのサポートが書かれています。
これは `_config.yaml` で ``google_analytics: UA-168023643-1`` といったように指定すれば有効になる部分です。

```default.html
<!DOCTYPE html>
<html lang="{{ site.lang | default: "en-US" }}" prefix="og: http://ogp.me/ns#">
  <head>
    {% if site.google_analytics %}
      <script async src="https://www.googletagmanager.com/gtag/js?id={{ site.google_analytics }}"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '{{ site.google_analytics }}');
      </script>
    {% endif %}
    <meta charset="UTF-8">
```
``</head>`` より前ならどこでもいいので、こんな感じに拡張しましょう。

```default.html
<!DOCTYPE html>
<html lang="｛｛ site.lang | default: "en-US" }}" prefix="og: http://ogp.me/ns#">
  <head>
    <meta property="og:url" content="｛｛ site.url }}｛｛ page.url }}" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="｛｛ page.title }}" />
    <meta property="og:site_name" content="｛｛ site.title | default: site.github.repository_name }}" />
   ｛% if page.description %}
    <meta property="og:description" content="｛｛ page.description }}" />
   ｛% else %}
    <meta property="og:description" content="｛｛ site.description | default: site.github.project_tagline }}" />
   ｛% endif %}
(以下同じ)
※Jekyllに置き換えられてしまいますので ｛ を倍角で書いています
```
この修正を加えて Github に push して、しばらく待てばOGPは生成されます。
対象のページを開いてHTMLソースを確認しましょう。
``site.title`` は ``_config.yaml`` で指定した `title:` に置き換えられます。設定されていない場合はリポジトリ名になります。
``site.description`` も ``_config.yaml`` で指定した `description:` に置き換えられます。設定されていない場合はリポジトリに設定された説明書きになります。

``page.url`` と ``page.title`` は ``/_posts/`` に投稿されるであろう個々の markdown (.mdファイル) で自動で生成されます。やったね！
さらに ``page.description`` は、個々の markdwon のヘッダで設定します。例えばこんな感じです。

```2020-12-26-TokyoVeganGyoza.md
---
layout: post
title: "食レポ #東京ヴィーガン餃子"
date: '2020-12-26 23:52:00'
author: o_ob
description: 東京ヴィーガン餃子の食レポです
preview: https://akihiko.shirai.as/assets/2020/2020-12-26-TokyoVeganGyoza.jpg
---

# 東京ヴィーガン餃子

（以下本文）
```

# カスタムでプレビュー画像を設定する
実は上のmarkdownでプレビュー画像を設定していますが、このままだと肝心のTwitterカード等に画像が表示されません。
まずは ``preview`` (勝手に拡張した要素) が指定されていなかった場合のデフォルト画像を ``/img/card.png`` に設置しましょう。
ここでは以下のURLにデフォルトの画像を置いたとします。
- https://akihiko.shirai.as/img/card.png
``<head>`` 内に以下を書き足します。

```default.html
   {% if page.preview %}
    <meta property="og:image" content="{{ page.preview }}" />
   {% else %}
    <meta property="og:image" content="https://akihiko.shirai.as/img/card.png" />
   {% endif %}
```

各ページの markdown で ``preview:`` が指定されていないときはデフォルトの画像が表示されます。
なお、この画像を外部のサイトにすることもできますが、本来的な意味で推奨されている行為かどうかよくわかりません。

# Twitter対応と確認

さて、Twitterカード上ではどのように見えるかはTwitter公式の [Card Validator](https://cards-dev.twitter.com/validator/) で確認できます。
確認したいページのURLを張り付けて ``Preview Card`` で仕上がりを確認できます。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/ba146659-0bd0-851e-8a1e-e2d9a3e4f0da.png)

例示した[このページ](http://akihiko.shirai.as/2020/08/01/dear-my-father.html)では、ページ個々の `description` も `preview` も指定していないので、デフォルトの設定が表示されています。正しい動作。


冒頭で紹介した投稿の場合は [こんな感じに表示できます](https://twitter.com/o_ob/status/1342952856710627328)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/aad09d67-85fa-ebe1-9b27-af23420ba631.png)

Twitterカードとしてはサイト管理者と投稿の作成者のTwitterアカウントを組み込むことができるそうなのですが、指定するとしても特に見た目に影響はないようです。

```default.html
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:site" content="@o_ob" />
    <meta name="twitter:creator" content="@o_ob" />
```

また、1日に何度も Card preview を使っていると表示できないという状況になります。
記述に問題があるわけではないので慌てず騒がす別のアカウントでAPIにログインしなおすなどしてみましょう（慌てた）。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/a647a3a1-029d-20a7-fd97-911296bc49a9.png)



# Facebook対応と確認

Facebookのほうはこちらの「[シェアデバッガー](https://developers.facebook.com/tools/debug/)」で確認できます。

``このURLはまだFacebookでシェアされていません【新しい情報を取得】`` というボタンを押すと OGPタグを取得しに行きます。
更新するときは ``もう一度スクレイピング`` で再取得できます。

ただし最近のFacebookの仕様には落とし穴があって、`fb:_app_id` が正しく設定されていないと、
`プロパティがありません 次のプロパティは必須です: fb:app_id` という警告を表示します。
また正しく設定しないと *個々のページではなく* トップのページの情報を自動的に利用することがあるようです。

これだとちょっとカッコ悪いので、デベロッパーサイト [developers.facebook.com/apps/](https://developers.facebook.com/apps/) から「アプリを作成」として、適当なアプリケーション開発のIDを取得して以下のように設定します（取得するだけ、すべての項目を埋めなくてもOK）。

```
   <meta property="fb:app_id" content="4090212771xxxxx" />
```
※``4090212771xxxxx``は私のサイトなので、別の情報を取得して置き換えてください。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/e16dac54-ac8d-997e-53c3-3da095bb0973.png)

正しく `fb:app_id` が設定されていると、取得したURLが個々のページになります。

# まとめなど



- Github Pages でも OGP は簡単に表示できる
- Jekyll 書式は怖くない、`/_layout/default.html` に分岐を書こう
- [サイト変数](http://jekyllrb-ja.github.io/docs/variables/)を使おう
- 概要とプレビュー画像を各投稿の markdown に記述しよう
- FacebookはアプリIDの取得が必要

Github Pages での Jekyll は挙動が見えないので、なかなか掴みづらいですが、最近では Environments に状況が表示されるようになりました。うまく使いこなすとサーバコストも全くかからない爆速サイトが出来上がりますので、上手に活用したいと思います。

## 追記：QiitaのOGP画像はどうやって生成しているの？

ついでに調べてみたのですが QiitaのOGP（投稿のタイトルがプレゼン形式でつくやつ）は[imgix](https://qiita-user-contents.imgix.net/)をつかってCDN側で生成しているようです。

月間10ドルぐらいでサーバレス・転送不要になるならこれもありですね。

`og:img` って外部サイト参照でもまあいいのかな、という気持ちになります。
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/191291/c070f089-4472-ab6b-b0b7-2c0cf0306dcc.png)


# 関連・参考
- [https://akihiko.shirai.as/blog/](https://akihiko.shirai.as/blog/) 実際に運用しているサイト
- [https://github.com/kaitas/kaitas.github.io](https://github.com/kaitas/kaitas.github.io) 上記のリポジトリ
- [Twitterカード](https://developer.twitter.com/ja/docs/tweets/optimize-with-cards/guides/getting-started) Twitter公式情報(日本語)
- [Github Jekyll Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/site.github.md) siteのプロパティを探すときに便利
- [Jekyll:サイト変数](http://jekyllrb-ja.github.io/docs/variables/) 日本語です
- [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag/blob/master/docs/usage.md) 使ってないです
- [リアルタイム画像処理機能が充実した CDN、「imgix」 を試してみたらとても簡単で便利だった件](https://hyper-text.org/archives/2018/03/imgix_cdn.shtml)

# 次回予告/今後書くかもしれない記事
- Github Pages にGoogle Analyticsを仕込んでアクセス状況を把握する
- Github Pages での Twitter埋め込みを簡単に実装する
- Github Pages で作ったブログサイトを CloudFlare を使って HTTPS 対応にする

こういう記事、興味あるようでしたら [Twitter@o_ob](https://twitter.com/o_ob) でリクエストいただけると幸いです

- [qiita](https://qiita.com/o_ob/items/6c71bc783df428116ef8)

