import 'bootstrap/dist/css/bootstrap.css'
import './assets/css/index.css'
import VueHighlightJS from 'vue3-highlightjs'
import 'highlight.js/styles/base16/papercolor-light.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// emitter from mitt
import mitt from 'mitt'
const emitter = mitt()

const app = createApp(App)

app.use(router)
app.use(VueHighlightJS);

app.config.globalProperties.$eventBus = emitter

app.mount('#app')

import 'bootstrap/dist/js/bootstrap.js'

