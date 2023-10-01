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
            <!-- Edit Button (Top Right) -->
            <v-btn icon class="edit-button" @click="editListing(index)">
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
                v-for="skill in listing.skills.split(', ')"
                :key="skill"
                :prepend-icon="getSkillIcon(skill)"
                class="ma-1"
                style="font-size: 12px;"
              >
                {{ skill }}
              </v-chip>
            </div>
            <div class="text-center mt-3 mb-6">
              <!-- Number of Applicants -->
              <v-btn @click="viewApplicants(index)" color="#ccbbaa" style="padding: 12px 20px; font-size: 18px;">
                View&nbsp; <span class="numapp">{{ listing.applicants.length }}</span> &nbsp;applicants
              </v-btn>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </template>
  
  <script>
  import axios from'axios';
  export default {
    data: () => ({
      selectedDepartment: "All",
      selectedCountry: "All",
      availableRoles: [
        // { department: 'Engineering', label: 'Software Engineer', numApplications:0, country:'Singapore',reportingmanager: 'John Doe'},
        // { department: 'Product Management', label: 'Product Manager', numApplications:7, country:'Singapore',reportingmanager: 'John Doe'},
        // { department: 'Analytics', label: 'Data Analyst', numApplications:4, country:'Indonesia',reportingmanager: 'John Doe'},
        // { department: 'Marketing', label: 'Marketing Specialist', numApplications:2, country:'Indonesia',reportingmanager: 'John Doe'},
        // { department: 'Sales', label: 'Sales Representative', numApplications:8, country: 'Vietnam',reportingmanager: 'John Doe'},
        // { department: 'Sales', label: 'Sales Associate', numApplications:3, country:'Indonesia',reportingmanager: 'John Doe'},
        // { department: 'HR', label: 'HR Coordinator', numApplications:9, country: 'Vietnam',reportingmanager: 'John Doe'},
      ],
      // appliedRoles: [
      //   { department: 'Sales', label: 'Sales Associate', numApplications:12,reportingmanager: 'John Doe'},
      //   { department: 'HR', label: 'HR Coordinator', numApplications:1,reportingmanager: 'John Doe'},
      // ],
    }),
    // created() {
    // // Listen for the 'listing-updated' event
    // EventBus.$on('listing-updated', (updatedListing) => {
    //   // Find the index of the updated listing in the 'availableRoles' array
    //   const index = this.availableRoles.findIndex((listing) => listing.label === updatedListing.label);

    //   if (index !== -1) {
    //     // Update the listing in the 'availableRoles' array
    //     this.availableRoles[index] = updatedListing;
    //   }
    // });
    // },
    mounted()
    {
      // axios.get(`http://localhost:5000/application/${this.id}`).then(
      //   (response)=>{
      //     this.appliedRoles = response.data.applied_role_listings
      //     console.log(this.appliedRoles)
      //   }
      // )
      axios.get('http://localhost:5000/application').then(
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

          // if (this.selectedDepartment === 'All' || !this.selectedDepartment) {
          // if (this.selectedCountry === 'All' || !this.selectedCountry) {
          //     return this.availableRoles;
          // } else {
          //     return this.availableRoles.filter((role) => role.country === this.selectedCountry);
          // }
          // } else {
          // if (this.selectedCountry === 'All' || !this.selectedCountry) {
          //     return this.availableRoles.filter((role) => role.department === this.selectedDepartment);
          // } else {
          //     return this.availableRoles.filter((role) =>
          //     role.department === this.selectedDepartment && role.country === this.selectedCountry
          //     );
          //     }
          // }
      },
    },
    methods: {
      applyNow(index) {
        console.log(`Applied for ${this.availableRoles[index].label}`);
      },
      editListing(index) {
        const selectedListing = this.filteredAvailableRoles[index];
        console.log(`Editing ${selectedListing.label}`);
        this.$router.push({ name: 'edit-listing', params: { index } });
        },
      getDepartmentIcon(department) {
        const departmentIcons = {
          'Engineering': 'mdi-code-braces',
        'Product Management': 'mdi-chart-pie',
        'Analytics': 'mdi-chart-bar',
        'Marketing': 'mdi-bullhorn',
        'Sales': 'mdi-cash-register',
        'HR': 'mdi-account-supervisor',
        'Others': 'mdi-account',
        'Management': 'mdi-compass',
        'IT': 'mdi-monitor',
        'Design': 'mdi-palette'
        };
        return departmentIcons[department] || 'mdi-help-circle';
      },
      getSkillIcon(skill) {
      const skillIcons = {
        'Python': 'mdi-language-python',
        'HTML': 'mdi-language-html5',
        'CSS': 'mdi-language-css3',
        'JavaScript': 'mdi-language-javascript',
        'PHP': 'mdi-language-php',
        'C#': 'mdi-language-c',
        'Ruby': 'mdi-language-ruby',
        'Angular.js': 'mdi-angularjs',
        'Vue.js': 'mdi-vuejs',
        'Leadership': 'mdi-chess-king',
        'Communication': 'mdi-message-outline',
        'Programming': 'mdi-code-braces',
        'Web Development': 'mdi-web',
        'Graphic Design': 'mdi-draw',
        'UI/UX': 'mdi-table-account'
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

  .numapp {
    font-weight: bold;
    /* font-size: 24px; */
  }

  </style>