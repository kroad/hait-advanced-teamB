<template>
  <v-container>
    <div class="keyboard">
      <div
        class="piano_key"
        v-for="key in piano_keys"
        :key="key.num"
        @mouseover="showScale(key.scale)"
        @click="playSound(key.num)"
      >
        <div class="wh" v-if="key.color == 'white'"></div>
        <div class="bl" v-if="key.color == 'black'"></div>
      </div>
    </div>
    <v-alert v-if="scale_pointed" border="left" color="indigo" dark
      >その音は{{ scale_pointed }}です</v-alert
    >
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      scale_pointed: "",
      piano_keys: [
        { num: "001", scale: "lowlowA", color: "white" },
        { num: "002", scale: "lowlowA#", color: "black" },
        { num: "003", scale: "lowlowB", color: "white" },
        { num: "004", scale: "lowlowC", color: "white" },
        { num: "005", scale: "lowlowC#", color: "black" },
        { num: "006", scale: "lowlowD", color: "white" },
        { num: "007", scale: "lowlowD#", color: "black" },
        { num: "008", scale: "lowlowE", color: "white" },
        { num: "009", scale: "lowlowF", color: "white" },
        { num: "010", scale: "lowlowF#", color: "black" },
        { num: "011", scale: "lowlowG", color: "white" },
        { num: "012", scale: "lowlowG#", color: "black" },
        { num: "013", scale: "lowA", color: "white" },
        { num: "014", scale: "lowA#", color: "black" },
        { num: "015", scale: "lowB", color: "white" },
        { num: "016", scale: "lowC", color: "white" },
        { num: "017", scale: "lowC#", color: "black" },
        { num: "018", scale: "lowD", color: "white" },
        { num: "019", scale: "lowD#", color: "black" },
        { num: "020", scale: "lowE", color: "white" },
        { num: "021", scale: "lowF", color: "white" },
        { num: "022", scale: "lowF#", color: "black" },
        { num: "023", scale: "lowG", color: "white" },
        { num: "024", scale: "lowG#", color: "black" },
        { num: "025", scale: "mid1A", color: "white" },
        { num: "026", scale: "mid1A#", color: "black" },
        { num: "027", scale: "mid1B", color: "white" },
        { num: "028", scale: "mid1C", color: "white" },
        { num: "029", scale: "mid1C#", color: "black" },
        { num: "030", scale: "mid1D", color: "white" },
        { num: "031", scale: "mid1D#", color: "black" },
        { num: "032", scale: "mid1E", color: "white" },
        { num: "033", scale: "mid1F", color: "white" },
        { num: "034", scale: "mid1F#", color: "black" },
        { num: "035", scale: "mid1G", color: "white" },
        { num: "036", scale: "mid1G#", color: "black" },
        { num: "037", scale: "mid2A", color: "white" },
        { num: "038", scale: "mid2A#", color: "black" },
        { num: "039", scale: "mid2B", color: "white" },
        { num: "040", scale: "mid2C", color: "white" },
        { num: "041", scale: "mid2C#", color: "black" },
        { num: "042", scale: "mid2D", color: "white" },
        { num: "043", scale: "mid2D#", color: "black" },
        { num: "044", scale: "mid2E", color: "white" },
        { num: "045", scale: "mid2F", color: "white" },
        { num: "046", scale: "mid2F#", color: "black" },
        { num: "047", scale: "mid2G", color: "white" },
        { num: "048", scale: "mid2G#", color: "black" },
        { num: "049", scale: "hiA", color: "white" },
        { num: "050", scale: "hiA#", color: "black" },
        { num: "051", scale: "hiB", color: "white" },
        { num: "052", scale: "hiC", color: "white" },
        { num: "053", scale: "hiC#", color: "black" },
        { num: "054", scale: "hiD", color: "white" },
        { num: "055", scale: "hiD#", color: "black" },
        { num: "056", scale: "hiE", color: "white" },
        { num: "057", scale: "hiF", color: "white" },
        { num: "058", scale: "hiF#", color: "black" },
        { num: "059", scale: "hiG", color: "white" },
        { num: "060", scale: "hiG#", color: "black" },
        { num: "061", scale: "hihiA", color: "white" },
        { num: "062", scale: "hihiA#", color: "black" },
        { num: "063", scale: "hihiB", color: "white" },
        { num: "064", scale: "hihiC", color: "white" },
        { num: "065", scale: "hihiC#", color: "black" },
        { num: "066", scale: "hihiD", color: "white" },
        { num: "067", scale: "hihiD#", color: "black" },
        { num: "068", scale: "hihiE", color: "white" },
        { num: "069", scale: "hihiF", color: "white" },
        { num: "070", scale: "hihiF#", color: "black" },
        { num: "071", scale: "hihiG", color: "white" },
        { num: "072", scale: "hihiG#", color: "black" },
        { num: "073", scale: "hihihiA", color: "white" },
        { num: "074", scale: "hihihiA#", color: "black" },
        { num: "075", scale: "hihihiB", color: "white" },
        { num: "076", scale: "hihihiC", color: "white" },
        { num: "077", scale: "hihihiC#", color: "black" },
        { num: "078", scale: "hihihiD", color: "white" },
        { num: "079", scale: "hihihiD#", color: "black" },
        { num: "080", scale: "hihihiE", color: "white" },
        { num: "081", scale: "hihihiF", color: "white" },
        { num: "082", scale: "hihihiF#", color: "black" },
        { num: "083", scale: "hihihiG", color: "white" },
        { num: "084", scale: "hihihiG#", color: "black" },
        { num: "085", scale: "hihihihiA", color: "white" },
        { num: "086", scale: "hihihihiA#", color: "black" },
        { num: "087", scale: "hihihihiB", color: "white" },
        { num: "088", scale: "hihihihiC", color: "white" },
      ],
    };
  },
  methods: {
    showScale(scale) {
      this.scale_pointed = scale;
    },
    playSound(num) {
      let audio = new Audio();
      audio.src = "/audio/piano" + num + ".wav";
      audio.currentTime = 0;
      audio.volume = 1;
      audio.play();
    },
  },
};
</script>

<style scoped>
* {
  vertical-align: top;
}

.keyboard {
  box-shadow: 0px 0px 40px -5px rgba(0, 0, 0, 0.4);
  display: flex;
  cursor: pointer;
  overflow: scroll;
}

.piano_key {
  position: relative;
}

.wh {
  width: 44px;
  height: 300px;
  background-color: white;
  border: solid 1px #eee;
  cursor: pointer;
}

.wh:hover {
  background-color: #e1e1e1;
}

.bl {
  width: 22px;
  height: 165px;
  background-color: #585858;
  margin-left: -11px;
  margin-right: -22px;
  position: absolute;
  z-index: 10;
  cursor: pointer;
}
.bl:hover {
  background-color: #202020;
}
</style>