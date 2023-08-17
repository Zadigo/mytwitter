<template>
  <section class="main">
    <!-- Left -->
    <div class="left-section shadow-sm bg-white">
      <div class="mt-3">
        <router-link :to="{ name: 'feed_view' }" class="btn btn-lg btn-primary btn-rounded btn-block shadow-none my-3">
          <font-awesome-icon :icon="['fs', 'home']" class="me-2" />Feed
        </router-link>
  
        <router-link :to="{ name: 'feed_view' }" class="btn btn-lg btn-primary btn-rounded btn-block shadow-none my-3">
          <font-awesome-icon :icon="['fs', 'magnifying-glass']" class="me-2" />Explorer
        </router-link>
  
        <router-link :to="{ name: 'feed_view' }" class="btn btn-lg btn-primary btn-rounded btn-block shadow-none my-3">
          <font-awesome-icon :icon="['fs', 'bell']" class="me-2" />Notifications
        </router-link>
  
        <router-link :to="{ name: 'feed_view' }" class="btn btn-lg btn-primary btn-rounded btn-block shadow-none my-3">
          <font-awesome-icon :icon="['fs', 'envelope']" class="me-2" />Messages
        </router-link>
  
        <router-link :to="{ name: 'feed_view' }" class="btn btn-lg btn-primary btn-rounded btn-block shadow-none my-3">
          <font-awesome-icon :icon="['fs', 'user']" class="me-2" />Profil
        </router-link>
      </div>
    </div>

    <!-- Middle -->
    <div class="middle bg-light position-relative">
      <router-view></router-view>
      <button v-if="isFeed" id="reply" type="button" class="btn btn-rounded btn-primary btn-lg">Reply</button>
    </div>

    <!-- Right -->
    <div class="right-section shadow-sm bg-white">c</div>
  </section>
</template>

<script>
import { storeToRefs } from 'pinia'
import { useFeed } from '@/store'
import { provide } from 'vue'

export default {
  setup () {
    const store = useFeed()
    const { posts } = storeToRefs(store)
    provide('posts', posts)
    return {
      store,
      posts
    }
  },
  computed: {
    isFeed () {
      return this.$route.name === 'feed_view'
    }
  },
  created () {
    this.getPosts()
  },
  mounted () {
    document.body.classList.add('bg-light')
  },
  unmounted () {
    document.body.classList.remove('bg-light')
  },
  methods: {
    async getPosts () {
      try {
        if (this.$session.exists('posts')) {
          this.store.loadFromCache()
        } else {
          const response = await this.$http.get('/posts')
          this.posts = response.data
          this.$session.create('posts', this.posts)
          this.$session.create('expiry', null)
        }
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
