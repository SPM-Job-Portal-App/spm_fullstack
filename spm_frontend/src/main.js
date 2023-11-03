/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

// Plugins
import { registerPlugins } from '@/plugins'

// V Calendar
import { setupCalendar, Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/style.css';

// cookies
import VueCookies from 'vue-cookies'

const app = createApp(App)

app.use(setupCalendar, {})
app.use(VueCookies)

if(app.$cookies.get('roleId') == null) {
    app.$cookies.set('roleId', 1, { expires: '1D', path: '/' }) 
    app.$cookies.set('roleTitle', 'Admin', { expires: '1D', path: '/' })
    app.$cookies.set('staffId', 130001, { expires: '1D', path: '/' })
    app.$cookies.set('staffRole', 1, { expires: '1D', path: '/' })
}

// Use the components
app.component('VCalendar', Calendar)
app.component('VDatePicker', DatePicker)

// export const EventBus = new Vue();

registerPlugins(app)

app.mount('#app')
