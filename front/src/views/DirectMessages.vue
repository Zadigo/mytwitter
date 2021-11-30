<template>
  <base-layout color="blue darken-1">
    <template>
      Nothing
    </template>
  </base-layout>
</template>

<script>
export default {
  name: 'DirectMessages',
  beforeMount() {
    this.$api.directMessages.get(1)
    .then((response) => {
      this.$store.commit('directMessagesModule/setDirectMessages', response.payload)
    })
    .catch((error) => {
      console.error(error)
    })
  }
}
</script>
