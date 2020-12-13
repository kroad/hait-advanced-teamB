<template>
  <v-list>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title> プレイリスト名 </v-list-item-title>
      </v-list-item-content>
      <v-list-item-content>
        <v-list-item-title> 曲数 </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item
      v-for="playlist in playlists"
      :key="playlist.id"
      link
      :to="'/playlists/' + playlist.name"
    >
      <v-list-item-content>
        {{ playlist.name }}
      </v-list-item-content>
      <v-list-item-content> {{ playlist.songs.length }} </v-list-item-content>
    </v-list-item>
  </v-list>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      playlists: "",
    };
  },
  mounted() {
    let vm = this;
    axios
      .get("http://127.0.0.1:8000/api/v1/playlist/")
      .then(function(response) {
        console.log(response.data.results);
        vm.playlists = response.data.results;
      })
      .catch(function(error) {
        console.log(error);
      });
  },
};
</script>
