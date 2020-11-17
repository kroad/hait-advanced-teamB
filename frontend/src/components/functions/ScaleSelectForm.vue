<template>
  <v-container>
    <v-row>
      <v-col>
        <v-select
          v-model="myVoice.z_lowest"
          :items="scale_jp"
          label="地声最低音"
          hint="地声で最も低い音を選んでください"
          persistent-hint
          outlined
          :rules="rules"
        >
        </v-select>
      </v-col>
      <v-col>
        <v-select
          v-model="myVoice.z_highest"
          :items="scale_jp"
          label="地声最高音"
          hint="地声で最も高い音を選んでください"
          persistent-hint
          outlined
          :rules="rules"
        >
        </v-select>
      </v-col>
      <v-col>
        <v-select
          v-model="myVoice.u_highest"
          :items="scale_jp"
          label="裏声最高音"
          hint="裏声で最も高い音を選んでください"
          persistent-hint
          outlined
          :rules="rules"
        >
        </v-select>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  data() {
    return {
      rules: [],
    };
  },
  computed: {
    ...mapGetters(["scale_jp", "scale_uni", "myVoice", "myVoiceIndex"]),
  },
};
</script>