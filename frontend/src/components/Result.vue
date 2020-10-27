<template>
  <v-container>
    <v-row>
      <v-col cols="12" v-for="artist in artists" :key="artist">
        <v-card hover ripple>
          <v-card-text>{{ artist }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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
</style>