import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    // グローバル変数みたいなもの
    state:{
        songs:[],
    },
    // 算出プロパティみたいなもの
    getters:{
        artists: function (state) {
            let artists = [];
            for (let song of state.songs) {
              if (!artists.includes(song.artist_name)) {
                artists.push(song.artist_name);
              }
            }
            return artists;
        },
        songs: state => state.songs,
    },
    mutations:{
        addSongs(state,response){
            state.songs = response.data;
        }
    },
    actions:{
        addSongs(context,response){
            console.log(context);
            console.log(response);
            context.commit("addSongs",response)
        }
    }

});