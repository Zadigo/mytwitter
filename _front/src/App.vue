<template>
  <div id="app">
    <v-app>
      <router-view :key="$route.name" />

      <!-- Modals -->
      <modal-new-comment />
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
