var _ = require('lodash')

var directMessagesModule = {
    namespaced: true,

    state: () => ({
        messages: []
    }),

    mutations: {
        setDirectMessages(state, payload) {
            // Stores the direct messages of
            // a givent user
            state.messages = payload
        }
    },

    getters: {
        hasMessages(state) {
            // Indicates if there are direct
            // messages
            return state.messages.length > 0
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
            // Stores all the comments
            state.comments = payload
        },

        setComment(state, payload) {
            // Add a newly created comment
            // to the stack
            state.comments.splice(0, 0, payload)
        },

        setReplies(state, payload) {
            // Stores all the replies for
            // the comments
            state.replies = payload
        },

        toggleLike(state, payload) {
            // Toggle the liked flag when
            // the user likes or unlikes an
            // item in the stack
            var item = {}
            var items = []

            if (payload.forReplies) {
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
            // Get a specific comment
            return (id) => {
                return _.find(state.comments, ['id', id])
            }
        },

        numberOfReplies(state) {
            // Get the total number of replies
            return state.replies.length
        },

        hasComments(state) {
            // Indicates if there are a comments
            return state.comments.length > 0
        }
    },

    modules: {
        directMessagesModule
    }
}

export default feedsModule
