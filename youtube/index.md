---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: youtube
title: YouTube
---

{% for yt in site.data.youtube %}

- {{ yt.memo }}

  [![{{ yt.memo }}({{ yt.year }})](https://img.youtube.com/vi/{{ yt.id }}/0.jpg)](https://www.youtube.com/watch?v={{ yt.id }})

{% endfor %}
