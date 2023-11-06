<template>
  <v-card>
    <v-tabs v-model="tab" bg-color="#664229">
      <v-tab value="availableRoles">Available Roles</v-tab>
      <v-tab value="appliedRoles">Applied Roles</v-tab>
    </v-tabs>

    <v-card-text>
      <v-row>
        <v-col cols="12" md="6">
          <!-- Filter by Department Dropdown -->
          <v-select
            v-model="selectedDepartment"
            :items="tab === 'availableRoles' ? departmentOptionsForAvailable : departmentOptionsForApplied"
            label="Filter by Department"
            dense
          ></v-select>
        </v-col>
        <v-col cols="12" md="6">
        <!-- Filter by Country Dropdown -->
        <v-select
          v-model="selectedCountry"
          :items="tab === 'availableRoles' ? countryOptionsForAvailable : countryOptionsForApplied"
          label="Filter by Country"
          dense
        ></v-select>
      </v-col>
      </v-row>

      <v-window v-model="tab">
        <v-window-item value="availableRoles">
          <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="(listing, index) in filteredAvailableRoles" :key="index">
              <!-- Listing Card with Margin -->
             
              <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;" :disabled="!listing.is_open">
                <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
                <div class="d-flex align-center justify-center department-icon-container">
                  <!-- Department Icon -->
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
                </div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ listing.role_name }}</div>
                <div class="text-center mt-2" style="color: #664229; font-size: 12px;">{{ listing.dept }} - {{ listing.country }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 5px; font-size: 12px;">Reporting Manager: {{ listing.reporting_manager }}</div>
                <div class="text-center mt-2" style="color: #664229; font-size: 12px;">
                  Application Period: {{ new Date(listing.opening_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }} - {{ new Date(listing.closing_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }}
                </div> 
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
                <!-- <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">
                  <v-chip
                    v-for="skill in listing.skills.split(', ').slice(0,4)"
                    :key="skill"
                    :color="acquiredSkills.includes(skill) || skill=='Nil' ? 'green' : 'red'"
                    :prepend-icon="getSkillIcon(skill)"
                    class="ma-1"
                    style="font-size: 12px;"
                  >
                    {{ skill || 'Nil' }}
                  </v-chip>
                  <div
                    v-if="listing.skills.split(', ').length > 4"
                    class="text-grey text-caption align-self-center"
                  >
                    (+{{ listing.skills.split(', ').length - 4 }} {{ listing.skills.split(', ').length - 4 == 1 ? "other": "others" }})
                  </div>
                </div> -->
                <v-card-actions class="justify-center">
                  <v-btn
                    variant="flat"
                    color="#e0b88a"
                    @click="listing.revealDesc = !listing.revealDesc"
                  >
                    Learn More
                  </v-btn>
                </v-card-actions>
                <div class="text-center mt-3 mb-6">
                  <v-btn v-if="listing.is_open" class="mx-auto px-4" :to="{ name: 'Apply Open Roles', params: { id: listing.id } }" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Apply Now</v-btn>
                  <v-btn v-else class="mx-auto px-4" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Expired</v-btn>
                </div>
                <v-expand-transition>
                  <v-card
                    v-if="listing.revealDesc"
                    class="v-card--reveal d-flex flex-column"
                    style="height: 100%;"
                  >
                    <v-card-text class="pb-0" style="overflow-y: auto">
                      <p class="text-h6 text--primary mb-4">
                        Description
                      </p>
                      <p>{{ listing.role_desc }}</p>
                    </v-card-text>
                    <v-spacer></v-spacer>
                    <v-card-actions class="pt-0 justify-center">
                      <v-btn
                        variant="text"
                        color="red"
                        @click="listing.revealDesc = false"
                        icon="mdi-close-circle"
                      >
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-expand-transition>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>

        <v-window-item value="appliedRoles">
          <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="(listing, index) in filteredAppliedRoles" :key="index">
              <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd; position: relative;">
                <!-- Close Button -->
                <v-btn icon class="cancel-button" style="margin-left: 4px; margin-top: 6px" @click="deleteApplication(listing)">
                  <v-icon color="#664229">mdi-close</v-icon>
                </v-btn>
                <div class="d-flex align-center justify-center department-icon-container">
                  <!-- Department Icon -->
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
                </div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ listing.role_name }}</div>
                <div class="text-center mt-2" style="color: #664229; font-size: 12px;">{{ listing.dept }} - {{ listing.country }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 5px; font-size: 12px;">Reporting Manager: {{ listing.reporting_manager }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">
                  Application Period: {{ new Date(listing.opening_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }} - {{ new Date(listing.closing_date).toLocaleDateString('en-US', { month: 'short', day: '2-digit', year: 'numeric' }) }}
                </div>
                <v-card-text>
                  <div class="text-center mt-2">
                    <v-chip
                      class="text-center"
                      color=#664229
                      style="font-size: 12px;"
                      @click="showSkillsOverlay(listing)"
                    >
                      Skills Required: {{ calculateSkillPercentage(listing.skills) }}
                    </v-chip>
                  </div>
                </v-card-text>
                <div class="text-center mt-3 mb-6">
                  <v-btn class="mx-auto px-4" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">
                    View Status
                  </v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>
        <skills-overlay v-model="skillsOverlay" :useAcquiredSkills="false" :calculateSkillPercentage=calculateSkillPercentage :acquiredSkills=acquiredSkills :getSkillIcon=getSkillIcon :listingData=listingData :closeSkillsOverlay=closeSkillsOverlay></skills-overlay>
        <cancel-application v-model="deleteApplicationOverlay" :role_name=deleteApplicationRoleName :close_overlay=closeDeleteApplicationOverlay></cancel-application>
        <error v-model="hasError" :close_overlay=closeErrorOverlay></error>
      </v-window>
    </v-card-text>
  </v-card>
</template>


<script>

import axios from'axios';
import SkillsOverlay from '../components/SkillsOverlay.vue';
import CancelApplication from '../components/CancelApplication.vue';
import Error from '../components/error.vue';
const isProduction = import.meta.env.PROD;
let apiUrl; // Declare apiUrl outside the conditional block

if (isProduction) {
  apiUrl = "http://spm-backend-lb-780988294.ap-southeast-1.elb.amazonaws.com";
} else {
  apiUrl = "http://localhost:5000";
}
export default {
  components: { SkillsOverlay, CancelApplication, Error },
 
  data: () => ({
    tab: 'availableRoles',
    selectedDepartment: 'All',
    selectedCountry: 'All',
    availableRoles: [],
    appliedRoles: [],
    skillsOverlay: false,
    deleteApplicationOverlay: false,
    deleteApplicationRoleName: null,
    id: '',
    showSkills: false,
    acquiredSkills: [],
    halfSkillsCount: 0,
    revealDesc: false,
    listingData: Object,
    hasError: false,
  }),
  mounted()
    {
      
    this.id = this.$cookies.get('staffId')
      axios.get(`${apiUrl}/application/${this.id}`).then(
        (response)=>{
          console.log(response.data.applied_role_listings)
          let temp_appliedRoles = []
          for (const [key,value] of Object.entries(response.data.applied_role_listings)){
            if (value[0].is_open){
              temp_appliedRoles.push(value[0])
            }
          }
          this.appliedRoles = temp_appliedRoles
          console.log(this.appliedRoles)
        }
      )
      axios.get(`${apiUrl}/listing/get_open_listings`)
      .then(
        (response)=>{
          this.availableRoles = response.data;
          if (response) {
            const roleRequests = response.data.map((role) => {
              return axios.get(`${apiUrl}/role/get_role_by_role_name/${role.role_name}`);
            });
            return Promise.all(roleRequests);
          }
        })
        .then((roleResponses) => {
          roleResponses.forEach((response, index) => {
            this.availableRoles[index]['role_desc'] = response.data.role_desc;
            this.availableRoles[index]['revealDesc'] = false;
          });
          console.log(this.availableRoles);
        }
      )
      axios.get(`${apiUrl}/staffskill/get_staff_skills/${this.id}`)
        .then((response) => {
          this.acquiredSkills = response.data
          this.halfSkillsCount = Math.ceil(this.acquiredSkills.length / 2);
        }
      )
    },
  computed: {
    departmentOptionsForAvailable() {
      const availableDepartments = [...this.availableRoles].map((role) => role.dept);
      const appliedDepartments = [...this.appliedRoles].map((role) => role.dept);
      appliedDepartments.forEach((dept) => {
        const index = availableDepartments.indexOf(dept);
        if (index !== -1) {
          availableDepartments.splice(index, 1);
        }
      });     
      const departments = [...new Set(availableDepartments)];
      return ['All', ...departments];
    },
    departmentOptionsForApplied() {
      const departments = [...new Set([...this.appliedRoles].map((role) => role.dept))];
      
      return ['All', ...departments];
    },
    countryOptionsForAvailable() {
      const availableCountries = [...this.availableRoles].map((role) => role.country);
      const appliedCountries = [...this.appliedRoles].map((role) => role.country);
      appliedCountries.forEach((country) => {
        const index = availableCountries.indexOf(country);
        if (index !== -1) {
          availableCountries.splice(index, 1);
        }
      });     
      const countries = [...new Set(availableCountries)];
      return ['All', ...countries];
    },
    countryOptionsForApplied() {
      const countries = [...new Set([...this.appliedRoles].map((role) => role.country))];
      return ['All', ...countries];
    },
    
    filteredAvailableRoles() {
    return this.availableRoles.filter((role) => {
      const departmentMatch = this.selectedDepartment === 'All' || role.dept === this.selectedDepartment;
      const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
      return departmentMatch && countryMatch && !this.getAppliedMatch(role);
    });
  },
  filteredAppliedRoles() {
    return this.availableRoles.filter((role) => {
      console.log(role)
      const departmentMatch = this.selectedDepartment === 'All' || role.dept === this.selectedDepartment;
      const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
      console.log(departmentMatch, countryMatch, this.getAppliedMatch(role))
      return departmentMatch && countryMatch && this.getAppliedMatch(role);
    });
  },
  },
  methods: {
    deleteApplication(listing){
      let application_data = {
        "role_listing": listing.id,
        "staff_id": this.id
      }
      axios.delete(`${apiUrl}/application`, {
        data: application_data
      }).then(
        (response) => {
          console.log(response)
          if (response.status === 201){
            this.deleteApplicationRoleName = listing.role_name;
            this.deleteApplicationOverlay = true;
          }
        }
      )
      .catch((err) => {
        console.log(err);
        this.hasError = true;
      })
    },
    closeDeleteApplicationOverlay(){
      this.deleteApplicationOverlay = false;
      location.reload();
    },
    closeErrorOverlay(){
      this.hasError = false;
    },
    getAppliedMatch(role) {
      for(const[key,value] of Object.entries(this.appliedRoles)){
        if(value.id == role.id){
          return true
        }
      }
      return false
    },
    showSkillsOverlay(listing) {
      this.listingData = listing
      this.skillsOverlay = true;
    },
    closeSkillsOverlay() {
      this.skillsOverlay = false;
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
      const acquiredSkillsCount = requiredSkillsArr.filter(skill => this.acquiredSkills.includes(skill)).length;

      if (totalSkills === 0) {
        return '0% (0 out of 0)';
      }

      const percentage = ((acquiredSkillsCount / totalSkills) * 100).toFixed(2);

      return `${percentage}% (${acquiredSkillsCount} out of ${totalSkills})`;
    },
    getSkillsRequired(requiredSkills){
      const requiredSkillsArr = requiredSkills.split(',').map(item => item.trim());
      console.log(requiredSkills)
      return requiredSkillsArr
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
</style>