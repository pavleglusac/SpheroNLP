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
      path: '/lessons',
      name: 'lessons',
      component: () => import('../views/LessonsView.vue')
    },
    {
      // dynamic route problem/id
      path: '/problem/:chapter_id/:task_id',
      name: 'problem',
      component: () => import('../views/ProblemView.vue')
    },
    {
      // vjezbanje
      path: '/vje',
      name: 'vjezbanje',
      component: () => import('../views/Vjezbanje.vue')
    },
    {
      // vjezbanje
      path: '/about',
      name: 'about',
      component: () => import('../views/About.vue')
    },
  ]
})

export default router

