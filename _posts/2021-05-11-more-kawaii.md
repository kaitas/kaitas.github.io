---
layout: post
title: "海外論文紹介：More Kawaii than a Real-Person Streamer - コミュニティがVTuberとどう関わり、どう認識しているか"
date: "2021-05-11 23:52:00"
author: aki
description: More Kawaii than a Real-Person Streamer - Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers
preview: http://img.youtube.com/vi/IuMhbo0MZrU/hqdefault.jpg
categories: Research
---

国際会議[CHI2021](https://chi2021.acm.org/) にて、興味深い論文「[リアルな配信者よりもカワイイ ：オタクコミュニティがバーチャル YouTuber とどのように関わり、どのように認識しているか](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)」（原題："More Kawaii than a Real-Person Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers"）がありましたので、著者の Zhicong Lu さんに Twitter 上でご許可をいただいて日本語翻訳させていただきました。日本発祥である VTuber 文化が、現在、どのように受容されているかを垣間見ることができます。また日本の学術コミュニティにおいても、より VTuber や SNS、配信者文化に関する学術的研究が活発になる事を期待します。

## Acknowledgements

This is authorized Japanese translation of "More Kawaii than a Real-Person Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers".
[Original PDF](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)

I appreciate to the original authors, specially to Prof. Zhicong Lu for his great contribution and agreement for this translation.

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392067792078213125">date</a></blockquote>

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/luzc08/status/1392134253211799552">date</a></blockquote>

### Credits

> More Kawaii than a Real-Person Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers
> Zhicong Lu, Chenxinran Shen, Jiannan Li, Hong Shen, Daniel Wigdor
> [https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)

- CHI '21: The 2021 ACM CHI Conference on Human Factors in Computing Systems
- Session: Cross-cultural Design / Reflection, Design, & Participation

> CHI ’21, May 8–13, 2021, Yokohama, Japan
> © 2021 Copyright held by the owner/author(s). Publication rights licensed to ACM.
> This is the author’s version of the work. It is posted here for your personal use. Not for redistribution. The definitive Version of Record was published in CHI Conference on Human Factors in Computing Systems (CHI ’21), May 8–13, 2021, Yokohama, Japan, https://doi.org/10.1145/3411764.3445660.

### About CHI2021

CHI は ACM の国際会議で、世界中の研究者や実務者が集まる最新のインタラクティブ技術について議論する歴史ある会議です。CHI は「カイ」と発音し、一般的に[HCI](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction)(Human Computer Interaction)の分野で最も権威のあるものと考えられており、毎年何千人もの国際的な参加者が集まります。今回横浜で開催された、CHI2021 は初めてのオンライン・バーチャル・カンファレンスとして開催されました。CHI2021 のテーマは「Making Waves, Combining Strengths」。HCI における最新の発見や進歩を取り上げ、既存の状況を揺るがすような波を起こすことを著者や参加者に促進し、CHI とは、様々な人が様々な視点から力を結集するプラットフォームであると考えています（[CHI2021](https://chi2021.acm.org/)ウェブサイトより）。

## 「リアルな配信者よりもカワイイ ：オタクコミュニティがバーチャル YouTuber とどのように関わり、どのように認識しているか」

## 概要

ライブ配信はますます人気が高まっており、ほとんどの配信者は実際の姿を見せています。しかし、2D または 3D のバーチャルなアバターに人間が声を吹き込んだ「バーチャル YouTuber（VTuber）」がライブ配信者として登場し、東アジアで視聴者数を伸ばしていることがわかっています。先行研究では、多くの視聴者が実在の人物であるストリーマーとのリアルな対人関係を求めていることが明らかになっていますが、VTuber のライブストリームの魅力や、実在の人物であるストリーマーとの受け止め方の違いについては、現在のところ不明です。私たちは、視聴者が VTuber とどのように関わり、アバターの背後にいる声優（中の人）のアイデンティティをどのように認識しているのかを理解するために、インタビュー調査を実施しました。その結果、バーチャル・アバターはユニークなパフォーマンスの機会をもたらし、その結果、VTuber の行動に対する視聴者の期待や解釈が異なることが明らかになりました。視聴者は、VTuber のアバターが声優から離れていることを意図的に支持していた。我々は、視聴者の認識と態度のニュアンスを明らかにし、VTuber の実践が一般的なライブ配信の理解に与える影響をさらに議論します。

<!--
Abstract
Live streaming has become increasingly popular, with most streamers presenting their real-life appearance. However, Virtual YouTubers (VTubers), virtual 2D or 3D avatars that are voiced by humans, are emerging as live streamers and attracting a growing viewership in East Asia. Although prior research has found that many viewers seek real-life interpersonal interactions with real-person streamers, it is currently unknown what makes VTuber live streams engaging or how they are perceived differently than real-person streamers. We conducted an interview study to understand how viewers engage with VTubers and perceive the identities of the voice actors behind the avatars (i.e., Nakanohito). The data revealed that Virtual avatars bring unique performative opportunities which result in different viewer expectations and interpretations of VTuber behavior. Viewers intentionally upheld the disembodiment of VTuber avatars from their voice actors. We uncover the nuances in viewer perceptions and attitudes and further discuss the implications of VTuber practices to the understanding of live streaming in general.
-->

### CCS CONCEPTS

• Human-centered computing → Human computer interaction (HCI); Empirical studies in HCI.

### KEYWORDS

virtual idols, live streaming, social media, user engagement, virtual YouTuber

### ACM Reference Format:

Zhicong Lu, Chenxinran Shen, Jiannan Li, Hong Shen, and Daniel Wigdor. 2021. More Kawaii than a Real-Person Live Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers. In CHI Conference on Human Factors in Computing Systems (CHI ’21), May 8–13, 2021, Yokohama, Japan. ACM, New York, NY, USA, 14 pages. https://doi.org/10.1145/3411764.3445660

Pre-recorded Presentations for the ACM CHI Virtual Conference on Human Factors in Computing Systems, May 8-13, 2021

## 1 はじめに

Twitch，YouTube，TikTok などのライブストリーミングの登場により，
実生活の体験 [40, 42, 59]，ライブイベント [23, 58]，創作活動 [15, 41, 44]，教育コンテンツ [14, 43, 44]，ビデオゲームのプレイ [24]などのライブ映像を共有することが，世界中でますます普及しています．
ライブストリーミングのライブチャットやバーチャルギフティングの機能により、視聴者はストリーマーや他の視聴者とテキストや絵文字などのモダリティでリアルタイムに対話することができます。このような双方向性の高さが、ストリーマーのコミュニティ形成を促進し、結果的にライブストリーミングは、視聴者が楽しみながらオンデマンドで情報を取得できる魅力的なメディアとなっている。ライブ・ストリーミングに関する先行研究では、ほとんどが実在の人物によるライブ・ストリーミングに焦点が当てられており、ライブ・ストリーミングがもたらす「リアルさ」が、ライブ・ストリーミングを魅力的で人気のあるものにする重要な要因であることがわかっています[23, 24, 44]。

しかし、東アジアにおけるバーチャル YouTuber（VTuber）の台頭は、これと矛盾するように思えます。バーチャル YouTuber やバーチャルストリーマーは、人間が声を当てた 2D または 3D のバーチャルなアバターであるため、ユニークなコンテンツ制作者のカテゴリーと言えます（図 1）。このようなストリーマーは，YouTube やニコニコ動画[13]，Bilibili[4]などで，熱心なファンを持ち，企業とのスポンサー契約を結んだ有名人になりつつあります．VTuber の人気は高く、日本や中国の多くの企業が「バーチャル・タレント」に多額のリソースを投じており、これらのアバターを管理するタレント・エージェンシーの設立につながっています。また、Instagram では、270 万人以上のフォロワーを持つ Lil Miquela のようなバーチャルインフルエンサーが登場しており[6]、このようなデジタルアバターの公人化は、東アジアだけの現象ではない。

2016 年以降、東アジアでは VTuber の人気が高まっていますが、ライブ映像の臨場感やリアルタイムでの対人交流を重視するメディアであるライブ・ストリーミングを介して VTuber を視聴する際に、視聴者がなぜ、どのようにエンゲージメントを高めるのかについては、理解が浅いです。また、バーチャルアバターの配信者と実在の人物の配信者の違いや、アバターの背後にいる声優や中の人のアイデンティティや存在感を、視聴者がどのように認識しているのかも不明である。このように、VTuber のライブ配信の動機や視聴行動を明らかにすることは、これまで実在の人物を対象としてきた HCI のライブ配信研究の主流を、バーチャルアバターの配信者や、ライブ配信とアニメやコミックなどのサブカルチャーの融合であるオタク・コミュニティの研究に広げることができる。

このような知識は、実在の人物とバーチャルアバターの両方のストリーマーをサポートする将来のライブストリーミングインターフェースの設計にも役立つでしょう。本研究では、VTuber の社会技術的現象と、そのジャンルやコミュニティに特有の慣習、機会、課題をよりよく理解するために、VTuber のライブストリームを視聴した経験が豊富なオタクコミュニティの VTuber 視聴者 21 名（VTuber を 1 年以上視聴しており、少なくとも週 1 回は視聴している）を対象に、インタビュー調査を実施した。インタビューの結果、VTuber や _なかのひと_ (Nakanohito) たちは、バーチャル・アバターを媒介にすることで、現実の姿やアイデンティティを明かすことなく、視聴者を巻き込み、コミュニティを形成し、視聴者の支持を得ることができることがわかった。

バーチャル・アバターは、ユニークなパフォーマンスの機会をもたらし、その結果、VTuber の行動に対する視聴者の期待や解釈が異なる。例えば、視聴者はバーチャルアバターとの間に距離を感じ、VTuber の攻撃的な言葉や「愚かな」行動に寛容であることが、実在するストリーマーと比較して明らかになった。また、分析の結果、視聴者は VTuber の完璧なイメージを頭の中に維持するために、なかのひとがアバターから離脱しているという信念を意図的に維持しているものの、労働争議が発生した際には、なかのひとのことを気にかけていることが明らかになった。今回の調査結果をもとに、ライブストリーミングにおけるリアルとバーチャルの境界線の曖昧さと変化、VTuber 事務所となかのひとの労働関係、そして今後のストリーミングプラットフォームにおけるアイデンティティ管理、透明性、公平性の必要性について考察します。このように、私たちの HCI への貢献は、i)VTuber のコミュニティの実践と動機、および中国の社会的・文化的文脈の中で彼らがどのようにこれらの実践に従事しているかについてのニュアンスのある説明、ii)VTuber と現実の人間のストリーマーに対する視聴者の認識、および仮想アバターの背後にいる声優について視聴者が抱いている信念の理解、iii)VTuber の実践がライブストリーミングとアバターベースの社会的相互作用に与える影響、です。

