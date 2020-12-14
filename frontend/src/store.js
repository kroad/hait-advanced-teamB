import Vue from "vue";
import Vuex from "vuex";
import api from "@/services/api";

Vue.use(Vuex);

// カラオケアプリに必要な情報
const karaokeModule = {
  strict: process.env.NODE_ENV !== "production",
  namespaced: true,
  // グローバル変数みたいなもの
  state: {
    songs: [],
    prob_and_artists: [],
    myVoice: {
      z_lowest: "",
      z_highest: "",
      u_highest: "",
    },
    scale_jp: [
      "lowlowA",
      "lowlowA#",
      "lowlowB",
      "lowlowC",
      "lowlowC#",
      "lowlowD",
      "lowlowD#",
      "lowlowE",
      "lowlowF",
      "lowlowF#",
      "lowlowG",
      "lowlowG#",
      "lowA",
      "lowA#",
      "lowB",
      "lowC",
      "lowC#",
      "lowD",
      "lowD#",
      "lowE",
      "lowF",
      "lowF#",
      "lowG",
      "lowG#",
      "mid1A",
      "mid1A#",
      "mid1B",
      "mid1C",
      "mid1C#",
      "mid1D",
      "mid1D#",
      "mid1E",
      "mid1F",
      "mid1F#",
      "mid1G",
      "mid1G#",
      "mid2A",
      "mid2A#",
      "mid2B",
      "mid2C",
      "mid2C#",
      "mid2D",
      "mid2D#",
      "mid2E",
      "mid2F",
      "mid2F#",
      "mid2G",
      "mid2G#",
      "hiA",
      "hiA#",
      "hiB",
      "hiC",
      "hiC#",
      "hiD",
      "hiD#",
      "hiE",
      "hiF",
      "hiF#",
      "hiG",
      "hiG#",
      "hihiA",
      "hihiA#",
      "hihiB",
      "hihiC",
      "hihiC#",
      "hihiD",
      "hihiD#",
      "hihiE",
      "hihiF",
      "hihiF#",
      "hihiG",
      "hihiG#",
      "hihihiA",
      "hihihiA#",
      "hihihiB",
      "hihihiC",
      "hihihiC#",
      "hihihiD",
      "hihihiD#",
      "hihihiE",
      "hihihiF",
      "hihihiF#",
      "hihihiG",
      "hihihiG#",
      "hihihihiA",
      "hihihihiA#",
      "hihihihiB",
      "hihihihiC",
    ],
    scale_uni: [
      "A0",
      "A#0",
      "B0",
      "C1",
      "C#1",
      "D1",
      "D#1",
      "E1",
      "F1",
      "F#1",
      "G1",
      "G#1",
      "A1",
      "A#1",
      "B1",
      "C2",
      "C#2",
      "D2",
      "D#2",
      "E2",
      "F2",
      "F#2",
      "G2",
      "G#2",
      "A2",
      "A#2",
      "B2",
      "C3",
      "C#3",
      "D3",
      "D#3",
      "E3",
      "F3",
      "F#3",
      "G3",
      "G#3",
      "A3",
      "A#3",
      "B3",
      "C4",
      "C#4",
      "D4",
      "D#4",
      "E4",
      "F4",
      "F#4",
      "G4",
      "G#4",
      "A4",
      "A#4",
      "B4",
      "C5",
      "C#5",
      "D5",
      "D#5",
      "E5",
      "F5",
      "F#5",
      "G5",
      "G#5",
      "A5",
      "A#5",
      "B5",
      "C6",
      "C#6",
      "D6",
      "D#6",
      "E6",
      "F6",
      "F#6",
      "G6",
      "G#6",
      "A6",
      "A#6",
      "B6",
      "C7",
      "C#7",
      "D7",
      "D#7",
      "E7",
      "F7",
      "F#7",
      "G7",
      "G#7",
      "A7",
      "A#7",
      "B7",
      "C8",
    ],
  },

  // 算出プロパティみたいなもの
  getters: {
    myVoiceIndex: (state) => {
      let z_lowest = state.scale_jp.indexOf(state.myVoice.z_lowest) + 1;
      let z_highest = state.scale_jp.indexOf(state.myVoice.z_highest) + 1;
      let u_highest = state.scale_jp.indexOf(state.myVoice.u_highest) + 1;
      return {
        z_lowest,
        z_highest,
        u_highest,
      };
    },
    songs: (state) => state.songs,
    prob_and_artists: (state) => state.prob_and_artists,
    scale_jp: (state) => state.scale_jp,
    scale_uni: (state) => state.scale_uni,
    myVoice: (state) => state.myVoice,
  },

  mutations: {
    storeSongs(state, response) {
      state.songs = response.data[1];
    },
    storeProbAndArtists(state, response) {
      state.prob_and_artists = response.data[0];
    },
  },

  actions: {
    storeSongs(context, response) {
      context.commit("storeSongs", response);
    },
    storeProbAndArtists(context, response) {
      context.commit("storeProbAndArtists", response);
    },
  },
};

