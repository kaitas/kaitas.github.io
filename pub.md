---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: defalut
title: Publications
---

# Books

{% for book in site.data.books %}

- "{{ book['タイトル(日本語)'] }}", {{ book['著者(翻訳者)(日本語)']}}, {{book['総ページ数']}} pages, 出版日 {{ book['出版年月'] }} ({{ book['出版者・発行元(日本語)'] }}, ISBN:{{book['ISBN']}}
  {% endfor %}
