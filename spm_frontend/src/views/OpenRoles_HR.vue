<template>
    <v-card class>
      <!-- Title -->
      <h1 class="page-title ml-8">Job Listings</h1>
      
      <v-card-text>

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
              <!-- <div class="text-center mt-2" style="color: #664229; font-size: 12px;">
                Application Period: {{ new Date(listing.opening_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }} - {{ new Date(listing.closing_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }}
              </div>  -->
              <v-card-text>
                <div class="text-center mt-2">
                  <v-chip
                    class="text-center"
                    color="#664229"
                    style="font-size: 12px;"
                    @click="showSkillsOverlay(listing)"
                  >
                    Skills Required: {{ calculateSkillPercentage(listing.skills) }}
                  </v-chip>
                </div>
              </v-card-text>
              <div class="text-center mt-3 mb-6">
                <!-- Number of Applicants -->
                <v-btn @click="viewApplicants(index)" color="#ccbbaa" style="padding: 12px 20px; font-size: 18px;">
                  View&nbsp; <span class="numapp">{{ listing.applicants.length }}</span> &nbsp;{{ listing.applicants.length == 1 ? "applicant": "applicants" }}
                </v-btn>
              </div>
              <skills-overlay v-model="skillsOverlay" :calculateSkillPercentage=calculateSkillPercentage :acquiredSkills=acquiredSkills :getSkillIcon=getSkillIcon :listingData=listingData :closeSkillsOverlay=closeSkillsOverlay></skills-overlay>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card-actions>
      <v-btn
        class="add-button"
        to="/createrolelisting"
        icon>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-card-actions>
  </template>
  
  <script>
  import axios from'axios';
  import SkillsOverlay from '../components/SkillsOverlayHR.vue';
  export default {
    components: { SkillsOverlay },
    
    data: () => ({
      selectedDepartment: "All",
      selectedCountry: "All",
      showSkills: false,
      availableRoles: [],
      skillsOverlay: false,
      listingData: Object
    }),
    mounted()
    {
      axios.get('http://localhost:5000/application').then(
        (response)=>{
          this.availableRoles = response.data[0];
          console.log(this.availableRoles)
        }
      )
    },
    computed: {
      filteredListings() {
        if (this.tab === 'availableRoles') {
          return this.filteredAvailableRoles.filter((listing) =>
            listing.role_name.toLowerCase().includes(this.searchText.toLowerCase())
          );
        } else if (this.tab === 'appliedRoles') {
          return this.filteredAppliedRoles.filter((listing) =>
            listing.role_name.toLowerCase().includes(this.searchText.toLowerCase())
          );
        }
      },
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
      applyNow(index) {
        console.log(`Applied for ${this.availableRoles[index].label}`);
      },
      showSkillsOverlay(listing) {
      this.listingData = listing
      this.skillsOverlay = true;
      },
      closeSkillsOverlay() {
        this.skillsOverlay = false;
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
      calculateSkillPercentage(requiredSkills) {
        const requiredSkillsArr = requiredSkills.split(',').map(item => item.trim());
        const totalSkills = requiredSkillsArr.length;
        return totalSkills
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
  };
  </script>
  
  <style scoped>

  .department-icon-container {
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .department-icon {
    font-size: 100px;
  }
  
  .v-card--reveal {
    bottom: 0;
    opacity: 1 !important;
    position: absolute;
    width: 100%;
    background-color: #eae4dd;
    color: #664229;
    padding: 10px;
  }
  .sheet-header{
    margin-left: 50px;
    margin-right: 50px;
  }
  
  .page-title {
    color: #664229;
    font-weight: bold;
    margin: 20px 0;
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