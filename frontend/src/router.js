import Vue from "vue"
import Router from "vue-router"
import SelectMode from "./components/pages/SelectMode";

Vue.use(Router)

export default new Router({
    mode:"history",
    routes:[
        {path:"/selectmode", component:SelectMode},
    ]
})