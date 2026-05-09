// router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TaskView from '../views/TaskView.vue'
import BoringView from '../views/BoringView.vue'

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/tasks', name: 'Tasks', component: TaskView },
  { path: '/borings', name: 'Borings', component: BoringView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
