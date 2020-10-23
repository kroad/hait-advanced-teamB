<template>
  <div>
    <Record />
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
  </div>
</template>

<script>
import axios from "axios";
import Record from "./Record";

export default {
  data() {
    return {
      info: {
        artist1: 1,
        artist2: null,
        heighest: 84,
        lowest: 1,
      },
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
          this.$store.dispatch("addSongs", response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  components: {
    Record,
  },
};
</script>

<style scoped>
div {
  color: red;
}
</style>