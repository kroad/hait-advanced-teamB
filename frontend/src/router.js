import Vue from "vue"
import Router from "vue-router"
import SendToApi from "./components/functions/SendToApi";

Vue.use(Router)

export default new Router({
    mode:"history",
    routes:[
        {path:"/record", component:SendToApi},
    ]
})