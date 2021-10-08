import Vue from 'vue'
import App from './App.vue'

// Store + Router
import router from './routes'
import store from './store'

// Styling
require('../node_modules/bootstrap/dist/css/bootstrap.min.css')

// Plugins
import globalPlugin from './plugins'
import vuetify from './plugins/vuetify'

// Components
import BaseLayout from './components/BaseLayout.vue'

Vue.config.productionTip = false

// Plugins
Vue.use(globalPlugin)

// Components
Vue.component('base-layout', BaseLayout)

new Vue({
  router,
  store,
  vuetify,

  render: h => h(App),
}).$mount('#app')
