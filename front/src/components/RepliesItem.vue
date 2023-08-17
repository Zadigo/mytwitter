<template>
  <section class="replies">
    <post-item v-for="reply in replies" :key="reply.id" :post="reply" />
  </section>
</template>

<script>
import { usePosts } from  '../composables/posts'
import { useFeed } from '@/store'

import PostItem from './PostItem.vue'

export default {
  components: {
    PostItem
  },
  setup () {
    const { getCurrentPost } = useFeed()
    const { getReplies, replies } = usePosts()
    return {
      replies,
      getCurrentPost,
      getReplies
    }
  },
  watch: {
    '$route.params.id' (n, o) {
      if (n !== o) {
        this.getCurrentPost(n)
        this.getReplies(n, (replies) => {
          this.$session.create('replies', replies)
        })
      }
    } 
  },
  mounted () {
    this.getReplies (1, (data) => {
      this.$session.create('replies', data)
    })
  }
}
</script>
