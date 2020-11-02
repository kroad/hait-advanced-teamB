<template>
  <div class="result-wrapper">
    <v-container>
      <v-row>
        <v-col>
          <v-toolbar dark>
            <v-toolbar-title>測定結果</v-toolbar-title>
          </v-toolbar>
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
        <v-col cols="12">
          <v-simple-table dark>
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-left">Artist</th>
                  <th class="text-left">類似度</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="artist in artists" :key="artist">
                  <td>{{ artist }}</td>
                  <td>{{ 50 }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
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