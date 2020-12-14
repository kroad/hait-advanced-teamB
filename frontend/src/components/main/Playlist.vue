<template>
  <v-container>
    <v-btn to="/playlists/"> 戻る </v-btn>
    <v-card>
      {{ name }}
    </v-card>
  </v-container>
</template>
<script>
export default {
  props: ["name"],
};
</script>
