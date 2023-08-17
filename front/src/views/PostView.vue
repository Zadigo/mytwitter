<template>
  <section class="post">
    <post-item :post="currentPost" />
    <div class="card shadow-none rounded-0 border-light">
      <div class="card-body">
        <div class="wrapper">
          <p class="fw-light">En réponse à {{ currentPost.userId }}</p>
          <textarea class="form-control" rows="5" cols="33" placeholder="Leave a comment here"></textarea>
          <div class="d-block d-flex justify-content-end shadow-none">
            <button type="button" class="btn btn-primary btn-rounded mt-2">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <replies-item />
  </section>
</template>

<script>
import { loadComponent } from '../composables/utils/index'
import { defineAsyncComponent } from 'vue'
import { mapActions, storeToRefs } from 'pinia'
import { useFeed } from '@/store'

import PostItem from '@/components/PostItem.vue'
import LoadingPostItem from '../components/LoadingPostItem.vue'

export default {
  components: {
    PostItem,
    RepliesItem: defineAsyncComponent({
      loader: loadComponent('RepliesItem'),
      loadingComponent: LoadingPostItem,
      delay: 1000
    })
  },
  setup () {
    const store = useFeed()
    const { currentPost } = storeToRefs(store)
    return {
      store,
      currentPost
    }
  },
  mounted () {
    this.store.getCurrentPost(this.$route.params.id)
  },
  methods: {
    ...mapActions(useFeed, ['getCurrentPost'])
  }
}
</script>

<style scoped>
textarea {
  resize: none;
}
</style>
