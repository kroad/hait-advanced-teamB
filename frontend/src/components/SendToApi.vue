<template>
  <div>
    <v-stepper v-model="e1" alt-labels>
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1"
          >最高音最低音を選択</v-stepper-step
        >
        <v-divider></v-divider>
        <v-stepper-step step="2">声を録音</v-stepper-step>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1">
          <v-container>
            <v-row>
              <v-col>
                <v-select
                  v-model="lowest"
                  :items="scale_jp"
                  label="地声最低音"
                  hint="地声で最も低い音を選んでください"
                  persistent-hint
                  outlined
                >
                </v-select>
              </v-col>
              <v-col>
                <v-select
                  v-model="heighest"
                  :items="scale_jp"
                  label="地声最高音"
                  hint="地声で最も高い音を選んでください"
                  persistent-hint
                  outlined
                >
                </v-select>
              </v-col>
              <!-- <v-col>
                <v-select
                  :items="scale_jp"
                  label="裏声最低音"
                  hint="裏声で最も高い音を選んでください"
                  persistent-hint
                  outlined
                >
                </v-select>
              </v-col> -->
            </v-row>
          </v-container>

          <v-btn color="primary" @click="e1 = 2"> 次へ </v-btn>

          <v-btn text>Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
      <v-stepper-items>
        <v-stepper-content step="2">
          <v-card class="mb-12" color="grey lighten-1">
            <Record />
          </v-card>

          <v-btn color="primary" @click="sendToSongApi">APIへリクエスト </v-btn>

          <v-btn text @click="e1 = 1">Cancel</v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
    <p>{{ heighest }}</p>
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
      scale_jp: [
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
        "hihihiA",
        "hihihiA#",
        "hihihiB",
        "hihihiC",
        "hihihiC#",
        "hihihiD",
        "hihihiD#",
        "hihihiE",
        "hihihiF",
        "hihihiF#",
        "hihihiG",
        "hihihiG#",
        "hihihihiA",
        "hihihihiA#",
        "hihihihiB",
        "hihihihiC",
      ],
      scale_uni: [
        "A0",
        "A#0",
        "B0",
        "C1",
        "C#1",
        "D1",
        "D#1",
        "E1",
        "F1",
        "F#1",
        "G1",
        "G#1",
        "A1",
        "A#1",
        "B1",
        "C2",
        "C#2",
        "D2",
        "D#2",
        "E2",
        "F2",
        "F#2",
        "G2",
        "G#2",
        "A2",
        "A#2",
        "B2",
        "C3",
        "C#3",
        "D3",
        "D#3",
        "E3",
        "F3",
        "F#3",
        "G3",
        "G#3",
        "A3",
        "A#3",
        "B3",
        "C4",
        "C#4",
        "D4",
        "D#4",
        "E4",
        "F4",
        "F#4",
        "G4",
        "G#4",
        "A4",
        "A#4",
        "B4",
        "C5",
        "C#5",
        "D5",
        "D#5",
        "E5",
        "F5",
        "F#5",
        "G5",
        "G#5",
        "A5",
        "A#5",
        "B5",
        "C6",
        "C#6",
        "D6",
        "D#6",
        "E6",
        "F6",
        "F#6",
        "G6",
        "G#6",
        "A6",
        "A#6",
        "B6",
        "C7",
        "C#7",
        "D7",
        "D#7",
        "E7",
        "F7",
        "F#7",
        "G7",
        "G#7",
        "A7",
        "A#7",
        "B7",
        "C8",
      ],
      heighest: "hihihihiC",
      lowest: "lowlowA",
      info: {
        artist1: 1,
        artist2: 2,
        artist3: 3,
        artist4: 4,
        artist5: 5,
        artist6: 6,
        artist7: 7,
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
            heighest: this.heighest,
            lowest: this.lowest,
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