---
layout: post
title: "海外論文紹介：More Kawaii than a Real-Person Streamer - コミュニティがVTuberとどう関わり、どう認識しているか"
date: "2021-05-11 23:52:00"
author: aki
description: More Kawaii than a Real-Person Streamer - Understanding How the Otaku Community Engages with and Perceives Virtual YouTubersの翻訳を通して、日本発祥である VTuber 文化が、現在、どのように受容されているかを垣間見ることができます。また日本の学術コミュニティにおいても、より VTuber や SNS、配信者文化に関する学術的研究が活発になる事を期待して、参考訳を掲載します。
preview: http://img.youtube.com/vi/IuMhbo0MZrU/hqdefault.jpg
categories: Research
---

国際会議[CHI2021](https://chi2021.acm.org/) にて、興味深い論文「[リアルな配信者よりもカワイイ ：オタクコミュニティがバーチャル YouTuber とどのように関わり、どのように認識しているか](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)」（原題："More Kawaii than a Real-Person Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers"）がありましたので、著者の Zhicong Lu さんに Twitter 上でご許可をいただいて日本語翻訳させていただきました。日本発祥である VTuber 文化が、現在、どのように受容されているかを垣間見ることができます。また日本の学術コミュニティにおいても、より VTuber や SNS、配信者文化に関する学術的研究が活発になる事を期待して、参考訳を掲載します。

[YouTube](https://www.youtube.com/watch?v=IuMhbo0MZrU&list=RDCMUCEfEi-IMiB87UsxY3765P6w)

<iframe width="560" height="315" src="https://www.youtube.com/embed/IuMhbo0MZrU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Acknowledgements

This is authorized Japanese translation of "More Kawaii than a Real-Person Streamer: Understanding How the Otaku Community Engages with and Perceives Virtual YouTubers".
[Original PDF](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)

I appreciate to the original authors, specially to Prof. Zhicong Lu for his great contribution and agreement for this translation.

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/luzc08/status/1392134253211799552">date</a></blockquote>

### Credit and copyright

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

### 訳者より: Notes and Disclaimer from translator (Akihiko SHIRAI)

- (2021/5/16)現在、粗訳が終わったところです。これから清書していきます。Twitter 上で前半を紹介していますので、興味ある人はこのスレッドを追ってみてください（Twitter の方が文字数制約があるのでより意訳になっていて読みやすいかもしれません）。

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392067792078213125">date</a></blockquote>

- Inserted tweets are by myself (Translator).
- 原文に対する質問やディスカッションは著者の[Zhicong Lu 先生](https://twitter.com/luzc08/status/1392134253211799552)にお問い合わせください。
- 翻訳に関するご指摘ご質問は白井まで。[Github の markdown](https://github.com/kaitas/kaitas.github.io/blob/master/_posts/2021-05-11-more-kawaii.md)なので直接プルリクエスト頂いても良いかと思います。
- 訳注と、必要なハイパーリンクがあれば加えていきたいと思います。
- こちらは白井の個人のブログになります。所属とは切り離して読み物として読んでいただければ幸いです。

## 「リアルな配信者よりもカワイイ：オタクコミュニティがバーチャル YouTuber とどのように関わり、どのように認識しているか」

## 概要

ライブ配信はますます人気が高まっており、ほとんどの配信者は実際の姿を見せています。しかし、2D または 3D のバーチャルなアバターに人間が声を吹き込んだ「バーチャル YouTuber（VTuber）」がライブ配信者として登場し、東アジアで視聴者数を伸ばしていることがわかっています。先行研究では、多くの視聴者が実在の人物であるストリーマーとのリアルな対人関係を求めていることが明らかになっていますが、VTuber のライブストリームの魅力や、実在の人物であるストリーマーとの受け止め方の違いについては、現在のところ不明です。私たちは、視聴者が VTuber とどのように関わり、アバターの背後にいる声優（中の人）のアイデンティティをどのように認識しているのかを理解するために、インタビュー調査を実施しました。その結果、バーチャル・アバターはユニークなパフォーマンスの機会をもたらし、その結果、VTuber の行動に対する視聴者の期待や解釈が異なることが明らかになりました。視聴者は、VTuber のアバターが「中の人」とは身体的に別物であることを意図的に支持していた。我々は、視聴者の認識と態度のニュアンスを明らかにし、VTuber の実践が一般的なライブ配信の理解に与える影響をさらに議論します。

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

<blockquote class="twitter-tweet" data-width="550" data-dnt="true" data-conversation="none"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392030359835975683">date</a></blockquote>

## 1 はじめに

Twitch，YouTube，TikTok などのライブストリーミングの登場により，
実生活の体験 [40, 42, 59]，ライブイベント [23, 58]，創作活動 [15, 41, 44]，教育コンテンツ [14, 43, 44]，ビデオゲームのプレイ [24]などのライブ映像を共有することが，世界中でますます普及しています．
ライブストリーミングのライブチャットやバーチャルギフティングの機能により、視聴者はストリーマーや他の視聴者とテキストや絵文字などのモダリティでリアルタイムに対話することができます。このような双方向性の高さが、ストリーマーのコミュニティ形成を促進し、結果的にライブストリーミングは、視聴者が楽しみながらオンデマンドで情報を取得できる魅力的なメディアとなっている。

ライブ・ストリーミングに関する先行研究では、ほとんどが実在の人物によるライブ・ストリーミングに焦点が当てられており、ライブ・ストリーミングがもたらす「リアルさ」が、ライブ・ストリーミングを魅力的で人気のあるものにする重要な要因であることがわかっています[23, 24, 44]。
しかし、東アジアにおけるバーチャル YouTuber（VTuber）の台頭は、これと矛盾するように思えます。バーチャル YouTuber やバーチャルストリーマーは、人間が声を当てた 2D または 3D のバーチャルなアバターであるため、ユニークなコンテンツ制作者のカテゴリーと言えます（図 1）。このようなストリーマーは，YouTube やニコニコ動画[13]，Bilibili[4]などで，熱心なファンを持ち，企業とのスポンサー契約を結んだ有名人になりつつあります．VTuber の人気は高く、日本や中国の多くの企業が「バーチャル・タレント」に多額のリソースを投じており、これらのアバターを管理するタレント・エージェンシーの設立につながっています。また、Instagram では、270 万人以上のフォロワーを持つ Lil Miquela のようなバーチャルインフルエンサーが登場しており[6]、このようなデジタルアバターの公人化は、東アジアだけの現象ではありません。

2016 年以降、東アジアでは VTuber の人気が高まっていますが、ライブ映像の臨場感やリアルタイムでの対人交流を重視するメディアであるライブ・ストリーミングを介して VTuber を視聴する際に、視聴者がなぜ、どのようにエンゲージメントを高めるのかについては、理解が浅いです。また、バーチャルアバターの配信者と実在の人物の配信者の違いや、アバターの背後にいる声優や中の人のアイデンティティや存在感を、視聴者がどのように認識しているのかも不明です。このように、VTuber のライブ配信の動機や視聴行動を明らかにすることは、これまで実在の人物を対象としてきた HCI のライブ配信研究の主流を、バーチャルアバターの配信者や、ライブ配信とアニメやコミックなどのサブカルチャーの融合であるオタク・コミュニティの研究に広げることができる。
このような知識は、実在の人物とバーチャルアバターの両方のストリーマーをサポートする将来のライブストリーミングインターフェースの設計にも役立つでしょう。

本研究では、VTuber の社会技術的現象と、そのジャンルやコミュニティに特有の慣習、機会、課題をよりよく理解するために、VTuber のライブストリームを視聴した経験が豊富なオタクコミュニティの VTuber 視聴者 21 名（VTuber を 1 年以上視聴しており、少なくとも週 1 回は視聴している）を対象に、インタビュー調査を実施した。インタビューの結果、VTuber や _なかのひと_ (Nakanohito) たちは、バーチャル・アバターを媒介にすることで、現実の姿やアイデンティティを明かすことなく、視聴者を巻き込み、コミュニティを形成し、視聴者の支持を得ることができることがわかりました。
バーチャル・アバターは、ユニークなパフォーマンスの機会をもたらし、その結果、VTuber の行動に対する視聴者の期待や解釈が異なる。例えば、視聴者はバーチャルアバターとの間に距離を感じ、VTuber の攻撃的な言葉や「愚かな」行動に寛容であることが、実在するストリーマーと比較して明らかになりました。また、分析の結果、視聴者は VTuber の完璧なイメージを頭の中に維持するために、なかのひとがアバターから離脱しているという信念を意図的に維持しているものの、労働争議が発生した際には、なかのひとのことを気にかけていることが明らかになりました。今回の調査結果をもとに、曖昧で変容し続けているライブストリーミングにおけるリアルとバーチャルの境界線、VTuber 事務所となかのひとの労働関係、そして今後のストリーミングプラットフォームにおけるアイデンティティ管理、透明性、公平性の必要性について考察します。

このように、私たちの HCI への貢献は、i)VTuber のコミュニティの実践と動機、および中国の社会的・文化的文脈の中で彼らがどのようにこれらの実践に従事しているかについてのニュアンスのある説明、ii)VTuber と現実の人間のストリーマーに対する視聴者の認識、および仮想アバターの背後にいる声優について視聴者が抱いている信念の理解、iii)VTuber の実践がライブストリーミングとアバターベースの社会的相互作用に与える影響、です。

<!--
1 INTRODUCTION Sharing live video of real life experiences [40, 42, 59], live events [23, 58], creative activities [15, 41, 44], educational content [14, 43, 44], or playing video games [24] is becoming increasingly widespread around the world, largely due to the emergence of live streaming on Twitch, YouTube, TikTok, etc. The live chat and virtual gifting features of live streaming enable viewers to interact with streamers and other viewers via text, emoji, or other modalities in real-time. This high degree of interactivity facilitates the building  of the streamer’s community and results in live streaming being an engaging medium for viewers to have fun and acquire information on demand. Prior research on live streaming has mostly focused on realperson live streams, finding that the “realness” afforded by live streaming is the key factor that makes them engaging and popular [23, 24, 44]. However, the emerging trend of virtual YouTubers (VTubers) in East Asia seems to contradict this. Virtual YouTubers or virtual streamers are a unique category of content creators because they are virtual 2D or 3D avatars that are voiced by a human (Figure 1). Such streamers are becoming celebrities on YouTube, NicoNico [13], and Bilibili [4], with dedicated fan bases and corporate sponsorship deals. VTubers are becoming so popular that many companies in Japan and China are investing a large amount of resources in “virtual talent” and have led to the establishment of talent agencies to manage these avatars. Such digital avatar public figures are also not a phenomenon only constrained to East Asia, since Instagram has seen emerging virtual influencers such as Lil Miquela, who has over 2.7 million followers [6]. Although VTubers have been gaining traction in East Asia since 2016, there is a limited understanding of why and how viewers become engaged while watching VTubers through live streaming, a medium which emphasizes the authentic nature of live video and real-time, interpersonal interactions. It is also unknown how viewers perceive the differences between virtual-avatar streamers and real-person streamers, and how they perceive the identity and presence of the voice actor or Nakanohito who is behind the avatar. Uncovering specific motivations and viewing practices of VTuber live streaming could expand mainstream live streaming research in HCI, which has mostly focused on real-person streamers, to studying virtual-avatar streamers and the emerging fusion of live streaming and the subcultures of anime and comics, i.e., the Otaku community. Such knowledge could also inform the design of future live streaming interfaces that support both real-person streamers and virtual-avatar streamers. To better understand the socio-technological phenomenon of VTubers and its genreand community-specific practices, opportunities, and challenges, we conducted an interview-based study with 21 VTuber viewers from the Otaku community who had extensive experience watching VTuber live streams (i.e., they had watched VTuber for over a year and watched at least once per week). The interviews revealed that through the mediation of virtual avatars, streamers or Nakanohitos can engage viewers, build communities, and gain viewers’ support without disclosing their real life appearance or identity. Virtual avatars bring unique performative opportunities which result in different viewer expectations and interpretations of VTuber behavior. For example, viewers felt more distance between themselves and the virtual avatars and showed tolerance to VTubers’ offensive language and ‘stupid’ behavior compared to real-person streamers. The analysis also revealed that although viewers intentionally maintained beliefs about Nakanohito’s disembodiments from their avatars so that viewers could maintain perfect images of VTubers in their minds, they still cared about Nakonohitos when labor disputes arose. Drawing on our findings, we discuss the blurry and ever-changing line between the real and virtual in live streaming, labor relationships between VTuber agencies and Nakanohitos, and the need for future streaming platforms to support identity management, transparency, and fairness. Thus, our contributions to HCI are: i) a nuanced description of the practices and motivations of VTubers’ communities and how they engage in these practices within the social and cultural contexts of China, ii) an understanding of viewers’ perceptions of VTubers versus real-person streamers and the beliefs viewers hold about the voice actors behind virtual avatars, iii) the implications of VTubers practices to live streaming and avatar-based social interactions.
-->

## 2 背景および関連研究

まず、VTuber の背景を説明し、アバターベースのバーチャルアイドルやバーチャルワールドでのソーシャルインタラクションに関する研究をレビューし、続いてライブストリーミングの動機と実践についてレビューします。

<!--
We first describe the background of VTubers, and then review research into avatar-based virtual idols and social interactions in virtual worlds, followed by a review of live streaming motivations and practices.
-->

### 2.1 背景

過去 30 年以上にわたり、日本のマンガ、アニメ、ビデオゲームは、東アジア、そしてより一般的には世界中で広く人気を博してきた。これにより、10 億ドル規模の産業と、マンガ、アニメ、および関連するサブカルチャーへの強い熱意を特徴とする独特のオタク・サブカルチャー[27]が生まれました。同時に，日本のアイドルも，作り出されたイメージや個性が大きな要因となって，大規模で熱狂的なファン層を形成してきた[20]．VTuber は、これらのトレンドが絡み合い始めたことで、革新的な文化現象として登場しました。

VTuber は日本で生まれ、2016 年に初登場して以来、急速に国際的な人気を獲得しています。2019 年 1 月中旬には、世界中で 10,000 人以上のアクティブな VTuber が存在し[2]、600 人以上の VTuber が 10,000 人以上のフォロワーを持ち、数百万回の再生回数を集めていました[3]。VTuber の影響力は、オタク系サブカルチャーの枠を超えて急速に拡大しています。たとえば，初代 VTuber の**キズナアイ**は，2018 年に日本政府観光局が実施する国際文化キャンペーンのアンバサダーに選ばれました［68］。

VTuber とは、ライブ動画配信や録画動画でパフォーマンスを配信するアニメーションの仮想アバターのことである。アバターの声は俳優が担当することが多く、日本語では「中の人」と呼ばれている。VTuber は，Live2D [45]などのツールを用いて作成された半身の 2D アバターを用いてストリーミングを行うのが一般的で，俳優の顔の動きをキャプチャしてアバターの表情を動かすことができます（図 1）．アバターの他の体の部分の動きは、デスクトップ・コンピュータから送られるコマンドを使って、Live2Dのようなプログラムの中で引き起こすことができます。全身のモーションキャプチャーシステムを利用できる VTuber は、3D アバターを使ってパフォーマンスを行うことができます。これにより、アバターの体の可動域を広げることができます。また、VTuber は、視聴者が投稿したコメントを読んで返信することも多く、実在するストリーマーと同様の活動を行っています。VTuber はユニークなペルソナを持っていることが多く、例えばキズナアイは 16 歳のブルネットのアニメ少女のような外見をしているが、彼女は最近開発された高度な人工知能だという設定で、その言動は AI エージェントの行動を真似たナイーブなものであったが、実際には彼女のパフォーマンスは複数の中の人によって動かされていました。

VTuber には、個人で運営するものと、事務所が運営するものがあります。にじさんじ[49]やホロライブ[26]のように、20 名以上の VTuber を並行して契約している営利目的の VTuber 機関もあります。これまでのところ、企業が運営する VTuber は、個人が運営する VTuber よりも多くの視聴者を集めています。例えば 2020 年 1 月、YouTube で最もフォローされている VTuber 100 人のうち、94 人が企業が運営する VTuber でした[3]。これは、企業が運営する VTuber は、プロがデザイン・設計したアバターを持ち、よりリアルなアバターの動きを生成するために高価なモーションキャプチャー機器を使用し、プロモーションやマーケティングを強化しているため、総合的に支持されているからだと考えられます。

個人で運営されている VTuber の中の人(声優)は、VTuber プロジェクトの全ての所有権を持ちます。対して、VTuber 事務所は VTuber を所有し、彼らの知的財産であると主張しています。VTuber 事務所の従業員は、今後の番組企画や他の中の人が自分のアバターを引き継ぐかどうかなど、自分のアバターの運営全般に対するコントロールが制限されており、労働争議に発展する可能性があります。

中国は、VTuber の最も重要な市場の一つです。多くの VTuber が、若い世代に人気のある動画プラットフォーム「BiliBili」で公式チャンネルを運営しています[4]。BiliBili では，中国や日本の個人や事務所が企画・運営する VTuber が存在します[9]．日本語を話す VTuber は，配信者と視聴者の間の言葉の壁を乗り越えるために，リアルタイムで中国語の字幕を表示したり，簡単な言葉で中国のファンとコミュニケーションをとったりしています．また，熱心な VTuber ファンは，ストリームのハイライトをキュレーションしたり，ソーシャルネットワーキングサイトやフォーラムでオンラインのソーシャルグループを形成して，VTuber 関連のトピックについて議論したりしています（例：National Geographic of Azeroth（NGA）フォーラム）[51]．中国における VTuber の視聴者に関する研究を行うことで，ライブ・ストリーミングがインターネット・ユーザーにとって主要な活動である中国において，視聴者がどのように VTuber に関わり，VTuber がどのように位置づけられるかの両方を捉えることを目的としています[44]．

