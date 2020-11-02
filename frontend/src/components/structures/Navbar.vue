<template>
  <div class="sidebar_component">
    <v-list color="primary" dark>
      <v-list-item two-line link to="/">
        <v-list-item-icon>
          <v-icon>mdi-music-circle</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>カラオケアプリ</v-list-item-title>
          <v-list-item-subtitle>KaraokeApp</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
        :to="item.path"
        exact
      >
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
        { title: "ホーム", icon: "mdi-home", path: "/measure/select/" },
        { title: "測定", icon: "mdi-microphone", path: "/measure/" },
        {
          title: "プレイリスト",
          icon: "mdi-playlist-music",
          path: "/playlist/",
        },
        { title: "ランキング", icon: "mdi-trophy", path: "/ranking/" },
        { title: "マイページ", icon: "mdi-account-box", path: "/mypage/" },
        { title: "ログアウト", icon: "mdi-logout-variant" },
        { title: "設定", icon: "mdi-cog", path: "/setting/" },
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