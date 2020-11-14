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
  background-color: #9E9E9E;
  height: 100%;
  width: 50px;
  transition: width 0.2s;
}
div:hover {
  width: 200px;
}
</style>