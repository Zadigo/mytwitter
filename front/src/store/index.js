import _ from 'lodash'
import { defineStore } from 'pinia'

const useFeed = defineStore('feed', {
  state: () => ({
    posts: [],
    currentPost: {},
    currentPostReplies: []
  }),

  actions: {
    loadFromCache () {
      if (this.posts.length === 0) {
        this.posts = this.$session.retrieve('posts')
      }
    },
    getCurrentPost (id) {
      this.loadFromCache()
      this.currentPost = _.find(this.posts, ['id', id * 1]) || {}
    }
  }
})

export {
  useFeed
}
