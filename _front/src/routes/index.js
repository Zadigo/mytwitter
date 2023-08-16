import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

var routes = [
    // {
    //     path: '/',
    //     redirect: 'feed',
    //     name: 'home',
    //     component: () => import('../views/Feed.vue')
    // },
    {
        path: '/feed',
        name: 'feed',
        component: () => import('../views/Feed.vue')
    },
    {
        path: '/conversation/:user([a-zA-Z0-9]+)/:id(\\d+)',
        name: 'conversation',
        component: () => import('../views/Conversation.vue')
    },
    {
        path: '/messages',
        name: 'messages',
        component: () => import('../views/DirectMessages.vue')
    },
    {
        path: '/user/:user([a-zA-Z0-0]+)',
        name: 'user',
        component: () => import('../views/User.vue')
    }
]

var router = new Router({
    mode: 'history',
    routes: routes,
    scrollBehavior: () => { window.scrollTo(0, 0) }
})

export default router