// 認証情報
const authModule = {
  strict: process.env.NODE_ENV !== "production",
  namespaced: true,
  state: {
    username: "",
    playlists: "",
    isLoggedIn: false,
  },
  getters: {
    username: (state) => state.username,
    playlists: (state) => state.playlists,
    isLoggedIn: (state) => state.isLoggedIn,
  },
  mutations: {
    set(state, payload) {
      state.username = payload.user.username;
      state.playlists = payload.user.playlist_set;
      state.isLoggedIn = true;
    },
    clear(state) {
      state.username = "";
      state.isLoggedIn = false;
    },
  },
  actions: {
    /**
     * 新規登録
     */
    register(context, payload) {
      return api
        .post("/auth/users/", {
          username: payload.username,
          password: payload.password1,
          re_password: payload.password2,
        })
        .then(() => {
          context.dispatch("login", {
            username: payload.username,
            password: payload.password1,
          });
        });
    },
    /**
    /**
     * ログイン
     */
    login(context, payload) {
      return api
        .post("/auth/jwt/create/", {
          username: payload.username,
          password: payload.password,
        })
        .then((response) => {
          // 認証用トークンをlocalStorageに保存
          localStorage.setItem("access", response.data.access);
          // ユーザー情報を取得してstoreのユーザー情報を更新
          return context.dispatch("reload");
        });
    },
    /**
     * ログアウト
     */
    logout(context) {
      // 認証用トークンをlocalStorageから削除
      localStorage.removeItem("access");
      // storeのユーザー情報をクリア
      context.commit("clear");
    },
    /**
     * ユーザー情報更新
     */
    reload(context) {
      return api.get("/auth/users/me/").then((response) => {
        const user = response.data;
        console.log(user);
        // storeのユーザー情報を更新
        context.commit("set", { user: user });
      });
    },
  },
};

// グローバルメッセージ
const messageModule = {
  strict: process.env.NODE_ENV !== "production",
  namespaced: true,
  state: {
    error: "",
    warnings: [],
    info: "",
  },
  getters: {
    error: (state) => state.error,
    warnings: (state) => state.warnings,
    info: (state) => state.info,
  },
  mutations: {
    set(state, payload) {
      if (payload.error) {
        state.error = payload.error;
      }
      if (payload.warnings) {
        state.warnings = payload.warnings;
      }
      if (payload.info) {
        state.info = payload.info;
      }
    },
    clear(state) {
      state.error = "";
      state.warnings = [];
      state.info = "";
    },
  },
  actions: {
    /**
     * エラーメッセージ表示
     */
    setErrorMessage(context, payload) {
      context.commit("clear");
      context.commit("set", { error: payload.message });
    },
    /**
     * 警告メッセージ（複数）表示
     */
    setWarningMessages(context, payload) {
      context.commit("clear");
      context.commit("set", { warnings: payload.messages });
    },
    /**
     * インフォメーションメッセージ表示
     */
    setInfoMessage(context, payload) {
      context.commit("clear");
      context.commit("set", { info: payload.message });
    },
    /**
     * 全メッセージ削除
     */
    clearMessages(context) {
      context.commit("clear");
    },
  },
};

const store = new Vuex.Store({
  modules: {
    karaoke: karaokeModule,
    auth: authModule,
    message: messageModule,
  },
});

export default store;
