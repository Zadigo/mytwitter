<template>
  <div id="app">
    <v-app>
      <router-view :key="$route.name"></router-view>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
</style>
