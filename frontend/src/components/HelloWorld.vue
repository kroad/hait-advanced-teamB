
<template>
  <div>
    <button v-on:click="sendAPItoSong1">API1へリクエストを送る</button>
    <button v-on:click="sendAPItoSong2">API2へリクエストを送る</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  props: {
  },
  data() {
    return {
    }
  },
  methods: {
    sendAPItoSong1:() => {
      axios
      .get("http://127.0.0.1:8000/api/v1/songs1/",{
        params: {
          artist:1,
          heighest__lte:70,
          lowest__gte:2
        }
      })
      .then(response => {
        console.log(response);
      })
    },
    sendAPItoSong2:() => {
      axios
      .get("http://127.0.0.1:8000/api/v1/songs2/",{
        params: {
          artist:1,
          heighest:70,
          lowest:2,
        }
      })
      .then(response => {
        console.log(response);
      })
    }
  },
}
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