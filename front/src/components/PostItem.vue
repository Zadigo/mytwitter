<template>
  <article :class="{'article-list': hoverable }" class="card shadow-none border-light rounded-0 p-4">
    <div class="card-header d-flex justify-content-between align-items-center border-0">
      <div class="d-flex justify-content-left align-items-center gap-4">
        <router-link :to="{ name: 'user_view', params: { id: post.userId } }" class="d-block link-dark d-flex justify-content-left align-items-center gap-4">
          <img src="https://placehold.co/70x70" alt="" class="img-fluid rounded-circle">
          <div class="infos">
            <p class="fw-bold m-0 username">Username</p>
            <p class="fw-lighter fs-6 m-0">@Username</p>
          </div>
        </router-link>
      </div>
      <button type="button" class="btn btn-light btn-floating">
        <font-awesome-icon :icon="['fas', 'ellipsis-vertical']" />
      </button>
    </div>

    <router-link :to="{ name: 'post_view', params: { id: post.id } }" class="link-dark">
      <div class="card-body px-5">
        <p class="card-text fw-light">
          {{ post.body }}
        </p>

        <img src="https://placehold.co/800x800" class="img-fluid" alt="">
      </div>
    </router-link>

    <div class="card-footer d-flex justify-content-around border-0 px-1">
      <button type="button" class="btn btn-light btn-rounded">
        <font-awesome-icon :icon="['fas', 'comment']" class="me-3" />1,75K
      </button>

      <button type="button" class="btn btn-light btn-rounded">
        <font-awesome-icon :icon="['fas', 'arrows-rotate']" class="me-3" />1,75K
      </button>
      
      <button type="button" class="btn btn-light btn-rounded">
        <font-awesome-icon :icon="['fas', 'heart']" class="me-3" />8,75K
      </button>
      
      <button type="button" class="btn btn-light btn-rounded">
        <font-awesome-icon :icon="['fas', 'chart-simple']" class="me-3" />3,75K
      </button>
      
      <button type="button" class="btn btn-light btn-rounded">
        <font-awesome-icon :icon="['fas', 'share']" class="me-3" />7,7K
      </button>
    </div>
  </article>
</template>

<script>
import { storeToRefs } from 'pinia'
import { useFeed } from '../store'

export default {
  props: {
    hoverable: {
      type: Boolean,
      default: false
    },
    post: {
      type: Object,
      required: true
    }
  },
  setup () {
    const store = useFeed()
    const { currentPostReplies } = storeToRefs(store)
    return {
      currentPostReplies,
      store
    }
  },
  beforeMount () {
    this.getReplies()
  },
  methods: {
    async getReplies () {
      this.currentPostReplies = []
    }
  }
}
</script>

<style scoped>
article {
  transition: all .3s ease-in-out;
}

.article-list:hover {
  cursor: pointer;
  background-color: rgb(251, 251, 251)
}
</style>
