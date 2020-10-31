import Vue from "vue";
import Router from "vue-router";
import SelectMode from "./components/pages/SelectMode";
import MainResult from "./components/pages/MainResult";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/measure/modes/select", component: SelectMode },
    { path: "/measure/result", component: MainResult },
  ],
});
