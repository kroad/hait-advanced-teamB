<template>
  <div>
    <v-container>
      <v-file-input
        show-size
        filled
        accept="audio/*"
        label="Audioファイルを入れてください"
        @change="fileToBlob"
        @click:clear="
          stop();
          resetSrc();
        "
      ></v-file-input>
      <v-slider
        v-model="pitch"
        hint="キーを変更できます"
        max="25"
        min="-25"
        persistent-hint
        thumb-label="always"
        append-icon="mdi-plus"
        prepend-icon="mdi-minus"
        @click:append="
          stop();
          pitchIn();
          pitchChange();
        "
        @click:prepend="
          stop();
          pitchOut();
          pitchChange();
        "
        @click="
          stop();
          pitchChange();
        "
      ></v-slider>
      <v-btn
        fab
        dark
        large
        color="purple"
        @click="start"
        :disabled="src === null"
      >
        <v-icon dark> mdi-play </v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        large
        color="purple"
        @click="restart"
        :disabled="src === null"
      >
        <v-icon dark> mdi-reload </v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        large
        color="purple"
        @click="stop"
        :disabled="src === null"
      >
        <v-icon dark> mdi-stop </v-icon>
      </v-btn>
    </v-container>
  </div>
</template>
<script>
import * as Tone from "tone";

export default {
  data() {
    return {
      src: null,
      pitch: 0,
    };
  },
  computed: {
    player() {
      let player = new Tone.Player(this.src);
      return player;
    },
    pitchShift() {
      let pitchShift = new Tone.PitchShift().toDestination();
      return pitchShift;
    },
    audio() {
      let audio = this.player.connect(this.pitchShift);
      return audio;
    },
  },
  methods: {
    fileToBlob(file) {
      this.stop();
      if (file) {
        this.src = window.URL.createObjectURL(file);
      }
    },
    pitchChange() {
      this.pitchShift.pitch = this.pitch;
    },
    start() {
      let audio = this.audio;
      Tone.loaded().then(() => {
        audio.start();
      });
    },
    stop() {
      this.audio.stop();
    },
    restart() {
      this.audio.restart();
    },
    resetSrc() {
      this.src = null;
    },
    pitchOut() {
      this.pitch = this.pitch - 1 || -25;
    },
    pitchIn() {
      this.pitch = this.pitch + 1 || 25;
    },
  },
};
</script>