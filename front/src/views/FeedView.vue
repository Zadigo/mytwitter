<template>
  <section class="posts">
    <!-- <loading-post-item></loading-post-item> -->
    <!-- Posts -->
    <post-item v-for="post in posts" :key="post.id" :post="post" :hoverable="true" />
  </section>
</template>

<script>
import { inject } from 'vue'

import PostItem from '@/components/PostItem'
// import LoadingPostItem from '@/components/LoadingPostItem.vue'

export default {
  components: {
    PostItem,
    // LoadingPostItem
  },
  setup () {
    const posts = inject('posts')
    return {
      posts
    }
  }
}
</script>
