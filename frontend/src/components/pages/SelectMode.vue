<template>
  <v-container>
    <SendToApi />
  </v-container>
</template>
<script>
import SendToApi from "../functions/SendToApi";

export default {
  // data() {
  //   return {
  //     componentId: "SendToApi",
  //   };
  // },
  components: {
    SendToApi,
  },
};
</script>
<style scoped>
</style>