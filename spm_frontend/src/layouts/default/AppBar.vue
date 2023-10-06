<template>
  <v-app-bar class="app-bar" flat app>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-icon class="ml-5" icon="mdi-circle-slice-4" />
    <v-toolbar-title>Staff</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn icon="mdi-help-circle"></v-btn>
    <v-btn icon="mdi-bell"></v-btn>
    <v-btn icon="mdi-account-circle"></v-btn>
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
          {name: "Open Roles", icon: "mdi-briefcase", routerLink: "/openroles"},
          {name: "Candidates", icon: "mdi-account-group", routerLink: "/candidates"},
          {name: "Settings", icon: "mdi-cog", routerLink: "/settings"}
        ],
        drawer: true
      }
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