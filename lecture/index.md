---
# Lecture noteを置く場所
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
# category: lecture
layout: lecture
title: Lecture Notes
---

{% for lec in site.data.lecture %}


- {{ lec.year }}　({{ lec.title }})

  [![{{ lec.title }}](https://img.youtube.com/vi/{{ lec.ytid }}/0.jpg)](https://www.youtube.com/watch?v={{ lec.ytid }})

{% endfor %}

year,month,day,conf,title,subtitle,web,ytid,slides

2021,11,11,GREE Tech Conf 2021,GREE VR Studio Laboratory「XR-UX Devプロジェクト」の成果紹介,q3gdhHtcnmI,ShortSession-7,https://techcon.gree.jp/2021/session/ShortSession-7,q3gdhHtcnmI,,https://www.slideshare.net/vrstudiolab/gree-vr-studio-laboratory-xrux-dev-greetc-2021nov11/
2020,9,18,GREE Tech Conf 2020,VTuber・XRライブエンタメ駆動の研究開発 - GREE VR Studio Laboratory のR2D,ShortSession-9,https://techcon.gree.jp/2020/session/ShortSession-9,KhOgvaF8-oo,

DHGS デジタルハリウッド大学 大学院 


- [DHGSVR21](https://akihiko.shirai.as/dhgs/)

Entertainment Systems

- [第12回VRC理系集会特別講演「メタバースと遊び研究の交差点」(2022/2/11)](https://akihiko.shirai.as/lecture/2022/02/12/Rikei-Meetup.html)
[![第12回VRC理系集会特別講演「メタバースと遊び研究の交差点」](https://img.youtube.com/vi/wGlwf8bsLQ4/0.jpg)](https://www.youtube.com/watch?v=wGlwf8bsLQ4)



