import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import vueDebounce from 'vue-debounce'
import axios from "axios";

Vue.config.productionTip = false
Vue.use(vueDebounce, {
  defaultTime: '800ms'
})

axios.defaults.baseURL = "http://localhost:8000/";

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
