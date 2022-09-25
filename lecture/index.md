---
# Lecture noteを置く場所
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: lecture
title: Lecture Notes
category: lecture
---

{% for lec in site.data.lecture %}


- {{ lec.year }}　({{ yt.title }})

  [![{{ yt.memo }}](https://img.youtube.com/vi/{{ yt.id }}/0.jpg)](https://www.youtube.com/watch?v={{ yt.id }})

{% endfor %}



# DHGS デジタルハリウッド大学 大学院 

year,month,day,conf,title,subtitle,web,ytid,slides

- [DHGSVR21](https://akihiko.shirai.as/dhgs/)

# Entertainment Systems

- [第12回VRC理系集会特別講演「メタバースと遊び研究の交差点」(2022/2/11)](https://akihiko.shirai.as/lecture/2022/02/12/Rikei-Meetup.html)
[![第12回VRC理系集会特別講演「メタバースと遊び研究の交差点」](https://img.youtube.com/vi/wGlwf8bsLQ4/0.jpg)](https://www.youtube.com/watch?v=wGlwf8bsLQ4)


# English


