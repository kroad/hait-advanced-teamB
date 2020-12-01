<template>
  <div class="main">
    <AlertMessage />
    <router-view></router-view>
  </div>
</template>

<script>
import AlertMessage from "../functions/AlertMessage";
export default {
  components: { AlertMessage },
};
</script>

<style scoped>
div.main {
  background-color: #bbdefb;
  height: 100%;
}
</style>