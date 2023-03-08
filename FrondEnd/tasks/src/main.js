import { createApp } from 'vue'

import App from './App.vue'

import Notifications from '@kyvg/vue3-notification'

import "bootstrap/dist/css/bootstrap.min.css"

import router from './router'

createApp(App).use(router).use(Notifications).mount('#app')

