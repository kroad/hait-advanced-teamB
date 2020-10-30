<template>
  <div>
    <component
      :is="componentId"
      @click-to-api="componentId = $event"
    ></component>
  </div>
</template>
<script>
import SendToApi from "../functions/SendToApi";
import MainResult from "../functions/MainResult";
export default {
  data() {
    return {
      componentId: "SendToApi",
    };
  },
  components: {
    SendToApi,
    MainResult,
  },
};
</script>
<style scoped>
</style>