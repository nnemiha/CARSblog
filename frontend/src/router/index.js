import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import MovieDetail from '../components/MovieDetail.vue'
import Register from '../components/Register.vue'
import Login from '../components/Login.vue'
import Account from '../components/Account.vue'
import Forum from '../components/Forum.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/movie/:id', component: MovieDetail },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/account', component: Account },
  { path: '/forum', component: Forum },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
