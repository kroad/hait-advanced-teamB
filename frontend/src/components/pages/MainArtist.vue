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
                  <v-list-item-title>{{ myVoice.z_highest }}</v-list-item-title>
                  <v-list-item-subtitle>地声最高音</v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-content>
                  <v-list-item-title>{{ myVoice.u_highest }}</v-list-item-title>
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
            <v-tabs v-model="tab" class="elevation-2" dark>
              <v-tabs-slider></v-tabs-slider>
              <v-tab v-for="i in tabs" :key="i" :href="`#tab-${i}`">
                {{ i }}
              </v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab" dark>
              <v-tab-item value="tab-音域内の曲">
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
                    v-for="song in singable"
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
                      {{ song.z_highest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_lowest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_highest_japan }}
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-tab-item>
              <v-tab-item value="tab-キーを変えれば歌える曲">
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
                    v-for="song in singableWithKeyChange"
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
                      {{ song.z_highest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_lowest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_highest_japan }}
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-tab-item>
              <v-tab-item value="tab-音域外の曲">
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
                    v-for="song in unsigable"
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
                      {{ song.z_highest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_lowest_japan }}
                    </v-list-item-content>

                    <v-list-item-content>
                      {{ song.u_highest_japan }}
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-tab-item>
            </v-tabs-items>
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
  data() {
    return {
      tab: null,
      tabs: ["音域内の曲", "キーを変えれば歌える曲", "音域外の曲"],
    };
  },
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
    singable() {
      let singable = [];
      for (let song of this.songsOfArtistUrl) {
        if (
          song.z_lowest_id >= this.myVoiceIndex.z_lowest &&
          song.z_highest_id <= this.myVoiceIndex.z_highest
        ) {
          singable.push(song);
        }
      }
      return singable;
    },
    singableWithKeyChange() {
      let singableWithKeyChange = [];
      let myVoiceRange =
        this.myVoiceIndex.z_highest - this.myVoiceIndex.z_lowest;
      for (let song of this.songsOfArtistUrl) {
        let songVoiceRange = song.z_highest_id - song.z_lowest_id;
        if (myVoiceRange >= songVoiceRange) {
          singableWithKeyChange.push(song);
        }
      }
      // singableに含まれているものは除く
      singableWithKeyChange = singableWithKeyChange.filter(
        (i) => this.singable.indexOf(i) == -1
      );
      return singableWithKeyChange;
    },
    unsigable() {
      let unsigable = [];
      let myVoiceRange =
        this.myVoiceIndex.z_highest - this.myVoiceIndex.z_lowest;
      for (let song of this.songsOfArtistUrl) {
        let songVoiceRange = song.z_highest_id - song.z_lowest_id;
        if (myVoiceRange < songVoiceRange) {
          unsigable.push(song);
        }
      }
      return unsigable;
    },
    myVoiceRange() {
      return this.myVoiceIndex.z_highest - this.myVoiceIndex.z_lowest;
    },
    songVoiceRange() {
      let songVoiceRange = [];
      for (let song of this.songsOfArtistUrl) {
        let voiceRange = song.z_highest_id - song.z_lowest_id;
        songVoiceRange.push(voiceRange);
      }
      return songVoiceRange;
    },
  },
};
</script>