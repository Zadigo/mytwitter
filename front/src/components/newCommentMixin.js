export default {
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
                    this.$store.commit('closeModal')
                    this.comment = null
                })
                .catch((error) => { console.error(error) })
            } else {
                this.$api.feed.createComment(this.comment)
                .then((response) => {
                    this.$store.commit('feedsModule/setComment', response.data)
                    this.$store.commit('closeModal')
                    this.comment = null
                })
                .catch((error) => { console.error(error) })
            }
        }
    }
}
