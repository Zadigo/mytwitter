<template>
  <v-card :to="{ name: 'conversation', params: { user: comment.user.username, id: toNumber(comment.id) } }" :color="color">
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
