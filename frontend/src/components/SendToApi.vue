<template>
  <div>
    <v-stepper v-model="e1" alt-labels dark>
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1"
          >最高音最低音を選択</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step step="2">声を録音</v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-card class="mb-12" color="green">
            <!-- <HighLowSelectForm /> -->
            <v-select
              :items="items"
              label="地声最低音"
              hint="地声で最も低い音を選んでください"
              persistent-hint
              outlined
            >
            </v-select>
            <v-select
              :items="items"
              label="地声最高音"
              hint="地声で最も高い音を選んでください"
              persistent-hint
              outlined
            >
            </v-select>
            <v-select
              :items="items"
              label="裏声最低音"
              hint="裏声で最も高い音を選んでください"
              persistent-hint
              outlined
            >
            </v-select>
          </v-card>

          <v-btn color="primary" @click="e1 = 2"> 次へ </v-btn>

          <v-btn text>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
      <v-stepper-items>
        <v-stepper-content step="2">
          <v-card class="mb-12" color="grey lighten-1">
            <Record />
          </v-card>

          <v-btn color="primary" @click="sendToSongApi">実行 </v-btn>

          <v-btn text>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
    <!-- <div>
      <label for="artist1">歌手1</label>
      <input id="artist1" type="number" v-model.number="info.artist1" />
    </div>
    <div>
      <label for="artist2">歌手2</label>
      <input id="artist2" type="number" v-model.number="info.artist2" />
    </div>
    <div>
      <label for="artist3">歌手3</label>
      <input id="artist3" type="number" v-model.number="info.artist3" />
    </div>
    <div>
      <label for="artist4">歌手4</label>
      <input id="artist4" type="number" v-model.number="info.artist4" />
    </div>
    <div>
      <label for="artist5">歌手5</label>
      <input id="artist5" type="number" v-model.number="info.artist5" />
    </div>
    <div>
      <label for="artist6">歌手6</label>
      <input id="artist6" type="number" v-model.number="info.artist6" />
    </div>
    <div>
      <label for="artist7">歌手7</label>
      <input id="artist7" type="number" v-model.number="info.artist7" />
    </div>
    <div>
      <label for="heighest">最高音</label>
      <input id="heighest" type="number" v-model.number="info.heighest" />
    </div>
    <div>
      <label for="lowest">最低音</label>
      <input id="lowest" type="number" v-model.number="info.lowest" />
    </div>
    <button v-on:click="sendToSongApi">APIへリクエストを送る</button> -->
  </div>
</template>

<script>
import axios from "axios";
import Record from "./Record";
// import HighLowSelectForm from "./HighLowSelectForm";

export default {
  components: {
    Record,
    // HighLowSelectForm,
  },
  data() {
    return {
      e1: 1,
      items: [
        "lowlowA",
        "lowlowA#",
        "lowlowB",
        "lowlowC",
        "lowlowC#",
        "lowlowD",
        "lowlowD#",
        "lowlowE",
        "lowlowF",
        "lowlowF#",
        "lowlowG",
        "lowlowG#",
        "lowA",
        "lowA#",
        "lowB",
        "lowC",
        "lowC#",
        "lowD",
        "lowD#",
        "lowE",
        "lowF",
        "lowF#",
        "lowG",
        "lowG#",
        "mid1A",
        "mid1A#",
        "mid1B",
        "mid1C",
        "mid1C#",
        "mid1D",
        "mid1D#",
        "mid1E",
        "mid1F",
        "mid1F#",
        "mid1G",
        "mid1G#",
        "mid2A",
        "mid2A#",
        "mid2B",
        "mid2C",
        "mid2C#",
        "mid2D",
        "mid2D#",
        "mid2E",
        "mid2F",
        "mid2F#",
        "mid2G",
        "mid2G#",
        "hiA",
        "hiA#",
        "hiB",
        "hiC",
        "hiC#",
        "hiD",
        "hiD#",
        "hiE",
        "hiF",
        "hiF#",
        "hiG",
        "hiG#",
        "hihiA",
        "hihiA#",
        "hihiB",
        "hihiC",
        "hihiC#",
        "hihiD",
        "hihiD#",
        "hihiE",
        "hihiF",
        "hihiF#",
        "hihiG",
        "hihiG#",
      ],
      info: {
        artist1: 1,
        artist2: 2,
        artist3: 3,
        artist4: 4,
        artist5: 5,
        artist6: 6,
        artist7: 7,
        heighest: 84,
        lowest: 1,
      },
    };
  },
  methods: {
    sendToSongApi() {
      axios
        .get("http://127.0.0.1:8000/api/v1/songs/", {
          params: {
            artist1: this.info.artist1,
            artist2: this.info.artist2,
            artist3: this.info.artist3,
            artist4: this.info.artist4,
            artist5: this.info.artist5,
            artist6: this.info.artist6,
            artist7: this.info.artist7,
            heighest: this.info.heighest,
            lowest: this.info.lowest,
          },
        })
        .then((response) => {
          this.$store.dispatch("addSongs", response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
div {
  color: red;
}
</style>