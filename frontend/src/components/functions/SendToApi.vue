<template>
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
        <ScaleSelectForm />
        <v-btn color="primary" @click="e1 = 2"> 次へ </v-btn>
      </v-stepper-content>
    </v-stepper-items>

    <v-stepper-items>
      <v-stepper-content step="2">
        <v-card class="mb-12" color="grey lighten-1">
          <Record />
        </v-card>
        <v-container>
          <v-row>
            <v-col cols="auto">
              <v-btn @click="e1 = 1">戻る</v-btn>
            </v-col>
            <v-col>
              <audio id="player" controls :src="voiceSource"></audio>
            </v-col>
            <v-col>
              <v-btn color="primary" @click="sendToSongApi"
                >APIへリクエスト</v-btn
              >
            </v-col>
          </v-row>
        </v-container>
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import axios from "axios";
import Record from "./Record";
import ScaleSelectForm from "./ScaleSelectForm";
import { mapGetters } from "vuex";

export default {
  components: {
    Record,
    ScaleSelectForm,
  },
  data() {
    return {
      e1: 1,
    };
  },
  computed: {
    ...mapGetters(["voiceSource", "myVoice"]),
  },
  methods: {
    sendToSongApi() {
      this.$emit("click-to-api", "MainResult");
      axios
        .get("http://127.0.0.1:8000/api/v1/songs/", {
          params: {
            z_lowest: this.myVoice.z_lowest,
            z_heighest: this.myVoice.z_heighest,
            // 後で送れるようにする
            // u_heighest: this.myVoice.u_heighest,
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
</style>