<!--
1 INTRODUCTION Sharing live video of real life experiences [40, 42, 59], live events [23, 58], creative activities [15, 41, 44], educational content [14, 43, 44], or playing video games [24] is becoming increasingly widespread around the world, largely due to the emergence of live streaming on Twitch, YouTube, TikTok, etc. The live chat and virtual gifting features of live streaming enable viewers to interact with streamers and other viewers via text, emoji, or other modalities in real-time. This high degree of interactivity facilitates the building  of the streamer’s community and results in live streaming being an engaging medium for viewers to have fun and acquire information on demand. Prior research on live streaming has mostly focused on realperson live streams, finding that the “realness” afforded by live streaming is the key factor that makes them engaging and popular [23, 24, 44]. However, the emerging trend of virtual YouTubers (VTubers) in East Asia seems to contradict this. Virtual YouTubers or virtual streamers are a unique category of content creators because they are virtual 2D or 3D avatars that are voiced by a human (Figure 1). Such streamers are becoming celebrities on YouTube, NicoNico [13], and Bilibili [4], with dedicated fan bases and corporate sponsorship deals. VTubers are becoming so popular that many companies in Japan and China are investing a large amount of resources in “virtual talent” and have led to the establishment of talent agencies to manage these avatars. Such digital avatar public figures are also not a phenomenon only constrained to East Asia, since Instagram has seen emerging virtual influencers such as Lil Miquela, who has over 2.7 million followers [6]. Although VTubers have been gaining traction in East Asia since 2016, there is a limited understanding of why and how viewers become engaged while watching VTubers through live streaming, a medium which emphasizes the authentic nature of live video and real-time, interpersonal interactions. It is also unknown how viewers perceive the differences between virtual-avatar streamers and real-person streamers, and how they perceive the identity and presence of the voice actor or Nakanohito who is behind the avatar. Uncovering specific motivations and viewing practices of VTuber live streaming could expand mainstream live streaming research in HCI, which has mostly focused on real-person streamers, to studying virtual-avatar streamers and the emerging fusion of live streaming and the subcultures of anime and comics, i.e., the Otaku community. Such knowledge could also inform the design of future live streaming interfaces that support both real-person streamers and virtual-avatar streamers. To better understand the socio-technological phenomenon of VTubers and its genreand community-specific practices, opportunities, and challenges, we conducted an interview-based study with 21 VTuber viewers from the Otaku community who had extensive experience watching VTuber live streams (i.e., they had watched VTuber for over a year and watched at least once per week). The interviews revealed that through the mediation of virtual avatars, streamers or Nakanohitos can engage viewers, build communities, and gain viewers’ support without disclosing their real life appearance or identity. Virtual avatars bring unique performative opportunities which result in different viewer expectations and interpretations of VTuber behavior. For example, viewers felt more distance between themselves and the virtual avatars and showed tolerance to VTubers’ offensive language and ‘stupid’ behavior compared to real-person streamers. The analysis also revealed that although viewers intentionally maintained beliefs about Nakanohito’s disembodiments from their avatars so that viewers could maintain perfect images of VTubers in their minds, they still cared about Nakonohitos when labor disputes arose. Drawing on our findings, we discuss the blurry and ever-changing line between the real and virtual in live streaming, labor relationships between VTuber agencies and Nakanohitos, and the need for future streaming platforms to support identity management, transparency, and fairness. Thus, our contributions to HCI are: i) a nuanced description of the practices and motivations of VTubers’ communities and how they engage in these practices within the social and cultural contexts of China, ii) an understanding of viewers’ perceptions of VTubers versus real-person streamers and the beliefs viewers hold about the voice actors behind virtual avatars, iii) the implications of VTubers practices to live streaming and avatar-based social interactions.
-->

