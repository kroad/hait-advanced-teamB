<template>
  <div>
    <template>
      <Result />
    </template>
  </div>
</template>

<script>
import Result from "../subbar/Result";
export default {
  components: {
    Result,
  },
};
</script>
<style scoped>
div {
  background-color: #9e9e9e;
  height: 100%;
  width: 50px;
  transition: width 0.1s;
}
div:hover {
  width: 200px;
}
</style>