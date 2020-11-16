<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-btn router-link :to="'/measure/result/' + artistUrl"> 戻る </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card>
            <v-container>
              <v-row>
                <v-col>
                  <v-card-title class="headline">
                    {{ songOfSongUrl.title }}
                  </v-card-title>
                  <v-card-subtitle>
                    {{ songOfSongUrl.artist_name }}
                  </v-card-subtitle>
                </v-col>
              </v-row>
              <v-row>
                <v-spacer></v-spacer>
                <v-col cols="2">
                  <v-icon>mdi-thumb-up-outline</v-icon>
                </v-col>
                <v-col cols="2">
                  <v-icon>mdi-thumb-down-outline</v-icon>
                </v-col>
                <v-col cols="2">
                  <v-icon>mdi-plus-circle-outline</v-icon>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>

      <v-row>
        <v-col>
          <v-card>
            <v-tabs v-model="tab" class="elevation-2">
              <v-tabs-slider></v-tabs-slider>
              <v-tab v-for="i in tabs" :key="i" :href="`#tab-${i}`">
                {{ i }}
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item value="tab-詳細">
                <v-list v-if="songOfSongUrl">
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ songOfSongUrl.artist_name }}
                      </v-list-item-title>
                      <v-list-item-subtitle>
                        アーティスト名
                      </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ songOfSongUrl.z_lowest_japan }}
                      </v-list-item-title>
                      <v-list-item-subtitle> 地声最低音 </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ songOfSongUrl.z_highest_japan }}
                      </v-list-item-title>
                      <v-list-item-subtitle> 地声最高音 </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title>
                        {{ songOfSongUrl.u_highest_japan }}
                      </v-list-item-title>
                      <v-list-item-subtitle> 裏声最高音 </v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-tab-item>

              <v-tab-item value="tab-歌詞">
                <v-card>
                  <v-card-text> 歌詞 </v-card-text>
                </v-card>
              </v-tab-item>

              <v-tab-item value="tab-コメント">
                <v-card>
                  <v-card-text> コメント </v-card-text>
                </v-card>
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
  data() {
    return {
      tab: null,
      tabs: ["詳細", "歌詞", "コメント"],
    };
  },
  props: ["artistUrl", "songUrl"],
  computed: {
    ...mapGetters(["songs"]),
    songOfSongUrl() {
      let songOfSongUrl;
      for (let song of this.songs) {
        if (this.songUrl == song.title) {
          songOfSongUrl = song;
        }
      }
      return songOfSongUrl;
    },
  },
};
</script>