## 2 BACKGROUND AND RELATED WORK

We first describe the background of VTubers, and then review research into avatar-based virtual idols and social interactions in virtual worlds, followed by a review of live streaming motivations and practices.

### 2.1 Background

Over the past 30 years, Japanese manga, anime, and video games have gained widespread popularity in East Asia and more generally, worldwide. This has given rise to a billion dollar industry and a unique Otaku subculture [27] that is characterized by a strong enthusiasm for manga, anime, and related subcultures. Concurrently, Japanese idols have also cultivated large and passionate fan bases, due in large part to their manufactured images and personalities [20]. VTubers have emerged as an innovative cultural phenomenon as these trends have begun to intertwine. VTubers originated in Japan and have rapidly gained international popularity since their first appearance in 2016. By midJanuary 2019, there were more than 10,000 active VTubers around the globe [2], and more than 600 VTubers had over 10,000 followers and had attracted millions of views [3]. The influence of VTubers has quickly grown beyond the Otaku subculture. The first VTuber, Kizuna Ai, for example, was chosen as the ambassador of an international culture campaign by the Japanese National Tourism Organization in 2018 [68].

A VTuber is an animated virtual avatar that delivers performances in live video streams or recorded videos. The avatar is often voiced by an actor, who is referred to as a Nakanohito (中の人) in Japanese. VTubers typically stream with half-body 2D avatars, which are created with tools such as Live2D [45] that capture the actor’s facial movements and drive the avatar’s facial expressions (Figure 1). The motions of other body parts of the avatar can be triggered within such programs using commands sent from desktop computers. VTubers who have access to full-body motion capture systems can perform with 3D avatars. This allows them to have a higher range of motion with the avatar’s body. Vtubers also often read comments that viewers post in-stream and respond to them, similar to the practices of real-person streamers. VTubers often have a unique persona, e.g., Kizuna Ai has the appearance of a 16-year-old brunette animated girl, who was a recently-developed advanced artificial intelligence and her words and actions were naive, imitating the behavior of an AI agent, although her performance was actually driven by several Nakanohitos.

