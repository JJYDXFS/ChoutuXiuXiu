import { createApp } from 'vue';
import App from './App.vue';
// import "./index.scss";
import router from "./router/index";
import ElementPlus from 'element-plus';

import "element-theme-ink";

import './index.css'

// 使用element-ui
const app = createApp(App)
app.use(ElementPlus).use(router);
// app.use(ElementPlus).use(router);
// 挂载根组件App.vue
app.mount('#app')
