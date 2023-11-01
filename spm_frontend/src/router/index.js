// Composables
import { createRouter, createWebHistory } from 'vue-router'
import DefaultLayout from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import OpenRolesStaff from '@/views/OpenRoles_Staff.vue'
import OpenRolesHR from '@/views/OpenRoles_HR.vue'
import ApplyOpenRoles from '@/views/ApplyOpenRoles.vue'
import Unauthorised from '@/views/Unauthorised.vue'
import ViewApplicants from '@/views/ViewApplicants.vue'
import CreateRoleListing from '@/views/CreateRoleListing.vue'
import CancelApplication from '@/components/CancelApplication.vue'
import EditListing from '@/components/EditListing.vue'
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
    component: DefaultLayout,
    meta: { requiresAuth: true, allowedRoles: [1,2] },
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
      {
        path: '/cancel-application/:index',
        name: 'cancel-application',
        component: CancelApplication,
      },
    ],
  },
  {
    path: '/roles/hr',
    component: DefaultLayout,
    meta: { requiresAuth: true, allowedRoles: [1,3,4] },
    children: [
      {
        path: '',
        name: 'Roles HR',
        component: OpenRolesHR,
        meta: { requiresAuth: true, allowedRoles: [1,3,4] },
      },
      {
        path: '/edit-listing/:index',
        name: 'edit-listing',
        component: EditListing,
        meta: { requiresAuth: true, allowedRoles: [1,4] },
      },
      {
        path: '/view-applicants/:id',
        name: 'view-applicants',
        component: ViewApplicants,
        meta: { requiresAuth: true, allowedRoles: [1,3,4] },
      },
    ],
  },
  {
    path: '/createrolelisting',
    component: DefaultLayout,
    meta: { requiresAuth: true, allowedRoles: [1,4] },
    children: [
      {
        path: '',
        name: 'Create Role Listing',
        component: CreateRoleListing,
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
