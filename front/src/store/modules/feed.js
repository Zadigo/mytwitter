var _ = require('lodash')

var directMessages = {
    namespaced: true,

    state: () => ({
        messages: []
    }),

    mutations: {
        setReplies(state, payload) {
            state.messages = payload
        }
    }
}

var feedsModule = {
    namespaced: true,

    state: () => ({
        comments: [],
        replies: []
    }),

    mutations: {
        setComments(state, payload) {
            state.comments = payload
        },

        setReplies(state, payload) {
            state.replies = payload
        },

        toggleLike(state, payload) {
            var isComment = payload.forReplies
            var item = {}
            var items = []
            if (isComment) {
                items = state.comments
            } else {
                items = state.replies
            }
            item = _.find(items, ['id', payload.id])
            item['liked'] = true
        }
    },
    
    getters: {
        getComment(state) {
            return (id) => {
                return _.find(state.comments, ['id', id])
            }
        },

        numberOfReplies(state) {
            return state.replies.length
        }
    },

    modules: {
        directMessages
    }
}

export default feedsModule
