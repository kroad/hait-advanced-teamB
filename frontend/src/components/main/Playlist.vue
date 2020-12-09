<template>
  <div>
    <p>Playlist</p>
    <p>{{ response }}</p>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      response: "",
    };
  },
  mounted() {
    console.log("hello");
    let vm = this;
    axios
      .get("http://127.0.0.1:8000/api/v1/playlist/")
      .then(function(response) {
        console.log(response.data);
        vm.response = response.data;
      })
      .catch(function(error) {
        console.log(error);
      });
  },
};
</script>
