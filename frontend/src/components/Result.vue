<template>
  <div class="result-wrapper">
    <v-list color="blue">
      <v-list-item v-for="(artist, index) in artists" :key="artist" link>
        <v-list-item-content>
          <v-list-item-title> {{ index + 1 }}-{{ artist }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["artists"]),
  },
};
</script>

<style scoped>
.result_wrapper {
  height: 100%;
}
</style>