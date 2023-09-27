<template>
    <v-card class>
      <!-- Title -->
      <h1 class="page-title ml-8">Available Jobs</h1>
  
      <v-row>
        <v-col cols="12" md="6">
          <v-select
            v-model="selectedDepartment"
            :items="departmentOptions"
            label="Filter by Department"
            @input="filterRoles"
            dense
            class="ml-8"
          ></v-select>
        </v-col>
      </v-row>
  
      <v-row class="ml-4">
        <v-col cols="4" v-for="(listing, index) in filteredAvailableRoles" :key="index">
          <!-- Listing Card with Margin -->
          <v-card class="mt-3 mb-2 ml-1 mr-8" style="background-color: #eae4dd;">
            <!-- Edit Button (Top Right) -->
            <v-btn icon class="edit-button" @click="editListing(index)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
            <div class="d-flex align-center justify-center department-icon-container">
              <!-- Department Icon -->
              <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.department) }}</v-icon>
            </div>
            <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px; font-weight: bold;">{{ listing.department }}</div>
            <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">{{ listing.label }}</div>
            <div class="text-center mt-3 mb-6">
              <!-- Number of Applicants -->
              <v-btn @click="viewApplicants(index)" color="#ccbbaa" style="padding: 12px 20px; font-size: 18px;">
                View&nbsp; <span class="numapp">{{ listing.numApplications }}</span> &nbsp;applicants
              </v-btn>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </template>
  
  <script>
  export default {
    data: () => ({
      selectedDepartment: null,
      availableRoles: [
        { department: 'Engineering', label: 'Software Engineer', numApplications:0},
        { department: 'Product Management', label: 'Product Manager', numApplications:7 },
        { department: 'Analytics', label: 'Data Analyst', numApplications:4 },
        { department: 'Marketing', label: 'Marketing Specialist', numApplications:2 },
        { department: 'Sales', label: 'Sales Representative', numApplications:8 },
        { department: 'Sales', label: 'Sales Associate', numApplications:3},
        { department: 'HR', label: 'HR Coordinator', numApplications:9},
      ],
      appliedRoles: [
        { department: 'Sales', label: 'Sales Associate', numApplications:12},
        { department: 'HR', label: 'HR Coordinator', numApplications:1},
      ],
    }),
    computed: {
      departmentOptions() {
        const departments = [...new Set(this.availableRoles.map((role) => role.department))];
        return ['All', ...departments];
      },
      filteredAvailableRoles() {
        if (this.selectedDepartment === 'All' || !this.selectedDepartment) {
          return this.availableRoles;
        } else {
          return this.availableRoles.filter((role) => role.department === this.selectedDepartment);
        }
      },
    },
    methods: {
      applyNow(index) {
        console.log(`Applied for ${this.availableRoles[index].label}`);
      },
      filterRoles() {
        // Add logic to filter roles based on selected department
      },
      editListing(index) {
        // Handle the edit button click for the role at the specified index.
        this.$router.push({ name: 'edit-listing', params: { index } });
        console.log(`Editing ${this.filteredAvailableRoles[index].label}`);
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
      getRandomApplicants() {
        // Generate random number of applicants (between 1 and 10) for each role listing
        return Math.floor(Math.random() * 10) + 1;
      },
    },
  };
  </script>
  
  <style scoped>
  .page-title {
    color: #664229;
    font-size: 24px;
    font-weight: bold;
    margin: 20px 0;
  }
  
  .department-icon-container {
    height: 200px;
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
    font-size: 24px;
  }

  </style>
  