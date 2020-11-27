<template>
  <div>
    <div>
      <div class="grid_wrapper" v-if="isLoggedIn">
        <div class="navbar">
          <Navbar />
        </div>
        <div class="subbar">
          <Subbar />
        </div>
        <main>
          <Main />
        </main>
        <footer>
          <Footer />
        </footer>
      </div>
      <div v-else>
        <LoginPage />
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "./Navbar";
import Subbar from "./Subbar";
import Main from "./Main";
import Footer from "./Footer";
import LoginPage from "../pages/LoginPage.vue";
import { mapGetters } from "vuex";

export default {
  name: "Base",
  computed: {
    ...mapGetters("auth", ["isLoggedIn"]),
  },
  components: {
    Navbar,
    Subbar,
    Main,
    Footer,
    LoginPage,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.grid_wrapper {
  display: grid;
  grid-template:
    "... ...... ...... .... ...... ..."
    "... navbar subbar main footer ..." minmax(100vh, 100%)
    "... ...... ...... .... ...... ..."
    / auto auto auto minmax(300px, 1fr) auto auto;
}
.navbar {
  grid-area: navbar;
}
.subbar {
  grid-area: subbar;
}
main {
  grid-area: main;
}
footer {
  grid-area: footer;
}
</style>