<template>
  <div class="row p-3">
    <div class="col-2">
      <b-avatar src="http://via.placeholder.com/200"></b-avatar>
    </div>
    
    <div class="col-10">
      <b-textarea v-model="comment" placeholder="What's new..." id="comment" rows="4"></b-textarea>
    </div>

    <div class="col-12 d-flex justify-content-between">
      <div>
        <v-btn icon><font-awesome-icon icon="image" /></v-btn>
        <v-btn icon><font-awesome-icon icon="smile-beam" /></v-btn>
        <v-btn @click="schedule" icon><font-awesome-icon icon="calendar" /></v-btn>
      </div>
      
      <div>
        <v-btn @click="createItem" :disabled="isDisabled">Répondre</v-btn>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseNewComment',
  props: {
    forReplies: {
      type: Boolean,
      default: false
    },
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
      // Create a new general comment on the
      // global feed
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
          this.$store.commit('feedsModule/setComment', response.data)
          this.comment = null
        })
        .catch((error) => { console.error(error) })
      }
    },
    schedule() {
      this.$store.commit('toggleModal', 'openSchedulingModal')
      this.$emit('scheduleMessage')
    }
  }
}
</script>

<style scoped>
  #comment {
    resize: none;
    background-color: transparent;
    color: white;
    font-size: 1.3rem;
    font-weight: 300;
    border-radius: 0;
    border: none;
  }
  .row {
    border-bottom: 1px solid white;
  }
</style>
