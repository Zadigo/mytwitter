var _ = require('lodash')

import axios from 'axios'
// import store from './store'

var client = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1/',
    headers: { 'Content-Type': 'application/json' },
    responseType: 'json',
    withCredentials: true
})

client.interceptors.request.use(
    // Before sending any POST requests,
    // especially those that requrie
    // Authorization header, intercep and
    // inject the Authorization Token header
    // to the request.
    request => {
        // There are cases where the user might not
        // be logged in. In which case this can cause
        // an error on the request
        // var token = store.state.authenticationModule.token
        var token = '0398370f47cdd1b81ddfc1400131953bc8a04739'
        if (!_.isNull(token)) {
            request.headers['Authorization'] = `Token ${token}`
        }
        return request
    },

    error => {
        return Promise.reject(error)
    }
)

// client.interceptors.response.use(
//     undefined,
//     error => {
//         // Intercept request errors and those that
//         // return a 401 Unautorized will automatically
//         // logout the user to prevent any issues
//         return new Promise(() => {
//             // if (error.response.status === 401 && error.config && !error.config.__isRetryRequest) {
//             if (error.response.status === 401) {
//                 console.log('Axios', error.response)
//                 store.dispatch('authenticationModule/logout')
//                 window.location.reload()
//             }
//             throw error
//         })
//     }
// )

export default client
