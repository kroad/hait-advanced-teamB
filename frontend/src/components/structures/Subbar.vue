<template>
  <div>
    <Result />
  </div>
</template>

<script>
import Result from "./Result";
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
  width: 50px;
  transition: width 0.2s;
}
div:hover {
  width: 200px;
}
</style>