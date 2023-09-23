// Composables
import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import OpenRoles from '@/views/OpenRoles.vue'
import ApplyOpenRoles from '@/views/ApplyOpenRoles.vue'
import Candidates from '@/views/Candidates.vue'
import Settings from '@/views/Settings.vue'

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
      },
    ],
  },
  {
    path: '/openroles',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Open Roles',
        component: OpenRoles,
      },
      {
        path: 'apply',
        name: 'Apply Open Roles',
        component: ApplyOpenRoles,
      },
    ],
  },
  {
    path: '/candidates',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Candidates',
        component: Candidates,
      },
    ],
  },
  {
    path: '/settings',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Settings',
        component: Settings,
      },
    ],
  },
  {
    path: '/createrolelisting',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Create Role Listing',
        component: () => import('@/views/CreateRoleListing.vue'),
      },
    ],
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
