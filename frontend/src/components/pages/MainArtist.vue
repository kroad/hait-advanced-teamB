<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-card dark>
            <v-card-title>{{ artistUrl }}</v-card-title>
            <v-card-text>
              あなたの音域で歌える曲だけを表示しています
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card dark>
            <v-card-title> あなたの音域 </v-card-title>
            <v-list>
              <v-list-item two-line>
                <v-list-item-content>
                  <v-list-item-title>{{ myVoice.z_lowest }}</v-list-item-title>
                  <v-list-item-subtitle>地声最低音</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-content>
                  <v-list-item-title>{{
                    myVoice.z_heighest
                  }}</v-list-item-title>
                  <v-list-item-subtitle>地声最高音</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-content>
                  <v-list-item-title>{{
                    myVoice.u_heighest
                  }}</v-list-item-title>
                  <v-list-item-subtitle>裏声最高音</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card dark>
            <v-list>
              <v-list-item>
                <v-list-item-content> 曲名 </v-list-item-content>
                <v-list-item-content> 地声最低音 </v-list-item-content>
                <v-list-item-content> 地声最高音 </v-list-item-content>
                <v-list-item-content> 裏声最低音 </v-list-item-content>
                <v-list-item-content> 裏声最高音 </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item
                link
                v-for="song in songsInRangeOfMyVoice"
                :key="song.id"
                router-link
                :to="'/measure/result/' + artistUrl + '/' + song.title"
              >
                <v-list-item-content>
                  {{ song.title }}
                </v-list-item-content>
                <v-list-item-content>
                  {{ song.z_lowest_japan }}
                </v-list-item-content>

                <v-list-item-content>
                  {{ song.z_heighest_japan }}
                </v-list-item-content>

                <v-list-item-content>
                  {{ song.u_lowest_japan }}
                </v-list-item-content>

                <v-list-item-content>
                  {{ song.u_heighest_japan }}
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn to="/measure/result"> 戻る </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  props: ["artistUrl"],
  computed: {
    ...mapGetters(["songs", "myVoice", "myVoiceIndex"]),
    songsOfArtistUrl() {
      let songsOfArtistUrl = [];
      for (let song of this.songs) {
        if (this.artistUrl == song.artist_name) {
          songsOfArtistUrl.push(song);
        }
      }
      return songsOfArtistUrl;
    },
    songsInRangeOfMyVoice() {
      let songsInRangeOfMyVoice = [];
      for (let song of this.songsOfArtistUrl) {
        if (
          song.z_lowest_id >= this.myVoiceIndex.z_lowest &&
          song.z_heighest_id <= this.myVoiceIndex.z_heighest
        ) {
          songsInRangeOfMyVoice.push(song);
        }
      }
      return songsInRangeOfMyVoice;
    },
  },
};
</script>