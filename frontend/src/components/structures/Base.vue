<template>
  <div class="grid_wrapper">
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
</template>

<script>
import Navbar from "./Navbar";
import Subbar from "./Subbar";
import Main from "./Main";
import Footer from "./Footer";
export default {
  name: "Base",
  components: {
    Navbar,
    Subbar,
    Main,
    Footer,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.grid_wrapper {
  display: grid;
  grid-template:
    "... ...... ...... .... ...... ..."
    "... navbar subbar main footer ..." 100vh
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