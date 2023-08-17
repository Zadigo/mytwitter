import { loadLayout, scrollToTop } from "@/composables/utils";
import { loadView } from "@/composables/utils";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: scrollToTop(),
  routes: [
    {
      path: '/',
      component: loadLayout('BaseFeed'),
      children: [
        {
          path: '',
          name: 'feed_view',
          component: loadView('FeedView')
        },
        {
          path: '/posts/:id(\\d+)',
          name: 'post_view',
          component: loadView('PostView')
        },
        {
          path: '/users/:id(\\d+)',
          name: 'user_view',
          component: loadView('UserView')
        }
      ]
    }
  ]
})

export default router
