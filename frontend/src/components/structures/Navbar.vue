<template>
  <div class="sidebar_component">
    <v-list color="primary">
      <v-list-item two-line>
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
  </div>
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
.sidebar_component {
  background-color: purple;
  height: 100%;
  width: 60px;
  transition: width 0.2s;
}
.sidebar_component:hover {
  width: 245px;
}
</style>