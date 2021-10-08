<template>
  <base-layout color="blue darken-1">
    <template>
      <div class="container-fluid">
        <header>
          <base-comment :comment="comment" :foReplies="false" color="blue lighten-1" />
        </header>

        <v-divider></v-divider>

        <base-new-comment :forReplies="true" :commentId="$route.params.id" />

        <div v-if="replies.length > 0"  id="replies">
          <base-comment v-for="(reply, index) in replies" :key="index" :comment="reply" :forReplies="true" :class="{ 'mt-2': index > 0 }" />
        </div>

      </div>
    </template>
  </base-layout>
</template>

<script>
import BaseComment from '../components/BaseComment.vue'
import { mapState } from 'vuex'
import BaseNewComment from '../components/BaseNewComment.vue'

export default {
  name: 'Conversation',
  components: { BaseComment, BaseNewComment },

  data() {
    return {
      comment: {}
    }
  },

  beforeRouteEnter (to, from, next) {
    next(vm => {
      vm.getComment(vm.$route.params['id'])
    })
  },

  mounted() {
    this.getComment(this.$route.params['id'])

    this.$api.feed.getReplies(this.$route.params['id'])
    .then((response) => {
      this.$store.commit('feedsModule/setReplies', response.data)
    })
    .catch((error) => {
      console.error(error)
    })
  },

  computed: {
    ...mapState('feedsModule', [
      'replies'
    ])
  },

  methods: {
    getComment(id) {
      this.comment = this.$store.getters['feedsModule/getComment'](id)
    }
  }
}
</script>
