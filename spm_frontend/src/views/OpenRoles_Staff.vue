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
            :items="departmentOptions"
            label="Filter by Department"
            dense
          ></v-select>
        </v-col>
        <v-col cols="12" md="6">
        <!-- Filter by Country Dropdown -->
        <v-select
          v-model="selectedCountry"
          :items="countryOptions"
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
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
                </div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ listing.role_name }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">{{ listing.dept }} - {{ listing.country }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 12px;">Skills Required</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">
                  <v-chip
                    v-for="skill in listing.skills.split(', ')"
                    :key="skill"
                    :color="acquiredSkills.includes(skill) ? 'green' : 'red'"
                    :prepend-icon="getSkillIcon(skill)"
                    class="ma-1"
                    style="font-size: 12px;"
                  >
                    {{ skill }}
                  </v-chip>
                </div>
          
                <div class="text-center mt-3 mb-6">
                  <v-btn v-if="listing.is_open" class="mx-auto px-4" :to="{ name: 'Apply Open Roles', params: { id: listing.id } }" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Apply Now</v-btn>
                  <v-btn v-else class="mx-auto px-4" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Expired</v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>

        <v-window-item value="appliedRoles">
          <v-row>
            <v-col cols="12" sm="6" md="4" lg="3" v-for="(listing, index) in filteredAppliedRoles" :key="index">
              <!-- Listing Card with Margin for Applied Roles -->
            
              <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
                <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
                <div class="d-flex align-center justify-center department-icon-container">
                  <!-- Department Icon -->
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.dept) }}</v-icon>
                </div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 18px; font-weight: bold;">{{ listing.role_name }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">{{ listing.dept }} - {{ listing.country }}</div>
                <div class="text-center mt-2" style="color: #664229; padding-top: 10px; font-size: 12px;">Skills Required</div>
                <div class="text-center mt-2" style="color: #664229; padding-bottom: 10px; font-size: 12px;">
                  <v-chip
                    v-for="skill in listing.skills.split(', ')"
                    :key="skill"
                    :color="acquiredSkills.includes(skill) ? 'green' : 'red'"
                    :prepend-icon="getSkillIcon(skill)"
                    class="ma-1"
                    style="font-size: 12px;"
                  >
                    {{ skill }}
                  </v-chip>
                </div>
                
                <div class="text-center mt-3 mb-6">
                  <v-btn class="mx-auto px-4" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">View Status</v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>
      </v-window>
    </v-card-text>
  </v-card>
</template>


<script>
import axios from'axios';
export default {
 
  data: () => ({
    tab: 'availableRoles',
    selectedDepartment: 'All',
    selectedCountry: 'All',
    availableRoles: [],
    appliedRoles: [],
    id: 1,
    acquiredSkills: [
      'Python',
      'Vue.js',
      'HTML',
      'CSS',
      'JavaScript',
      'Communication',
      'Programming',
      'Web Development',
    ],
  }),
  mounted()
    {
      axios.get(`http://localhost:5000/application/${this.id}`).then(
        (response)=>{
          this.appliedRoles = response.data.applied_role_listings
          console.log(this.appliedRoles)
        }
      )
      axios.get('http://localhost:5000/listing').then(
        (response)=>{
          this.availableRoles = response.data[0];
          console.log(this.availableRoles)
        }
      )
    },
  computed: {
    departmentOptions() {
      const departments = [...new Set([...this.availableRoles, ...this.appliedRoles].map((role) => role.dept))];
      
      return ['All', ...departments];
    },
    countryOptions() {
      const countries = [...new Set([...this.availableRoles, ...this.appliedRoles].map((role) => role.country))];
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
    return this.appliedRoles.filter((role) => {
      const departmentMatch = this.selectedDepartment === 'All' || role.dept === this.selectedDepartment;
      const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
      const appliedMatch = this.appliedRoles.includes(role.id);
      return departmentMatch && countryMatch && this.getAppliedMatch(role);
    });
  },
  },
  methods: {
    getAppliedMatch(role) {
      for(const[key,value] of Object.entries(this.appliedRoles)){
        if(value.id == role.id){
          return true
        }
      }
      return false
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
</style>
