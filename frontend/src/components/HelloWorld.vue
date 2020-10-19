
<template>
  <div>
    <button v-on:click="sendAPIRequest">APIへリクエストを送る</button>
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
    sendAPIRequest:() => {
      axios
      .get("http://127.0.0.1:8000/api/v1/songs/",{
        params: {
          artist:1,
          heighest__lte:70,
          lowest__gte:2
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