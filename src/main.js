import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import '../node_modules/bulma/css/bulma.css'; // include Bulma CSS
import '../node_modules/zenscroll/zenscroll.js'; // include Zenscroll for smooth scrolling
import '../node_modules/animate.css/animate.css'; // include Animate.CSS for animations

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