<!--
Over the past 30 years, Japanese manga, anime, and video games have gained widespread popularity in East Asia and more generally, worldwide. This has given rise to a billion dollar industry and a unique Otaku subculture [27] that is characterized by a strong enthusiasm for manga, anime, and related subcultures. Concurrently, Japanese idols have also cultivated large and passionate fan bases, due in large part to their manufactured images and personalities [20]. VTubers have emerged as an innovative cultural phenomenon as these trends have begun to intertwine. VTubers originated in Japan and have rapidly gained international popularity since their first appearance in 2016. By midJanuary 2019, there were more than 10,000 active VTubers around the globe [2], and more than 600 VTubers had over 10,000 followers and had attracted millions of views [3]. The influence of VTubers has quickly grown beyond the Otaku subculture. The first VTuber, Kizuna Ai, for example, was chosen as the ambassador of an international culture campaign by the Japanese National Tourism Organization in 2018 [68].

A VTuber is an animated virtual avatar that delivers performances in live video streams or recorded videos. The avatar is often voiced by an actor, who is referred to as a Nakanohito (中の人) in Japanese. VTubers typically stream with half-body 2D avatars, which are created with tools such as Live2D [45] that capture the actor’s facial movements and drive the avatar’s facial expressions (Figure 1). The motions of other body parts of the avatar can be triggered within such programs using commands sent from desktop computers. VTubers who have access to full-body motion capture systems can perform with 3D avatars. This allows them to have a higher range of motion with the avatar’s body. Vtubers also often read comments that viewers post in-stream and respond to them, similar to the practices of real-person streamers. VTubers often have a unique persona, e.g., Kizuna Ai has the appearance of a 16-year-old brunette animated girl, who was a recently-developed advanced artificial intelligence and her words and actions were naive, imitating the behavior of an AI agent, although her performance was actually driven by several Nakanohitos.

VTubers can be operated by an individual or an agency. Some for-profit VTuber agencies, such as Nijisanji [49] and Hololive [26], have more than 20 VTubers under contract in parallel. So far, corporate-operated VTubers have attracted larger viewership than individual-operated ones. In January 2020, for example, 94 out of the 100 most followed VTubers on YouTube were run by agencies [3]. This is likely because corporate-run VTubers are overall better supported because they have professionally designed and engineered avatars, use more expensive motion capture equipment to generate more realistic avatar movement, and have stronger promotion and marketing. The Nakanohitos (i.e., voice actors) of individual-operated VTubers typically have full ownership over their VTuber projects. In contrast, VTuber agencies own their VTubers and claim that they are their intellectual property. Employees of these agencies have limited control over changes to the overall operation of their avatar, such as future program planning or if another Nakanohito will take over their avatar, which can potentially lead to labor disputes. China is one of the most important VTuber markets. A large number of VTubers operate official channels on BiliBili, a video platform that is highly popular among young generations [4]. On BiliBili, there are VTubers designed and managed by Chinese and Japanese individuals and agencies [9]. To overcome the language barriers between streamers and viewers, Japanese-speaking VTubers stream with real-time Chinese subtitles, or use simpler words to communicate with Chinese fans. Dedicated VTuber fans also curate stream highlights and form online social groups on social networking sites and forums to discuss VTuber-related topics, e.g., the National Geographic of Azeroth (NGA) forum [51]. By contributing a study of viewers of VTubers in China, we aim to capture both how viewers engage with VTubers and how VTubers are appropriated in China, where live streaming is a predominate activity for Internet users [44].
-->

### 2.2 アバターを用いたバーチャルアイドル及びバーチャル世界での社会的相互作用

アバターを使ったバーチャルアイドルの歴史は、1990 年代半ばにさかのぼります。日本では、1996 年から 1997 年にかけて、**伊達杏子**と**寺井由紀**の 2 人のアバター・ベースのアイドルが誕生したのが最初です。2007 年にはクリプトン・フューチャー・メディアから**初音ミク**が発売されました。ヤマハのソフトウェアエンジン「ボーカロイド」をベースに、16 歳の女性をイメージして作られたミクは、瞬く間に世界的なブームを巻き起こしました。研究者たちは、ミクのようなアバター・ベースのアイドルをフェミニストの観点から考察し、女性の表現とジェンダーの本質化が、仮想世界においても女性のステレオタイプを永続させると主張しています[34, 35]。
他の研究者らは、バーチャルであることで実在の人を再現するのに限界があるにも関わらず、実身体からの独立がファンとアイドルの間に新たな関係を開拓したと述べました[5]。
そして、アマチュアやプロのミュージシャン、アニメーター、アーティスト、ファンが分散型のグローバル・ネットワークを形成し、大規模なコラボレーションやピア・プロダクションを通じて、ミクを再現したりリミックスしたりして文化的な表現を行っていることは、企業によるミクのフランチャイズの支配とは異なるものであると指摘しています[36, 67]。ミクのような最近のアバター・ベースのアイドルが世界的に成功しているにもかかわらず、これらのバーチャル・アイドルは、ファンとのリアルタイムのインタラクティビティを達成していないと言えるでしょう。私たちの研究は、VTuber のライブストリーミングに焦点を当てることで、この研究ラインに貢献しています。VTuber は、ライブパフォーマンスの自発性と予測不可能性を利用して、リアルタイムで視聴者と対話します。

また，HCI において重要なテーマとなっている，アバターを用いた仮想世界（VW）でのソーシャル・インタラクションにも注目しています[16]．これまでの研究では，World of Warcraft のようなゲーム指向の VW（例：[12, 46]）や Second Life のような社会指向の VW（例：[47, 48]）におけるユーザの知覚についての知見が得られています．ユーザーは通常，自分で作成・操作した仮想体（＝アバター）を介してこれらの VW に入り，アバターを使って様々な社会活動を行いながら相互に交流します。ユーザーは、VW でのオンライン・インタラクションを通じて、理想の自分（＝ Ego Ideals）であったり、本当の自分とは異なるもの（＝ Role Player）であったり、さらには複数のアイデンティティを構築します[8, 22, 48]。構築されたアイデンティティとアバターの外見は、VW における社会的相互作用に影響を与えます。例えば、顔のある人間らしいリアルなアバターは、よりポジティブな社会的相互作用を可能にする傾向があることが先行研究で明らかになっており[52, 66]、お互いに共通点がある場合には他の仮想アバターをより親密に扱うことができます[1]。また，仮想現実に実在する身体を持つエージェント（＝エンボディメント）は，信頼関係と非言語的リアリズムを高める［31］．一部の VW では、ユーザーは音楽コンサートなどのライブパフォーマンスを行い[54]、ファンベースを確立することができます[11, 29]。しかし、VW におけるアバターベースのインタラクションは、VTuber のライブストリーミングと同じレベルの表現力やインタラクティビティに達しないことが多く、また、視聴者はストリーマーと同じ VW にいないため、VTuber の知覚と VW におけるバーチャルキャラクターの知覚は異なります。私たちは、このような研究におけるアイデンティティとエンボディメントの議論に触発され、VTuber のライブストリーミングを探求しています。

<!--
The history of avatar-based virtual idols can be traced back to the mid-1990s. The first two avatar-based idols, Kyoko Date and Yuki Terai, were created in Japan in 1996-1997. In 2007, Hatsune Miku was released by Crypton Future Media. Building on Yamaha’s software engine Vocaloid, and illustrated as a 16-year-old female character, Miku soon became an international phenomenon. Scholars have examined avatar-based idols such as Miku from a feminist perspective, arguing that the female representation and the essentializing of gender perpetuate female stereotypes, even in virtual worlds [34, 35]. Others have examined the fan communities around avatar-based idols, noting that although being virtual has limited idols’ capacities to emulate real people, independence from a living body has cultivated a new type of relationship between fans and the idol [5] — amateur and professional musicians, animators, artists, and fans formed a distributed global network and recreated and remixed Miku for cultural expression through large-scale collaborations and peer-production, which differed from the corporate control of Miku’s franchise [36, 67]. Despite the international success of recent avatar-based idols like Miku, these virtual idols have arguably never achieved real-time interactivity with their fans. Our work contributes to this line of research by focusing specifically on VTuber live streaming, where VTubers interact with viewers in real time, harnessing both the spontaneity and unpredictability of live performances.

Also relevant is avatar-based social interactions in virtual worlds (VWs), which has been a key theme in HCI [16]. Past research has offered insights into user perception in game-oriented VWs such as World of Warcraft (e.g., [12, 46]) and social-oriented VWs such as Second Life (e.g., [47, 48]). Users usually enter these VWs through virtual bodies (i.e., avatars) that are created and controlled by them, and interact with each other using their avatar in a variety of social activities. Through online interactions in VWs, users construct their identities that might be their ideal selves (i.e., Ego Ideals), something different than they truly are (i.e., Role Players), or even multiple identities [8, 22, 48]. The constructed identity and the avatar appearance both influence social interactions in VWs. For example, prior work has found that human-like and more realistic avatars with faces tend to enable more positive social interactions [52, 66], and people treat other virtual avatars more intimately if they have commonality [1]. Agents with real/physical body (i.e. embodiment) in virtual reality also increase rapport and nonverbal realism [31]. In some VWs, users can deliver live performances [54], such as musical concerts, and establish fan bases [11, 29]. Though relevant, avatar-based interactions in VWs often do not reach the same level of expressiveness and interactivity of VTuber live streaming, and perception of VTuber differs from virtual character perception in VW because viewers are not in the same VW as the streamer. We are inspired by the discussion of identity and emobodiment in this line of research to explore VTuber live streaming.
-->

### 2.3 ライブ・ストリーミングの動機と実践

HCI におけるライブ・ストリーミングに関する先行研究では、ライブ・ストリーミングの双方向性と社会性が、ライブ・ストリーミングを魅力的なものにしていることがわかっています[24, 44]。ライブ・ストリーミング・プラットフォームのユビキタスな性質により、ライブ・ストリーミングは、楽しみ、学び、インスピレーションを得て、スキルを向上させ、オンライン・コミュニティを構築し、コミュニティ・メンバーとの社会的関係を形成する方法として、多くのユーザーに活用されてきました[60]。

ビデオゲームの領域は、ライブストリーミングの中でも人気の高いトピックです。Twitch のストリーマーは、自分のゲームプレイの様子を生中継したり、他の人のゲームプレイを観戦したりします。彼らはまた，ゲームプレイのスキルを共有したり，視聴者に興味深いビデオゲームの情報を提供したりすることで，ライブストリーミングを利用して，同じ興味を共有するゲーマーのコミュニティを育成しています[24, 30, 53, 56, 64]．また，ビデオゲームのライブストリーミング中に，視聴者とストリーマーの間のコミュニケーションチャネルを拡張する新しいユーザインタフェースも設計・開発されています[21, 37]．これらのプロジェクトでは，ライブストリームにおける視聴者のエンゲージメントの向上が見られましたが，その結果は主にゲームのライブストリームに限られていました．

他の分野のライブストリーマーも、パフォーマンス（歌など）、教育 [7, 25]、知識の共有 [43]、プログラミング [14]、文化的実践 [41]、創造的活動 [44]など、ライブストリーミングを活用してコミュニティのメンバーとつながり、参加しています。これらの研究では、異なるライブ・ストリーミング・コミュニティの中で、異なる動機、人口統計、実践、および関与レベルが発見されており、多様なユーザー・ニーズをサポートするライブ・ストリーミング・インターフェースの設計を改善するために、ライブ・ストリーミング・ユーザー・グループをさらに理解する必要性が強調されています。

ライブ・ストリーミングのアフォーダンス（ライブ・チャットや絵文字など）は、コンピュータ媒介コミュニケーション（CMC）における Hyperpersonal Model に関連しています[55, 61, 62]。VTuber は、仮想のアバターで自分自身を選択的に表現するメッセージの送信者と見なすことができ、視聴者は、VTuber のコンテンツを解釈し、印象を形成する受信者と見なすことができます。Hyperpersonal Model によると、発信者は受信者とのやりとりにおいて、従来の対面コミュニケーションに比べて多くの利点があるとされています（最適なイメージを形成するために自己表現を修正できることや、比較的匿名性が高いことなど）。その結果、テキストベースの CMC では、対面でのコミュニケーションに比べて手掛かりが限られているため、受信者は送信者の自己表現に内在する手掛かりを過剰に解釈する傾向があります。VTuber の視聴者は、なかのひとの外見や非言語的行動を見ることができないため、手がかりが少なくなってしまいます。

ライブストリーミングの研究の主流は、実在する人物の姿でライブストリーミングを行うストリーマーのライブストリームに集中していました。本研究は、オタク・コミュニティの視聴者が VTuber のバーチャル・キャラクターにどのように関わり、どのように知覚するかを理解することで、HCI における広範なライブ・ストリーミング研究に貢献するものです。

<!--
Prior work about live streaming in HCI has found that the interactivity and the sociality of live streams are what make live streaming engaging [24, 44]. Due to the ubiquitous nature of live streaming platforms, live streaming has been leveraged by many users as a way to have fun, to learn, to get inspirations, to improve their skills, and to build online communities and form social relationships with community members [60].

The domain of video games has been a popular topic within live streaming. Streamers on Twitch often broadcast their own live gameplay experience or spectate on others’ gameplay. They also share gameplay skills and inform viewers of interesting video games thus using live streaming to cultivate a community of gamers who share similar interests [24, 30, 53, 56, 64]. Novel user interfaces that extend communication channels between viewers and streamers during video game live streams have also been designed and developed [21, 37]. Although these projects found increased viewer engagement in live streams, their findings were largely confined to video game live streams.

Live streamers in other domains have also leveraged live streaming to connect and engage community members, such as for performance (e.g., singing), education [7, 25], knowledge sharing [43], programming [14], cultural practices [41], and creative activities [44]. These aforementioned studies have found different motivations, demographics, practices, and engagement levels within different live streaming communities, highlighting the need to further understand live streaming user groups to improve the design of live streaming interfaces to support a variety of user needs.

The affordances of live streaming (e.g., live chats and emojis) is relevant to the Hyperpersonal Model in computer-mediated communication (CMC) [55, 61, 62]. VTubers can be viewed as message senders who selectively present themselves with virtual avatars, and viewers can be viewed as receivers who interpret the content and form impressions of VTubers. The Hyperpersonal Model suggests that senders often have a number of advantages in their interactions with receivers, compared to traditional face-to-face communications (e.g., the ability to modify self-presentation to develop an optimized image and relative anonymity). As a result, receivers tend to over interpret the cues inherent in senders’ selfpresentations because the cues in text-based CMC are limited compared to face-to-face interactions. VTuber viewers cannot see the appearance and non-verbal behaviors of Nakanohitos, resulting in reduced cues.

The mainstream live streaming research mostly focused on live streams of real-person streamers who live stream with their real-life appearance. This work contributes to the broader live streaming research in HCI by understanding how viewers of the Otaku community engage with and perceive virtual characters of VTubers.
-->

## 3 手法

VTuber のライブ・ストリームを視聴するオタク・コミュニティの視聴者の動機や状況を理解し、彼らが VTuber とどのように関わり、認識しているのかを理解するために、VTuber のライブ・ストリームを週 1 回以上、1 年以上にわたって視聴している 21 人の視聴者を対象に、インタビュー形式の質的研究を行いました（表 1）。研究プロトコルは、オンラインのアーカイブデータをもとに作成し、機関内審査委員会（IRB）の承認を得ました。

<!--
To understand the motivational and situational contexts of viewers from the Otaku community who watch VTuber live streams, and how they engage with and perceive VTubers, we conducted a qualitative interview-based study with 21 viewers who had been watching live streams of VTubers at least once a week for at least a year (Table 1). The study protocol was informed by online archival data and approved by the institutional review board (IRB).
-->

### 3.1 インタビュー対象者の募集

VTuber は主に Otaku コミュニティからの視聴者を惹きつけているため[9]、潜在的な「熱心な」視聴者には、個人的なつながりか、アクティブユーザー数とスレッド数の両方で中国最大の VTuber ディスカッションボードである National Geographic of Azeroth（NGA）フォーラム[51]の VTuber ディスカッションボードを通じて意図的にアプローチした[57]。4 人のインタビュイーは，著者の一人が参加しているアニメ・コミック・ゲーム（ACG）ファンの WeChat グループからで，WeChat 上のダイレクトメッセージで参加を呼びかけた．残りの 17 人のインタビュー対象者は、NGA フォーラムから募集した。フォーラムには中国語で募集広告が掲載され、参加希望者は WeChat または電子メールで研究チームに連絡するよう求められた。視聴者を自認し、VTuber のライブストリームを週に 1 回以上視聴し、1 年以上の視聴経験がある人全員に参加を呼びかけた。本研究では、視聴者の個人的な経験を重視しており、この種のストリーミングを調査した先行研究はないため、視聴者の認識に影響を与える可能性のある要因を探るためには、意図的なサンプリングが有効でした。しかし、このような方法で募集したため、インタビュー対象者は男性に偏り、ほとんどが学生でした。これは、VTuber の視聴者層について研究チームが持っていた逸話的証拠と一致しています。

<!--
Because VTubers mostly attract viewers from the Otaku community [9], potential “dedicated” viewers were purposefully approached through either personal connections or VTuber discussion board on the National Geographic of Azeroth (NGA) forum [51], which is the largest VTuber discussion board in China, in terms of both the number of active users and threads [57]. Four interviewees were from a WeChat group of anime, comics, and gaming (ACG) fans that one of the authors joined, and were invited to participate through direct messaging on WeChat. The other 17 interviewees were recruited from the NGA forum. A recruitment advertisement was posted in Chinese on the forum soliciting those who wanted to participate to contact the research team through WeChat or e-mail. All those who self-identified as viewers and who watched at least one VTuber’s live stream once a week with over one year of watching experience were invited to participate. Since this study valued the individual experiences of viewers and there is no previous work exploring this specific type of streaming, purposive sampling was helpful to explore factors that could influence viewers’ perceptions. Due to this recruitment method, however, the recruited interviewees skewed male and were mostly students. This aligns with anecdotal evidence that the research team had about VTuber viewer demographics.
-->

