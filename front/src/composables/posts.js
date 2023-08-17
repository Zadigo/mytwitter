import { ref } from 'vue'
import { client } from '../plugins/axios'

export function usePosts () {
  const posts = ref([])
  const replies = ref([])

  async function getReplies (postId, callback) {
    // Get the replies for a given post
    try {
      postId
      const response = await client.get('/posts')
      replies.value = response.data
      if (callback) {
        callback(replies.value)
      }
    } catch (e) {
      console.log(e)
    }
  }

  return {
    posts,
    replies,
    getReplies
  }
}
