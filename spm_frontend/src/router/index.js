// Composables
import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import Unauthorised from '@/views/Unauthorised.vue'
import VueCookies from 'vue-cookies'

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
    path: '/unauthorised',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'Unauthorised',
        component: Unauthorised,
      },
    ],
  },
  {
    path: '/openroles/staff',
    component: () => import('@/layouts/default/Default.vue'),
    meta: { requiresAuth: true, allowedRoles: [1,2] },
    children: [
      {
        path: '',
        name: 'Open Roles Staff',
        component: () => import('@/views/OpenRoles_Staff.vue'),
      },
      {
        path: 'apply/:id',
        name: 'Apply Open Roles',
        component: () => import('@/views/ApplyOpenRoles.vue'),
      },
      {
        path: '/cancel-application/:index',
        name: 'cancel-application',
        component: () => import('@/components/CancelApplication.vue'),
      },
    ],
  },
  {
    path: '/roles/hr',
    component: () => import('@/layouts/default/Default.vue'),
    meta: { requiresAuth: true, allowedRoles: [1,3,4] },
    children: [
      {
        path: '',
        name: 'Roles HR',
        component: () => import('@/views/OpenRoles_HR.vue'),
        meta: { requiresAuth: true, allowedRoles: [1,3,4] },
      },
      {
        path: '/edit-listing/:index',
        name: 'edit-listing',
        component: () => import('@/components/EditListing.vue'),
        meta: { requiresAuth: true, allowedRoles: [1,4] },
      },
      {
        path: '/view-applicants/:id',
        name: 'view-applicants',
        component: () => import('@/views/ViewApplicants.vue'),
        meta: { requiresAuth: true, allowedRoles: [1,3,4] },
      },
    ],
  },
  {
    path: '/createrolelisting',
    component: () => import('@/layouts/default/Default.vue'),
    meta: { requiresAuth: true, allowedRoles: [1,4] },
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

router.beforeEach((to, from, next) => {
  const roleId = parseInt(VueCookies.get('roleId'))
  const staffRole = parseInt(VueCookies.get('staffRole'))
  const routeMeta = to.meta;
  
  if (routeMeta.requiresAuth && roleId == undefined) {
    next({ name: 'Unauthorised' });
  } else if (routeMeta.requiresAuth && (!routeMeta.allowedRoles.includes(roleId) || !routeMeta.allowedRoles.includes(staffRole) || roleId != staffRole)) {
    next({ name: 'Unauthorised' }); 
  } else {
    next();
  }
})

export default router