### 3.2 背景資料の収集

VTuber 現象についての視点を広げ、インタビュープロトコルのデザインを補強するために、インタビューの前と最中にオンラインリソースから広範な背景資料を収集しました。主な情報源は、NGA フォーラムの VTuber ディスカッションボードでした[51]。この掲示板のユーザーは、カジュアルな視聴者から、愛する VTuber に多大な時間や金銭的支援を提供する熱心なファンまで様々です。このような多様なユーザーがいることで、幅広い意見を収集することができました。さらに、この掲示板では、VTuber についての深い議論や熱い討論が行われている。これらのスレッドは、研究チームが、進化する VTuber 業界の最新情報を入手し、インタビューのための関連テーマを特定するのに役立ちました。

筆者 1 名は、2019 年 10 月から 2019 年 12 月の間、この掲示板の投稿を毎日追いかけ、視聴者の VTuber に対する認識、VTuber のライブ配信やナカノヒトや VTuber 事務所に関する議論、VTuber 業界の重要な変化などを反映した上位のアクティブなスレッドを購読しました。人気 VTuber の名前や所属事務所、VTuber や中の人などの概念をキーワードにして、フォローすべきスレッドを検索しました。52 のフォーラムスレッドから 1059 件の投稿を抽出しました。Strauss のオープンコーディング法[10]を用いて、スレッド内の投稿を分析し、予備的なテーマを特定し、それをインタビュープロトコルに反映させました。

<!--
To broaden the perspectives on the VTuber phenomenon and scaffold the interview protocol design, we collected extensive background material from online resources before and during the interview process. The primary source of information was the VTuber discussion board of the NGA forum [51]. The users of the board vary from casual viewers to highly dedicated fans who offer significant time or monetary support to their beloved VTubers. Such user diversity on this board allowed us to sample a broad range of opinions. Furthermore, the board archives some in-depth discussions and heated debates about VTubers. These threads helped the research team stay up-to-date with the evolving VTuber industry and identify relevant themes for the interviews.

One author followed the posts in this discussion board daily between October 2019 and December 2019, following the top active threads reflecting viewers’ perceptions of VTubers, their discussions about VTuber’s live streams, Nakanotitos and VTuber agencies, and important changes in the VTuber industry. We used keywords including popular VTubers’ names and agencies, and notions like VTuber and Nakanohito to search for threads to follow. Altogether 1059 posts from across 52 forum threads were sampled. Strauss’ open coding method was used [10] to analyze the posts in the threads and identified preliminary themes, which were incorporated into the interview protocol.
-->

### 3.3 インタビュー手順

VTuber の熱心な視聴者 21 名に半構造化インタビューを実施しました。インタビューは、2019 年の 11 月と 12 月、2020 年の 3 月と 4 月に、ビデオまたはオーディオコールを使って遠隔地で行われました。各インタビューは約 60 分で、インタビュー対象者には 50 CNY の謝礼が提供されました。インタビューでは、視聴者が VTuber のコンテンツを視聴する動機、どのような種類のコンテンツを視聴したか、視聴して楽しかったか、VTuber のライブストリームの好きな点と嫌いな点、VTuber や他の視聴者とどのように交流したか、などについて質問しました。また、VTuber と生身の人間の違いや、バーチャル・ライブ・ストリーミングの中でのナカノヒトの役割についても考えてもらいました。企業が運営する VTuber では、ナカノヒトが正当な理由なく交代させられるなど、不当な扱いを受けているケースが多いため、インタビューの際にはこれらの問題について考えてもらいました。

インタビューの 2 週間前に、インタビュアーとの信頼関係を築くために、インタビュアーに連絡を取り、好きな VTuber の面白い動画を紹介してもらいました。すべてのインタビュー対象者は、インタビューの前に少なくとも 1 本の動画を送ってくれました。2 人の著者が動画を確認し、主なテーマを記録しました。インタビューでは、VTuber がどのようなパフォーマンスをして視聴者を惹きつけているか、どのような話題でおしゃべりしているか、予想外のドラマチックな瞬間など、彼らが共有したコンテンツに合わせた質問をしました。インタビューは北京語で行われ、オーディオテープに録音され、個人を特定できる情報を削除した上で、テープ起こしサービス iflyrec.cn によって書き起こされました。

<!--
Semi-structured interviews were conducted with 21 dedicated viewers of VTubers. The interviews were conducted remotely using video or audio calls in November and December of 2019 and March and April of 2020. Each interview lasted approximately 60 minutes and interviewees were provided with a 50 CNY honorarium for their time. The interviews included questions about viewer’s motivations to watch VTubers’ content, what types of content they watched or enjoyed watching, what they liked and disliked about VTubers’ live streams, how they interacted with VTubers and other viewers, and so on. Interviewees were also primed to think about differences between VTubers and real-person streamers and their perceptions towards the roles that Nakanohitos play within virtual live streaming. Because there were many cases where corporateoperated VTubers were mistreated, e.g., Nakanohitos being replaced without a fair reason, we asked interviewees to reflect on these issues during the interview

To build rapport with interviewees, we contacted them 2 weeks prior to the interviews and asked them to share interesting videos of their favorite VTubers. All interviewees sent at least one video prior to the interviews. Two authors reviewed the videos and noted main themes. During the interviews, we then asked questions tailored to the content they had shared, e.g., how VTubers performed and engaged viewers, what topics they chatted about, unexpected dramatic moments, etc. Interviews were conducted in Mandarin, audio-taped, and transcribed by the transcription service iflyrec.cn after removing all personally identifiable information.
-->

### 3.4 データ分析

インタビューの記録は，オープン・コーディング法[10]を用いて分析した．北京語を母国語とする 2 人の著者が、帰納的アプローチを用いて個別にトランスクリプトをコーディングし、意見の相違についてはミーティングを行い、コードについての合意を得ました。その後、すべてのコードを英語に翻訳し、親和性ダイアグラムを用いて研究チームで議論し、新たなテーマを見つけ出しました。すべてのコードは、付箋紙に書き写し、ランダムな順序で並べました。そして、そのメモを繰り返しテーマの階層に並べ直し、VTuber のライブストリーミングに対する視聴者の行動、エンゲージメント、認識について合意に達しました。また、収集した背景資料は、VTuber のコミュニティのサブカルチャーやコードの全体的な文脈に関する知識を補うために使用しました。

多くのインタビュイーの回答には、ミソジニーやセクシズムの感情が見られました。
ミソジニーは、オタクのサブカルチャーとバーチャルアイドル業界の両方に根ざしているのかもしれない。性差別はオタクサブカルチャーに蔓延しているようで、そこでは可愛らしさが望まれたり、コミュニティにとって性的さが魅力的であったりします[27]。また、バーチャルアイドル業界は、性差別を積極的に利用し、商業化しています[5]。私たちは、既存の VTuber コミュニティにおけるジェンダーバイアスが、本研究で観察された行動やインタラクションの一因となっている可能性を十分に認識しています。複数のジェンダーの研究チームは、女性蔑視的なニュアンスが排除され、反映されるようにインタビューの回答を文脈化しました。

<!--
The interview transcripts were analyzed using an open coding method [10]. Two native Mandarin-speaking authors coded the transcripts individually using an inductive approach and met to discuss disagreements to gain consensus about codes. All the codes were then translated into English and were discussed by the research team using affinity diagramming to find emerging themes. All codes were transcribed on sticky notes and then arranged in a random order. We then iteratively rearranged the notes into a hierarchy of themes and reached a consensus about viewer behaviors, engagement, and perceptions of VTuber live streaming. The collected background material was also used to supplement our knowledge about the subculture of VTubers’ communities and the overall context for the codes. Misogyny and sexism sentiment was present in many interviewee’s responses.

The misogyny might be rooted from both the Otaku subculture and the virtual idol industry. Sexism seems prevalent in the Otaku subculture, where cuteness is desired or sexually attractive for the community [27]. The virtual idol industry also actively exploits and commercializes sexism [5]. We fully acknowledge the existing gender biases in the existing VTuber communities, which might contribute to the behaviors and interactions observed in this study. The multi-gender research team has contextualized interviewee responses to ensure the misogynistic undertones are eliminated and reflected upon.
-->

> Table 1: Summary of participants interviewed. Preferred platforms: YouTube (YT), Bilibili (BB), Niconico (NN)

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392041621647024129">date</a></blockquote>

## 4 発見

### 4.1 視聴者の動機

インタビューに参加した人々は，自分が熱心なオタク・サブカルチャーのメンバーであり，日本のマンガ，アニメ，ゲームの熱心な消費者であると述べました．彼らは、VTuber の多くがアニメ・キャラクター風の外見を持ち、オタク・サブカルチャーに関連したコンテンツを配信する傾向がある[27]ことから、彼らの嗜好や興味に合致すると考えました。彼らが VTuber のライブ配信に魅力を感じたのは、VTuber の外見や特別にデザインされたペルソナに魅力を感じたことと、VTuber のライブ配信では、「メアはとてもカワイイので、彼女のライブを見逃すと後悔する」（P19）、「VTuber の配信では、非現実的なキャラクターが現実のものとなり、好きなキャラクターとおしゃべりしたり、交流したりすることができて、とてもカッコイイ」（P15）など、好きなアニメのキャラクターと触れ合える機会が提供されるからです。また、週に数回という熱心な視聴行動は、アニメやマンガの長期連載を追うことへの強い関心によるものだといいます。「私は彼女のライブ配信をほとんど毎回視聴します。まるでアニメの全話を追いかけているような感覚です」（P3）。「VTuber のコンテンツは、生身の人間が配信するよりもクリエイティブで想像を超えたものになる可能性がある」（P17）として、好奇心や創造性を VTuber 視聴の主な動機として挙げる人もいました。その他の動機としては、先行研究[24, 44, 60]と同様に、リラクゼーションや娯楽、暇つぶし、仲間やコミュニティの感覚を味わうためなどが挙げられました。

<!--
All interviewees described themselves as dedicated members of the Otaku subculture and were enthusiastic consumers of Japanese manga, anime, and video games. They found that VTubers, most of whom have anime-character-style appearances and tend to deliver content related to the Otaku subculture [27], aligned with their tastes and interests. They were attracted to VTuber live streaming because VTuber appearances and specially-designed persona appealed to them, and VTuber live streaming gave them opportunities to interact with their favorite anime characters, e.g., “Mea is so kawaii that I will regret if I miss her show” (P19) and “VTuber streaming turns an unreal character into reality, so that you can chat and interact with characters you like, which is very cool” (P15). They also attributed their dedicated viewing behaviors (several times per week) to their strong interests in following a long series of anime or manga, e.g., “I watch her live streams almost every time she streams. It’s just like following every episode of an anime” (P3). Several interviewees also noted curiosity and creativity as a main motivation to watch VTuber, because “vtubers’ content could be more creative and beyond imagination than real-person streamers” (P17). Other motivations included to seek relaxation and entertainment, to pass time, and to experience a sense of company and community, similar to prior findings [24, 44, 60].
-->

### 4.2 配信のコンテンツとインタラクション

インタビュー対象者は、VTuber のライブ・ストリームを見て、実在の人物のライブ・ストリームと同じような内容を見ていました。しかし、先行研究と比較すると、VTuber の提供するコンテンツや、視聴者のライブストリームへの関わり方に特徴がありました。

<!--
Interviewees watched VTubers’ live streams about similar content as in real-person live streams. However, compared to prior research, there were unique content provided by VTubers’ and ways that viewers engaged with live streams.
-->

#### 4.2.1 主要な活動：歌、おしゃべり、ゲーム

インタビュー対象者によると，VTuber の活動としては，歌，チャット，ゲームの 3 つがよく見られます。現実のストリーマーの同様のパフォーマンス[44]と比較して、VTuber のコンテンツは、よりマンガやアニメのサブカルチャーに沿ったものになる傾向がありました。例えば、「VTuber は皆、アニメ、マンガ、ゲームに特化している。より深みがあるので、共鳴する部分も多いのかな」（P7）。また、「VTuber はいつも想像を絶する番組作りで感心させられる」（P12）、「まるでVTuberたちが一緒に遊んでいるかのような初心者向けの（ボードゲームの）企画だった」（P4）など、配信が楽しいものになるような独創的な番組企画も重視されていました。

また、バーチャル・アバターがもたらす斬新なストリーミングの機会もいくつか挙げられました。例えば、ゲームの共同配信では、2 人の Vtuber がアバターを入れ替えて配信しました。「慣れ親しんだ魂が新しい体になる、なんて楽しいんだろう！」（P17）、「彼らのアバターが今までやったことのないことをする」（P20）など、アバターと中の人のミスマッチに興奮している様子が伺えます。P19 は、あるVTuber が運営するショーでは、ステージ上のほとんどのキャラクターが VTuber のアバターのバリエーションで表現されていて、すべての声を同じ中の人が担当しているという話をしていた。

一般的には、3D アバターの方が 2D アバターよりも優れているという意見はありませんでしたが、3D アバターは全身の動きを利用してより高い表現力を得ることができるという点が評価されています。しかし、現在の 3D モーションキャプチャー技術は、経済的に不安定な VTuber にとっては高価なものであるため、2D アバターでも「おしゃべりするには十分」（P18）であると認識しているようでした。

<!--
Interviewees reported that singing, chatting, and gaming were the three most common VTuber activities they watched. In comparison to similar performances of real-person streamers [44], VTubers’ content tended to align more with manga and anime subcultures, e.g., “VTubers all have some specialties in anime, manga, and video game. There is more depth to it so is there more resonance.” (P7). There was also a strong emphasis on creative program planning to ensure that the streams are entertaining, e.g.,“VTubers always impress us with unimaginable program design” (P12). and “it was a (board game) campaign for newbies as if they played together” (P4).

Interviewees also noted several novel streaming opportunities that virtual avatars afford. For example, during a gaming co-streaming session, two Vtubers switched their avatars. Interviewees were excited by the mismatches between avatars and the Nakanohitos, e.g., “Familiar souls, new bodies, what fun it is!”(P17), and “Their avatars do things that they have never done before”(P20). P19 mentioned another VTuber who ran a show where most characters on the stage were represented by variants of the VTuber avatar that were all voiced by the same Nakanohito.

In general, interviewees did not have a strong preference on the 3D avatar streams over 2D ones, although appreciating 3D avatar’s ability to leverage full-body motions to achieve a higher degree of expressiveness. However, interviewees also recognized that current 3D motion capture technologies were costly for individual VTubers with unstable financial source, so 2D avatars were “good enough for chatting” (P18).
-->

#### 4.2.2 ナカノヒトの日常に関するコンテンツ

