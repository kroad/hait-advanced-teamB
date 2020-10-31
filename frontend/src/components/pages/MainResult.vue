<template>
  <div class="result-wrapper">
    <v-list color="blue">
      <v-list-item v-for="song in songs" :key="song.id" link>
        <v-list-item-content>
          <v-list-item-title> {{ song }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
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