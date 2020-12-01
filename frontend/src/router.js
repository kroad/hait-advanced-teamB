import Vue from "vue";
import Router from "vue-router";

import ModeChoice from "./components/main/ModeChoice";
import MyvoiceMode from "./components/main/MyvoiceMode";
import SelectMode from "./components/main/SelectMode";
import RecordMode from "./components/main/RecordMode";
import Result from "./components/main/Result";
import Artist from "./components/main/Artist";
import Song from "./components/main/Song";
import LoginResiter from "./components/main/LoginResiter";
import Piano from "./components/main/Piano";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/login", component: LoginResiter },
    { path: "/piano", component: Piano },
    { path: "/measure", component: ModeChoice },
    { path: "/measure/myvoice", component: MyvoiceMode },
    { path: "/measure/select", component: SelectMode },
    { path: "/measure/record", component: RecordMode },
    { path: "/measure/result", component: Result },
    { path: "/measure/result/:artistUrl", component: Artist, props: true },
    {
      path: "/measure/result/:artistUrl/:songUrl",
      component: Song,
      props: true,
    },
  ],
});
