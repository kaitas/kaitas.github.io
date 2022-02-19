---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: defalut
title: Books
---

{% for book in site.data.books %}

{{book}}

- {{ book['タイトル(日本語)'] }}　({{ book[出版者・発行元(日本語)] }})

{% endfor %}

アクション名,アクションタイプ,類似業績マージ優先度,ID,タイトル(日本語),タイトル(英語),担当区分,著者(翻訳者)(日本語),著者(翻訳者)(英語),原著者(日本語),原著者(英語),担当範囲(日本語),担当範囲(英語),出版者・発行元(日本語),出版者・発行元(英語),概要(日本語),概要(英語),出版年月,総ページ数,担当ページ,記述言語,査読の有無,著書種別,国際共著,DOI,ISBN,URL,URL2,主要な業績かどうか,公開の有無
