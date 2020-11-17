<template>
  <div class="result-wrapper">
    <v-list color="grey" dark>
      <v-list-item link to="/measure/result/" exact>
        <v-list-item-content>
          <v-list-item-title>測定結果</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        v-for="(item, index) in prob_and_artists"
        :key="item.artist"
        link
        router-link
        :to="'/measure/result/' + item.artist"
      >
        <v-list-item-icon>
          <v-icon>{{ index + 1 }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>{{ item.artist }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["prob_and_artists"]),
  },
};
</script>

<style scoped>
.result_wrapper {
  height: 100%;
}
</style>