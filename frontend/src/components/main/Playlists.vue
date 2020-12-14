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
      </v-list-item>
    </v-list>
    <v-alert border="top" colored-border type="info" elevation="2" v-else
      >登録されたプレイリストはありません</v-alert
    >
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("auth", ["playlists"]),
  },
};
</script>
