---
layout: post
title: "RenderTexture"
date: '2020-12-20 23:52:00'
author: aki
categories: Unity
---

UnityのRenderTextureとムービーテクスチャについて調べたくなったので基本をおさらいしてみた。

- 公式 Unity ユーザマニュアル (2019.4 LTS) [レンダーテクスチャ](https://docs.unity3d.com/ja/current/Manual/class-RenderTexture.html)


> Render Textures are special types of Textures that are created and updated at run time. To use them, you first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. The Water prefabs in Unity Standard Assets are an example of real-world use of Render Textures for making real-time reflections and refractions.

レンダーテクスチャは、ランタイムに作成され更新される特別なタイプのテクスチャです。これを使用するには、まず新しいレンダー テクスチャを作成し、それにレンダリングするカメラを指定します。その後、通常のテクスチャと同じようにマテリアル内でレンダーテクスチャを使用できます。Unity Standard AssetsのWaterプレハブは、リアルタイムの反射や屈折を作成するためのレンダーテクスチャの実際の使用例です。

以下の手順で、ゲーム内で、ライブアリーナカメラを非常に素早く作成できます。

1. Assets >Create >Render Texture を使って、新しい Render Texture アセットを作成します。
1. GameObject > Camera を使って、新しいカメラを作成します。
1. 新しいカメラの Target Texture にレンダーテクスチャを割り当てます。
1. GameObject > 3D Object > Cube を使用して、新しい 3D キューブを作成します。
1. レンダリングテクスチャをキューブにドラッグして、レンダリングテクスチャを使用するマテリアルを作成します。
1. プレイモードに入り、キューブのテクスチャが新しいカメラの出力に基づいてリアルタイムで更新されることを確認します。

# Twitterは以下の感じでなら使える

  <blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr">最近のMike先生 <a href="https://t.co/zI9q0D2BXf">https://t.co/zI9q0D2BXf</a></p>&mdash; Akihiko SHIRAI, Ph.D #EnjoyStayHome🦠 (@o_ob) <a href="https://twitter.com/o_ob/status/1286321513243631616?ref_src=twsrc%5Etfw">July 23, 2020</a></blockquote>

  <blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr">7年前、大学の教員になることを告げたら「マンガで食えなくなったヤツは、すぐに学校で素人相手に偉そうに教えたがるよね」と、知人から言われた。面と向かってだよ。その当時から連載を持っていたし、大学で教えるようになった後にヒット作も出しているんだけど、こういう認識の人っているんだよな…</p>&mdash; はぁとふる倍国土 (@keiichisennsei) <a href="https://twitter.com/keiichisennsei/status/1286106295435632641?ref_src=twsrc%5Etfw">July 23, 2020</a></blockquote>
