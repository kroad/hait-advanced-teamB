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
      <label for="artist3">歌手3</label>
      <input id="artist3" type="number" v-model.number="info.artist3" />
    </div>
    <div>
      <label for="artist4">歌手4</label>
      <input id="artist4" type="number" v-model.number="info.artist4" />
    </div>
    <div>
      <label for="artist5">歌手5</label>
      <input id="artist5" type="number" v-model.number="info.artist5" />
    </div>
    <div>
      <label for="artist6">歌手6</label>
      <input id="artist6" type="number" v-model.number="info.artist6" />
    </div>
    <div>
      <label for="artist7">歌手7</label>
      <input id="artist7" type="number" v-model.number="info.artist7" />
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
        artist2: 2,
        artist3: 3,
        artist4: 4,
        artist5: 5,
        artist6: 6,
        artist7: 7,
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
            artist3: this.info.artist3,
            artist4: this.info.artist4,
            artist5: this.info.artist5,
            artist6: this.info.artist6,
            artist7: this.info.artist7,
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