import { createApp, markRaw } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { createPinia } from 'pinia'
import { createAxios } from './plugins/axios'

import App from './App.vue'
import router from './router'

import '@/plugins/fontawesome'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'mdb-ui-kit/css/mdb.min.css'
import { createVueSession } from './plugins/vue-storages'

const app = createApp(App)
const session = createVueSession()
const pinia = createPinia()
pinia.use(({ store }) => {
  store.$session = markRaw(session)
})
app.use(session)
app.use(pinia)
app.use(router)
app.use(createAxios())
app.component('FontAwesomeIcon', FontAwesomeIcon)
app.mount('#app')
