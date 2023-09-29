<template>
    <div class="mx-10 mt-6">
      <h1 class="page-title">Edit Listing</h1>
      <!-- Input fields for editing -->
      <v-text-field v-model="editedListing.label" label="Label" class="mt-5"></v-text-field>
      <v-text-field v-model="editedListing.department" label="Department"></v-text-field>
      <v-text-field v-model="editedListing.description" label="Description"></v-text-field>
      <v-text-field v-model="editedListing.country" label="Country of Opening"></v-text-field>
      <v-text-field v-model="editedListing.reportingmanager" label="Reporting Manager"></v-text-field>
      <v-btn @click="saveChanges" class="mt-3" color="#ccbbaa">Save Changes</v-btn>
    </div>
  </template>
  
  <script>
//   import { EventBus } from '@/main';
  export default {
    data() {
      return {
        editedListing: {
          department: '',
          label: '',
          numApplications: 0,
        },
      };
    },
    methods: {
      saveChanges() {
        // Handle saving changes here
        console.log('Saving changes:', this.editedListing);
      // Emit an event to notify the parent component (Open Roles HR) about the changes
        // EventBus.$emit('listing-updated', this.editedListing);
      // You can also use an API call to save the changes to your backend
    },
    },
  };
  </script>

<style scoped>
  .page-title {
    color: #664229;
    font-weight: bold;
    margin: 20px 0;
  }
</style>