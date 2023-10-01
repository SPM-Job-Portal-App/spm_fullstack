// Composables
import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import OpenRolesStaff from '@/views/OpenRoles_Staff.vue'
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
    path: '/openroles/staff',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Open Roles Staff',
        component: OpenRolesStaff,
      },
      {
        path: 'apply/:id',
        name: 'Apply Open Roles',
        component: ApplyOpenRoles,
      },
    ],
  },
  {
    path: '/openroles/hr',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Open Roles HR',
        component: () => import('@/views/OpenRoles_HR.vue'),
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
  {
    path: '/edit-listing/:index', // Define a route parameter :index
    name: 'edit-listing',
    component: () => import('@/components/EditListing.vue'),
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
