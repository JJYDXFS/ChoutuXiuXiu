import { createApp } from 'vue'
import ElementPlus from 'element-plus'

import App from './App.vue'
import './index.css'

// 使用element-ui
const app = createApp(App)
app.use(ElementPlus);
// 挂载根组件App.vue
app.mount('#app')
