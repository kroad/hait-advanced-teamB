<template>
  <v-app>
    <GlobalNavigationBar />
    <v-main>
      <HelloWorld />
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import GlobalNavigationBar from "./pages/GlobalNavigationBar";

export default {
  name: "App",
  components: {
    GlobalNavigationBar,
    HelloWorld,
  },
};
</script>
