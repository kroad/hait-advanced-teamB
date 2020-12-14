<template>
  <v-container>
    <v-row
      ><v-col>
        <v-btn to="/playlists/"> 戻る </v-btn>
      </v-col></v-row
    >
    <v-row
      ><v-col>
        <v-list v-if="playlist">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title> 曲名 </v-list-item-title>
            </v-list-item-content>
            <v-list-item-content>
              <v-list-item-title> アーティスト名 </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item
            v-for="song in playlist.songs"
            :key="song.id"
            link
            :to="'/playlists/' + playlist.name + '/' + song.title"
          >
            <v-list-item-content>
              {{ song.title }}
            </v-list-item-content>
            <v-list-item-content> {{ song.artist_name }} </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col></v-row
    >
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  props: ["name"],
  computed: {
    ...mapGetters("auth", ["playlists"]),
    playlist() {
      let playlist = [];
      if (this.playlists.length > 0) {
        playlist = this.playlists.filter(
          (playlist) => playlist.name == this.name
        );
      }
      return playlist[0];
    },
  },
};
</script>
