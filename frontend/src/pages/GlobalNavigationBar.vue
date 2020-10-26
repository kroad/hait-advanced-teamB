<template>
  <v-navigation-drawer
    color="grey darken-4"
    expand-on-hover
    mini-variant
    permanent
    dark
    app
  >
    <v-list dense nav class="py-0">
      <v-list-item two-line class="pt-6">
        <v-list-item-icon>
          <v-icon>mdi-music-circle</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Application</v-list-item-title>
          <v-list-item-subtitle>Subtext</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  data() {
    return {
      items: [
        { title: "ホーム", icon: "mdi-home" },
        { title: "プレイリスト", icon: "mdi-playlist-music" },
        { title: "マイページ", icon: "mdi-account-box" },
        { title: "ログアウト", icon: "mdi-logout-variant" },
        { title: "設定", icon: "mdi-cog" },
      ],
    };
  },
};
</script>
<style scoped>
</style>