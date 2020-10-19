
<template>
  <div>
    <div>
      <div>
        <label for="artist1">歌手1</label>
        <input id="artist1" type="number" v-model.number="info.artist1" />
      </div>
      <div>
        <label for="artist2">歌手2</label>
        <input id="artist2" type="number" v-model.number="info.artist2" />
      </div>
      <div>
        <label for="heighest">最高音</label>
        <input id="heighest" type="number" v-model.number="info.heighest" />
      </div>
      <div>
        <label for="lowest">最低音</label>
        <input id="lowest" type="number" v-model.number="info.lowest" />
      </div>
      <button v-on:click="sendToSongApi">APIへリクエストを送る</button>
      <h2>結果</h2>
      <div v-for="song in songs" :key="song.id">
        <div>アーティスト：{{ song.artist_name }}</div>
        <div>曲名：{{ song.title }}</div>
        <div>最高音：{{ song.heighest_name }}</div>
        <div>最低音：{{ song.lowest_name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {},
  data() {
    return {
      info: {
        artist1: 1,
        artist2: null,
        heighest: 84,
        lowest: 1,
      },
      songs: [],
    };
  },
  methods: {
    sendToSongApi() {
      axios
        .get("http://127.0.0.1:8000/api/v1/songs/", {
          params: {
            artist1: this.info.artist1,
            artist2: this.info.artist2,
            heighest: this.info.heighest,
            lowest: this.info.lowest,
          },
        })
        .then((response) => {
          this.songs = response.data;
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
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