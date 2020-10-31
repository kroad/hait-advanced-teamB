<template>
  <div class="result-wrapper">
    <v-container fluid>
      <v-toolbar color="indigo darken-5" dark>
        <v-toolbar-title>測定結果</v-toolbar-title>
      </v-toolbar>
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
    ...mapGetters(["artists", "songs"]),
  },
};
</script>

<style scoped>
.result_wrapper {
  height: 100%;
}
</style>