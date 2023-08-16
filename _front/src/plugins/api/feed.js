export default ($axios) => ({
    getComments: () => {
        return $axios({
            method: 'get',
            url: '/conversations'
        })
    },

    getComment: (id) => {
        return $axios({
            method: 'get',
            url: `/conversations/${id}`
        })
    },

    createComment: (comment) => {
        return $axios({
            method: 'post',
            url: '/conversations/create',
            data: { text: comment }
        })
    },

    deleteComment: ($axios) => {
        return (id) => {
            return $axios({
                method: 'delete',
                url: `/conversations/${id}/delete`
            })
        }
    },

    deleteReply: () => {
        return (id) => {
            $axios({
                method: 'delete',
                url: `/replies/${id}/delete`
            })
        }
    },
    
    createReply: (commentId, comment) => {
        return $axios({
            method: 'post',
            url: `/conversations/${commentId}/replies/create`,
            data: { text: comment }
        })
    },

    like: (forReplies, itemId) => {
        var elementType = forReplies ? 'replies' : 'conversations'
        return $axios({
            method: 'post',
            url: `/${elementType}/${itemId}/vote`
        })
    },

    getReplies: (id) => {
        return $axios({
            method: 'get',
            url: `/conversations/${id}/replies`
        })
    }
})

// `/user/${user}/follow`
// `/user/${user}/unfollow`
