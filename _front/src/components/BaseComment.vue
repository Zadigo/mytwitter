<template>
  <v-card :to="{ name: 'conversation', params: { user: comment.user.username, id: toNumber(comment.id) } }" :color="color" class="p-2">
    <v-card-title>
      {{ comment.user.username }}
    </v-card-title>
    
    <v-card-text>
      {{ comment.text }}
    </v-card-text>

    <comment-actions :forReplies="forReplies" :comment="comment" :likes="comment.likes" :replies="comment.replies" />
  </v-card>
</template>

<script>
import CommentActions from '../components/CommentActions.vue'

export default {
  name: 'BaseComment',
  props: {
    color: String,
    comment: {
      type: Object,
      default: () => { return {} }
    },
    forReplies: Boolean
  },
  components: { CommentActions },
  methods: {
    toNumber(value) {
      return parseInt(value)
    }
  }
}
</script>

<style scoped>
  #comment {
    border-bottom: 1px solid white;
    color: white;
  }
  .v-card {
    border-radius: 0;
  }
</style>
