<template>
  <div>
    <SubbarResult />
  </div>
</template>

<script>
import SubbarResult from "../functions/SubbarResult";
export default {
  components: {
    SubbarResult,
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