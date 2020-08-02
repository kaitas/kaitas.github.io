<HTML>
 <HEAD>
  <LINK REL="stylesheet" HREF="style.css" TYPE="text/css">
  <TITLE>WiiRemoteで学ぶ プログラミング数学・物理</TITLE>
 </HEAD>
 <BODY>

<?php
// 出力例 somefile.txt was last modified: December 29 2002 22:16:23.

$filename = 'index.php';
if (file_exists($filename)) {
    echo "$filename was last modified: " . date ("F d Y H:i:s.", filemtime($filename));
}
?>
 



<H1 class="toptitle">
WiiRemoteで学ぶ プログラミング数学・物理
</H1>
<OL>
<li>hoge</li>
<li>hoge</li>
<li>hoge</li>
<li>hoge</li>
</OL>
<pre>

1. WiiRemoteのススメ
	1.1 はじめに
		本書の概要
			任天堂コンセプト
			任天堂スペック
		フィジカルコンピューティングの可能性

2. WiiRemoteの基礎知識
	2.1 PC上で利用するWiiRemote概論
		WiiRemoteをPCで利用する
		WiiRemoteをPCで使うのは違法？
	2.2 Bluetooth接続
		WiiRemoteとPCをBluetoothで接続する
		Bluetoothアダプタを選ぶ
		コラム：Bluetoothスタックに対する不満
	2.3 実験してみよう
		WiinRemoteを使ってみる
		GlovePIEを使ってみる
		その他のツール紹介
			WiiAcc
			WiiFlash
	2.4 センサーバーを自作する
		センサーバーのしくみ
		目には見えない赤外線
		電子部品をそろえる・工作する
	2.5 プログラミング環境のセットアップ
		Visual C++ 2008 Express Editionのセットアップ
		コラム：VC混在環境を解決するVersionSelector
			VC2008のインストール
		WindowsDDKのセットアップ
			ISOファイルのマウント
	2.6 API紹介
		tiny hiddll
			Wii Remote Test1の実行
			wii test1.cppのリビルド
			wii test1.cppの流れ
		Wiim
		WiiYourself!

3. WiiRemoteで学ぶ、物理・数学・プログラミング
	3.1 コマンドラインサンプル
		WiiRemoteとの通信
		姿勢検出
		赤外線検出
		バイブレータとLED
		ポーリング受信と動作周波数の測定
		Socket通信
		WiiYourself!を用いた開発
		4点検出
	3.2 WiiRemoteで学ぶ数学物理
		重力加速度を見る
		振りぬく力・パンチ力測定
		モーション解析
	3.3 プロジェクトサンプル
		車輪の動き検出
		3DCGとの組み合わせ
		WiiLander
		フリースロー
		だるま落とし（物理エンジンとの連携）

4. Flash編
	4.1 WiiFlashを使ってみよう
		環境設定
			CS3のセットアップ
		WiiFlash のダウンロードとセットアップ
		WiiFlashの基本機能
		サンプルのテストでみる基本的な使い方
	4.2 プロジェクトサンプル
		なりきりライトセーバー
		おえかき
		DropShadow
		ChunChun

Appendix
	WiiFit
	Linux, MaxOSXで使う
	赤外線反射式インタフェース




</pre>
 </BODY>
</HTML>
