<template>
  <div>
    <Result />
  </div>
</template>

<script>
import Result from "../components/Result";
export default {
  components: {
    Result,
  },
};
</script>
<style scoped>
div {
  background-color: gray;
  height: 100%;
  width: 100px;
  transition: width 0.2s;
}
div:hover {
  width: 100%;
}
</style>