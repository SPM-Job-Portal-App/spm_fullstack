<template>
    <v-card class>
      <!-- Title -->
      <h1 class="page-title ml-8">Job Listings</h1>
  
      <v-row>
        <v-col cols="12" md="6">
          <!-- Filter by Department Dropdown -->
          <v-select
            v-model="selectedDepartment"
            :items="departmentOptions"
            label="Filter by Department"
            dense
            class="ml-8"
          ></v-select>
        </v-col>

        <v-col cols="12" md="6">
          <!-- Filter by Country Dropdown -->
          <v-select
            v-model="selectedCountry"
            :items="countryOptions"
            label="Filter by Country"
            dense
            class="ml-8"
          ></v-select>
        </v-col>
      </v-row>
  
      <v-row class="ml-4">
        <v-col cols="12" sm="6" md="4" lg="3" v-for="(listing, index) in filteredAvailableRoles" :key="index">
          <!-- Listing Card with Margin -->
          <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
            <!-- Badge to indicate open or closed listing (Top Left) -->
            <span class="ml-5">
              <v-badge v-if="!listing.is_open"
                color="error"
                content="Closed"
              ></v-badge>
              <v-badge v-else
                color="success"
                content="Open"
              ></v-badge>
            </span>
            <!-- Edit Button (Top Right) -->
            <v-btn icon class="edit-button" @click="editListing(listing.id)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
            <div class="d-flex align-center justify-center department-icon-container">
              <!-- Department Icon -->
              <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
            </div>
            <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ listing.role_name }}</div>
            <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">{{ listing.dept }} - {{ listing.country }}</div>
            <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 12px;">Skills Required</div>
            <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">
              <v-chip
                v-for="skill in listing.skills.split(', ').slice(0,4)"
                :key="skill"
                :prepend-icon="getSkillIcon(skill)"
                class="ma-1"
                style="font-size: 12px;"
              >
                {{ skill || 'None' }}
              </v-chip>
              <div
                v-if="listing.skills.split(', ').length > 4"
                class="text-grey text-caption align-self-center"
              >
                (+{{ listing.skills.split(', ').length - 4 }} {{ listing.skills.split(', ').length - 4 == 1 ? "other": "others" }})
              </div>
            </div>
            <div class="text-center mt-3 mb-6">
              <!-- Number of Applicants -->
              <v-btn @click="viewApplicants(listing.id)" color="#ccbbaa" style="padding: 12px 20px; font-size: 18px;">
                View&nbsp; <span class="numapp">{{ listing.applicants.length }}</span> &nbsp;{{ listing.applicants.length == 1 ? "applicant": "applicants" }}
              </v-btn>
            </div>
            <div class="text-center mt-3 mb-6">
              <!-- Button to close role listing -->
              <v-btn :disabled=!listing.is_open @click="closeRoleListing(listing.id)" color="#ccbbaa" style="padding: 12px 20px; font-size: 18px;">
                Close role listing
              </v-btn>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
    <v-card-actions>
      <v-btn
        class="add-button"
        to="/createrolelisting"
        icon
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-card-actions>

    <!-- success message with overlay -->
    <OverlayMessage
    :show.sync="successOverlay"
    title="Role Listing Closed Successfully"
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
    title="Error Closing Role Listing"
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
  import axios from'axios';
  import OverlayMessage from "../components/OverlayMessage.vue";
  export default {
    data: () => ({
      selectedDepartment: "All",
      selectedCountry: "All",
      availableRoles: [],
      successOverlay: false,
      failureOverlay: false,
    }),
    mounted()
    {
      axios.get('http://localhost:5000/application/getapplications').then(
        (response)=>{
          this.availableRoles = response.data[0];
          console.log(this.availableRoles)
        }
      )
    },
    computed: {
      departmentOptions() {
        const departments = [...new Set(this.availableRoles.map((role) => role.dept))];
        return ['All', ...departments];
      },
      countryOptions() {
          const countries = [...new Set(this.availableRoles.map((role) => role.country))];
          console.log(countries); 
          return ['All', ...countries];
      },
      filteredAvailableRoles() {
        return this.availableRoles.filter((role) => {
          const departmentMatch = this.selectedDepartment === 'All' || role.dept === this.selectedDepartment;
          const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
          return departmentMatch && countryMatch;
        });
      },
    },
    methods: {
        toggleOverlay(){
        this.loading = false
        this.successOverlay = false
        this.failureOverlay = false
      },
      closeRoleListing(index) {
        axios.put('http://localhost:5000/listing/close_role_listing/' + index)
        .then(response => {
          console.log(response)
          this.successOverlay = true;
        })
        .catch(error => {
          this.failureOverlay = true;
          console.log(error)
        })
      },
      applyNow(index) {
        console.log(`Applied for ${this.availableRoles[index].label}`);
      },
      viewApplicants(id) {
        this.$router.push({ name: 'view-applicants', params: { id } });
      },
      editListing(index) {
        this.$router.push({ name: 'edit-listing', params: { index } });
      },
      getDepartmentIcon(department) {
        const departmentIcons = {
          'Design': 'mdi-palette',
          'Chariman': 'mdi-chess-king',
          'CEO': 'mdi-chess-queen',
          'Sales': 'mdi-phone-in-talk',
          'Solutioning': 'mdi-lightbulb',
          'Engineering': 'mdi-state-machine',
          'HR': 'mdi-account-group',
          'Finance': 'mdi-cash-register',
          'Consultancy': 'mdi-compass',
          'IT': 'mdi-code-tags'
        };
        return departmentIcons[department] || 'mdi-help-circle';
      },
      getSkillIcon(skill) {
        const skillIcons = {
          'Account Management': 'mdi-bank',
          'Accounting and Tax Systems': 'mdi-bank',
          'Accounting Standards': 'mdi-bank',
          'Applications Development': 'mdi-code-braces',
          'Applications Integration': 'mdi-code-braces',
          'Applications Support and Enhancement': 'mdi-code-braces',
          'Audit Compliance': 'mdi-bank-check',
          'Audit Frameworks': 'mdi-bank-check',
          'Budgeting': 'mdi-cash',
          'Business Acumen': 'mdi-cash',
          'Business Development': 'mdi-cash',
          'Business Environment Analysis': 'mdi-cash',
          'Business Needs Analysis': 'mdi-cash',
          'Business Negotiation': 'mdi-cash',
          'Business Presentation Delivery': 'mdi-cash',
          'Business Requirements Mapping': 'mdi-cash',
          'Business Risk Management': 'mdi-cash',
          'Call Centre Management': 'mdi-message-outline',
          'Collaboration': 'mdi-message-outline',
          'Communication': 'mdi-message-outline',
          'Configuration Tracking': 'mdi-message-outline',
          'Customer Acquisition Management': 'mdi-message-outline',
          'Customer Relationship Management': 'mdi-message-outline',
          'Data Analytics': 'mdi-data-matrix',
          'Database Administration': 'mdi-data-matrix',
          'Developing People': 'mdi-account-group',
          'Digital Fluency': 'mdi-account-group',
          'Employee Communication Management': 'mdi-account-group',
          'Employee Engagement Management': 'mdi-account-group',
          'Finance Business Partnering': 'mdi-finance',
          'Financial Acumen': 'mdi-finance',
          'Financial Closing': 'mdi-finance',
          'Financial Management': 'mdi-finance',
          'Financial Planning': 'mdi-finance',
          'Financial Reporting': 'mdi-finance',
          'Financial Statements Analysis': 'mdi-finance',
          'Financial Transactions': 'mdi-finance',
          'Human Resource Advisory': 'mdi-account-switch',
          'Human Resource Practices Implementation': 'mdi-account-switch',
          'Human Resource Strategy Formulation': 'mdi-account-switch',
          'Human Resource Systems Management': 'mdi-account-switch',
          'Infrastructure Deployment': 'mdi-domain',
          'Infrastructure Support': 'mdi-domain',
          'Learning and Development Programme Management': 'mdi-school',
          'Learning Needs Analysis': 'mdi-school',
          'Network Administration and Maintenance': 'mdi-domain',
          'Onboarding': 'mdi-account-group',
          'Organisational Design': 'mdi-account-group',
          'People and Performance Management': 'mdi-account-group',
          'Pricing Strategy': 'mdi-cash',
          'Problem Management': 'mdi-help',
          'Problem Solving': 'mdi-help',
          'Product Management': 'mdi-clipboard-text',
          'Professional and Business Ethics': 'mdi-clipboard-text',
          'Project Management': 'mdi-clipboard-text',
          'Regulatory Compliance': 'mdi-police-badge',
          'Regulatory Risk Assessment': 'mdi-police-badge',
          'Regulatory Strategy': 'mdi-police-badge',
          'Sales Closure': 'mdi-sale',
          'Sales Strategy': 'mdi-sale',
          'Security Administration': 'mdi-electron-framework',
          'Sense Making': 'mdi-electron-framework',
          'Service Level Management': 'mdi-electron-framework',
          'Skills Framework Adoption': 'mdi-electron-framework',
          'Software Configuration': 'mdi-microsoft-visual-studio-code',
          'Software Design': 'mdi-microsoft-visual-studio-code',
          'Software Testing': 'mdi-microsoft-visual-studio-code',
          'Solution Architecture': 'mdi-microsoft-visual-studio-code',
          'Solutions Design Thinking': 'mdi-microsoft-visual-studio-code',
          'SOP Development and Implementation': 'mdi-vhs',
          'Stakeholder Management': 'mdi-vhs',
          'Strategy Planning': 'mdi-vhs',
          'System Integration': 'mdi-vhs',
          'Talent Management': 'mdi-account-multiple',
          'Tax Computation': 'mdi-cash',
          'Tax Implications': 'mdi-cash',
          'Technology Application': 'mdi-semantic-web',
          'Technology Integration': 'mdi-semantic-web',
          'Technology Road Mapping': 'mdi-semantic-web',
          'User Interface Design': 'mdi-semantic-web'
        };
        return skillIcons[skill] || 'mdi-help-circle';
      },
      getRandomApplicants() {
        return Math.floor(Math.random() * 10) + 1;
      },
    },
    components: {
      OverlayMessage
    },
  };
  </script>
  
  <style scoped>
  .page-title {
    color: #664229;
    font-weight: bold;
    margin: 20px 0;
  }
  
  .department-icon-container {
    height: 180px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .department-icon {
    font-size: 100px;
  }
  
  .edit-button {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 1;
    color: #664229;
  }

  .add-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1;
    color: white;
    background-color: #664229;
  }

  .numapp {
    font-weight: bold;
    /* font-size: 24px; */
  }

  </style>