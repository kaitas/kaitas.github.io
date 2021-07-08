---
layout: post
title: "Teachable Machineが面白いので一回やってみて"
date: "2021-07-08 23:52:00"
author: aki
description: 機械学習をノーコードで学べるTeachableMachineを紹介
categories: tech
preview: https://teachablemachine.withgoogle.com/assets/img/Hero_image_16x9.jpg
---

[https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/)

TeachableMachine 画像撮影から学習ぶん回すまでが早くて速くてわかりやすくて素晴らしい・・・。
ノード接続だけでできる、YahooAPI の時のような衝撃。
（ファン音がすごいのでミュート推奨）

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1413003115360448513">date</a></blockquote>

声もある、モーションもある・・・
表情はデフォルトのテンプレでは無理ね

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1413003142841593860">date</a></blockquote>

Web で連続撮影できるサービスは結構あったと思うけど（買収された？）、Drive に ZIP で保存できるし、他のフレームワークや開発環境でも利用できる。
そして「舞台裏」とか「？」とかの用語解説が初学者にとっても優しい・・・

<blockquote class="twitter-tweet" data-width="550" data-dnt="true"><p lang="ja" dir="ltr"></p><a href="https://twitter.com/o_ob/status/1413003147627302916
">date</a></blockquote>

[tensorflow で利用するためのコード](https://github.com/googlecreativelab/teachablemachine-community/blob/master/snippets/markdown/pose/tensorflowjs/javascript.md)がすぐに手に入る

<div>Teachable Machine Pose Model</div>
<button type="button" onclick="init()">Start</button>
<div><canvas id="canvas"></canvas></div>
<div id="label-container"></div>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
<script type="text/javascript">
    // More API functions here:
    // https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/pose

    // the link to your model provided by Teachable Machine export panel
    const URL = "{{URL}}";
    let model, webcam, ctx, labelContainer, maxPredictions;

    async function init() {
        const modelURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";

        // load the model and metadata
        // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
        // Note: the pose library adds a tmPose object to your window (window.tmPose)
        model = await tmPose.load(modelURL, metadataURL);
        maxPredictions = model.getTotalClasses();

        // Convenience function to setup a webcam
        const size = 200;
        const flip = true; // whether to flip the webcam
        webcam = new tmPose.Webcam(size, size, flip); // width, height, flip
        await webcam.setup(); // request access to the webcam
        await webcam.play();
        window.requestAnimationFrame(loop);

        // append/get elements to the DOM
        const canvas = document.getElementById("canvas");
        canvas.width = size; canvas.height = size;
        ctx = canvas.getContext("2d");
        labelContainer = document.getElementById("label-container");
        for (let i = 0; i < maxPredictions; i++) { // and class labels
            labelContainer.appendChild(document.createElement("div"));
        }
    }

    async function loop(timestamp) {
        webcam.update(); // update the webcam frame
        await predict();
        window.requestAnimationFrame(loop);
    }

    async function predict() {
        // Prediction #1: run input through posenet
        // estimatePose can take in an image, video or canvas html element
        const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
        // Prediction 2: run input through teachable machine classification model
        const prediction = await model.predict(posenetOutput);

        for (let i = 0; i < maxPredictions; i++) {
            const classPrediction =
                prediction[i].className + ": " + prediction[i].probability.toFixed(2);
            labelContainer.childNodes[i].innerHTML = classPrediction;
        }

        // finally draw the poses
        drawPose(pose);
    }

    function drawPose(pose) {
        if (webcam.canvas) {
            ctx.drawImage(webcam.canvas, 0, 0);
            // draw the keypoints and skeleton
            if (pose) {
                const minPartConfidence = 0.5;
                tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
                tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
            }
        }
    }

</script>
