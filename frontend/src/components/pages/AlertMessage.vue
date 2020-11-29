<template>
  <v-container fluid>
    <v-alert v-if="info" dismissible type="success">{{ info }}</v-alert>
    <div v-for="(warning, key) in warnings" :key="warning">
      <v-alert dismissible type="warning"
        >{{ key }}:{{ warning.toString() }}</v-alert
      >
    </div>
    <v-alert v-if="error" dismissible type="error">{{ error }}</v-alert>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("message", ["error", "warnings", "info"]),
  },
};
</script>