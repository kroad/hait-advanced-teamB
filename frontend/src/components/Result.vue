<template>
  <div>
    <h2>結果</h2>
    <div v-for="artist in artists" :key="artist">
      <p>アーティスト：{{ artist }}</p>
      <div v-for="song in songs" :key="song.id">
        <template v-if="song.artist_name === artist">
          <p>曲名：{{ song.title }}</p>
          <p>最高音：{{ song.heighest_name }}</p>
          <p>最低音：{{ song.lowest_name }}</p>
          <hr />
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["artists", "songs"]),
  },
};
</script>