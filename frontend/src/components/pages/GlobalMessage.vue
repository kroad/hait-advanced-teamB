<template>
  <div id="messages">
    <v-alert v-show="message.error" class="mb-0">
      {{ message.error }}
    </v-alert>
    <v-alert v-show="message.warnings.length > 0" class="mb-0">
      <p v-for="warning in message.warnings" :key="warning" class="mb-0">
        {{ warning }}
      </p>
    </v-alert>
    <v-alert v-show="message.info" class="mb-0">
      {{ message.info }}
    </v-alert>
  </div>
</template>

<script>
export default {
  computed: {
    message: function () {
      return this.$store.state.message;
    },
  },
};
</script>