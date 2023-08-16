<template>
  <section class="posts">
    <!-- Posts -->
    <post-item v-for="post in posts" :key="post.id" :post="post" :hoverable="true" />
  </section>
</template>

<script>
import PostItem from '@/components/PostItem'
import { inject } from 'vue';

export default {
  components: {
    PostItem
  },
  setup () {
    const posts = inject('posts')
    return {
      posts
    }
  }
}
</script>
