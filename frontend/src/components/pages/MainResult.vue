<template>
  <div class="result-wrapper">
    <v-container>
      <v-row>
        <v-col>
          <v-card dark>
            <v-card-title>測定結果</v-card-title>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card dark>
            <v-card-title> あなたの音域 </v-card-title>
            <v-list>
              <v-list-item two-line>
                <v-list-item-content>
                  <v-list-item-title>{{ myVoice.z_lowest }}</v-list-item-title>
                  <v-list-item-subtitle>地声最低音</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item two-line>
                <v-list-item-content>
                  <v-list-item-title>{{
                    myVoice.z_heighest
                  }}</v-list-item-title>
                  <v-list-item-subtitle>地声最高音</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-list-item two-line>
                <v-list-item-content>
                  <v-list-item-title>{{
                    myVoice.u_heighest
                  }}</v-list-item-title>
                  <v-list-item-subtitle>裏声最高音</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card>
            <v-list dark>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title> アーティスト名 </v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                  <v-list-item-title> 類似度 </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item
                v-for="artist in artists"
                :key="artist"
                link
                :to="'/measure/result/' + artist"
              >
                <v-list-item-content>
                  {{ artist }}
                </v-list-item-content>
                <v-list-item-content> 50 </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["artists", "songs", "myVoice"]),
  },
};
</script>

<style scoped>
.result_wrapper {
  height: 100%;
}
</style>