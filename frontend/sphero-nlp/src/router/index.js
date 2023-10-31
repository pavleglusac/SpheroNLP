import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      // dynamic route problem/id
      path: '/problem/:id',
      name: 'problem',
      component: () => import('../views/ProblemView.vue')
    },
    {
      // vjezbanje
      path: '/vje',
      name: 'vjezbanje',
      component: () => import('../views/Vjezbanje.vue')
    },
  ]
})

export default router