VTubers can be operated by an individual or an agency. Some for-profit VTuber agencies, such as Nijisanji [49] and Hololive [26], have more than 20 VTubers under contract in parallel. So far, corporate-operated VTubers have attracted larger viewership than individual-operated ones. In January 2020, for example, 94 out of the 100 most followed VTubers on YouTube were run by agencies [3]. This is likely because corporate-run VTubers are overall better supported because they have professionally designed and engineered avatars, use more expensive motion capture equipment to generate more realistic avatar movement, and have stronger promotion and marketing. The Nakanohitos (i.e., voice actors) of individual-operated VTubers typically have full ownership over their VTuber projects. In contrast, VTuber agencies own their VTubers and claim that they are their intellectual property. Employees of these agencies have limited control over changes to the overall operation of their avatar, such as future program planning or if another Nakanohito will take over their avatar, which can potentially lead to labor disputes. China is one of the most important VTuber markets. A large number of VTubers operate official channels on BiliBili, a video platform that is highly popular among young generations [4]. On BiliBili, there are VTubers designed and managed by Chinese and Japanese individuals and agencies [9]. To overcome the language barriers between streamers and viewers, Japanese-speaking VTubers stream with real-time Chinese subtitles, or use simpler words to communicate with Chinese fans. Dedicated VTuber fans also curate stream highlights and form online social groups on social networking sites and forums to discuss VTuber-related topics, e.g., the National Geographic of Azeroth (NGA) forum [51]. By contributing a study of viewers of VTubers in China, we aim to capture both how viewers engage with VTubers and how VTubers are appropriated in China, where live streaming is a predominate activity for Internet users [44].

