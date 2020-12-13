<template>
  <div class="main">
    <AlertMessage />
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
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