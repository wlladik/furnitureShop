import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import DeliveryView from '../views/DeliveryView.vue'
import ItemsView from '../views/ItemsView.vue'
import OrderView from '../views/OrderView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/delivery',
      name: 'delivery',
      component: DeliveryView
    },
    {
      path: '/items',
      name: 'items',
      component: ItemsView
    },
    {
      path: '/order',
      name: 'order',
      component: OrderView
    },
  ]
})

export default router