### 2.2 Avatar-Based Virtual Idols and Social Interactions in Virtual Worlds

The history of avatar-based virtual idols can be traced back to the mid-1990s. The first two avatar-based idols, Kyoko Date and Yuki Terai, were created in Japan in 1996-1997. In 2007, Hatsune Miku was released by Crypton Future Media. Building on Yamaha’s software engine Vocaloid, and illustrated as a 16-year-old female character, Miku soon became an international phenomenon. Scholars have examined avatar-based idols such as Miku from a feminist perspective, arguing that the female representation and the essentializing of gender perpetuate female stereotypes, even in virtual worlds [34, 35]. Others have examined the fan communities around avatar-based idols, noting that although being virtual has limited idols’ capacities to emulate real people, independence from a living body has cultivated a new type of relationship between fans and the idol [5] — amateur and professional musicians, animators, artists, and fans formed a distributed global network and recreated and remixed Miku for cultural expression through large-scale collaborations and peer-production, which differed from the corporate control of Miku’s franchise [36, 67]. Despite the international success of recent avatar-based idols like Miku, these virtual idols have arguably never achieved real-time interactivity with their fans. Our work contributes to this line of research by focusing specifically on VTuber live streaming, where VTubers interact with viewers in real time, harnessing both the spontaneity and unpredictability of live performances.

