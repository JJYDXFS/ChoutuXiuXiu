import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../App.vue'),
    meta: {
      title: 'Index'
    }
  },
  {
    path: '/MediaProcess',
    component: () => import('../components/MediaProcess.vue'),
    meta: {
      title: 'MediaProcess'
    }
  },
  {
    path: '/FaceRecognition',
    component: () => import('../components/FaceRecognition.vue'),
    meta: {
        title: 'FaceRecognition'
    }
  },
  {
    path: '/FaceLocation',
    component: () => import('../components/FaceLocation.vue'),
    meta: {
        title: 'FaceLocation'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ y: 0 }),
  routes: routes
})

export default router

