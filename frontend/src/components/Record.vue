<template>
  <div>
    <input
      type="file"
      accept="audio/*"
      capture="microphone"
      id="recorder"
      @change="playSound"
    />
    <button @click="record">録音</button>
    <audio id="player" controls :src="source"></audio>
    <button @click="speaker">音を鳴らす</button>

    <p>{{ source }}</p>
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
    speaker() {
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

    playSound(event) {
      let file = event.target.files[0];
      this.source = URL.createObjectURL(file);
    },

    record() {
      navigator.mediaDevices
        .getUserMedia({ audio: true, video: false })
        .then((stream) => {
          let recorder = new MediaRecorder(stream);
          let chunks = [];
          recorder.addEventListener("dataavailable", (e) => {
            chunks.push(e.data);
            console.log(e);
            console.log(chunks);
          });
          recorder.addEventListener("stop", () => {
            const blob = new Blob(chunks, { type: "audio/wav" });
            this.source = window.URL.createObjectURL(blob);
            console.log(blob);
          });
          recorder.start(1000);
          setTimeout(() => {
            recorder.stop();
          }, 5000);
        })

        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>