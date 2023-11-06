<template>
    <v-card class height="100%">
      <!-- Title -->
      <h1 class="page-title ml-8">Applicants</h1>
  
      <v-row>
        <v-col cols="12" md="5">
          <!-- Filter by Department Dropdown -->
          <v-select
            v-model="selectedDepartment"
            :items="departmentOptions"
            label="Filter by Department"
            dense
            class="ml-8"
          ></v-select>
        </v-col>

        <v-col cols="12" md="5">
          <!-- Filter by Country Dropdown -->
          <v-select
            v-model="selectedCountry"
            :items="countryOptions"
            label="Filter by Country"
            dense
            class="ml-8"
          ></v-select>
        </v-col>

        <v-col cols="12" md="1" class="d-flex justify-center">
          <v-btn icon @click="sortApplicants()" :color="sort ? '#eae4dd' : 'white'">
            <v-icon>mdi-filter-variant</v-icon>
          </v-btn>
        </v-col>
      </v-row>
  
      <v-row v-if="applicants.length > 0" class="ml-4">
        <v-col cols="12" sm="6" md="4" lg="3" v-for="(applicant, index) in filteredApplicants" :key="index">
          <!-- Applicant Card with Margin -->
          <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
            <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
            <div class="d-flex align-center justify-center department-icon-container">
              <!-- Department Icon -->
              <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(applicant.dept) }}</v-icon>
            </div>
            <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ applicant.staff_first_name }} {{ applicant.staff_last_name }}</div>
            <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">{{ applicant.dept }} - {{ applicant.country }}</div>
            <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">{{ applicant.email }}</div>
            <v-card-text>
              <div class="text-center mt-2">
                <v-chip
                  class="text-center"
                  color=#664229
                  style="font-size: 12px;"
                  @click="showApplicantSkillsOverlay(applicant.skills)"
                >
                  Show Applicant Skills
                </v-chip>
              </div>
              <div class="text-center mt-2">
                <v-chip
                  class="text-center"
                  color=#664229
                  style="font-size: 12px;"
                  @click="showSkillsOverlay(applicant.skills)"
                >
                  Skills Matched: {{ calculateSkillPercentage(applicant.skills) }}
                </v-chip>
              </div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-else-if="loading" class="d-flex align-center justify-center h-75">
        <v-col cols="auto">
          <h2>Loading...</h2>
        </v-col>
      </v-row>
      <v-row v-else class="d-flex align-center justify-center h-75">
        <v-col cols="auto">
          <h2>No Applicants</h2>
        </v-col>
      </v-row>
    </v-card>
    <skills-overlay v-model="skillsOverlay" :useAcquiredSkills="true" :calculateSkillPercentage=calculateSkillPercentage :acquiredSkills=acquiredSkills :getSkillIcon=getSkillIcon :listingData=listingData :closeSkillsOverlay=closeSkillsOverlay></skills-overlay>
    <v-overlay v-model="applicantSkillsOverlay" class="align-center justify-center">
      <v-sheet
        elevation="12"
        max-width="800"
        rounded="lg"
        width="100%"
        class="pa-4 text-center mx-auto"
        style="background-color: #eae4dd; color: #664229; overflow-y: auto; max-height: 80vh;"
      >
        <h2 class="text-h5 mb-6 sheet-header">Applicant Skills</h2>
        <div class="text-medium-emphasis text-body-2">
          <ul v-if="acquiredSkills.length != 0" style="margin-top: 15px; list-style-type: none">
            <li class="skill-row" v-for="skill in acquiredSkills" :key="skill">
              <v-chip
                :prepend-icon="getSkillIcon(skill)"
                class="ma-1"
                style="font-size: 12px; color: #664229;"
              >
              {{skill}}
              </v-chip>
            </li>
          </ul>
          <b v-else>No skills!</b>
        </div>
        <v-divider class="mb-4"></v-divider>
        <div class="text-end">
          <v-btn
            class="text-none"
            rounded
            variant="flat"
            width="90"
            @click="closeApplicantSkillsOverlay"
          >
            Close
          </v-btn>
        </div>
      </v-sheet>
    </v-overlay>
  </template>
  
  <script>
  import axios from'axios';
  import SkillsOverlay from '../components/SkillsOverlay.vue';
  const isProduction = import.meta.env.PROD;
  if(isProduction){
    var apiUrl = "http://spm-backend-lb-780988294.ap-southeast-1.elb.amazonaws.com"
  }
  else{
    var apiUrl = "http://localhost:5000"
  }
  export default {
    components: {SkillsOverlay},
    data: () => ({
      selectedDepartment: "All",
      selectedCountry: "All",
      staffIds: [],
      applicants: [],
      roleListingId: null,
      acquiredSkills: null,
      listing: null,
      skillsOverlay: false,
      applicantSkillsOverlay: false,
      showSkills: false,
      listingData: Object,
      loading: true,
      sort: true
    }),
    mounted()
    {
      this.roleListingId = this.$route.params.id
      axios.get(`${apiUrl}/listing/${this.roleListingId}`)
      .then(
        (response)=>{
          this.listing = response.data;
          if (this.listing) {
            axios.get(`${apiUrl}/roleskill/get_skills_by_role_name/${this.listing.role_name}`)
            .then(
              (res)=>{
                this.listing['skills'] = res.data || [];
                console.log(this.listing);
              }
            )
          }
        }
      )
      axios.get(`${apiUrl}/application/get_applicants/${this.roleListingId}`)
      .then(
        (response,)=>{
          this.staffIds = response.data.applicants_list;
          if (this.staffIds) {
            const requests = this.staffIds.map((staffId) => {
              return axios.get(`${apiUrl}/staff/get_staff_by_id/${staffId}`)
              .then(
                (res)=>{
                  if(res.data && res){
                    const tempApplicant = res.data;
                    tempApplicant['id'] = staffId
                    return axios.get(`${apiUrl}/staffskill/get_staff_skills/${staffId}`)
                    .then(
                      (r)=>{
                        tempApplicant['skills'] = r.data;
                        if(this.listing != null && this.listing.skills != null){
                          const requiredSkillsArr = this.listing.skills;
                          const totalSkills = requiredSkillsArr.length;
                          const acquiredSkillsCount = requiredSkillsArr.filter(skill => tempApplicant['skills'].includes(skill)).length;
                          const percentage = ((acquiredSkillsCount / totalSkills) * 100).toFixed(2);
                          tempApplicant['skillsMatch'] = parseFloat(percentage)
                        }
                        this.applicants.push(tempApplicant);
                      }
                    )
                  }
                }
              )
            })
            Promise.all(requests)
              .then(() => {
                this.loading = false;
                console.log(this.applicants);
              })
              .catch(() => {
                this.loading = false;
              })
          }
        }
      )
      .catch(() => {
        this.loading = false;
      })
    },
    computed: {
      departmentOptions() {
        const departments = [...new Set(this.applicants.map((applicant) => applicant.dept))];
        return ['All', ...departments];
      },
      countryOptions() {
          const countries = [...new Set(this.applicants.map((applicant) => applicant.country))];
          console.log(countries); 
          return ['All', ...countries];
      },
      filteredApplicants() {
        const filtered = this.applicants.filter((applicant) => {
          const departmentMatch = this.selectedDepartment === 'All' || applicant.dept === this.selectedDepartment;
          const countryMatch = this.selectedCountry === 'All' || applicant.country === this.selectedCountry;
          return departmentMatch && countryMatch;
        });
        if(this.sort) {
          return filtered.sort((a,b) => b.skillsMatch - a.skillsMatch);
        } else {
          return filtered.sort((a,b) => a.skillsMatch - b.skillsMatch);
        }
      },
    },
    methods: {
      sortApplicants() {
        this.sort = !this.sort
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
      calculateSkillPercentage(acquiredSkills) {
        if(this.listing != null && this.listing.skills != null && acquiredSkills != undefined){
          const requiredSkillsArr = this.listing.skills;
          console.log('requiredSkillsArr',requiredSkillsArr)
          const totalSkills = requiredSkillsArr.length;
          const acquiredSkillsCount = requiredSkillsArr.filter(skill => acquiredSkills.includes(skill)).length;
  
          if (totalSkills === 0) {
            return '0% (0 out of 0)';
          }
  
          const percentage = ((acquiredSkillsCount / totalSkills) * 100).toFixed(2);
  
          return `${percentage}% (${acquiredSkillsCount} out of ${totalSkills})`;
        }
      },
      showSkillsOverlay(acquiredSkills) {
        const tempListingData = { ...this.listing };
        if (Array.isArray(tempListingData.skills)) {
          tempListingData.skills = tempListingData.skills.join(',');
        }
        this.listingData = tempListingData
        this.acquiredSkills = acquiredSkills
        this.skillsOverlay = true;
      },
      closeSkillsOverlay() {
        this.skillsOverlay = false;
      },
      closeApplicantSkillsOverlay() {
        this.applicantSkillsOverlay = false;
      },
      showApplicantSkillsOverlay(acquiredSkills) {
        this.applicantSkillsOverlay = true;
        this.acquiredSkills = acquiredSkills;
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
  </style>