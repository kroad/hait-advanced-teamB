<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4">
        <Result />
      </v-col>
      <v-col>
        <SongForm />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import SongForm from "./SongForm";
import Result from "./Result";

export default {
  name: "HelloWorld",
  components: { SongForm, Result },
};
</script>
