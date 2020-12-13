<template>
  <div class="sidebar_component">
    <v-list color="grey darken-4" dark>
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
      <v-list-item v-if="isLoggedIn" link exact to="/playlists/">
        <v-list-item-icon>
          <v-icon>mdi-playlist-music</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>プレイリスト</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="isLoggedIn" link exact to="/mypage/">
        <v-list-item-icon>
          <v-icon>mdi-account-box</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>マイページ</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="isLoggedIn" link exact @click="clickLogout">
        <v-list-item-icon>
          <v-icon>mdi-logout-variant</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>ログアウト</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-else link exact @click="clickLogin" to="/login/">
        <v-list-item-icon>
          <v-icon>mdi-login-variant</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>ログイン/新規登録</v-list-item-title>
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
          title: "キーを変えて演奏",
          icon: "mdi-folder-music",
          path: "/keychange/",
        },
        { title: "鍵盤", icon: "mdi-piano", path: "/piano/" },
        { title: "ランキング", icon: "mdi-trophy", path: "/ranking/" },
        { title: "設定", icon: "mdi-cog", path: "/setting/" },
      ],
    };
  },
  computed: {
    username: function () {
      return this.$store.getters["auth/username"];
    },
    isLoggedIn: function () {
      return this.$store.getters["auth/isLoggedIn"];
    },
  },
  methods: {
    // ログアウトリンク押下
    clickLogout: function () {
      this.$store.dispatch("auth/logout");
      this.$store.dispatch("message/setInfoMessage", {
        message: "ログアウトしました。",
      });
      this.$router.replace("/login");
    },
    // ログインリンク押下
    clickLogin: function () {
      this.$store.dispatch("message/clearMessages");
    },
  },
};
</script>
<style scoped>
.sidebar_component {
  background-color: #212121;
  height: 100%;
  width: 60px;
  transition: width 0.2s;
}
.sidebar_component:hover {
  width: 245px;
}
</style>