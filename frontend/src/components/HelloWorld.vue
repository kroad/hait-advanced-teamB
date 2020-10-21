
<template>
  <div>
    <SongForm />
    <Result />
  </div>
</template>

<script>
import SongForm from "./SongForm";
import Result from "./Result";

export default {
  name: "HelloWorld",
  components: {
    Result,
    SongForm,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  padding: 0.5em 1em;
  margin: 2em 0;
  border: double 5px #4ec4d3;
}
</style>