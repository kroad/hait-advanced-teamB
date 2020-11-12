<template>
  <div>
    <v-btn @click="record" fab x-large dark color="purple">
      <v-icon>mdi-microphone</v-icon>
    </v-btn>
    <a id="download" hidden>ダウンロード</a>
  </div>
</template>

<script>
export default {
  data() {
    return {
      source: "",
    };
  },
  methods: {
    record() {
      // for html
      const downloadButton = document.getElementById("download");

      // for audio
      let audio_sample_rate = null;
      let scriptProcessor = null;
      let audioContext = null;

      // audio data
      let audioData = [];
      let bufferSize = 1024;
      let vm = this;

      // export関数にaudioData(リスト型)を渡して出来たwavファイルをダウンロードボタンのhrefに追加し、ダウンロード属性をtest.wavにし、勝手にクリックして自動ダウンロード
      // オーディオコンテキストを閉じて使っていたシステムのオーディオリソースを全て解放する
      let saveAudio = function () {
        let wavBlob = exportWAV(audioData);
        downloadButton.href = wavBlob;
        vm.$store.dispatch("storeWavBlob", wavBlob);
        downloadButton.download = "test.wav";
        downloadButton.click();
        audioContext.close();
      };

      // export WAV from audio float data
      // ここが一番難しいけど理解する必要はとりあえずないかな
      let exportWAV = function (audioData) {
        let encodeWAV = function (samples, sampleRate) {
          let buffer = new ArrayBuffer(44 + samples.length * 2);
          let view = new DataView(buffer);

          let writeString = function (view, offset, string) {
            for (let i = 0; i < string.length; i++) {
              view.setUint8(offset + i, string.charCodeAt(i));
            }
          };

          let floatTo16BitPCM = function (output, offset, input) {
            for (let i = 0; i < input.length; i++, offset += 2) {
              let s = Math.max(-1, Math.min(1, input[i]));
              output.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7fff, true);
            }
          };

          writeString(view, 0, "RIFF"); // RIFFヘッダ
          view.setUint32(4, 32 + samples.length * 2, true); // これ以降のファイルサイズ
          writeString(view, 8, "WAVE"); // WAVEヘッダ
          writeString(view, 12, "fmt "); // fmtチャンク
          view.setUint32(16, 16, true); // fmtチャンクのバイト数
          view.setUint16(20, 1, true); // フォーマットID
          view.setUint16(22, 1, true); // チャンネル数
          view.setUint32(24, sampleRate, true); // サンプリングレート
          view.setUint32(28, sampleRate * 2, true); // データ速度
          view.setUint16(32, 2, true); // ブロックサイズ
          view.setUint16(34, 16, true); // サンプルあたりのビット数
          writeString(view, 36, "data"); // dataチャンク
          view.setUint32(40, samples.length * 2, true); // 波形データのバイト数
          floatTo16BitPCM(view, 44, samples); // 波形データ

          return view;
        };

        let mergeBuffers = function (audioData) {
          let sampleLength = 0;
          for (let i = 0; i < audioData.length; i++) {
            sampleLength += audioData[i].length;
          }
          let samples = new Float32Array(sampleLength);
          let sampleIdx = 0;
          for (let i = 0; i < audioData.length; i++) {
            for (let j = 0; j < audioData[i].length; j++) {
              samples[sampleIdx] = audioData[i][j];
              sampleIdx++;
            }
          }
          return samples;
        };

        // ここが本体
        let dataview = encodeWAV(mergeBuffers(audioData), audio_sample_rate);
        let audioBlob = new Blob([dataview], { type: "audio/wav" });
        let myURL = window.URL || window.webkitURL;
        let url = myURL.createObjectURL(audioBlob);
        return url;
      };

      // save audio data
      // handleSuccessの中のScriptProcessorで呼ばれる
      // e.inputBuffer.getChannelData(0)から取ってきたデータをbufferDataに入れてreturnする
      let onAudioProcess = function (e) {
        let input = e.inputBuffer.getChannelData(0);
        let bufferData = new Float32Array(bufferSize);
        for (let i = 0; i < bufferSize; i++) {
          bufferData[i] = input[i];
        }
        audioData.push(bufferData);
      };

      // getusermedia
      let handleSuccess = function (stream) {
        audioContext = new AudioContext();
        audio_sample_rate = audioContext.sampleRate;
        scriptProcessor = audioContext.createScriptProcessor(bufferSize, 1, 1);
        let mediastreamsource = audioContext.createMediaStreamSource(stream);
        mediastreamsource.connect(scriptProcessor);
        scriptProcessor.onaudioprocess = onAudioProcess;
        scriptProcessor.connect(audioContext.destination);

        console.log("record start?");

        // when time passed without pushing the stop button
        // 5秒で終わり
        setTimeout(function () {
          console.log("10 sec");
          saveAudio();
          console.log("saved audio");
        }, 5000);
      };

      // getUserMedia
      // これがマイクを呼び出し、streamをhandleSuccessに処理してもらう
      navigator.mediaDevices
        .getUserMedia({ audio: true, video: false })
        .then(handleSuccess);
    },

    audioApi() {
      window.AudioContext = window.AudioContext || window.webkitAudioContext;
      // Create the instance of AudioContext
      let context = new AudioContext();
      // Create the instance of OscillatorNode
      let oscillator = context.createOscillator();
      // for legacy browsers
      oscillator.start = oscillator.start || oscillator.noteOn;
      oscillator.stop = oscillator.stop || oscillator.noteOff;
      // for legacy browsers
      context.createGain = context.createGain || context.createGainNode;
      // Create the instance of GainNode
      let gain = context.createGain();
      // OscillatorNode (Input) -> GainNode (Volume) -> AudioDestinationNode (Output)
      oscillator.connect(gain);
      gain.connect(context.destination);
      // Start sound
      oscillator.start(0);
      // Stop sound (after 5 sec)
      window.setTimeout(function () {
        oscillator.stop(0);
      }, 3000);
      // 音量調整
      gain.gain.value = 0.1;
    },
  },
};
</script>