インタビュー参加者は、ナカノヒトがライブストリーム中に自分の個人的な日常生活を共有したり、現実世界の出来事について話したりすることを楽しんでいました。インタビューに答えてくれた人の多くは、熱心にアニメを見ていて、自分の好きなアニメのキャラクターが空想上のアニメの世界にしか存在しないことを知っています。しかし、VTuber が共有する日常生活のコンテンツは、皮肉にも VTuber がそうであるように見える典型的なアニメ・キャラクターよりも、視聴者に近いものとなっています。「**神楽めあ**は彼女（ナカノヒト）がどう過ごしているかについて話し、最近の日本の台風など様々な話題に言及します。彼女の経験はリアルで、現実の世界との共通点を感じさせるものです。彼女は、典型的なアニメキャラクターよりもずっと身近に感じられる」（P3）。この感覚は、P8 も「以前は、マネタイズのプレッシャーのために、仕事を終えてもプレッシャーから逃れられない『社畜（会社の奴隷）』だった神楽めあの中の人に、（本物らしさを）感じることができる」と語っています。この神楽めあの例では、企業が運営する VTuber であるにもかかわらず（[訳注[1]](#訳注)）、日常生活を公開することで、視聴者は彼女から「本物らしさ」を感じ取り、親近感を抱くことができます。また、「彼女が友達同士のおしゃべりのように生活を共有しているようで、面白いというよりはホッとする」（P5）というように、仲間意識を持つことも大切にしています。

<!--
Interviewees enjoyed that Nakanohitos shared their personal daily lives and talked about real-world events during live streams. Most interviewees are dedicated anime watchers and are aware that their favorite anime characters only exist in fantasized anime worlds. The daily life content that VTubers share, however, brings them closer to viewers than typical anime characters, which VTubers ironically appear to be, e.g., “Kagura Mea talks about how she (the Nakanohito) has been doing and comments on different events, like the recent typhoon in Japan ... Her experiences feel real, (it is) something that has a sense of commonalities with the real world ... She feels much closer than a typical anime character” (P3). This feeling was echoed by P8, “before, because of the pressure of monetization, (you can feel) the authenticity of Mea’s Nakanohito, a ‘corporate slave’ who could not escape from pressure even after getting off her work”. In this example of Kagura Mea, although she is a corporate-run VTuber, her sharing of daily lives made viewers perceive more ‘authenticity’ from her and feel closer to her. Our interviewees also valued having a sense of community and company, i.e., “(it is) like someone sharing her life just like chat between friends, (which is) more relieving than interesting”(P5).
-->

#### 4.2.3 コラボ配信

また、VTuber のライブ・ストリーミングの魅力的でポピュラーな形態として、複数のインタビュイーから、実在人物の共同配信に似たコラボ配信が挙げられています[38]。複数の VTuber のアバターが 1 つのバーチャル・ステージで一緒にパフォーマンスをする場合（図 1c）と、VTuber が他の実在のストリーマーと一緒にストリーミングする場合があります。後者の場合、VTuber と実在のストリーマーは通常、合成ビデオ・ストリームの中で並んで表示されるが、例外的に VTuber が物理的な世界のディスプレイに表示されることもあります。インタビューに答えてくださった 4 人の対象者が言及したように、VTuber の**高槻りつ**さんと生身のストリーマーである**鈴木悠太（ゆゆうた）**さんは、最も人気のある共演者の一組です。二人は、まるで恋人同士のように、ライブの様子を一緒に配信することがあります。彼らがお互いをサポートし、親密に交流している様子を、インタビュー対象者は楽しんでいました。

視聴者の中には、お気に入りの VTuber との共演をきっかけに、新たな VTuber を発見する人も少なくありません。VTuber が配信するパフォーマンスは、歌やチャット、ゲームなどが中心だが、VTuber の配信の魅力は、配信者同士の交流にあるとインタビュー対象者は強調しました。P6 は、「雑談のやりとりなど、一人での配信では見られない新しいコンテンツがたくさんある」と説明した。また、P7が「アンサンブルキャストのテレビ番組を見るように、ストリーマーのグループがお互いに親密な関係にあるのを見るのが好きです」と説明するように、VTuber 同士の友情や人間関係を楽しんでいる人もいました。

<!--
Co-streaming is also mentioned by several interviewees as an engaging and popular form of VTuber live streaming, similar to real-person co-streaming [38]. In some instances, the avatars of multiple VTubers perform on one virtual stage together (Figure 1c), whereas in other cases, VTubers stream with other realperson streamers. In the latter situation, VTubers and real-person streamers are typically shown side-by-side in a composite video stream, with occasional exceptions where VTubers appear on a display in the physical world. As mentioned by four interviewees, one of the most popular co-streaming pairs is VTuber Takatsuki Ritsu and real-person streamer Suzuki Yuyuuta. They sometimes co-stream live performances together, acting as if they were in romantic or platonic relationship. Interviewees enjoyed watching the pair support and interact with each other intimately.

Many viewers discovered new VTubers to watch because they had previously co-streamed with their favorite VTubers. Although the performances that VTubers co-stream are mostly composed of singing, chatting, and gaming, interviewees highlighted the interactions between streamers as what made VTuber streams engaging. P6 explained that "there is a lot of new content that you do not see in single-streamer sessions, like the exchange of banter". Some interviewees enjoyed displays of friendship or inter-personal relationships between VTubers, as P7 described, “I like seeing a group of streamers in close relationships with each other, like watching an ensemble cast TV show. ”.
-->

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392041634913603584">date</a></blockquote>

#### 4.2.4 体験に影響する技術的制約

現在、バーチャル・ストリーミングに利用できる技術は、コンテンツの多様性を制限し、視聴者との関係を築く上での制約となっていることがわかりました。

彼らはまず、アバターにもっと豊かで自然な表情を持たせたいと考えました。2D の VTuber をアニメーションさせるための最も一般的なツールである「Live2D」では、アバターのさまざまな部分のアニメーションがあらかじめ記録され、再生されます。2D アバターの顔には、眉毛、目、口など、アニメーションできる部分が限られているため、VTuber の言葉によるコミュニケーションが硬いように見えてしまいます。P6 は、「VTuber の表情がもっと豊かになって、自然に会話しているように見えるようになるといいですね……話しているときに表情が変わったりして」と語りました。

また、VTuber のパフォーマンスの多くは、中の人がパソコンの前で行う空間に限定されており、全身を使った動きや物理的な世界とのインタラクションはほとんどないことが分かりました。モーションキャプチャー技術は、3D アバターの全身アニメーションを可能にし、VTuber のコンテンツのレパートリーをダンスやモーション・センシング・ゲームなどに拡大することができるが、コストがかかり、制限がないわけではありません。P8 のコメントによると、「VTuber はフェイスキャプチャーに依存しているため、常にカメラを見ていなければなりません。大企業の中には 3D モーションキャプチャーを導入しているところもありますが、まだまだキャプチャーできずリアルな人間のストリームでしか見ることができないことは多いです」。バーチャル・ストリーミングの中では、実物を手に取って操作するなど、物理的な世界とのインタラクションが、技術的に大きな課題となっています。

<!--
Interviewees found that the technologies currently available for virtual streaming limit the diversity of content that is created and constrain streamers’ abilities to engage with viewers.

They first desired for avatars to have richer and more natural facial expressions. The most popular tool for animating 2D VTubers, Live2D, plays pre-recorded animations of different parts of an avatar. Since there are only a few animatable sections of a 2D avatar’s face (i.e., the eyebrows, eyes, and mouth), this limited set of available facial expressions made VTuber’s verbal communications look rigid. P6 remarked, “I hope that VTubers can have richer facial expressions, such that in conversations, they look more like real people talking naturally... facial expression changes as she talks”.

Viewers also found that most performances of VTubers were confined to the space that a Nakanohito had in front of their desktop computer and involved little full-body movement or interaction with the physical world. Motion capture technology can drive the full-body animation of 3D avatars and expand the repertoire of VTubers’ content to include dancing and motion sensing games, but it is costly and not free of limitations. As P8 commented, "VTubers rely on face capture and therefore have to look at the camera all the time. Some large companies have 3D motion capture, but there are still many things that it cannot capture and only visible on real-person streams". Within virtual streaming, interaction with the physical world, such as picking up and interacting with real objects, remains a substantial technical challenge.
-->

#### 4.2.5 配信の内外での視聴者のインタラクション

VTuber の視聴者間のインタラクションは、リアルな人のストリームでのインタラクションと多くの共通要素を持っているが [44, 64]、微妙な違いもあります。視聴者は VTuber を金銭的に支援することも厭わないが、サブカルチャーのアイデンティティを強化するために、ミームなどの文化的トークンの使用に注意を払っています。全てのインタビュー対象者が、YouTube Super Chat や Bilibili のチャンネルバッジを購入して VTuber を支援したことがあると回答しました。彼らの主な動機は，「（VTuber の）番組を見ていて，本当に楽しくてワクワクするときは，最低限の金額を払って応援する」（P7）など，現実のストリーム視聴者と同じように，楽しいコンテンツを提供するストリーマーを応援することにありました[44]．

今回のインタビューでは、VTuber のコミュニティにおけるミームの重要な役割が明らかになりました。コミュニティのメンバーは、VTuber のパフォーマンスの劇的な瞬間を、ライブストリームのスクリーンショットを使ってミームとして作成することが多いです。これらのミームは、図や文字で表現されることもあれば、その両方が混在することもあります（図 2）。NGA VTuber ディスカッションボードでは、人気のある VTuber のミームを新規参入者に紹介するためのスレッドがコミュニティで維持されていました。さらに、ミームは、ライブストリームやファングループのディスカッションのコメントで広く参照され、再現されました。視聴者は、ふざけて「Persecution(迫害/虐待)」と呼ばれる、ライブ配信中に配信者に関するいたずら心のあるミームを連続投稿する一群のミームに関わっていました。視聴者の間では、Persecution は、集団行動として、ストリームの全体的な娯楽性を高めるとともに、視聴者の集団的なアイデンティティを強化するものです[17]。VTuber のコミュニティでは、メンバーは、ミームの知識を学び、不適切と思われるミームの使用を拒否することで、グループのアイデンティティを強化しようとしました。P13 は、「ファングループのチャットで使われている最新のミームを理解できるように、より多くのストリームを見るようになりました」と報告しました。このような熱心な視聴者にとって、ミームの正しい意味や使い方を知ることは、外部の人間と差別化するための文化資本の一形態となり得ます[50]。

<!--
VTuber viewer interactions share many common elements with those within real-person streams [44, 64] but also bear subtle differences. While viewers were willing to provide monetary support to VTubers, they paid more attention to the usage of cultural tokens, such as memes, to reinforce their subculture identities. All interviewees reported that they had supported VTubers by purchasing YouTube Super Chat and Bilibili channel badges through a hierarchical membership system. Their main motivation was to show support for streamers who provided enjoyable content, similar to real-person stream viewers [44], e.g., "When I am really happy and excited while watching the (VTuber’s) program, I will pay the minimum amount to encourage her" (P7).

Our interviews revealed the important role of memes in VTuber communities. Members of these communities frequently created memes out of dramatic moments of VTubers’ performances with screenshots of live streams. These memes often took graphical or textual forms, or a mixture of both (Figure 2). On the NGA VTuber discussion board, there were community-maintained threads dedicated to introducing popular VTuber memes to newcomers. Further, memes were widely referenced and recreated in the comments of live streams and fan group discussions. Viewers often engaged in a particular type of group meme, playfully termed “persecution”, which involved the burst posting of mischievous memes about a streamer during their live stream. “Persecution”, as a group action, adds to the overall entertaining atmosphere of a stream while reinforcing the collective identity of the viewers [17]. In VTuber communities, members sought to strengthen the group’s identity by learning meme knowledge and rejecting meme usage that they deemed inappropriate. P13 reported that “I started to watch more streams so that I can understand the most recent memes used in the fan group cha”. For these dedicated viewers, knowing the correct meaning and usage of memes can be a form of cultural capital to differentiate them from outsiders [50].
-->

> Figure 2: Memes of VTubers. Names of VTubers with meme text translated, if available, from left to right: Nekomiya Hinata (What are the bosses talking about?), Tsukino Mito, Sasaki Saku (Arrogant), Natsuiro Matsur, Kizuna Ai (Ehyo-yo), Minato Aqua and Kagura Nana (How could crying help?).

<blockquote class="twitter-tweet" data-width="550" data-dnt="true" data-conversation="none"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1392041648977158147">date</a></blockquote>

### 4.3 VTuberと実在の配信者の間で認識されている違い

すべてのインタビュイーは、プラットフォームが宣伝する実在の配信者と VTuber の両方を視聴したことがありますが、実在の配信者よりも VTuber をより多く視聴する傾向がありました。VTuber と実在の配信者の違いについて明確に尋ねたところ、ほとんどのインタビュイーは、最初は両者に大きな違いはないと答えました。しかし、よくよく考えてみると、ほとんどの人が暗黙のうちにいくつかの重要な違いを感じていることを述べました。

<!--
All interviewees had watched both real-person streamers and VTubers, especially those promoted by the platform, and they tended to watch VTubers more than real-person streamers. When asked explicitly about the differences they perceived between VTubers and real-person streamers, most interviewees first reported no significant differences between the two. However, upon reflection, most of them implicitly mentioned several key differences they perceived.
-->

#### 4.3.1 配信者の行動に関する期待の違い

VTuber のアバターは、2 次元または 3 次元の「仮想」の形をしているため、VTuber が「仮想世界にいる」という意識を無意識に持っているとインタビュー対象者は言います。また、VTuber を見ていると、ゲームやアニメ、漫画などの仮想世界に対する期待と同じように、仮想世界に対して期待する規範が異なると感じます。「人間のストリーマーが『自分は異空間から来ました』と言ったら、それは嘘っぽくておかしいと感じます。しかし、VTuber がそれを言っても違和感はありません。彼女は仮想世界にいるのだから、彼女が言うことは仮想世界のことであり、そこでは不可能なことはほとんどないのです」（P5）。視聴者は仮想世界で起こりうることへの期待が（現実世界と）異なるため、実生活では恥ずかしい、受け入れられない、不適切な行動でも、VTuber の文脈では普通、受け入れられる、適切であることが多いです。例えば、視聴者は、VTuber の汚い言葉や攻撃的な言葉、「愚かな」行動に寛容であるように見えます。「私は彼女が時々ばかな行動をするし、彼女の表情がだらけていると思います。でも、彼女はバーチャル・キャラクターだから、そういうことをしても構わないと思っている。それが彼女のかわいらしさでもあります。もし人間のストリーマーがそのような行動をしたら、恥ずかしいし、奇妙すぎると思うでしょう」（P2）。

何人かのインタビュイーは、ストリーマーが視聴者からバーチャルギフトを募る傾向があることについてコメントしています。これは、中国のライブストリーミングに見られるユニークな報酬メカニズムです。彼らは、一部の実在のストリーマーがバーチャルギフトを勧誘する行為を嫌ったり、多くのお金を稼いでいるストリーマーに嫉妬したり、批判したりしていました。「私は美女の歌い手のような実在の配信者を視聴するのが嫌いです。彼らが俗物的だと思うからです。彼らはプレゼントを贈った人のランキングを強調しすぎる。自分の配信に力を入れることなく、視聴者にお金を要求するだけだから」（P3）。

しかし、VTuber の勧誘行為は、インタビューを受けた人たちには受け入れられているようだ。何人かのインタビュアーは、お金儲けに熱心なペルソナを持つ VTuber、神楽めあを挙げています。彼女の勧誘行為は、彼女のファンには受け入れられている、あるいは好意的に受け止められているようです。例えば、「彼女の勧誘行為は、彼女が自分のペルソナのように振る舞っていることがほとんどだと思います。彼女は本当に俗物的ではないし、金の亡者であるわけでもないです。彼女がギフトを要求するとき、彼女はかわいくて、それが私の好みです」（P8）。また、インタビュー対象者は「VTuber へのプレゼントは、ゲームでいうところのバーチャルグッズのようなもの。実在の人物にチップを渡す感覚ではない」（P3）など、お気に入りの VTuber にバーチャルギフトを購入することにも積極的なようです。

<!--
Interviewees noted that because a VTuber’s avatar is in a 2-D or 3-D “virtual” form, they unconsciously adopted a mindset that the VTuber was “in the virtual world”. They felt that when watching VTubers, they had different expected norms for the virtual world, similar to their expectations for the virtual worlds in games, anime, or comics. “If a human streamer says that she is from a different space, I would feel it is fake and strange. However, if a VTuber says this, I won’t think it strange. I think she is in the virtual world, so all she says is about the virtual world, where almost nothing is impossible. ”(P5) Because viewers have different expectations for what could happen in the virtual world, many behaviors that might be embarrassing, unacceptable, or inappropriate in real life could be normal, acceptable, and appropriate in VTubers’ contexts. For example, viewers seem more tolerant of VTubers’ dirty or offensive language or “stupid” behaviors, e.g., “I think sometimes she behaves in a stupid way, and her facial expression is dull. However, I know she is a virtual character, so such behaviors are acceptable. They make her cute. If a human streamer behaves like that, I will feel it embarrassing and too strange.” (P2)

Several interviewees commented on streamers’ inclinations to solicit virtual gifts from viewers, a unique reward mechanism prevalent within live streaming in China. They disliked some real-person streamers’ solicitation behaviors for virtual gifts and were jealous of, and had judgements about, streamers who earned much money, e.g., “I don’t like to watch real-person streamers, such as beautiful girls singing. I think they are snobbish. They emphasize the leaderboard of top gift-senders too much. They only ask for money from viewers without putting effort into their streams.”(P3).

However, VTubers’ solicitation behaviors seemed more acceptable to interviewees. Several interviewees mentioned Kagura Mea, a VTuber who has a persona of being enthusiastic to make money and often asks for gifting during her streams. Her acts of solicitation were seen as acceptable, or even favored, by her fans, e.g., “I think her solicitation is mostly that she acts like her persona. She is not really snobbish or money-mad. When she asks for gifts, it is cute, and I like it” (P8). Interviewees also seemed more willing to purchase virtual gifts for their favorite VTubers, e.g., “Purchasing virtual gifts for VTubers seems like purchasing virtual goods in games. It feels less like tipping to a real person” (P3).
-->

#### 4.3.2 距離感

視聴者は、生身の人間である配信者よりも、VTuber に距離感を感じているといいます。この距離感は、アバターを操る中の人のリアルな表情や非言語的な情報を視聴者が直接見ることができないという、アバターとの仮想的な媒介関係に起因するものであると考えられます。「VTuber のライブ配信を見ていると、仮面をかぶった俳優の演技を見ているような気分になります。私はアバターの背後に人がいると知っているのに、そうではないように感じるし彼女が遠く見えます」（P3）。

この距離感は、VTuber のペルソナによってさらに強調されます。多くの VTuber は、エキゾチック、ヴァンパイア、悪魔、姫、妖精、エイリアン、未来的な存在（futuristic）など、特定のアイデンティティを持ってデザインされており、アバターの視覚的な外見もそれらのアイデンティティに沿ったものとなっています。P13 が「VTuber を見て、リアルタイムでコメントして、自分のコメントが VTuber に読まれたり、反応されたりするのは、生身の人間から反応されるのとは違うと思う。たとえキャラクターの後ろに人間がいたとしても、別の世界のバーチャルなものと対話しているような感覚です」と説明するように、これらの独特なアイデンティティや見た目によってVTuberは人間ではないように感じられます。

このような距離感によって、視聴者は中の人の外見などよりも、ライブ配信の実際の内容に注目するようになります。例えば、「アバターは、内容やパフォーマンスに注目する雰囲気を作り、VTuber の背後にいる実在の人物からパフォーマンスや内容、ストーリーを切り離す」（P5）。

<!--
Interviewees reported that they felt more distant from VTubers than real-person streamers when watching live streams. This sense of distance partly originated from their virtual mediation with the avatar, wherein viewers could not directly see the real facial expressions or other non-verbal cues of the Nakanohito controlling the avatar, as noted by P3, “Watching VTubers’ live streams is like watching the performance of an actor wearing a mask. Although I know there is a human behind the avatar, it feels different and she becomes more distant”.

The sense of distance is further enhanced by the persona of the VTuber. Many VTubers are designed with a specific identity, e.g., exotic, vampire, devil, princess, fairy, alien, or futuristic, and the visual appearances of these avatars aligned with these identities. Due to these unique identities and appearances, VTubers were perceived less like a human, and thus, more distant from viewers, as described by P13, “When I am watching VTubers and commenting in real time, and my comments get read and responded by VTubers, I think it is different from getting responses from a real-person streamer. It is like interacting with something virtual, from a different world, even if there’s a human behind the character.”

This sense of distance causes viewers to pay more attention to the actual content of live streams than the appearance or other characteristics of the Nakanohito, e.g., “The avatar creates an atmosphere where I pay more attention to the content and performance, and isolate the performance, content, and stories from the real person behind the VTuber” (P5).
-->

#### 4.3.3 公のペルソナとアイデンティティ

芸能人やストリーマーのペルソナが暗黙的なものであるのに対し、VTuber のペルソナは明快で明白なものであると認識されます。彼らは、新しい VTuber が配信を開始するたびに、VTuber のペルソナに関する基本的な情報を明示的に提供するための自己紹介ビデオが制作され、オンラインで広く共有されていると報告しました。動画にはバーチャルキャラクターの背景やペルソナ、特徴などが含まれていることが多いです。このような動画は、視聴者にとって重要な導入体験であり、VTuber への最初の興味をかき立てるものです。しかし、VTuber の行動がデザインされたペルソナと一致するかどうかについては、多様な慣習があり、ペルソナは時間的に動的なものであることが多いとインタビューに答えています。

VTuber が作り出すペルソナは、アニメや漫画などのありふれたペルソナのテンプレートに沿って、サブカルチャー・コミュニティのメンバーにとって魅力的とされる個性的な要素を組み合わせた、シンプルで「フラット」なものになる傾向があります。日本の哲学者である東浩紀がコメントしたように、アニメのペルソナはしばしば「萌え（愛情）データベース」から構築されます[18]。VTuberは通常、彼らのペルソナが実在の人間より単純であることを保証する1つの核となる特徴を持ち、それはしばしば彼らを独特で有名なものにします。例えば、「**猫宮ひなた**は、猫耳をつけたかわいい女の子で、FPS（ファースト・パーソン・シューティング）ゲームを得意とするペルソナを持っています。彼女は PUBG で 16 人のプレイヤーを殺した有名なストリームで私を感動させてくれました」（P6）。

VTuber の中には、そのような本来の理想的な人物像に厳密に沿うことで、中の人をロールプレイヤーに変えてしまう人もいます。キズナアイはそのようなロールプレイング VTuber の一例であり、アニメや漫画によく出てくる、可愛くて明るくてたまにおっちょこちょいな女の子として登場します。視聴者はこの VTuber の素朴な人柄を容易に把握することができ、彼女の配信に触れるたびに、その可愛らしさの印象が蓄積され、強化されていきます。

他の VTuber のペルソナは、デザインされたペルソナとは異なり、中の人の特徴や実生活を公開しているものもあるなど、より柔軟なものとなっています。デザインされたペルソナと提示された VTuber 像との乖離は、新興の VTuber ではますます顕著になってきています。初期のペルソナと進化したペルソナの対比は、VTuber のコンテンツをより楽しいものにすることができます。例えば、「多くの新人 VTuber は、ペルソナに関する面白い紹介動画からスタートし、多くの視聴者の注目を集めます。しかし、実際に配信を開始してみると、ペルソナとは全く似ていないので、みんなびっくりしてしまう」（P5）などの声が聞かれました。

デザインされたペルソナを構成する個性的な要素は、よく受け入れられているものの、長年 VTuber を見てきた視聴者にとっては、慣れ親しんだもの、あるいは反復的なものに感じられるかもしれません。インタビューによると、VTuber の中には、視聴者を惹きつけるために「ドラマや対立」（P11）を生み出すために、意図的に相反する性格を持つ人がいるといいます。また、この矛盾は、中の人の性格とデザインされたペルソナの違いによるものだと指摘する人もいる。定期的に配信することで、中の人の性格やスタイルが無意識のうちに明らかになり、徐々に VTuber のペルソナに変化していくことが多いです。例えば、「中の人のリアルなリアクションが見られる場合もあり、彼女のスタイルや人格がわかる」（P15）。

<!--
Interviewees perceived that unlike real celebrities or streamers whose public personas are more implicit, the public personas of VTubers are more explicit and obvious. They reported that every time a new VTuber begins to stream, a self introduction video is produced and widely shared online to explicitly provide basic information about the persona of the VTuber. CHI ’21, May 8–13, 2021, Yokohama, Japan Zhicong Lu et al. The video often includes background stories of the virtual character, hisher persona, and characteristics. Such videos are an important on-boarding experience for viewers and drum up initial interests in a VTuber. However, interviewees believed that there were diverse practices with respect to the degree to which streamers’ behaviors aligned with a designed persona and also that personas were often temporally dynamic.

The personas that VTubers have created tend to follow commonplace anime or manga persona templates that seem simple and “flat”, combining personality elements that are known to be attractive to subculture community members. As the Japanese philosopher Azuma Hiroki commented, anime personas are often constructed out of the ‘moe (affection) database’ [18]. VTubers usually have one core characteristic that stood out to ensure that their persona was less complicated than a real human, which often makes them unique and popular, e.g., “Nekomiya Hinata has a persona of a cute girl with cat ears, who is skillful in playing FPS (first person shooter) games. She really impressed me in her famous stream where she killed 16 players in PUBG” (P6).

Some VTubers strictly aligned with such original ideal personas, thus transforming a Nakanohito into a role player. Kizuna Ai is an example of such a role-playing VTuber and is presented as a cute, cheerful and occasionally careless girl that is commonly seen in anime and manga. Viewers can easily grasp the simple persona of this VTuber and the impression of cuteness that she exudes accumulates and is reinforced with every exposure a viewer has to her stream.

Other VTubers’ personas can be more flexible, e.g., diverging from the originally designed persona, with some even disclosing the Nakanohito’s characteristics or real life. The discrepancy between the designed persona and the presented image of the VTuber has become more and more prevalent for emerging VTubers. The contrast between the initial and evolving personas can make a VTuber’s content more fun to watch, e.g., “Many new VTubers start from an interesting introduction video about the persona, which attracts many viewers’ attention. However, after they officially started streaming, everyone is astonished, because they do not act like the persona at all” (P5).

The personality elements that compose the designed personas, while well-accepted, may feel familiar or even repetitive to some long-time VTuber viewers. Interviewees noted that some VTubers intentionally have a conflicting personality to generate “drama and conflict” (P11) to attract viewers. Others noted that this discrepancy is due to the differences between Nakanohito’s personalities and designed personas. Through streaming regularly, Nakanohitos’ personalities and styles are often revealed unconsciously, gradually transforming into the VTuber’s persona, e.g., “I can see some of the Nakanohito’s real reactions in some cases, and it tells me about the style or personality of her” (P15).
-->

#### 4.3.4 状況によるペルソナの変容

また、公開されたペルソナは、視聴者の好みによって状況的に変化します。VTuber の中には、デザインされたペルソナと公開されたペルソナの不一致によって最初のうちは人気を得るものの、人気が出てくるとそれが課題になる人もいます。人気が出てくると、提示されたペルソナは、ニッチな視聴者にしかアピールできないため、フォロワーを集め続けることができない場合があります。この場合、多くの VTuber は、フォロワーが減らないように、より多くの視聴者に受け入れられるようにペルソナを調整しなければなりません。これは神楽めあにも起こったことで、例えば「めあは汚い言葉や不条理な行動で有名でした。しかし、以前よりも人気が出てきた今、彼女は荒らしを避けるために汚い言葉の使用を意図的に減らしています」（P7）。明示的なペルソナ変更は、視聴者と VTuber の間に相互作用を生み出す機会にもなっています。例えば、「VTuber がペルソナと矛盾した行動をとると、私たちはよくペルソナのことを言ってからかう。彼女は自分の行動を真剣に言い訳して説明します。それは私たちにとって、とても不条理で現実離れしていて、説明するのが難しい」(P21)。

VTuber のパフォーマティブな性質上、VTuber のデザインされたペルソナからの逸脱が、視聴者を惹きつけるための意図的な企画によるものなのか、それとも中の人の個性が溶け込んでいるのかを判断するのは困難です。このように、VTuber は商業的で視聴者を中心とした雰囲気を持っているため、彼らのアイデンティティーは両極端に流動的であり、視聴者へのアピールを維持するために変化することもあります。

<!--
Public personas also undergo situational changes with viewers’ preferences. While some VTubers gain initial popularity due to the discrepancies between their designed and presented personas, this becomes a challenge when they begin to gain traction. As they become more popular, a presented persona may not continue to attract followers because the discrepancies might only appeal to a niche group of viewers. In this case, many VTubers have to adjust their personas so that they cater to a broader audience and avoid losing followers. This happened with Kagura Mea, e.g., “Mea was famous for her dirty language and absurd behaviors. However, now she’s more popular than before, she intentionally reduces the use of dirty language to avoid attracting trolls”(P7). Explicit persona changes also provide opportunities to generate interactions between viewers and VTubers, e.g., “We often make fun of the VTuber by mentioning her persona when she behaves inconsistently with her persona. She will seriously explain her behaviors with excuses. It looks very absurd and beyond the reality for us, and hard to explain ”(P21).

Due to the performative nature of VTubers, it is hard to determine whether deviations from a VTuber’s designed persona result from intentional planning to attract viewership or from the Nakanohito’s personality blending in. The highly commercial and viewership-driven atmosphere among VTubers also results in their identities being more fluid between the ends of the spectrum and open to changes to maintain viewer appeal.
-->

#### 4.3.5 複数のチャンネルでの存在

また、VTuber は、様々なチャンネルを使って、バーチャルな生活や存在感を現実世界に広げているとインタビュー対象者は言及しました。アニメ、コミック、ガレージキット（アニメキャラクターの模型）、ゲーム、小説、ラジオなど、さまざまなチャンネルで VTuber が活躍していることが紹介されました。例えば、人気 VTuber の中には、キャラクターとその空想上の生活を描いたアニメやコミックを持っている人がいます。好きな VTuber の友達になりきって交流できるゲームも日本では人気があります。また、VTuber はオフラインのイベントに参加してファンと交流することもあります。つまり、VTuber は公共の大型ディスプレイに映し出され、リアルタイムでファンと交流するのです。

ほとんどの人は、このようなアーティファクトに興味を持ち、好きな VTuber と現実の世界でつながっていられる手段だと認識していた。また、これらのアーティファクト（例：ガレージキット）は、VTuber を現実世界に「物理的に」拡張する手段と考えており、好きな VTuber を応援するために購入を希望している。
「彼女のガレージキットを購入することで、現実の世界で彼女のコピーを手に入れ、それを私のそばに置くことができると考えています。それは彼女を応援することでもあります」（P8）など。

<!--
Interviewees also mentioned that VTubers extend their virtual lives and presence into the real world using many different channels. Interviewees provided several examples of VTubers’ growth into anime, comics, garage kits (i.e., model figures portraying anime characters), video games, novels, and traditional radio broadcasting channels. For example, several popular VTubers have anime and comics that tell stories about their characters and their imaginary lives. Video games that enable fans to role play as a friend of their favorite VTuber and interact with them are also popular in Japan. VTubers also travel to offline events to meet their fans, i.e., they are shown on a public large display and interact with fans in real time.

Most interviewees were interested in such artefacts and perceived them as a way to stay connected with their favorite VTubers in real life, in the real world. They also regarded these artefacts (e.g., garage kit) as a way to extend VTubers “physically” in the real world, and they desired to purchase them to support their favorite VTubers, e.g., “I think through buying a garage kit of her, I get a copy of her in the real world which can be with me. It is also my way to support her” (P8).
-->

### 4.4 ナカノヒトの身体的分離の認識及びナカノヒトの労働

中の人とは、アバターの背後で VTuber の声や動きをコントロールする人のことです。中の人は、VTuber の声や動きをコントロールする役割を担い、声質やライブ配信中に視聴者との会話を盛り上げる才能が求められます。中の人は、VTuber のパフォーマンスや視聴者との交流において重要な役割を担っていますが、VTuber の中の人は、ほとんどのライブ配信において見えません。多くの中の人は、個人情報保護の観点や企業の方針などから、自分の素性を公開していません。公開している場合でも、VTuber のアイデンティティは、中の人のアイデンティティよりも、企業や配信者が最初に設定した仮想アバターのペルソナによって決定されることがほとんどです。例えば、女性漫画家である**佃煮のりお**は、人気男性 VTuber である**犬山たまき**の中の人です。男性のキャラクターを女性が演じていることはわかっていても、バーチャルアバターの人物像に惹かれる視聴者は多いです。彼らは、佃煮のりおと犬山たまきが、あたかもコラボ配信をしているかのように同時進行で会話をするユニークな番組を楽しみます（図 3）。

このように、中の人とバーチャル・アバターとの関係が希薄であることは、バーチャル・ライブ・ストリーミングの特徴であり、アイデンティティ管理やユーザー・エンゲージメントに関する課題をもたらします。

<!--
A Nakanohito (中の人) is the person performing behind an avatar who provides the VTuber’s voice and controls their movements. A proficient Nakanohito must have a pleasant voice and talent for generating interesting conversations with viewers during live streams. Although they play a pivotal role in VTubers’ performances and interactions with viewers, a VTuber’s Nakanohito remains invisible throughout most live streams. Most Nakanohitos do not disclose their personal identity to the public, due to privacy concerns or corporations’ policies. Even for those who do disclose some of their personal information to the public, VTubers’ identities are mostly determined by the persona of the virtual avatar that was initially set by the company or the streamer rather than the Nakanohito’s identity. For example, Tsukudani Norio (佃煮のりお) is a female manga artist, who is the Nakanohito of a popular male VTuber Inuyama Tamaki (犬山たまき). Although viewers know that a female is portraying a male character, many viewers are still attracted to the persona of the virtual avatar. They enjoy watching a unique show wherein Tsukudani Norio and Inuyama Tamaki stream simultaneously talking to each other, as if they were co-streaming (Figure 3).

The degree of disembodiment between Nakanohitos and their virtual avatars is unique in virtual live streaming, as it brings forth challenges related to identity management and user engagement.
-->

#### 4.4.1 ナカノヒトとアバターの分離を意図的に維持する

VTuber のコミュニティでは、なかのひとの個人情報はデリケートなものであり、視聴者がネット上でそのような話をすることは避けるべきであるという認識で一致しているとインタビューに答えています。例えば、NGA の VTuber サブフォーラムでは、なかのひとの正体や個人情報の公開を禁止することが第一のルールとなっています（図 4）。これらのコミュニティメンバーは、中の人の個人情報の拡散を制限することで、VTuber の中の人との分離を積極的に維持しています。ほとんどのインタビュイーは、なかのひとに興味はあっても、その素性を知ることにはあまり関心がないと答えており、なかのひとのプライバシーを詮索するような行為を否定しています。たとえば、「なかのひとの素性を知ったり聞いたりすることはない。彼らのプライバシーは尊重されるべきだ」（P8）。中の人の個人情報を話さないというルールは企業や他のステークホルダーから要求されたり、提案されたりするものだと指摘する人もいます。「彼らの戦略はリスクやトラブルを避けるため中の人を見えなくすることであり、中の人に関する議論を禁じることは運営や経営にとって良いことなのかもしれません」（P13）。興味深いことに、ほとんどのコミュニティメンバーは、これらのルールが企業の利益のためのものだと知っていても、それを支持し、守りました。

<!--
Interviewees noted that the VTuber community agreed that personal information about Nakanohitos is sensitive and viewers should avoid talking about it online. For example, on the VTuber sub-forum of NGA, the first rule was that discussions about the identity of Nakanohitos and disclosing their personal information was prohibited (Figure 4). These community members actively maintain the disembodiment of VTubers by limiting the spread of Nakanohito’s personal information. Most interviewees reported that although they were curious about Nakanohitos, they had little interest in knowing their identities and they denounced behaviors relating to prying into Nakanohitos’ privacy, e.g., “I tend not to know or ask about Nakanohitos’ identities. Their privacy should be respected” (P8). Some interviewees noted that rules about not discussing Nakanohito’s personal information are required or suggested by corporations or other stakeholders, because “their strategies are to make Nakanohito more invisible to avoid risks or trouble. Prohibiting discussions about Nakanohito could be good for their operation and management” (P13). Interestingly, most community members supported and followed these rules even if they knew that they were for corporate interests.
-->

> Figure 3: Tsukudani Norio talking with her own VTuber avatar in a live stream. Left: Tsukudani Norio talking in her real identity; Right: Tsukudani Norio talking as VTuber Inuyama Tamaki with her own face covered.

> Figure 4: Rules of NGA’s VTuber subforum. Translation of text: (1) Discussing a Nakanohitoe’s identity is prohibited, unless it has been disclosed implicitly in activities; (2) Discussing accidentally leaked Nakanohito personal information is prohibited; (3) Under certain circumstances, discussions about certain Nakanohito-related topics may be allowed by the forum committee.

#### 4.4.2 完全な印象を保つためにナカノヒトとアバターの分離を維持する

バーチャル・アバターの完璧なイメージを維持するために、分離を意図的に支持するインタビュイーもいました。「中の人がVTuberのペルソナと全く異なる、例えば中の人の容姿がアバターほどかわいくないなどのことを知ってしまった場合は、彼女のビデオやストリームを見て、とてもがっかりしたり、不快に感じたりして、彼女を見捨ててしまうこともあります」（P8）。このような女性蔑視的な感情は、オタク・コミュニティ[27]における可愛らしさへの嗜好や、VTuber との心理的な距離感、VTuber を実在の人物よりもキャラクターとして認識していることが根底にあると考えられます。

中の人は裏方であり、配信時には声を公開したり変えたりするだけなので、視聴者が中の人の本当の人格やアイデンティティを推察する情報は限られています。一方で、バーチャルなアバターは、ペルソナの設定や背景のストーリーがよく練られていることが多く、視聴者に「完璧な印象」を与えることができます。時間が経つにつれ、視聴者は「中の人もアバターのように完璧な存在である」と思うようになるかもしれません。視聴者の中には、中の人の本当の姿を見てしまうと、自分の中のファンタジーが崩れてしまう人もいます。

「VTuber はバーチャルの世界では完璧。彼女のパフォーマンスを評価するためには、私たちは中の人とは距離を置くべきだと思います。近くで見ているとファンタジーが台無しになる。神楽めあの中の人の情報を探ろうとした人がいました。その人は、自分の想像とは違う写真を見つけました。その人はがっかりして、二度と彼女のストリームを見なかったのです。しかし、実際にはその中の人は自分の写真をネットにアップしていなかったのです」(P10)。

<!--
Some interviewees intentionally supported disembodiment for the sake of maintaining the perfect image of the virtual avatar in their mind, e.g., “In some cases, if I know that the Nakanohito is totally different from her persona, for example, if her style is not as cute as the avatar. I may get very disappointed and feel uncomfortable when watching her videos or streams, even abandon her” (P8). This misogyny sentiment may root from preferences for cuteness in the Otaku community [27], the psychological distance they perceived with the VTuber, and that they perceived the VTuber more as a character than as a real person.

Because Nakanohitos are behind the scenes and only disclose or alter their voice when streaming, viewers have limited information to infer about Nakanohitos’ real personalities and identities. On the other hand, virtual avatars often have well-designed persona settings and background stories which often leave “perfect impressions” on viewers. As time goes on, viewers may begin to believe that the Nakanohito is also as perfect as the virtual avatar. For some viewers, seeing the real side of the Nakanohito would ruin the fantasy in their mind, e.g.,

“VTuber is perfect in the virtual world. We should keep a distance from the Nakanohito to appreciate her performance. Watching up close will ruin the fantasy. Someone tried to dig out information about Kagura Mea’s Nakanohito. He found a photo of her that does not align with his imagination. He was so disappointed that he never watched her streams again. But actually the Nakanohito did not post her photos online.” (P10)
-->

#### 4.4.3 企業が中の人を交代させることへの無関心

中の人とバーチャル・アバターの乖離は、中の人の交代についての無関心さにも表れている。キズナアイのケースなど、中の人が事務所に置き換えられたケースについては、すべてのインタビュアーが言及している。自分の好きな VTuber の中の人が入れ替わったらどう思うか」という質問に対しては、ほとんどの人が「関係ない」と回答しています。

中には、VTuber と一緒に体験したコンテンツの質を重視する人もいて、それは中の人自身の努力というよりも、チームワークの賜物であることが多いようです。このようなケースでは、中の人が自分の体験に与える影響は限られたものになります。例えば、「多くの浅い視聴者は、ストリームやペルソナの質が変わらなければ、中の人が交代したことに気づかないでしょう。チームがプロフェッショナルであれば、中の人が交代しても実現できる」（P4）。

中の人を経験豊富な人に代えたほうが、より質の高いコンテンツを提供できると考えている人もいました。例えば、「VTuber にとって中の人は欠かせない存在だが、彼女がプロジェクトの全てではありません。新しい中の人が面白ければ、その人のライブ配信を見続けます」（P6）など、人よりも中の人のスキルを重視しているようです。

中の人が交代する可能性を、VTuber独自の特徴として考えているインタビュアーもいた。例えば、P11 は、VTuber の中の人が入れ替わることは、人が人生のステージを変えていくことに似ており、それによって新たな新鮮さや魅力が生まれると述べています。「私はVTuber も人間と同じように成長していくものだと考えるようにしています。違う中の人はVTuberの異なるライフステージを代表しますが、VTuberは同じVTuberのままなのです。会社がスムーズに中の人を異動させてくれれば、それはそれでいいと思います」。

<!--
The disembodiment of Nakanohito and virtual avatars is also reflected by indifferent attitudes towards replacing Nakanohitos. All interviewees mentioned cases where Nakanohitos were replaced by agencies, e.g., Kizuna Ai’s case. When asked to reflect on how they would feel if their favorite VTuber’s Nakanohito were replaced, most interviewees did not think it would matter.

Some interviewees cared most about the quality of the content they experienced with a VTuber, which was often the outcome of teamwork, rather than a Nakanohito’s own efforts. In these cases, the influence of Nakanohitos on their experiences was limited, e.g., “Many shallow viewers will not notice that the Nakanohito is replaced if the quality of the streams and personas remain unchanged... If the team is professional, it is achievable even if Nakanohito is replaced”(P4).

Some interviewees thought that replacing the Nakanohito with a more experienced one would provide better quality content. They cared more about the Nakanohito’s skill set than the person, e.g., “The Nakanohito is essential for a VTuber, but she is not the entire project. If the new one is interesting enough, I will keep watching her live streams” (P6).

Some interviewees considered the possibility of replacing Nakanohito as a unique feature. For example, P11 noted that having different Nakanohitos for one VTuber was similar to a person journeying through different life stages, which could bring new levels of freshness and engagement, “I prefer to think in this way that VTuber can grow over time just like human ... Different Nakanohitos represent the VTuber in different life stages, but it is the same VTuber. I will accept this if the company transfers Nakanohitos smoothly”
-->

#### 4.4.4 視聴者は中の人の労働の公平性を気にかけている

多くの人は、ナカノヒトが交代することは受け入れられるが、交代するにはそれなりの理由が必要だと考えている。特に、なかのひとたちの労働条件や待遇を気にしていました。

2019 年 4 月、**「ゲーム部プロジェクト」**に参加していた 4 人のなかのひとが、運営会社であるUnlimitedから残業やセクハラなどの不当な扱いを受けたと告発しました。同社はすぐに 4 人のなかのひとたちを交代させました。これを受けて、視聴者コミュニティからの不買運動により、最終的に「ゲーム部」プロジェクトは終了しました。一方で、適切な理由があれば、視聴者は交代を受け入れることができます。例えば、**ReVdol** のうち1人の VTuber の中の人が一身上の都合で辞任しましたが、視聴者はほとんど彼女の選択を支持しました。

また、インタビューに答えてくださった方全員が、元の中の人が公平に扱われていることを確認しない限り、新しい中の人を受け入れることはないとおっしゃっていました。例えば、P4 は「会社が儲けたいからといって、なかのひとを変えてしまうのはひどいことだ」と述べています。P3 は「会社がナカノヒトを酷使したら許せない」と述べています。

<!--
Although most interviewees could accept the replacement of a Nakanohito, they felt that they were owed a proper reason for this change in personnel. In particular, they cared about Nakanohitos’ working conditions and fair treatment.

In 2019 April, four Nakanohitoes in the Game Club project accused the Unlimited operating company of unfair treatment, including overtime work and sexual harassment. The company soon replaced all four Nakanohitos. In response to this, the Game Club project was eventually terminated due to a boycott from the viewer community. On the other hand, the viewers can accept the replacement if there are appropriate reasons. For example, the Nakanohito of one of ReVdol’s VTubers resigned for personal reasons, and viewers mostly supported her choice.

All interviewees mentioned that they would not accept a new Nakanohito without confirming that the original Nakanohito was treated fairly. For example, P4 mentioned that “It’s an awful thing to change Nakanohito only because the company wants to make more money.”. P3 stated that, “we won’t forgive the company if they abuse a Nakanohito”.
-->

## 5 考察

私たちの研究は、VTuber のライブストリーミングの多くの新しい側面を明らかにしました。ここでは、私たちが発見した重要な点を紹介し、先行研究との比較を行い、HCI への洞察と示唆を議論します。

<!--
Our study uncovered many novel facets of VTuber live streaming. We now reflect and highlight our key findings, situate our results with prior research, and discuss insights and implications for HCI.
-->

### 5.1 多層化したアイデンティティ及びライブ配信におけるバーチャルとリアルの境界線

今回の調査結果から、VTuber のライブストリーミングは、仮想世界と現実世界が融合したパフォーマンスの一形態であることが示唆されました。しかし、現実の自分と仮想の自分の境界は常に変化しており、社会的な相互作用に影響を与えている。

これらの結果はまず、VTuber ライブストリーミングにおいて、視聴者が仮想アバターを媒介として中の人のパフォーマンスを見る場合、アバターに対する視聴者の解釈は様々な要因に依存し、CMC の Hyperpersonal Model [61, 62]とは必ずしも一致しないことを示す証拠となる。視聴者の VTuber を見る動機も重要な要素であろう。一方で、バーチャルなアバターとそのペルソナに魅力を感じる視聴者は、VTuber の行動とペルソナの間の整合性に厳しいかもしれません。シンプルでわかりやすいペルソナと個性的な外見を持つアバターからの合図を過剰に解釈してしまうことがあります。そのため、視聴者は VTuber に対して完璧に近い印象を持つことができ、ファンのようについていくことができ、これは Hyperpersonal Model に合致する。このようなファンは、アニメ領域のファンダムのように、アバターと独自の結びつきを維持しているようだ。一方で、VTuber を友人のように思っている視聴者もいて、VTuber が架空の、あるいは中の人の現実の日常生活を共有することを楽しんでいる。このような視聴者にとっては、VTuber の行動とペルソナの整合性はあまり重要ではなく、バーチャル・アバターというアニメの仮面に隠された中の人の個性、あるいは中の人の「キャラクター」の方が重要なのである。これは VTuber の意図するところではないことが多く、Hyperpersonal Model にも合致しません。このようにアイデンティティが多層化することで、アバターと中の人の解釈に矛盾が生じる視聴者が出てくるのではないでしょうか。視聴者は、VTuber の複数のアイデンティティを選択的に解釈し、創造的に関与するエージェンシーを持っています。

VTuber がライブ配信するコンテンツは、バーチャルとリアルが混在しています。VTuber は、現実世界でのスキルや経験に基づいたコンテンツを提供することで、仮想世界のペルソナを構築しており、VTuber と視聴者の間には距離感があります。このペルソナが VTuber の仮想的なアイデンティティを構築するが、これは先行研究[39]と同様である。さらに、ライブストリームやソーシャルネットワーク（ファングループなど）における視聴者のインタラクションも、VTuber のアイデンティティ構築に影響を与えることを示している。ライブストリームの予測不可能性は、視聴者が VTuber と共同体験するストーリーを増やすことに貢献し、これらのストーリーは徐々に VTuber のペルソナに融合していく。視聴者がコミュニティ内でミームを作成して拡散することで、VTuber のオンライン・アイデンティティをさらに高めることができる。

VTuber の配信では、バーチャルとリアルの境界線がダイナミックで曖昧であるため、視聴者はバーチャルなアバターと中の人を別々に考えるのではなく、VTuber をバーチャル世界のキャラクターとして、現実世界の社会的規範に左右されないように考えることが多い。このような考え方は、VTuber の不適切な行動に対して視聴者を寛容にさせ、中の人を交代させるVTuber事務所に対して視聴者が無関心であることの一因となっていると考えられる。しかし、VTuber の仮想と現実の境界がどこにあるかは、視聴者個人によって異なり、外部からの影響によっても変化する可能性がある。時には、現実の複雑さが入り込んできて、幻想が壊れることもある。視聴者がコミュニティ内の集団行動（ボイコットなど）を通じて、事務所がナカノヒトを虐待したり、納得のいく理由もなく交代させたりしていることを知り、バーチャルな「側」が崩壊したのはその顕著な例である。このことは、バーチャルなアバターを媒介とした空間において、透明性と公平性を求める集団行動の重要性についての Kou ら[32]の所見を反映している。

<!--
Our findings suggest that VTuber live streaming is a form of performance where the virtual and the real worlds converge. However, the boundaries between real and virtual selves are ever-changing, thus influencing social interactions.

These results first provide evidence that in VTuber live streaming, where viewers watch performances of Nakanohitos through the mediation of a virtual avatar, viewer’s interpretations of the avatar depend on a number of factors, and do not always align with the Hyperpersonal Model of CMC [61, 62]. Viewers’ motivations to watch VTuber may be an important factor. On one hand, some viewers who are more attracted by the virtual avatar and its persona may be more strict about the consistency between VTuber’s behaviors and personas. They may often over-interpret cues from an avatar who has a simple and straight-forward persona and unique appearance. Viewers can thus form a close-to-perfect impression of a VTuber and follow her like fans, which aligns with the Hyperpersonal Model. These fans seem to maintain a unique tie to the avatar, similar to fandom in the anime domain. On the other hand, some viewers regard VTubers as friends and enjoy when VTubers share details about their daily life with them, either fictional or from the Nakanohito’s real life. For these viewers, consistency between VTuber’s behaviors and persona is less important because they care more about the personality or even the ‘character’ of the Nakanohito, which is the presented self of the Nakanohito behind the anime mask of the virtual avatar. This is often not the intention of VTubers and does not align with the Hyperpersonal Model. Such multiple layers of identity may be the reason why some viewers may have conflicting interpretations of the avatar and Nakanohito. Viewers have agency to selectively interpret and creatively engage with VTubers’ multiple identities.

The content that VTubers live stream is a mixture of virtual and real. VTubers build their virtual world persona by providing content based on their skills and experiences in the real world, resulting in a sense of distance between the VTuber and their viewers. This persona constructs the virtual identity of the VTuber, which echoes prior research [39]. We further show that viewers’ interactions in live-streams and social networks (e.g. fan groups) also affect VTubers’ identity construction. The unpredictability of live streams can contribute to more stories that viewers co-experience with a VTuber and these stories gradually merge into a VTuber’s persona. Viewers’ interactions within the community, encouraged by the creation and spreading of memes, can further add to VTubers’ online identities.

Because the line between virtual and real in VTuber streaming is dynamic and blurry, viewers often do not consider a virtual avatar and the Nakanohito separately, but rather, regard the VTuber as a character in the virtual world and thus less subject to real world social norms. This mindset makes viewers more tolerant to VTubers’ inappropriate behaviors and may contribute to viewers’ indifferent attitudes towards agencies replacing Nakanohitos. However, where the virtuality-reality boundary of VTubers lies varies on individual viewers and may be shifted by external influences. Occasionally, the complexity of reality cuts in and breaks the illusion. A notable example occurred when the virtual “side” collapsed when viewers found out, through collective actions within the community (e.g., boycotts), that agencies were mistreating Nakanohitos and replacing them without an acceptable reason. This echoes findings of Kou et al. [32] about the importance of collective actions in seeking transparency and fairness in spaces mediated by virtual avatars.
-->

### 5.2 企業の役割及び（バーチャル）ライブ配信者の労働

これまでの文献では、ライブ・ストリーミング業界の労働問題について論じられています。例えば、Woodcock and Johnson [65]は、感情的労働と非物質的労働という理論的レンズを用いて、Twitch におけるさまざまなストリーマーの活動（観客とのパラソーシャルな親密性の構築、寄付の募集など）を調査し、現代のデジタルワークの風景の一部としてライブストリーミングを研究するためのさらなる取り組みを求めました。

このような研究に貢献するために、今回の結果は、熱心な視聴者が、ライブストリーミングにおける労働、すなわち、しばしば隠され、目に見えないナカノヒトの労働をどのように認識し、気にかけているかを示しました。個人ブランドを構築して報酬を得ることができる実在のストリーマー [44, 64]とは異なり、なかのひとたちは、ほとんどがストリームの舞台裏にいるため、個人ブランディングを行うことは困難です。VTuber の場合、視聴者からのブランドや感情的な愛着は、ほとんどが仮想アバターに対するものです。そのため、企業がなかのひとたちを交代させることに無関心な視聴者がいたのかもしれません。

また、VTuber のコンテンツ制作に必要な技術やアバターの知的財産は企業に帰属することが多く、なかのひとは不利な立場に置かれています。企業はいつでもコストをかけずになかのひとを変更することができます。これは、東アジアのポップカルチャーにおける消費者資本主義の極端な例であり、バーチャル・アイドルが自律的な存在でないことが、「彼女を交換可能で使い捨て可能なイメージ商品にしている」ということである[19]。このことはまた、ライブストリーミング産業が成長し、より利益を生むようになると、新たな労働搾取の形態も出現する可能性があることを思い起こさせる。現在、私たちは、なかのひとを含むさまざまなタイプのストリーマーが貢献している労働について、また、業界を規制し、労働者の権利を保護するために利用可能な政策オプションについて、限られた理解しか持っていません。

<!--
Previous literature has discussed labor issues in the live streaming industry. For example, Woodcock and Johnson [65] used the theoretical lenses of affective and immaterial labor to explore a range of streamer activities on Twitch (e.g., building para-social intimacy with spectators, soliciting donations, etc.), and called for more efforts to study live streaming as part of the landscape of contemporary digital work.

Contributing to this line of research, these results showed how dedicated viewers perceive and care about the labor in live streaming, i.e., the often hidden and invisible labor of Nakanohitos. Unlike real-person streamers who can build their personal brand and be rewarded [44, 64], it is hard for Nakanohitos to conduct personal branding, as they are mostly behind the scenes of a stream. For VTubers, the brand and emotional attachments from viewers are mostly for the virtual avatar. This could be why some viewers had indifferent attitudes towards corporations replacing Nakanohitos.

Additionally, most of the time, the intellectual property of the avatar and the technologies required for producing VTuber content belongs to a corporation, which places a Nakanohito at a disadvantaged position. A corporation could change Nakanohitos at any time, without much cost. This is an extreme example of consumer capitalism in pop culture in East Asia, in that a virtual idol’s lack of an autonomous existence “makes her an interchangeable and disposable image commodity” [19]. This also reminds us that as the live streaming industry grows and becomes more lucrative, new forms of labor exploitation may also emerge. Currently, we have a limited understanding of the labor contributed by different types of streamers, including Nakanohito, and of the policy options that might be leveraged to regulate the industry and to protect labor rights.
-->

### 5.3 VTuberのライブ配信における課題

新興の VTuber ライブストリーミングを探ることで、バーチャルライブストリーマーが抱えるいくつかのユニークな課題を明らかにし、その結果を先行研究と比較することで、ライブストリーマーのプロ意識についての洞察を得ました。

<!--
By exploring the emerging VTuber live streaming, we unveiled several unique challenges that virtual live streamers have and compare our findings to prior research to provide insights into the professionalism of live streamers.
-->

#### 5.3.1 バーチャルなアイデンティティの構築

熱心な視聴者は、VTuber がストーリーやパフォーマンスを通じてアイデンティティをダイナミックに構築し、異なる嗜好を持つ視聴者を惹きつけたり、中の人の性格や生活の一部を意図的に明らかにしてコントラストを生み出し、視聴者を楽しませたりしていると認識していた。これらの結果は、Second Life 上のファッション・ブロガーのアイデンティティの再構築に関する知見を反映したもので、「仮想の身体は、継続的なアイデンティティの再構築の連続体の一片に過ぎない」というものです[39]。VTuber のオンライン・アイデンティティは、刻々と変化するアバターの身体と、中の人のリアルなアイデンティティを媒介としている。

また、ライブ配信の視聴者も、VTuber のアイデンティティに大きな影響を与えています。ライブ配信中の視聴者のコメントは、VTuber の既存のペルソナを補完したり変容させたりする瞬間を生み出し、また、ライブ配信中に作られたミームをグループチャットや他のファンコミュニティで広めるなど、ライブ配信にとどまらない交流が行われています。VTuber のパーソナリティは、最初はシンプルなデザインですが、視聴者とのやりとりの中で、より複雑に変化していきます。これは、VTuber にとっての課題でもあります。バーチャル・アイデンティティが複雑化し、視聴者の期待がダイナミックに変化すると、中の人は一貫したペルソナやイメージを効果的に維持することができず、ファンを失う可能性があります。

<!--
Dedicated viewers perceived that VTubers construct their identities dynamically through stories and performances to attract viewers with different tastes or to intentionally reveal parts of a Nakanohito’s personality or life to generate contrast and amuse viewers. These results echo findings about the identity reassembling of fashion bloggers on Second Life, in that “a virtual body is only a slice of the continuum of ongoing identity reassemblin” [39]. VTubers’ online identities are mediated through ever-changing avatar bodies and Nakanohito’s real identities.

Live streaming viewers also have a profound impact on VTubers’ identities. Their comments during live streams create moments that complement and transform streamers’ existing personas and their interactions go beyond the live streams, e.g., spreading memes created during live streams in group chats and other fan communities. VTubers’ personalities usually begin with simple designs, but evolve to be more complicated through the interactions they have with viewers. This creates challenges for VTubers. As their virtual identities become more complex and viewers’ expectations change dynamically, Nakanohitos cannot effectively maintain a consistent persona or image, which will potentially lead them to lose fans.
-->

#### 5.3.2 交代可能、または複数の中の人

VTuber の特徴は、アバターと中の人が、コミュニティと企業の両方から意図的に切り離されていることです。そのため、VTuber は中の人を入れ替えたり、複数の中の人が同じアバターの後ろで別々のコンテンツを演じたりすることができます。例えば、2 人のなかのひとが一緒に配信し、1 人はゲームをし、もう 1 人は視聴者との交流に専念することができます。また、それぞれのなかのひとが得意とするコンテンツを交代で視聴者に届けることもできます。コンテンツの質が損なわれず、プロセスが透明である限り、視聴者がこうした慣行を受け入れていることは驚くべきことです。しかし、こうしたやり方は、VTuber のチームに課題をもたらします。なかのひとを変更することで、VTuber の喋り方などが変わってしまうことがあり、それがまたファン離れにつながってしまうこともあります。

<!--
VTubers are unique in that the avatar and the Nakanohito are intentionally disembodied by both the community and a corporation. Because of this, VTubers could have Nakanohitos replaced or even have multiple Nakanohitos performing different content behind the same avatar together or separately. For example, two Nakanohitos could stream together, with one focusing on playing a game and another on interacting with viewers. Different Nakanohitos could also take turns delivering content that they have expertise in to viewers. It is surprising that viewers are accepting these practices, as long as the quality of the content remains untainted and the process is transparent. These practices, however, bring challenges to VTubers’ teams. Changing Nakanohito sometimes also changes the talking style or other traits of the VTuber, which may again leads to a loss of fans.
-->

#### 5.3.3 コンテンツの多様性

4.2.4 で述べたように、VTuber は、技術的な制約のために、実在するストリーマーのような表現方法を行うことができません。まず、VTuber は、手作りチュートリアル[41]や旅行体験の共有[42]など、多くの人気ストリーミングジャンルの舞台である、現実世界との物理的なインタラクションを伴うコンテンツを提供することができません。VTuber が実在のストリーマーと共演する試みはあるが、VTuber の存在は、物理的な環境にあるコンピュータ・ディスプレイにしか固定できない。さらに、ゲームやアニメーション映画のような他のコンピュータ・グラフィック体験におけるキャラクターとは対照的に、VTuber のアバターは、彼らが存在する仮想環境とほとんど相互作用しないため、強化された物語やストーリーテリングの機会を逃してしまう。

<!--
As discussed in 4.2.4, VTubers can not perform in an expressive manner as real-person streamers can due to technology constraints. Firstly, VTubers cannot provide content involving physical interactions with the real world which is the stage for many popular streaming genres, such as handcrafting tutorials [41] or travel experience sharing [42]. While there have been attempts by VTubers to co-stream with real-person streamers, the presence of VTubers can only be fixed to computer displays in physical environments. Moreover, in contrast to the characters in other computer graphic experiences such as games or animated movies, VTuber avatars rarely interact with the virtual environments they reside in, missing out on opportunities for enhanced narratives and storytelling.
--->

### 5.4 デザインの示唆

VTuber に関する私たちの発見は、HCI や CSCW で現在行われている、インクルーシブ・ライブストリーミング、AI を介したコミュニケーション[28]、ソーシャルメディア上での欺瞞に関する議論に関連しています。仮想アバターを使えば，自分の障害や不完全さを公表したくない人も，別のアイデンティティを構築することで，自分の才能を発信したり，ライブストリーミングでストーリーを共有したりすることを快適に感じるかもしれない．今後、AI 技術がさらに進化すれば、さまざまなバーチャルアイドルの外見を自動的に生成したり、キャラクターデザインや背景ストーリーを作成したり、さらには声を変えたりすることがより容易になるでしょう。現実のホストの声、表情、ジェスチャーを機械学習によってシミュレートする、完全に AI を搭載したテレビ番組のホストを作り始めた企業もすでにある[33]。ここでは、将来のライブ・ストリーミング・サービスの設計、実装、および調査に役立つ、いくつかの設計上の考慮事項について詳しく説明します。

<!--
Our findings about VTuber relates to the ongoing discussion in HCI and CSCW about inclusive live streaming, AI-mediated communication [28], and deception on social media. With virtual avatars, people who are unwilling to disclose their disabilities or imperfections may feel more comfortable broadcasting their talents and sharing stories through live streaming by constructing a different identity. With more and more advanced AI technology, automatically generating the appearance of different virtual idols, creating character designs and background stories, or even altering voices, will become much easier. Some companies have already begun creating fully AI-powered TV program hosts that use machine learning to simulate the voice, facial expressions, and gestures of real-life hosts [33]. We now detail several design considerations which should inform the design, implementation, and exploration of future live streaming services.
-->

#### 5.4.1 アイデンティティ管理のためのデザイン

我々の結果は、VTuber が自分のアイデンティティを動的に構築し、中の人の特徴や視聴者のコミュニティへの参加状況に応じて、時間の経過とともにアイデンティティを進化させていくことを示している。さらに、VTuber は異なる中の人を持つこともあれば、複数の中の人が協力してパフォーマンスを行うこともあります。このように複雑な要素があるため、VTuber が一貫したアイデンティティを維持することは困難ですが、安定したファン層を維持するためには重要です。そのため、VTuber のためのコラボレーション・アイデンティティ管理ツールを提供することで、中の人たちがライブ・ストリーム中に一貫したアイデンティティを維持するためのガイドラインや実行可能な戦略を提供することができると考えられます。例えば、視聴者がライブストリーム中になかのひとのアイデンティティを明らかにするリスクのあるコメントを送ってきた場合、ツールはなかのひとにそのリスクを警告し、構築されたアイデンティティに沿った方法でコメントに対応するよう導くことができる。また、1 つの VTuber に複数のなかのひとが出演している場合には、そうしたツールはなかのひとに合わせて出力を調整する必要があります。将来的には自然言語処理によってこれらの機能が自動化されるかもしれませんが、現在のストリーマーは、モデレーターの役割と同様に、リスクのあるコメントにフラグを立てたり、アイデンティティを維持するための提案を提供したりする「アシスタント」に頼ることができます[63]。

<!--
Our results highlight that VTubers construct their identities dynamically, often evolving them over time based on characteristics of Nakanohitos or viewers community participation. Further, VTubers could have different Nakanohitos or even multiple Nakanohitos who collaborate to perform. Due to this potential complexity, maintaining a consistent identity will remain challenging for VTubers but is crucial to maintaining a stable fan base. There is thus a design opportunity to provide collaborative identity managing tools for VTubers, which could provide Nakanohitos with guidelines and actionable strategies to maintain a consistent identity during live streams. For example, when viewers send comments that risk revealing the identity of a Nakanohito during a live stream, the tool could alert the Nakanohito about the risk and guide them to respond to the comments in manner consistent with their constructed identity. Such tools may also need to tailor their output to different Nakanohitos if there are multiple Nakanohitos performing for one VTuber. While future natural language processing may make these features automatic, current streamers could rely on an “assistant” to help them flag risky comments and provide suggestions for maintaining identity, similar to the role of moderators [63].
--->

#### 5.4.2 透明性と公平性のためのデザイン

中の人が入れ替わったり、複数の中の人がいたりすることは、VTuber のライブ配信の中でも独特の動きです。コンテンツの質が安定していて、中の人にとって透明で公平なプロセスであれば問題ないが、視聴者にとっては、予告なしに中の人が入れ替わったかどうかを判断するのは難しく、事後的に知った場合には、その企業を不買運動することもあるという。そこで、企業は、残業しない、理由なく交代させないなど、なかのひとが企業から公平に扱われているかどうかの情報を開示し、なかのひとの見えない労働を可視化する必要があります。また、中の人の健康状態や感情をある程度視聴者に知らせることもできるが、中の人のプライバシー保護には注意が必要である。

<!--
Replacing Nakanohito or having multiple Nakanohitos is a unique dynamic within VTuber live streaming. While interviewees were fine with this when the quality of content remained consistent and the process was transparent and fair to Nakanohito, it was hard for viewers to determine if a Nakanohito was replaced without notice, and if they found out after the fact, they have been known to boycott the corporation. It is thus necessary for corporations to make the invisible labor of Nakanohitos more visible by disclosing information such as whether the Nakanohitos are treated fairly by the corporation, for example, not working overtime or being replaced without a convincing reason. The health or emotional states of Nakanohitos can also be made known to the viewers to some extent although care must be taken to protect Nakanohito’s privacy.
-->

#### 5.4.3 バーチャルとリアル両方のためのデザイン

今回の調査では、VTuber のライブ・ストリーミングによってリアルとバーチャルの境界線が曖昧になったときに起こりうる機会についても明らかになりました。VTuber のライブ・ストリームは、現実のライブ・ストリーマーに刺激を与えるクリエイティブなパフォーマンス形態を示唆しています。インタビュー対象者は、一つの仮想世界に複数の VTuber が同居している様子を熱心に見ている様子が伺えた。しかし、現在のリアル・パーソン・ライブ配信のほとんどは、複数の配信者の映像が画面上に並置されているだけです。これは、マーカーレス・モーションキャプチャーなどの技術を用いて、地理的な障壁を取り除き、VTuber の共同ストリーミング体験を実在のストリーマーに提供するデザインチャンスを示唆しています。将来の複合現実技術は、VTuber のライブストリームの視聴者の体験を高める可能性があります。拡張現実（Augmented Reality）は、VTuber の人間サイズの 3D アバターを現実世界に出現させることができる。バーチャル・リアリティでは、VTuber が出演する仮想世界に視聴者を没入させることができます。リアルとバーチャルを融合させたライブストリーミングは、文化遺産や観光、知識の共有など、特定のアプリケーション分野と組み合わせることで、より多くの視聴者を惹きつけることができる可能性を秘めています。

<!--
Our findings also revealed the opportunities that can occur when blurring the line between the real and the virtual through VTubers’ live streaming. VTubers’ live streams suggest creative performance forms that could inspire real-person live streamers. Interviewees showed great enthusiasm towards watching multiple VTubers co-located in one virtual world. Most current real-person co-streaming, however, only displays the juxtaposition of multiple streamers’ videos on the screen. This suggests a design opportunity to break geographic barriers and bring the co-streaming experience of VTubers to realperson streamers, using technologies such as markerless motion capture. Future Mixed Reality technologies could enhance viewers’ experiences of VTuber live streams. Augmented reality could bring human-sized 3D avatars of VTubers to the real world. Virtual reality could immerse the viewers in the the virtual world where the VTuber performs. Live streaming that blurs the real and the virtual has the potential to be further combined with specific application areas, such as cultural heritage, tourism, and knowledge sharing, to better engage broader viewership.
-->

### 5.5 本研究の限界と将来課題

本研究を解釈する際に考慮すべきいくつかの限界があることを指摘します。
本研究では、若年層と男性に偏った熱心な視聴者のサンプルのインタビューデータを使用しました。
今後の研究では、より多くの多様なサンプルを用いて、VTuber コミュニティに対する理解を深めていく必要があります。
本研究の性質上、調査結果の因果関係の結論や一般化はできませんでした。
VTuber の中の人、モデレーター、その他のサポート役、企業の経営者など、様々なステークホルダーにインタビューすることで、この現象についてより多くの知見を得ることができると考える。
また、参加者に特定の VTuber に参加してもらい、VTuber に対する反応を対照実験で分析するという別の方法も、今後の研究で検討していく必要があるだろう。

<!--
We note several limitations of our study that should be considered when interpreting this work. Our study drew from the interview data of a sample of dedicated viewers that skewed young and male. Future research is needed to expand and deepen our understanding of the VTuber community with a larger and more diverse sample, even in different countries. Due to the nature of this study, causal conclusions or generalizability of the findings could not be made. Interviewing different stakeholders, such as Nakanohitos of VTubers, their moderators, other supporting roles, and managers of corporations could probably reveal more insights about this phenomenon. Alternative methodology where participants are invited to engage with a particular set of VTubers with their reactions to VTubers analyzed in a controlled experiment could also be explored in future research.
-->

## 6 結果

本論文では、オタクコミュニティが VTuber とどのように関わり、どのように認識しているのかを検証した。
その結果、VTuber のライブ配信の内容や視聴者の動機は、実在のストリーマーと同様であることがわかった。
しかし、視聴者は、VTuber の行動に異なる期待を持ち、VTuber に対して強い距離感を感じることで、VTuber を現実の配信者とは異なるものとして認識していた。
視聴者は、VTuber の完璧なイメージを維持するために、なかのひとをアバターから切り離すことを意図的に行っていましたが、労働の公正さや透明性に関しては、なかのひとを気にかけていました。今回の結果は、視聴者と VTuber がライブ・ストリーミングの領域で遭遇する固有の課題（協調的なアイデンティティ管理や現実世界との限られた交流など）を明らかにすることで、将来のライブ・ストリーミング・プラットフォームの設計にインスピレーションを与え、VTuber や AI を搭載したバーチャル・ストリーマーが視聴者に与える影響や効果をコミュニティがよりよく理解することを可能にします。

<!--
This work examined how the Otaku community engages with and perceive VTubers. The results revealed that the content and viewer motivations of VTuber live streaming were similar to real-person streamers. Viewers, however, perceived VTubers differently from real-person streamers by holding different expectations for VTuber’s behaviors and feeling a stronger sense of distance towards them. Viewers also intentionally maintained the disembodiment of Nakanohitos from avatars to preserve VTubers’ perfect images, though they still cared about the Nakanohito with respect to labor fairness and transparency. By identifying unique challenges that viewers and VTubers encounter within the realm of live streaming, e.g., collaborative identity management and limited interactions with the real world, these results could inspire the design of future live streaming platforms and enable the community to better understand the influence and effects of VTubers or even AI-powered virtual streamers, on audiences.
-->

## References

[See original PDF](https://www.cs.cityu.edu.hk/~zhiconlu/assets/pdf/CHI2021Vtuber.pdf)

- [1] Jeremy N Bailenson, Andrew C Beall, Jack Loomis, Jim Blascovich, and Matthew Turk. 2004. Transformed social interaction: Decoupling representation from behavior and form in collaborative virtual environments. Presence: Teleoperators & Virtual Environments 13, 4 (2004), 428–441.
- [2] 株式会社ユーザーローカル . 2020. バーチャル YouTuber、本日 1 万人を 突破（ユーザーローカル調べ）｜株式会社ユーザーローカル . https: //www.userlocal.jp/press/20200115vi/. [Online; accessed 16-January-2020].
- [3] 株式会社ユーザーローカル. 2020. ファン数ランキング バーチャルYouTuberランキング https://virtual-youtuber.userlocal.jp/document/ ranking. [Online; accessed 16-January-2020].
- [4] Bilibili. 2020. Bilibili. https://www.bilibili.com/.
- [5] Daniel Black. 2012. The virtual idol: Producing and consuming digital femininity. In Idols and celebrity in Japanese media culture. Palgrave Macmillan, London, UK, 209–228.
- [6] Raymond Blanton and Darlene Carbajal. 2019. Not a Girl, Not Yet a Woman: A Critical Case Study on Social Media, Deception, and Lil Miquela. In Handbook of Research on Deception, Fake News, and Misinformation Online. IGI Global, Hershey, PA, USA, 87–103.
- [7] Di Laura Chen, Dustin Freeman, and Ravin Balakrishnan. 2019. Integrating Multimedia Tools to Enrich Interactions in Live Streaming for Language Learning. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. ACM, ACM, New York, NY, USA, 438.
- [8] Mark Childs. 2011. Identity: A Primer. Springer London, London, 13–31. https: //doi.org/10.1007/978-0-85729-361-9_2
- [9] 依光流. 2018. 冯提莫不是 B 站直播的杀招，Vtuber 才是. Retrieved May 31, 2020 from https://www.ifanr.com/1325444
- [10] Juliet Corbin and Anselm Strauss. 1998. Basics of qualitative research: Techniques and procedures for developing grounded theory. Sage Publications, Inc, Thousand Oaks, CA, USA.
- [11] Donna Z Davis. 2010. Exploring the media effects of three-dimensional online immersive worlds and how they impact both virtual and real social capital. University of Florida.
- [12] Nicolas Ducheneaut, Nicholas Yee, Eric Nickell, and Robert J Moore. 2006. Alone together?: exploring the social dynamics of massively multiplayer online games. In Proceedings of the SIGCHI conference on Human Factors in computing systems. ACM, ACM, New York, NY, USA, 407–416.
- [13] Dwango. 2020. Niconico. https://www.nicovideo.jp/.
- [14] Travis Faas, Lynn Dombrowski, Alyson Young, and Andrew D. Miller. 2018. Watch Me Code: Programming Mentorship Communities on Twitch.Tv. Proc. ACM Hum.-Comput. Interact. 2, CSCW, Article Article 50 (Nov. 2018), 18 pages. https://doi.org/10.1145/3274319
- [15] C Ailie Fraser, Joy O Kim, Alison Thornsberry, Scott Klemmer, and Mira Dontcheva. 2019. Sharing the Studio: How Creative Livestreaming can Inspire, Educate, and Engage. In Proceedings of the 2019 on Creativity and Cognition. ACM, ACM, New York, NY, USA, 144–155.
- [16] Guo Freeman, Samaneh Zamanifard, Divine Maloney, and Alexandra Adkins. 2020. My Body, My Avatar: How People Perceive Their Avatars in Social Virtual Reality. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (CHI EA ’20). Association for Computing Machinery, New York, NY, USA, 1–8. https://doi.org/10.1145/3334480.3382923
- [17] Noam Gal, Limor Shifman, and Zohar Kampf. 2016. “It Gets Better”: Internet memes and the construction of collective identity. New Media & Society 18, 8 (2016), 1698–1714. https://doi.org/10.1177/1461444814568784 arXiv:https://doi.org/10.1177/1461444814568784
- [18] Patrick W Galbraith. 2009. Moe: Exploring virtual potential in post-millennial Japan. electronic journal of contemporary japanese studies 9, 3 (2009).
- [19] Patrick W Galbraith. 2012. Idols: The image of desire in Japanese consumer capitalism. In Idols and celebrity in Japanese media culture. Springer, New York, NY, USA, 185–208.
- [20] Patrick W Galbraith and Jason G Karlin. 2012. Introduction: The mirror of idols and celebrity. In Idols and celebrity in Japanese media culture. Springer, New York, NY, USA, 1–32.
- [21] Seth Glickman, Nathan McKenzie, Joseph Seering, Rachel Moeller, and Jessica Hammer. 2018. Design Challenges for Livestreamed Audience Participation Games. In Proceedings of the 2018 Annual Symposium on ComputerHuman Interaction in Play (CHI PLAY ’18). ACM, New York, NY, USA, 187–199. https://doi.org/10.1145/3242671.3242708
- [22] Mar Gonzalez-Franco, Anthony Steed, Steve Hoogendyk, and Eyal Ofek. 2020. Using Facial Animation to Increase the Enfacement Illusion and Avatar SelfIdentification. IEEE Transactions on Visualization and Computer Graphics 26, 5 (2020), 2023–2029.
- [23] Oliver L. Haimson and John C. Tang. 2017. What Makes Live Events Engaging on Facebook Live, Periscope, and Snapchat. In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI ’17). ACM, New York, NY, USA, 48–60. https://doi.org/10.1145/3025453.3025642
- [24] William A. Hamilton, Oliver Garretson, and Andruid Kerne. 2014. Streaming on Twitch: Fostering Participatory Communities of Play Within Live Mixed Media. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’14). ACM, New York, NY, USA, 1315–1324. https://doi.org/10.1145/2556288. 2557048
- [25] William A. Hamilton, Nic Lupfer, Nicolas Botello, Tyler Tesch, Alex Stacy, Jeremy Merrill, Blake Williford, Frank R. Bentley, and Andruid Kerne. 2018. Collaborative Live Media Curation: Shared Context for Participation in Online Learning. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI ’18). ACM, New York, NY, USA, Article 555, 14 pages. https://doi.org/10. 1145/3173574.3174129
- [26] Hololive. 2020. Hololive. https://www.hololive.tv/.
- [27] Mizuko Ito, Daisuke Okabe, and Izumi Tsuji. 2012. Fandom unbound: Otaku culture in a connected world. Yale University Press, NEw Haven, CT, USA.
- [28] Maurice Jakesch, Megan French, Xiao Ma, Jeffrey T Hancock, and Mor Naaman. 2019. AI-Mediated Communication: How the Perception that Profile Text was Written by AI Affects Trustworthiness. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. ACM, ACM, New York, NY, USA, 239.
- [29] Phylis Johnson. 2010. Second Life, Media, and the Other Society. Peter Lang.
- [30] Lucas Kempe-Cook, Stephen Tsung-Han Sher, and Norman Makoto Su. 2019. Behind the Voices: The Practice and Challenges of Esports Casters. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). ACM, New York, NY, USA, Article Paper 565, 12 pages. https://doi.org/10.1145/ 3290605.3300795
- [31] Kangsoo Kim, Arjun Nagendran, Jeremy N. Bailenson, Andrew Raij, Gerd Bruder, Myungho Lee, Ryan Schubert, Xin Yan, and Gregory F. Welch. 2017. A Large-Scale Study of Surrogate Physicality and Gesturing on Human–Surrogate Interactions in a Public Space. Frontiers in Robotics and AI 4 (2017), 32. https://doi.org/10. 3389/frobt.2017.00032
- [32] Yubo Kou, Xinning Gui, Shaozeng Zhang, and Bonnie Nardi. 2017. Managing disruptive behavior through non-hierarchical governance: Crowdsourcing in League of Legends and Weibo. Proceedings of the ACM on Human-Computer Interaction 1, CSCW (2017), 62.
- [33] Lily Kuo. 2018. World’s first AI news anchor unveiled in China. Retrieved June 7, 2019 from https://www.theguardian.com/world/2018/nov/09/worlds-first-ainews-anchor-unveiled-in-china
- [34] Ka Yan Lam. 2016. The Hatsune Miku Phenomenon: More Than a Virtual J-Pop Diva. The Journal of Popular Culture 49, 5 (2016), 1107–1124.
- [35] Linh K Le. 2014. Examining the rise of Hatsune Miku: the first international virtual idol. The UCI Undergraduate Research Journal 13, 1 (2014), 1–12.
- [36] Alex Leavitt, Tara Knight, and Alex Yoshiba. 2016. Producing Hatsune Miku: Concerts, Commercialization, and the Politics of Peer Production. In Media Convergence in Japan. Kinema Club, New Haven, CT, USA, 200–229.
- [37] Pascal Lessel, Alexander Vielhauer, and Antonio Krüger. 2017. Expanding Video Game Live-Streams with Enhanced Communication Channels: A Case Study. In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI ’17). ACM, New York, NY, USA, 1571–1576. https://doi.org/10.1145/3025453. 3025708
- [38] Jie Li, Xinning Gui, Yubo Kou, and Yukun Li. 2019. Live Streaming as CoPerformance: Dynamics between Center and Periphery in Theatrical Engagement. Proceedings of the ACM on Human-Computer Interaction 3, CSCW, Article 64 (Nov. 2019), 22 pages. https://doi.org/10.1145/3359166
- [39] Christine Liao. 2011. Virtual fashion play as embodied identity re/assembling: Second Life fashion bloggers and their avatar bodies. In Reinventing ourselves: contemporary concepts of identity in virtual Worlds. Springer, London, UK, 101– 127.
- [40] Danielle Lottridge, Frank Bentley, Matt Wheeler, Jason Lee, Janet Cheung, Katherine Ong, and Cristy Rowley. 2017. Third-Wave Livestreaming: Teens’ Long Form Selfie. In Proceedings of the 19th International Conference on HumanComputer Interaction with Mobile Devices and Services (MobileHCI ’17). Association for Computing Machinery, New York, NY, USA, Article 20, 12 pages. https://doi.org/10.1145/3098279.3098540
- [41] Zhicong Lu, Michelle Annett, Mingming Fan, and Daniel Wigdor. 2019. “I Feel It is My Responsibility to Stream”: Streaming and Engaging with Intangible Cultural Heritage through Livestreaming. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). ACM, New York, NY, USA, Article Paper 229, 14 pages. https://doi.org/10.1145/3290605.3300459
- [42] Zhicong Lu, Michelle Annett, and Daniel Wigdor. 2019. Vicariously Experiencing it all without Going Outside: A Study of Outdoor Livestreaming in China. Proceedings of the ACM on Human-Computer Interaction 3, CSCW (2019), 1–28.
- [43] Zhicong Lu, Seongkook Heo, and Daniel Wigdor. 2018. StreamWiki: Enabling Viewers of Knowledge Sharing Live Streams to Collaboratively Generate Archival Documentation for Effective In-Stream and Post-Hoc Learning. Proceedings of the ACM on Human-Computer Interaction 2, CSCW (2018), Article 112. https: //doi.org/10.1145/3274381
- [44] Zhicong Lu, Haijun Xia, Seongkook Heo, and Daniel Wigdor. 2018. You Watch, You Give, and You Engage: A Study of Live Streaming Practices in China. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI ’18). ACM, New York, NY, USA, Article Paper 466, 13 pages. https://doi. org/10.1145/3173574.3174040
- [45] Tetsuya Nakajo. 2020. Live2D. https://www.live2d.com/en/.
- [46] Bonnie Nardi. 2010. My life as a night elf priest: An anthropological account of World of Warcraft. University of Michigan Press, Ann Arbor, MI, USA.
- [47] Carman Neustaedter and Elena Fedorovskaya. 2009. Capturing and sharing memories in a virtual world. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, ACM, New York, NY, USA, 1161–1170.
- [48] Carman Neustaedter and Elena Fedorovskaya. 2009. Presenting Identity in a Virtual World through Avatar Appearances. In Proceedings of Graphics Interface 2009 (GI ’09). Canadian Information Processing Society, CAN, 183–190.
- [49] Nijisanji. 2020. Nijisanji. https://nijisanji.ichikara.co.jp/.
- [50] Asaf Nissenbaum and Limor Shifman. 2017. Internet memes as contested cultural capital: The case of 4chan’s /b/ board. New Media & Society 19, 4 (2017), 483–501. https://doi.org/10.1177/1461444815609313 arXiv:https://doi.org/10.1177/1461444815609313
- [51] National Geographic of Azeroth Forum. 2020. National Geographic of Azeroth Forum: VTuber Discussion Board. https://bbs.nga.cn/thread.php?fid=-60204499.
- [52] Soo Youn Oh, Jeremy Bailenson, Nicole Krämer, and Benjamin Li. 2016. Let the Avatar Brighten Your Smile: Effects of Enhancing Facial Expressions in Virtual Environments. PLOS ONE 11, 9 (09 2016), 1–18. https://doi.org/10.1371/journal. pone.0161794
- [53] Anthony J. Pellicone and June Ahn. 2017. The Game of Performing Play: Understanding Streaming As Cultural Production. In Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (CHI ’17). ACM, New York, NY, USA, 4863–4874. https://doi.org/10.1145/3025453.3025854
- [54] Linden Research. 2014. Live Performances Second Live Wiki. Retrieved May 23, 2020 from http://wiki.secondlife.com/wiki/Live_Performances
- [55] Jeff T. Sheng and Sanjay R. Kairam. 2020. From Virtual Strangers to IRL Friends: Relationship Development in Livestreaming Communities on Twitch. Proc. ACM Hum.-Comput. Interact. 4, CSCW2, Article 94 (Oct. 2020), 34 pages. https: //doi.org/10.1145/3415165
- [56] Stephen Tsung-Han Sher and Norman Makoto Su. 2019. Speedrunning for Charity: How Donations Gather Around a Live Streamed Couch. Proc. ACM Hum.-Comput. Interact. 3, CSCW, Article Article 48 (Nov. 2019), 26 pages. https: //doi.org/10.1145/3359150
- [57] SimilarWeb. 2020. Bbs.nga.cn Analytics Market Share Stats & Traffic Ranking. https://www.similarweb.com/website/bbs.nga.cn. [Online; accessed 16-January2020].
- [58] John Tang, Gina Venolia, Kori Inkpen, Charles Parker, Robert Gruen, and Alicia Pelton. 2017. Crowdcasting: Remotely Participating in Live Events Through Multiple Live Streams. Proc. ACM Hum.-Comput. Interact. 1, CSCW, Article 98 (Dec. 2017), 18 pages. https://doi.org/10.1145/3134733
- [59] John C. Tang, Gina Venolia, and Kori M. Inkpen. 2016. Meerkat and Periscope: I Stream, You Stream, Apps Stream for Live Streams. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (CHI ’16). ACM, New York, NY, USA, 4770–4780. https://doi.org/10.1145/2858036.2858374
- [60] TL Taylor. 2018. Watch me play: Twitch and the rise of game live streaming. Vol. 24. Princeton University Press, Princeton, NJ, USA.
- [61] Joseph B Walther. 1996. Computer-mediated communication: Impersonal, interpersonal, and hyperpersonal interaction. Communication research 23, 1 (1996), 3–43.
- [62] Joseph B Walther. 2011. Theories of computer-mediated communication and interpersonal relations. The handbook of interpersonal communication 4 (2011), 443–479.
- [63] Donghee Yvette Wohn. 2019. Volunteer Moderators in Twitch Micro Communities: How They Get Involved, the Roles They Play, and the Emotional Labor They Experience. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems. ACM, ACM, New York, NY, USA, 160.
- [64] Donghee Yvette Wohn, Guo Freeman, and Caitlin McLaughlin. 2018. Explaining viewers’ emotional, instrumental, and financial support provision for live streamers. In Proceedings of the 2018 CHI conference on human factors in computing systems (CHI ’18). ACM, ACM, New York, NY, USA, 474.
- [65] Jamie Woodcock and Mark R Johnson. 2019. The Affective Labor and Performance of Live Streaming on Twitch.tv. Television & New Media 20 (2019), 1527476419851077. Issue 8.
- [66] Nick Yee, Jeremy N Bailenson, and Kathryn Rickertsen. 2007. A Meta-Analysis of the Impact of the Inclusion and Realism of Human-like Faces on User Experiences in Interfaces. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI ’07). Association for Computing Machinery, New York, NY, USA, 1–10. https://doi.org/10.1145/1240624.1240626
- [67] Yiyi Yin. 2018. Vocaloid in China: Cosmopolitan music, cultural expression, and multilayer identity. Global Media and China 3, 1 (2018), 51–66. https://doi.org/10.1177/2059436418778600
- [68] Japan National Tourism Organization New York. 2018. JNTO to Launch ’Come to Japan’ Campaign With Kizuna AI, the World’s First Virtual YouTuber. Retrieved May 31, 2020 from https://www.prnewswire.com/news-releases/jnto-to-launchcome-to-japan-campaign-with-kizuna-ai-the-worlds-first-virtual-youtuber300608037.html

