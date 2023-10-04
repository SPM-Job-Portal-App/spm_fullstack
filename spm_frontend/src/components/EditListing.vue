<template>
    <div class="mx-10 mt-6">
      <h1 class="page-title">Edit Listing</h1>
      <!-- Input fields for editing -->
      <v-select v-model="listing.role_name" :items="availableRoles" label="Role Name" class="mt-5"></v-select>
      <v-select v-model="listing.dept" :items="availableDepartments" label="Department"></v-select>
      <v-select v-model="listing.country" :items="availableCountries" label="Country of Opening"></v-select>
      <!-- <v-select v-model="listing.skills" :items="availableSkills" label="Skills" chips multiple></v-select> -->
      <v-text-field v-model="listing.reporting_manager" label="Reporting Manager"></v-text-field>
      <v-select v-model="listing.is_open"  :items="availableIsOpen" label="Open"></v-select>
      <div class="text-center">
        <p class="text-grey">Closing Date</p>
        <VDatePicker v-model="closingDate" :disabled-dates="disabledDates" mode="date" expanded />
        <v-btn @click="saveChanges" class="mt-3 mr-3" color="#ccbbaa" :loading="loading">Save Changes</v-btn>
        <v-btn to="/openroles/hr" class="mt-3" color="#ccbbaa" :loading="loading">Discard Changes</v-btn>
      </div>
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
        closingDate: null,
        openingDate: null,
        disabledDates: [{ start: null, end: new Date() }],
        index: this.$route.params.index,
        listing: {},
        loading: false,
        successOverlay: false,
        failureOverlay: false,
        feedbackMessage: '',
        availableRoles: [
          'Account Manager',
          'Consultancy Director',
          'Consultant',
          'Sales Director',
          'Solutioning Director',
          'Finance  Executive',
          'Finance Director',
          'Finance Manager',
          'Developer',
          'Senior Engineer',
          'Engineering Director',
          'Sales Manager',
          'HR Director',
          'IT Director',
          'IT Analyst',
          'Support Engineer',
          'Call Centre',
          'Admin Executive',
          'HR Executive',
          'Junior Engineer',
          'L&D Executuve',
          'Ops Planning Exec'
        ],
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
        // availableSkills: [
        //   'Account Management',
        //   'Accounting and Tax Systems',
        //   'Accounting Standards',
        //   'Applications Development',
        //   'Applications Integration',
        //   'Applications Support and Enhancement',
        //   'Audit Compliance',
        //   'Audit Frameworks',
        //   'Budgeting',
        //   'Business Acumen',
        //   'Business Development',
        //   'Business Environment Analysis',
        //   'Business Needs Analysis',
        //   'Business Negotiation',
        //   'Business Presentation Delivery',
        //   'Business Requirements Mapping',
        //   'Business Risk Management',
        //   'Call Centre Management',
        //   'Collaboration',
        //   'Communication',
        //   'Configuration Tracking',
        //   'Customer Acquisition Management',
        //   'Customer Relationship Management',
        //   'Data Analytics',
        //   'Database Administration',
        //   'Developing People',
        //   'Digital Fluency',
        //   'Employee Communication Management',
        //   'Employee Engagement Management',
        //   'Finance Business Partnering',
        //   'Financial Acumen',
        //   'Financial Closing',
        //   'Financial Management',
        //   'Financial Planning',
        //   'Financial Reporting',
        //   'Financial Statements Analysis',
        //   'Financial Transactions',
        //   'Human Resource Advisory',
        //   'Human Resource Practices Implementation',
        //   'Human Resource Strategy Formulation',
        //   'Human Resource Systems Management',
        //   'Infrastructure Deployment',
        //   'Infrastructure Support',
        //   'Learning and Development Programme Management',
        //   'Learning Needs Analysis',
        //   'Network Administration and Maintenance',
        //   'Onboarding',
        //   'Organisational Design',
        //   'People and Performance Management',
        //   'Pricing Strategy',
        //   'Problem Management',
        //   'Problem Solving',
        //   'Product Management',
        //   'Professional and Business Ethics',
        //   'Project Management',
        //   'Regulatory Compliance',
        //   'Regulatory Risk Assessment',
        //   'Regulatory Strategy',
        //   'Sales Closure',
        //   'Sales Strategy',
        //   'Security Administration',
        //   'Sense Making',
        //   'Service Level Management',
        //   'Skills Framework Adoption',
        //   'Software Configuration',
        //   'Software Design',
        //   'Software Testing',
        //   'Solution Architecture',
        //   'Solutions Design Thinking',
        //   'SOP Development and Implementation',
        //   'Stakeholder Management',
        //   'Strategy Planning',
        //   'System Integration',
        //   'Talent Management',
        //   'Tax Computation',
        //   'Tax Implications',
        //   'Technology Application',
        //   'Technology Integration',
        //   'Technology Road Mapping',
        //   'User Interface Design'
        // ],
        availableIsOpen: ['True', 'False'],
      };
    },
    mounted()
    {
      axios.get('http://localhost:5000/listing/get_open_listings').then(
        (response)=>{
          const listings = response.data;
          for (let item of listings){
            if (item.id == this.index) {
              this.listing = item
              // this.listing.skills = this.listing.skills.length > 0 ? this.listing.skills.split(/, |,/) : []
              // this.listing.skills = this.listing.skills.filter((skill) => {return skill != 'Nil'})
              this.listing.is_open = this.listing.is_open ? 'True' : 'False'
              break
            }
          }
          console.log(this.listing)
        }
      ),
      axios.get(`http://localhost:5000/listing/${this.index}`).then(
        (response)=>{
          console.log(response)
          this.openingDate = response.data.opening_date
          this.closingDate = response.data.closing_date
        }
      )
    },
    methods: {
      saveChanges() {
        // Handle saving changes here
        // this.listing.skills = this.listing.skills.filter((skill) => {return skill !== ''})
        // this.listing.skills = this.listing.skills.join(", ")
        this.listing.reporting_manager = this.listing.reporting_manager == 'Nil' ? null : parseInt(this.listing.reporting_manager)
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