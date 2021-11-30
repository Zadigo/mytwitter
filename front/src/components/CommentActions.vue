<template>
  <v-card-actions>
    <v-btn @click="reply" text>
      <v-icon>mdi-comment</v-icon>
      <v-badge :content="comment.replies" overlap></v-badge>
    </v-btn>

    <v-btn @click="like" text>
      <v-icon v-if="comment.liked" color="red darken-3">mdi-heart</v-icon>
      <v-icon v-else>mdi-heart</v-icon>
      <v-badge :content="comment.likes" overlap></v-badge>
    </v-btn>

    <v-btn @click="share" text>
      <v-icon>mdi-share</v-icon>
    </v-btn>
  </v-card-actions>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'CommentActions',
  props: {
    comment: null,
    forReplies: {
      type: Boolean,
      default: false
    }
  },

  computed: {
    ...mapGetters('feedsModule', [
      'numberOfReplies'
    ])
  },

  methods: {
    share() {},
    like() {
      // Like a comment and send the correct method depending
      // if this card is for a comment or a reply
      this.$api.feed.like(this.forReplies, this.comment.id)
      .then(() => {
        this.$store.commit('feedsModule/toggleLike', { forReplies: this.forReplies, id: this.comment.id })
      })
      .catch((error) => { console.error(error) })
    },
    reply() {}
  }
}
</script>
