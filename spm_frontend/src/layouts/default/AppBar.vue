<template>
  <v-app-bar class="app-bar" flat app>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-icon class="ml-5" icon="mdi-circle-slice-4" />
    <v-toolbar-title>{{ currentRole.roleTitle }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon="mdi-help-circle"></v-btn>
    <v-btn icon="mdi-bell"></v-btn>
    <v-btn icon>
      <v-icon>mdi-account-circle</v-icon>
      <v-menu activator="parent">
        <v-list>
          <v-list-item
            v-for="(role, index) in roles"
            :key="index"
            @click="setCookie(role)"
          >
            <v-list-item-title>{{ role.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-btn>
  </v-app-bar>
  <v-navigation-drawer v-model="drawer" app>
    <v-list nav dense>
      <v-list-item v-for="item in items" :to="item.routerLink" :key="item.name">
        <div class="list-item">
          <v-icon :icon="item.icon" />
          <v-list-item-title class="ml-2">{{ item.name }}</v-list-item-title>
        </div>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
  export default {
    data() {
      return {
        items: [
          {name: "Home", icon: "mdi-home", routerLink: "/"},
          {name: "Open Roles", icon: "mdi-briefcase", routerLink: "/openroles/staff"},
          {name: "Candidates", icon: "mdi-account-group", routerLink: "/candidates"},
          {name: "Settings", icon: "mdi-cog", routerLink: "/settings"}
        ],
        drawer: true,
        roles: [
          {title: "Admin", id: 1},
          {title: "User", id: 2},
          {title: "Manager", id: 3},
          {title: "HR", id: 4},
        ],
        currentRole: { 'roleTitle': 'None', 'roleId': 0 }
      }
    },
    mounted() {
      if(this.currentRole.roleTitle == 'None') {
        this.$cookies.set('roleId', 1, 1)
        this.$cookies.set('roleTitle', 'Admin', 1)
        this.currentRole = { 'roleTitle': 'Admin', 'roleId': 1 }
      } else {
        this.currentRole = { 'roleTitle': this.$cookies.get('roleTitle'), 'roleId': this.$cookies.get('roleId') }
      }
      console.log(this.$cookies.get('roleId'),this.$cookies.get('roleTitle'))
    },
    methods: {
      setCookie(selectedRole) {
        this.$cookies.set('roleId', selectedRole.id, 1);
        this.$cookies.set('roleTitle', selectedRole.title, 1);
        this.currentRole.roleTitle = selectedRole.title
        this.currentRole.roleId = selectedRole.id
        console.log(this.$cookies.get('roleId'),this.$cookies.get('roleTitle'))
      },
    }
  }
</script>

<style scoped>
  .app-bar {
    border-bottom: 1px lightgrey solid;
  }
  .list-item {
    display: flex;
    align-items: center;
    margin-left: 4px;
  }
</style>