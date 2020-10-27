<template>
  <v-app>
    <GlobalNavigationBar />
    <v-main>
      <div>
        <GlobalSubBar />
        <HelloWorld />
      </div>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import GlobalNavigationBar from "./pages/GlobalNavigationBar";
import GlobalSubBar from "./pages/GlobalSubBar";

export default {
  name: "App",
  components: {
    GlobalNavigationBar,
    GlobalSubBar,
    HelloWorld,
  },
};
</script>
<style  scoped>
div {
  display: flex;
}
</style>
