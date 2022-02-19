# Books

{% for book in site.data.books %}

- "{{ book['タイトル(日本語)'] }}" {{ book['著者(翻訳者)(日本語)']}}, {{book['総ページ数']}} pages, 出版日 {{ book['出版年月'] }} ({{ book['出版者・発行元(日本語)'] }}), ISBN:{{book['ISBN']}}
  {% endfor %}
