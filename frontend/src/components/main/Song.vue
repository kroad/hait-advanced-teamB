<template>
  <div>
    <v-container>
      <v-row>
        <v-col>
          <v-btn :to="'/measure/result/' + artistUrl"> 戻る </v-btn>
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
                    {{ songOfSongUrl.artist.name }}
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
                  <v-dialog v-model="dialog1" scrollable max-width="400px">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn color="primary" dark v-bind="attrs" v-on="on" icon>
                        <v-icon>mdi-plus-circle-outline</v-icon>
                      </v-btn>
                    </template>
                    <v-card>
                      <v-card-title
                        >どのプレイリストに追加しますか？
                      </v-card-title>
                      <v-divider></v-divider>
                      <v-card-text style="height: 300px">
                        <v-radio-group
                          v-model="playlistToAdd"
                          column
                          v-for="playlist in playlists"
                          :key="playlist.id"
                        >
                          <v-radio
                            :label="playlist.name"
                            :value="playlist.id"
                          ></v-radio>
                        </v-radio-group>
                      </v-card-text>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="dialog1 = false"
                        >
                          閉じる
                        </v-btn>
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="dialog1 = false"
                          :disabled="!playlistToAdd"
                        >
                          保存
                        </v-btn>
                        <v-btn
                          color="blue darken-1"
                          text
                          @click="dialog2 = !dialog2"
                        >
                          新規プレイリストを作成
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  <v-dialog v-model="dialog2" max-width="500px">
                    <v-card>
                      <v-card-title>
                        <span>新規プレイリスト</span>
                        <v-spacer></v-spacer>
                      </v-card-title>
                      <v-card-text>
                        <v-text-field
                          label="プレイリスト名"
                          v-model="newPlaylist"
                          :rules="[rules.required]"
                        ></v-text-field>
                      </v-card-text>
                      <v-card-actions>
                        <v-btn color="primary" text @click="dialog2 = false">
                          閉じる
                        </v-btn>
                        <v-btn
                          color="primary"
                          text
                          @click="
                            dialog2 = false;
                            dialog1 = false;
                            createPlaylist();
                          "
                          :disabled="!newPlaylist"
                        >
                          保存
                        </v-btn>
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
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
                        {{ songOfSongUrl.artist.name }}
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
import api from "@/services/api";

export default {
  data() {
    return {
      tab: null,
      tabs: ["詳細", "歌詞", "コメント"],
      playlistToAdd: "",
      dialog1: false,
      dialog2: false,
      newPlaylist: "",
      rules: {
        required: (value) => !!value || "Required.",
      },
    };
  },
  props: ["artistUrl", "songUrl"],
  computed: {
    ...mapGetters("karaoke", ["songs"]),
    ...mapGetters("auth", ["playlists", "userId"]),
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
  methods: {
    createPlaylist() {
      api
        .post("/playlist/", {
          name: this.newPlaylist,
          user: this.userId,
          songs: [],
        })
        .then(() => {
          this.$store.dispatch("auth/reload");
        });
    },
  },
};
</script>