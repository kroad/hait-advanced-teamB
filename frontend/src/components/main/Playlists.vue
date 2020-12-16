<template>
  <v-container>
    <v-list v-if="playlists.length > 0">
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
        <v-list-item-action>
          <v-btn icon @click.prevent="deletePlaylist(playlist.id)">
            <v-icon color="grey lighten-1">mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
    </v-list>
    <v-alert border="top" colored-border type="info" elevation="2" v-else
      >登録されたプレイリストはありません</v-alert
    >
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";
import api from "@/services/api";

export default {
  data() {
    return {
      playlistId: "",
    };
  },
  computed: {
    ...mapGetters("auth", ["playlists"]),
  },
  methods: {
    deletePlaylist(id) {
      api.delete("/playlist/" + id).then(() => {
        this.$store.dispatch("auth/reload");
      });
    },
  },
};
</script>
