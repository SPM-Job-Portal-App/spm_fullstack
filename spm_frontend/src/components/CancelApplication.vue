<template>
    <!-- success message with overlay -->
    <OverlayMessage
      :show.sync="successOverlay"
      title="Application Successfully Cancelled"
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
      title="Application Not Successfully Cancelled"
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
        index: this.$route.params.index,
        listing: {},
        loading: false,
        successOverlay: false,
        failureOverlay: false,
        feedbackMessage: '',
        availableRoles: [],
        appliedRoles: [],
        
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
    this.fetchAppliedRoles();
    //   axios.get('http://localhost:5000/listing/get_all_listings').then(
    //     (response)=>{
    //       const listings = response.data;
    //       for (let item of listings){
    //         if (item.id == this.index) {
    //           this.listing = item
    //           this.listing.is_open = this.listing.is_open ? 'True' : 'False'
    //           break
    //         }
    //       }
    //       console.log(this.listing)
    //     }
    //   ),
    //   axios.get(`http://localhost:5000/listing/${this.index}`).then(
    //     (response)=>{
    //       console.log(response)
    //       this.openingDate = response.data.opening_date
    //       this.closingDate = response.data.closing_date
    //     }
    //   ),
    //   axios.get('http://localhost:5000/role').then(
    //     (response)=>{
    //       for(const idx in response.data.roles){
    //         this.availableRoles.push(response.data.roles[idx].Role)
    //       }
    //     }
    //   )
    //   axios.get('http://localhost:5000/staff/get_staff').then(
    //     (response)=>{
    //       for(const staff of response.data.staff){
    //         if(staff.Role == 3){
    //           this.reportingManagers.push(staff['Staff Name'])
    //           this.reportingManagersIds[staff['Staff Name']] = staff['Staff Id']
    //         }
    //       }
    //     }
    //   )
    },
    methods: {
        async fetchAppliedRoles() {
            try {
                const response = await axios.get('http://localhost:5000/get_all_');
                if (response.status === 200) {
                this.appliedRoles = response.data; 
                } else {
                console.error('Failed to fetch applied roles:', response.data);
                }
            } catch (error) {
                console.error('Error while fetching applied roles:', error);
            }
        },
        async cancelApplication(listing) {
            try {
                const response = await axios.delete(`http://localhost:5000/get_listing_by_index/${this.index}`, {
                data: {
                    applicationId: listing.id,
                },
                });

                if (response.status === 200) {
                const index = this.appliedRoles.findIndex(role => role.id === listing.id);
                if (index !== -1) {
                    this.appliedRoles.splice(index, 1); 
                    this.successOverlay = true;
                }
                } else {
                console.error('Failed to cancel the application:', response.data);
                this.failureOverlay = true;
                }
            } catch (error) {
                console.error('Error while canceling the application:', error);
                this.failureOverlay = true;
            }
        },


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
        axios.put(`http://localhost:5000/listing/${this.index}`, this.listing)
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