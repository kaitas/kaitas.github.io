---
layout: default
---

Data is reterieved from [researchmap.jp](https://researchmap.jp/akihiko)

# Books

{% for book in site.data.books %}

1. _{{ book['タイトル(日本語)'] }}({{ book['タイトル(英語)'] }})_ {{ book['著者(翻訳者)(日本語)']}}{% if book['担当区分'] contains "single_work" or book['担当区分']== "single_work" %}単著{% endif %}, {{book['総ページ数']}} pages, 出版日 {{ book['出版年月'] }} ({{ book['出版者・発行元(日本語)'] }}), ISBN:{{book['ISBN']}}

{% endfor %}

# Awards

{% for aw in site.data.awards %}

1. _{{ aw['賞名(英語)'] }}_, {{ aw['受賞者・グループ(英語)']}}, To _{{ aw['タイトル(英語)']}}_, given by {{ aw['授与機関(英語)']}} at {{aw['受賞年月']}}

{% endfor %}

# Published Papers

> アクション名,アクションタイプ,類似業績マージ優先度,ID,タイトル(日本語),タイトル(英語),著者(日本語),著者(英語),担当区分,概要(日本語),概要(英語),出版者・発行元(日本語),出版者・発行元(英語),出版年月,誌名(日本語),誌名(英語),巻,号,開始ページ,終了ページ,記述言語,査読の有無,招待の有無,掲載種別,国際・国内誌,国際共著,DOI,ISSN,eISSN,URL,URL2,主要な業績かどうか,公開の有無

{% for p in site.data.published_papers %}
{%comment%} https://shopify.github.io/liquid/basics/types/#string {%endcomment%}

{% unless p['タイトル(日本語)'] == empty %}

1. {{p['著者(英語)']}}, {{p['タイトル(英語)']}}, {{p['誌名(英語)']}}, Vol.{{p['巻']}}, No.{{p['号']}}, pp. {{p['開始ページ']}}--{{p['終了ページ']}}, {{p['出版者・発行元(英語)']}}, {{p['出版年月']}}.

{% else %}

1. {{p['著者(日本語)']}}, {{p['タイトル(日本語)']}}, {{p['誌名(日本語)']}}, {{p['巻']}}巻, {{p['号']}}号, pp. {{p['開始ページ']}}--{{p['終了ページ']}}, {{p['出版者・発行元(日本語)']}}, {{p['出版年月']}}.

{% endfor %}

# Association Memberships

<!--アクション名,アクションタイプ,類似業績マージ優先度,ID,所属学協会名(日本語),所属学協会名(英語),年月(From),年月(To),URL,主要な業績かどうか,公開の有無-->

{% for aso in site.data.association_memberships %}

- {{ aso['所属学協会名(日本語)'] }}

{% endfor %}
