<template>
  <div>
    <v-btn @click="record" fab x-large dark color="purple">
      <v-icon>mdi-microphone</v-icon>
    </v-btn>
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
      navigator.mediaDevices
        .getUserMedia({ audio: true, video: false })
        .then((stream) => {
          let recorder = new MediaRecorder(stream);
          let chunks = [];
          recorder.addEventListener("dataavailable", (e) => {
            chunks.push(e.data);
            // 後で消す
            console.log(e);
            console.log(chunks);
          });
          recorder.addEventListener("stop", () => {
            const blob = new Blob(chunks, { type: "audio/wav" });
            this.$store.dispatch("addVoice", blob);
            // 後で消す
            console.log(blob);
          });
          recorder.start(1000);
          setTimeout(() => {
            recorder.stop();
          }, 5000);
        })
        .catch((error) => {
          // 後で消す
          console.log(error);
        });
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