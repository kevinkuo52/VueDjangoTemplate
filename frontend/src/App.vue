<template>
  <div id="app">
    <nav-bar/>
    <search-box/>
  </div>
</template>

<script>
import SearchBox from './components/SearchBox.vue'
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    SearchBox
  },
  data() {
    }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
} */
</style>
