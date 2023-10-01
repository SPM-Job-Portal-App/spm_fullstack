<template>
    <div class="mx-10 mt-6">
      <h1 class="page-title">Edit Listing</h1>
      <!-- Input fields for editing -->
      <v-text-field v-model="listing.role_name" label="Role Name" class="mt-5"></v-text-field>
      <v-text-field v-model="listing.dept" label="Department"></v-text-field>
      <v-text-field v-model="listing.country" label="Country of Opening"></v-text-field>
      <v-text-field v-model="listing.skills" label="Skills"></v-text-field>
      <v-text-field v-model="listing.reporting_manager" label="Reporting Manager"></v-text-field>
      <v-text-field v-model="listing.is_open" label="Open"></v-text-field>
      <v-btn @click="saveChanges" class="mt-3" color="#ccbbaa" :loading="loading">Save Changes</v-btn>
    </div>

    <!-- success message with overlay -->
    <OverlayMessage
    :show.sync="successOverlay"
    title="Application Sent Successfully"
    :message="feedbackMessage"
    buttonText="Done"
    buttonColor="success"
    icon="mdi-check-circle"
    iconColor="success"
    iconSize="112"
    @close-overlay="toggleOverlay"
    route="/openroles/hr"
    ></OverlayMessage>

<!-- failure message with overlay -->
    <OverlayMessage
    :show.sync="failureOverlay"
    title="Application Sent Unsuccessfully"
    :message="feedbackMessage"
    buttonText="Close"
    buttonColor="red"
    icon="mdi-close-circle"
    iconColor="red"
    iconSize="112"
    @close-overlay="toggleOverlay"
    route="/openroles/hr"
    ></OverlayMessage>

  </template>
  
  <script>
//   import { EventBus } from '@/main';
  import axios from'axios';
  import OverlayMessage from './OverlayMessage.vue';
  export default {
    data() {
      return {
        // editedListing: {
        //   department: '',
        //   label: '',
        //   numApplications: 0,
        // },
        index: this.$route.params.index,
        listing: {},
        loading: false,
        successOverlay: false,
        failureOverlay: false,
        feedbackMessage: ''
      };
    },
    mounted()
    {
      axios.get('http://localhost:5000/listing').then(
        (response)=>{
          const listings = response.data[0];
          for (let item of listings){
            if (item.id == this.index) {
              this.listing = item
              break
            }
          }
          console.log(this.listing)
        }
      )
    },
    methods: {
      saveChanges() {
        // Handle saving changes here
        console.log('Saving changes:', this.listing);
        this.loading = true
        axios.put(`http://localhost:5000/listing/update/${this.index}`, this.listing)
        .then(
            (response)=>{
              this.successOverlay = true
              if(response.data.message) {
                this.feedbackMessage = response.data.message
              }
              else {
                this.feedbackMessage = "Update successful!"
              }
              console.log(response)
            }
        )
        .catch(error => {
            this.failureOverlay = true
            if(error.response.data.message) {
              this.feedbackMessage = error.response.data.message
            }
            else {
              this.feedbackMessage = "An error occured during the update process!"
            }
            console.error(error);
        })
      // Emit an event to notify the parent component (Open Roles HR) about the changes
        // EventBus.$emit('listing-updated', this.editedListing);
      // You can also use an API call to save the changes to your backend
      },
      toggleOverlay() {
        this.loading = false
        this.successOverlay = false
        this.failureOverlay = false
      }
    },
    components: {
      OverlayMessage,
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