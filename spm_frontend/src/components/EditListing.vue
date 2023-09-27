<template>
    <div>
      <h1>Edit Listing</h1>
      <!-- Input fields for editing -->
      <v-text-field v-model="editedListing.department" label="Department"></v-text-field>
      <v-text-field v-model="editedListing.label" label="Label"></v-text-field>
      <v-text-field v-model="editedListing.numApplications" label="Number of Applicants"></v-text-field>
      <v-btn @click="saveChanges">Save Changes</v-btn>
    </div>
  </template>
  
  <script>
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
        // You can also use an API call to save the changes to your backend
      },
    },
  };
  </script>
  