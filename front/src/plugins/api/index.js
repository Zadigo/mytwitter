import authAPI from './auth'
import profileAPI from './profile'
import feedAPI from '../api/feed'
import client from '../../axiosclient'
import directMessages from './dms'

// var subscribeUser = ($axios) => {
//     return (email) => {
//         return $axios({
//             method: 'post',
//             url: '/subscribe',
//             data: { email: email }
//         })
//     }
// }

// var getToken = ($axios) => {
//     return $axios({
//         url: 'auth/token',
//         method: 'get'
//     })
// }

export default {
    auth: authAPI(client),
    feed: feedAPI(client),
    profile: profileAPI(client),
    directMessages: directMessages(client)
}
