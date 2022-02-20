# Books

{% for book in site.data.books %}

1. "{{ book['タイトル(日本語)'] }}" {{ book['著者(翻訳者)(日本語)']}}, {{book['総ページ数']}} pages, 出版日 {{ book['出版年月'] }} ({{ book['出版者・発行元(日本語)'] }}), ISBN:{{book['ISBN']}}

{% endfor %}

# Awards

{% for aw in site.data.awards %}

1. _{{ aw['賞名(英語)'] }}_, {{ aw['受賞者・グループ(英語)']}}, {{ aw['タイトル(英語)']}} given by {{ aw['授与機関(英語)']}} at {{aw['受賞年月']}}

{% endfor %}

# Association Memberships

<!--アクション名,アクションタイプ,類似業績マージ優先度,ID,所属学協会名(日本語),所属学協会名(英語),年月(From),年月(To),URL,主要な業績かどうか,公開の有無-->

{% for aso in site.data.association_memberships %}

- {{ aso['所属学協会名(日本語)'] }}

{% endfor %}
