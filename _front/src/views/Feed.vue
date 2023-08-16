<template>
  <base-layout color="blue darken-4">
    <template>
      <base-new-comment :forReplies="false" />

      <div v-if="hasComments" id="comments">
        <transition-group>
          <base-comment v-for="(comment, index) in comments" :key="index" :comment="comment" :class="{ 'mt-3': index > 0 }" color="blue darken-1" />        
        </transition-group>

        <!-- Modals -->
        <scheduling />
      </div>

      <div class="p-4" id="comments" v-else>
        There are no comments. Please follow some people if you want
        to populate your feed
      </div>
    </template>
  </base-layout>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import BaseComment from '../components/BaseComment.vue'
import BaseNewComment from '../components/BaseNewComment.vue'
import Scheduling from '../components/modals/Scheduling.vue'

export default {
  name: 'Feed',
  components: { BaseNewComment, BaseComment, Scheduling },
  
  beforeMount() {
    // Get all the comments for the
    // current timeline
    this.$api.feed.getComments()
    .then((response) => {
      this.$store.commit('feedsModule/setComments', response.data)
    })
    .catch((error) => {
      console.error(error)
    })
  },

  computed: {
    ...mapState('feedsModule', ['comments']),
    ...mapGetters('feedsModule', ['hasComments'])
  }
}
</script>
