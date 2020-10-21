
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>