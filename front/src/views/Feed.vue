<template>
  <base-layout color="blue darken-1">
    <template>
      <div class="container-fluid">
          <base-new-comment :forReplies="false" />
          <base-comment v-for="(comment, index) in comments" :key="index" :comment="comment" :class="{ 'mt-3': index > 0 }" color="blue darken-1" />
      </div>
    </template>
  </base-layout>
</template>

<script>
import BaseComment from '../components/BaseComment.vue'
import BaseNewComment from '../components/BaseNewComment.vue'
import { mapState } from 'vuex'

export default {
  name: 'Feed',
  components: { BaseComment, BaseNewComment },

  beforeMount() {
    this.$api.feed.getComments()
    .then((response) => {
      this.$store.commit('feedsModule/setComments', response.data)
    })
    .catch((error) => {
      console.error(error)
    })
  },

  computed: {
    ...mapState('feedsModule', [
      'comments'
    ])
  }
}
</script>
