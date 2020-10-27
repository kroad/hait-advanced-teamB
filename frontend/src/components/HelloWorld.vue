<template>
  <div>
    <GlobalSubBar />
    <SongForm />
  </div>
</template>

<script>
import SongForm from "./SongForm";
import GlobalSubBar from "../pages/GlobalSubBar";

export default {
  name: "HelloWorld",
  components: {
    SongForm,
    GlobalSubBar,
  },
};
</script>
<style scoped>
</style>