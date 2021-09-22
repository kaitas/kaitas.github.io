---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
title: YouTube
---

[![KIDS WORKSHOP 2021 "みんなで(バーチャル)世界旅行" Digest](https://img.youtube.com/vi/UcuHIW3HGP4/0.jpg)](https://www.youtube.com/watch?v=UcuHIW3HGP4)

<div class="YouTube">
{%- if page.title -%}
<h1 class="page-heading">{{ page.title }}</h1>
{%- endif -%}
{{ content }}
{% for yt in site.data.youtube %}
[![{{ yt.title }}](https://img.youtube.com/vi/{{ yt.id }}/0.jpg)](https://www.youtube.com/watch?v={{ yt.id }})
{% endfor %}
</div>
