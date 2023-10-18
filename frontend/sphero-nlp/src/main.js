import 'bootstrap/dist/css/bootstrap.css'
import './assets/css/index.css'
import VueHighlightJS from 'vue3-highlightjs'
import 'highlight.js/styles/base16/papercolor-light.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)
app.use(VueHighlightJS);

app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js'

