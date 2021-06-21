import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../pages/index.vue'),
    meta: {
      title: 'Index'
    }
  },
  {
    path: '/VideoFaceRe',
    component: () => import('../components/VideoFaceRe.vue'),
    meta: {
      title: 'VideoFaceRe'
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
  },
  {
    path: '/WearHat',
    component: () => import('../components/WearHat.vue'),
    meta: {
        title: 'WearHat'
    }
  },
  {
    path: '/Makeup',
    component: () => import('../components/Makeup.vue'),
    meta: {
        title: 'Makeup'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  scrollBehavior: () => ({ y: 0 }),
  routes: routes
})

export default router

