<template>
  <v-card-actions>
    <v-btn @click="reply" text>
        <v-icon>mdi-comment</v-icon><v-badge overlap>
        {{ replies == 0 ? numberOfReplies : replies }}
      </v-badge>
    </v-btn>

    <v-btn @click="like" text>
      <v-icon v-if="comment.liked" color="red darken-1">mdi-heart</v-icon>
      <v-icon v-else>mdi-heart</v-icon>
      <v-badge overlap>{{ likes }}</v-badge>
    </v-btn>
    <v-btn @click="share" text><v-icon>mdi-share </v-icon></v-btn>
  </v-card-actions>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'CommentActions',
  props: {
    likes: {
      type: Number,
      default: 0
    },
    replies: {
      type: Number,
      default: 0
    },
    comment: null,
    forReplies: Boolean
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
