import Vue from 'vue'
import Vuex from 'vuex'
import feedsModule from './modules/feed'

Vue.use(Vuex)

var store = new Vuex.Store({    
    state: () => ({
        authenticated: false,
        token: null,
        openNewCommentModal: false,
        openSchedulingModal: false
    }),

    mutations: {
        toggleModal(state, name) {
            // Toggle the modal for creating
            // a new comment
            state[name] = !state[name]
        },
        closeModal(state, name) {
            // Close the modal -; for functions that
            // do not require toggling with the state
            state[name] = false
        }
    },
    
    modules: {
        feedsModule
    }
})

export default store