## Glossary

### 訳注
1. 「企業が運営する」と書かれているが、神楽めあ氏が過去に所属していた「ぱりぷろ（Project Paryi）」は個人運営のプロジェクトであるため誤解と考えられる。なお、ぱりぷろは[2019年4月に解散を発表](https://www.moguravr.com/paryiproject-dissolution/)しており、所属者は現在個人勢として活動している。

### 後で置き換える用の用語集

- ライブストリーミング → ライブ配信
- ストリーマー → 配信者
- 中の人 → ナカノヒト（Nakanohito）

### 日英対訳辞書

English        | 和訳          　　　　　 | コメント
---------------|------------------------|---------------
 Nakanohito | VTuberを演じている声優・アクター | 「中の人」という日本語そのまま
 disembodiment | （VTuberと中の人の）分離 |
 (VTuber) agencies | VTuber事務所 |
 Live streaming | ライブ配信 |
 Co-streaming | コラボ配信 |
 Persecution | 迫害/虐待？　配信のチャット欄でスタンプなどのミームを集団で連投すること | ※適切な翻訳があれば教えてください
 persona | ペルソナ。VTuberが設定として持っている人物像 |
 replacement of a Nakanohito | 中の人の交代 |

### Tools and acknowledgements

I note my appreciation for these great tools.

- [Deepl](https://www.deepl.com/translator)
- [https://dream-exp.net/shaper/](https://dream-exp.net/shaper/)
- [VTuber-IME 辞書](https://twitter.com/VRStudioLab/status/1136889624360472577)

翻訳協力

- Kenichi Ito ([@kn1cht](https://github.com/kn1cht))
