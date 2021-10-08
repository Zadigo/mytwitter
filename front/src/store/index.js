import Vue from 'vue'
import Vuex from 'vuex'
import feedsModule from './modules/feed'

Vue.use(Vuex)

var store = new Vuex.Store({    
    state: () => ({
        authenticated: false,
        token: null
    }),

    mutations: {
        setFeed(state) {
            state
        }
    },
    
    modules: {
        feedsModule
    }
})

export default store
