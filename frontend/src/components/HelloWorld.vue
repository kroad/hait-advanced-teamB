
<template>
  <div>
    <SongForm />
    <Result :songs="songs" :artists="artists" />
  </div>
</template>

<script>
import Result from "./Result";
import SongForm from "./SongForm";

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