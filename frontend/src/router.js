import Vue from "vue";
import Router from "vue-router";
import SelectMode from "./components/pages/SelectMode";
import MainResult from "./components/pages/MainResult";
import MainArtist from "./components/pages/MainArtist";
import MainSong from "./components/pages/MainSong";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/measure/select", component: SelectMode },
    { path: "/measure/result", component: MainResult },
    { path: "/measure/result/:artistUrl", component: MainArtist, props: true },
    {
      path: "/measure/result/:artistUrl/:songUrl",
      component: MainSong,
      props: true,
    },
  ],
});
