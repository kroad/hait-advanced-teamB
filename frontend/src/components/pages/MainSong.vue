<template>
  <div>
    <v-container>
      <p>{{ artistUrl }}{{ songUrl }}</p>
    </v-container>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  props: ["artistUrl", "songUrl"],
  computed: {
    ...mapGetters(["songs"]),
  },
};
</script>