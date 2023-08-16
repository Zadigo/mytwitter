import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import App from './App.vue'

// Store + Router
import router from './routes'
import store from './store'

// Mixins
import globalMixin from './mixins'

// Styling
import './plugins/fontawesome'
import './plugins/bootstrap-vue'

// Plugins
import globalPlugin from './plugins'
import vuetify from './plugins/vuetify'

// Components
import BaseLayout from './components/BaseLayout.vue'
import ModalNewComment from './components/ModalNewComment.vue'

Vue.config.productionTip = false

// Plugins
Vue.use(globalPlugin)

// Mixins
Vue.mixin(globalMixin)

// Components
Vue.component('base-layout', BaseLayout)
Vue.component('modal-new-comment', ModalNewComment)

new Vue({
  router,
  store,
  vuetify,

  render: h => h(App),
}).$mount('#app')
