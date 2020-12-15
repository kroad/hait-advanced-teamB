<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-btn to="/measure/result"> 戻る </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card>
            <v-card-title>{{ songsOfArtistUrl[0].artist.name }}</v-card-title>
            <v-card-text>
              あなたの音域で歌える曲だけを表示しています
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <v-card>
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
          <v-card>
            <v-tabs v-model="tab" class="elevation-2">
              <v-tabs-slider></v-tabs-slider>
              <v-tab v-for="i in tabs" :key="i" :href="`#tab-${i}`">
                {{ i }}
              </v-tab>
            </v-tabs>
            <v-tabs-items v-model="tab">
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
                    v-for="song in singableAsItIs"
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
                    <v-list-item-content> 変更すべきキー </v-list-item-content>
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
                      {{ song.keyToChange }}
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
                    v-for="song in unsingable"
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
    ...mapGetters("karaoke", ["songs", "myVoice", "myVoiceIndex"]),
    songsOfArtistUrl() {
      let songsOfArtistUrl = [];
      for (let song of this.songs) {
        if (this.artistUrl == song.artist.name) {
          songsOfArtistUrl.push(song);
        }
      }
      return songsOfArtistUrl;
    },
    singableAsItIs() {
      let singableAsItIs = [];
      for (let song of this.songsOfArtistUrl) {
        if (
          song.z_lowest_id >= this.myVoiceIndex.z_lowest &&
          song.z_highest_id <= this.myVoiceIndex.z_highest
        ) {
          singableAsItIs.push(song);
        }
      }
      return singableAsItIs;
    },
    singableWithKeyChange() {
      let singable = [];
      let myVoiceRange =
        this.myVoiceIndex.z_highest - this.myVoiceIndex.z_lowest;
      for (let song of this.songsOfArtistUrl) {
        let songVoiceRange = song.z_highest_id - song.z_lowest_id;
        if (
          (myVoiceRange >= songVoiceRange &&
            song.z_lowest_id < this.myVoiceIndex.z_lowest) ||
          (myVoiceRange >= songVoiceRange &&
            song.z_highest_id > this.myVoiceIndex.z_highest)
        ) {
          singable.push(song);
        }
      }
      // 変更すべきキーも追加
      let singableWithKeyChange = [];
      for (let song of singable) {
        let high = this.myVoiceIndex.z_highest - song.z_highest_id;
        let low = this.myVoiceIndex.z_lowest - song.z_lowest_id;
        let posiNega = Math.sign(high);
        if (high === low && posiNega === 1) {
          song.keyToChange = "+" + high;
        } else if (high === low && posiNega === -1) {
          song.keyToChange = high;
        } else if (posiNega === 1) {
          song.keyToChange = "+" + low + " ~ +" + high;
        } else {
          song.keyToChange = low + " ~ " + high;
        }
        singableWithKeyChange.push(song);
      }
      return singableWithKeyChange;
    },
    unsingable() {
      let unsingable = [];
      let singable = this.singableAsItIs.concat(this.singableWithKeyChange);
      // singable以外の曲
      unsingable = this.songsOfArtistUrl.filter(
        (i) => singable.indexOf(i) == -1
      );
      return unsingable;
    },
  },
};
</script>