Also relevant is avatar-based social interactions in virtual worlds (VWs), which has been a key theme in HCI [16]. Past research has offered insights into user perception in game-oriented VWs such as World of Warcraft (e.g., [12, 46]) and social-oriented VWs such as Second Life (e.g., [47, 48]). Users usually enter these VWs through virtual bodies (i.e., avatars) that are created and controlled by them, and interact with each other using their avatar in a variety of social activities. Through online interactions in VWs, users construct their identities that might be their ideal selves (i.e., Ego Ideals), something different than they truly are (i.e., Role Players), or even multiple identities [8, 22, 48]. The constructed identity and the avatar appearance both influence social interactions in VWs. For example, prior work has found that human-like and more realistic avatars with faces tend to enable more positive social interactions [52, 66], and people treat other virtual avatars more intimately if they have commonality [1]. Agents with real/physical body (i.e. embodiment) in virtual reality also increase rapport and nonverbal realism [31]. In some VWs, users can deliver live performances [54], such as musical concerts, and establish fan bases [11, 29]. Though relevant, avatar-based interactions in VWs often do not reach the same level of expressiveness and interactivity of VTuber live streaming, and perception of VTuber differs from virtual character perception in VW because viewers are not in the same VW as the streamer. We are inspired by the discussion of identity and emobodiment in this line of research to explore VTuber live streaming.

### 2.3 Live Streaming Motivations and Practices

Prior work about live streaming in HCI has found that the interactivity and the sociality of live streams are what make live streaming engaging [24, 44]. Due to the ubiquitous nature of live streaming platforms, live streaming has been leveraged by many users as a way to have fun, to learn, to get inspirations, to improve their skills, and to build online communities and form social relationships with community members [60].

The domain of video games has been a popular topic within live streaming. Streamers on Twitch often broadcast their own live gameplay experience or spectate on others’ gameplay. They also share gameplay skills and inform viewers of interesting video games thus using live streaming to cultivate a community of gamers who share similar interests [24, 30, 53, 56, 64]. Novel user interfaces that extend communication channels between viewers and streamers during video game live streams have also been designed and developed [21, 37]. Although these projects found increased viewer engagement in live streams, their findings were largely confined to video game live streams.

Live streamers in other domains have also leveraged live streaming to connect and engage community members, such as for performance (e.g., singing), education [7, 25], knowledge sharing [43], programming [14], cultural practices [41], and creative activities [44]. These aforementioned studies have found different motivations, demographics, practices, and engagement levels within different live streaming communities, highlighting the need to further understand live streaming user groups to improve the design of live streaming interfaces to support a variety of user needs.

The affordances of live streaming (e.g., live chats and emojis) is relevant to the Hyperpersonal Model in computer-mediated communication (CMC) [55, 61, 62]. VTubers can be viewed as message senders who selectively present themselves with virtual avatars, and viewers can be viewed as receivers who interpret the content and form impressions of VTubers. The Hyperpersonal Model suggests that senders often have a number of advantages in their interactions with receivers, compared to traditional face-to-face communications (e.g., the ability to modify self-presentation to develop an optimized image and relative anonymity). As a result, receivers tend to over interpret the cues inherent in senders’ selfpresentations because the cues in text-based CMC are limited compared to face-to-face interactions. VTuber viewers cannot see the appearance and non-verbal behaviors of Nakanohitos, resulting in reduced cues.

The mainstream live streaming research mostly focused on live streams of real-person streamers who live stream with their real-life appearance. This work contributes to the broader live streaming research in HCI by understanding how viewers of the Otaku community engage with and perceive virtual characters of VTubers.

## 3 METHOD

## 4 FINDINGS

## 5 DISCUSSION

## 6 CONCLUSION

## References

### Glossary - 後で置き換える用の用語集

- ライブストリーミング → ライブ配信
- ストリーマー → 配信者

### Tools

- Deepl
- [https://dream-exp.net/shaper/](https://dream-exp.net/shaper/)
