<template>
  <b-modal v-model="openNewCommentModal" :hide-footer="true" centered>
    <div class="row">
      <div class="col-2">
        <b-avatar src="http://via.placeholder.com/100"></b-avatar>
      </div>

      <div class="col-10">
        <b-textarea v-model="comment" placeholder="What's new..." id="comment" rows="4"></b-textarea>
      </div>

      <div class="col-12 d-flex justify-content-between">
        <div>
          <v-btn icon><font-awesome-icon icon="image" /></v-btn>
          <v-btn icon><font-awesome-icon icon="smile-beam" /></v-btn>
          <v-btn icon><font-awesome-icon icon="calendar" /></v-btn>
        </div>
        
        <div>
          <v-btn @click="createItem" :disabled="isDisabled">Répondre</v-btn>
        </div>
      </div>
    </div>
  </b-modal>
</template>

<script>
import newCommentMixin from './newCommentMixin'

export default {
  name: 'ModalNewComment',
  mixins: [newCommentMixin],
  beforeMount() {
    // pass
  },
  computed: {
    openNewCommentModal: {
      get() {
        return this.$store.state.openNewCommentModal
      },
      set() {
        this.$store.commit('toggleModal', 'openNewCommentModal')
      }
    }    
  }
}
</script>
