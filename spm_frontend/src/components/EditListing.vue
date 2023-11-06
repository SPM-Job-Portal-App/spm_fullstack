<template>
    <div class="mx-10 mt-6">
      <h1 class="page-title">Edit Listing</h1>
      <!-- Input fields for editing -->
      <v-select v-model="listing.role_name" :items="availableRoles" label="Role Name" class="mt-5"></v-select>
      <v-select v-model="listing.dept" :items="availableDepartments" label="Department"></v-select>
      <v-select v-model="listing.country" :items="availableCountries" label="Country of Opening"></v-select>
      <v-select v-model="listing.reporting_manager" :items="reportingManagers" label="Reporting Manager"></v-select>
      <v-select v-model="listing.is_open"  :items="availableIsOpen" label="Open"></v-select>
      <v-row class="text-center">
        <v-col>
          <p class="text-grey">Opening Date</p>
          <VDatePicker v-model="openingDate" :disabled-dates="disabledDates" mode="date" expanded />
        </v-col>
        <v-col>
          <p class="text-grey">Closing Date</p>
          <VDatePicker v-model="closingDate" :disabled-dates="disabledDates" mode="date" expanded />
        </v-col>
      </v-row>
      <v-row class="text-center">
        <v-col>
          <v-btn @click="saveChanges" class="mt-3 mr-3" color="#ccbbaa" :loading="loading" :disabled="!isConfirmButtonEnabled">Save Changes</v-btn>
          <v-btn to="/roles/hr" class="mt-3" color="#ccbbaa" :loading="loading">Discard Changes</v-btn>
        </v-col>
      </v-row>
    </div>

    <!-- success message with overlay -->
    <OverlayMessage
      :show.sync="successOverlay"
      title="Update Is Successful"
      :message="feedbackMessage"
      buttonText="Done"
      buttonColor="success"
      icon="mdi-check-circle"
      iconColor="success"
      iconSize="112"
      @close-overlay="toggleOverlay"
      route="/roles/hr"
    ></OverlayMessage>

  <!-- failure message with overlay -->
      <OverlayMessage
      :show.sync="failureOverlay"
      title="Update Is Unsuccessful"
      :message="feedbackMessage"
      buttonText="Close"
      buttonColor="red"
      icon="mdi-close-circle"
      iconColor="red"
      iconSize="112"
      @close-overlay="toggleOverlay"
      route="/roles/hr"
      ></OverlayMessage>

  </template>
  
  <script>
//   import { EventBus } from '@/main';
  import axios from'axios';
  import OverlayMessage from './OverlayMessage.vue';
  const isProduction = import.meta.env.PROD;
  let apiUrl; // Declare apiUrl outside the conditional block

if (isProduction) {
  apiUrl = "http://spm-backend-lb-780988294.ap-southeast-1.elb.amazonaws.com";
} else {
  apiUrl = "http://localhost:5000";
}
  export default {
    data() {
      return {
        closingDate: new Date(),
        openingDate: new Date(),
        index: this.$route.params.index,
        listing: {},
        loading: false,
        successOverlay: false,
        failureOverlay: false,
        feedbackMessage: '',
        availableRoles: [],
        availableDepartments: [
          'Design',
          'Chariman',
          'CEO',
          'Sales',
          'Solutioning',
          'Engineering',
          'HR',
          'Finance',
          'Consultancy',
          'IT'
        ],
        availableCountries: ['Singapore', 'Malaysia', 'Indonesia', 'Vietnam', 'Hong Kong'],
        availableIsOpen: ['True', 'False'],
        reportingManagers: ['Nil'],
        reportingManagersIds: [],
        disabledDates: this.getDisabledDates(),
      };
    },
    computed: {
      isConfirmButtonEnabled() {
        const isDatesValid = this.openingDate <= this.closingDate;
        return (
          isDatesValid
        );
      },
    },
    mounted()
    {
      axios.get(`${apiUrl}/listing/get_all_listings`).then(
        (response)=>{
          const listings = response.data;
          for (let item of listings){
            if (item.id == this.index) {
              this.listing = item
              this.listing.is_open = this.listing.is_open ? 'True' : 'False'
              break
            }
          }
          console.log(this.listing)
        }
      ),
      axios.get(`${apiUrl}/listing/${this.index}`).then(
        (response)=>{
          console.log(response)
          this.openingDate = response.data.opening_date
          this.closingDate = response.data.closing_date
        }
      ),
      axios.get(`${apiUrl}/role`).then(
        (response)=>{
          for(const idx in response.data.roles){
            this.availableRoles.push(response.data.roles[idx].Role)
          }
        }
      )
      axios.get(`${apiUrl}/staff/get_staff`).then(
        (response)=>{
          for(const staff of response.data.staff){
            if(staff.Role == 3){
              this.reportingManagers.push(staff['Staff Name'])
              this.reportingManagersIds[staff['Staff Name']] = staff['Staff Id']
            }
          }
        }
      )
    },
    methods: {
      saveChanges() {
        // Handle saving changes here
        this.listing.reporting_manager = this.listing.reporting_manager == 'Nil' ? null : this.reportingManagersIds[this.listing.reporting_manager]
        this.listing.is_open = this.listing.is_open == 'True' ? true : false
        const opening_date = new Date(this.openingDate)
        const closing_date =  new Date(this.closingDate)
        this.listing['opening_date'] = `${opening_date.getFullYear()}-${opening_date.getMonth()+1}-${opening_date.getDate()}`
        this.listing['closing_date'] = `${closing_date.getFullYear()}-${closing_date.getMonth()+1}-${closing_date.getDate()}`
        
        console.log('Saving changes:', this.listing);
        this.loading = true
        axios.put(`${apiUrl}/listing/${this.index}`, this.listing)
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
      },
      getDisabledDates(){
        const currentDate = new Date()
        currentDate.setDate(currentDate.getDate() - 1)
        return [{ start: null, end: currentDate }]
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