<template>
  <div>
    <template>
      <SubbarResult />
    </template>
  </div>
</template>

<script>
import SubbarResult from "../pages/SubbarResult";
export default {
  components: {
    SubbarResult,
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