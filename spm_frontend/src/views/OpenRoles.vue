<template>
    <v-card>
      <v-tabs v-model="tab" bg-color="#664229">
        <v-tab value="availableRoles">Available Roles</v-tab>
        <v-tab value="appliedRoles">Applied Roles</v-tab>
      </v-tabs>
  
      <v-card-text>
        <v-row>
          <v-col cols="12" md="6">
            <v-select
              v-model="selectedDepartment"
              :items="departmentOptions"
              label="Filter by Department"
              @input="filterRoles"
              dense
            ></v-select>
          </v-col>
        </v-row>
  
        <v-window v-model="tab">
          <v-window-item value="availableRoles">
            <v-row>
              <v-col cols="4" v-for="(listing, index) in filteredAvailableRoles" :key="index">
                <!-- Listing Card with Margin -->
               
                <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
                  <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
                  <div class="d-flex align-center justify-center department-icon-container">
                    <!-- Department Icon -->
                    <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.department) }}</v-icon>
                  </div>
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px; font-weight: bold;">{{ listing.department }}</div>
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">{{ listing.label }}</div>
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">Skills : {{ listing.description }}</div>
            
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">{{ listing.skill }}</div>
                  <div class="text-center mt-3 mb-6">
                    <v-btn class="mx-auto px-4" @click="applyNow(index)" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Apply Now!</v-btn>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-window-item>
  
          <v-window-item value="appliedRoles">
            <v-row>
              <v-col cols="4" v-for="(listing, index) in filteredAppliedRoles" :key="index">
                <!-- Listing Card with Margin for Applied Roles -->
              
                <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
                  <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
                  <div class="d-flex align-center justify-center department-icon-container">
                    <!-- Department Icon -->
                    <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.department) }}</v-icon>
                  </div>
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px; font-weight: bold;">{{ listing.department }}</div>
                  <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">{{ listing.description }}</div>
                  
                  <div class="text-center mt-3 mb-6">
                    <v-btn class="mx-auto px-4" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Applied</v-btn>
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
      selectedDepartment: null,
      availableRoles: [],
      appliedRoles: [
    
      ],
    }),
    mounted()
      {
        axios.get('http://localhost:5000/role').then(
          (response)=>{
            this.availableRoles = response.data.roles;
            
            console.log(this.availableRoles[0])
            


          }
          
        )

      },
    computed: {
      departmentOptions() {
        const departments = [...new Set([...this.availableRoles, ...this.appliedRoles].map((role) => role.department))];
        
        return ['All', ...departments];
      },
      
      filteredAvailableRoles() {
        if (this.selectedDepartment === 'All' || !this.selectedDepartment) {
          return this.availableRoles;
        } else {
          return this.availableRoles.filter((role) => role.department === this.selectedDepartment);
        }
      },
      filteredAppliedRoles() {
        if (this.selectedDepartment === 'All' || !this.selectedDepartment) {
          return this.appliedRoles;
        } else {
          return this.appliedRoles.filter((role) => role.department === this.selectedDepartment);
        }
      },
    },
    methods: {
      applyNow(index) {
        console.log(`Applied for ${this.availableRoles[index].label}`);
      },
      filterRoles() {
      },
      getDepartmentIcon(department) {
        const departmentIcons = {
          Engineering: 'mdi-code-braces',
          'Product Management': 'mdi-chart-pie',
          Analytics: 'mdi-chart-bar',
          Marketing: 'mdi-bullhorn',
          Sales: 'mdi-cash-register',
          HR: 'mdi-account-supervisor',
          Others: 'mdi-account',
        };
        return departmentIcons[department] || 'mdi-help-circle';
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
