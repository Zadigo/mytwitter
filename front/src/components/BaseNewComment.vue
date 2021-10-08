<template>
  <v-sheet class="my-5">
    <div class="row">
      <div class="col-3">
        <v-img src="http://via.placeholder.com/100" avatar></v-img>
      </div>
      
      <div class="col-auto">
        <v-text-field v-model="comment" type="textarea"></v-text-field>
      </div>

      <div class="col-12">
        <v-btn @click="createItem" :disabled="isDisabled">Répondre</v-btn>
      </div>
    </div>
  </v-sheet>
</template>

<script>
export default {
  name: 'BaseNewComment',
  props: {
    forReplies: Boolean,
    commentId: {
      type: Number,
      required: false
    }
  },

  data() {
    return {
      comment: null
    }
  },

  computed: {
    isDisabled() {
      return this.comment === null | this.comment === '' ? true : false
    }
  },

  methods: {
    createItem() {
      if (this.forReplies) {
        this.$api.feed.createReply(this.commentId, this.comment)
        .then((response) => {
          this.$store.commit('feedsModule/setReplies', response.data)
          this.comment = null
        })
        .catch((error) => { console.error(error) })
      } else {
        this.$api.feed.createComment(this.comment)
        .then((response) => {
          this.$store.commit('feedsModule/setComments', response.data)
          this.comment = null
        })
        .catch((error) => { console.error(error) })
      }
    }
  }
}
</script>
