import Vue from "vue";
import Router from "vue-router";

import ModeChoice from "./components/pages/ModeChoice";
import MyvoiceMode from "./components/pages/MyvoiceMode";
import SelectMode from "./components/pages/SelectMode";
import RecordMode from "./components/pages/RecordMode";
import MainResult from "./components/pages/MainResult";
import MainArtist from "./components/pages/MainArtist";
import MainSong from "./components/pages/MainSong";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/measure", component: ModeChoice },
    { path: "/measure/myvoice", component: MyvoiceMode },
    { path: "/measure/select", component: SelectMode },
    { path: "/measure/record", component: RecordMode },
    { path: "/measure/result", component: MainResult },
    { path: "/measure/result/:artistUrl", component: MainArtist, props: true },
    {
      path: "/measure/result/:artistUrl/:songUrl",
      component: MainSong,
      props: true,
    },
  ],
});
