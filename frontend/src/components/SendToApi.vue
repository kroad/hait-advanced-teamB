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
import { mapGetters } from "vuex";
// import HighLowSelectForm from "./HighLowSelectForm";

export default {
  components: {
    Record,
    // HighLowSelectForm,
  },
  data() {
    return {
      e1: 1,
      heighest: "hihihihiC",
      lowest: "lowlowA",
    };
  },
  computed: {
    ...mapGetters(["scale_jp", "scale_uni"]),
  },
  methods: {
    sendToSongApi() {
      axios
        .get("http://127.0.0.1:8000/api/v1/songs/", {
          params: {
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