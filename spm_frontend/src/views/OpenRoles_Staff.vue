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
            @input="filterRoles"
            dense
          ></v-select>
        </v-col>
        <v-col cols="12" md="6">
          <!-- Filter by Country Dropdown -->
          <v-select
            v-model="selectedCountry"
            :items="countryOptions"
            label="Filter by Country"
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
                <div class="text-center" style="color:#664229; font-size: 18px; font-weight: bold;">
                  {{ listing.label }}
                </div>
                <div class="text-center mt-7" style="color:#8C7251; padding: 10px; font-size: 18px;">
                  <b>Department:</b> {{ listing.department }}
                </div>
                <div class="text-center mt-2" style="color: #8C7251; padding: 10px; font-size: 18px;">
                  <b>Description:</b> Lorem ipsum lorem ipsum
                </div>
                <div class="text-center mt-2" style="color: #8C7251; padding: 10px; font-size: 18px;">
                  <b>Country of Opening:</b> {{ listing.country }}
                </div>
                <div class="text-center mt-2" style="color:#8C7251 ; padding: 10px; font-size: 18px;">
                  <b>Reporting Manager:</b> {{ getReportingManager() }}
                </div>
                <div class="text-center mt-3 mb-6">
                  <v-btn class="mx-auto px-4" @click="applyNow(index)" color="#ccbbaa" style="padding: 10px 0; font-size: 18px; margin-top:3px">Apply Now!</v-btn>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-window-item>

        <v-window-item value="appliedRoles">
          <v-row>
            <v-col cols="4" v-for="(listing, index) in filteredAppliedRoles" :key="index">
              <!-- Listing Card with Margin for Applied Roles -->
              <v-card class="mt-6 mb-2 ml-1 mr-8" style="background-color: #eae4dd; width: 250px; height: 400px;">
                <!-- Department Icon Container (Centered Both Vertically and Horizontally) -->
                <div class="d-flex align-center justify-center department-icon-container">
                  <!-- Department Icon -->
                  <v-icon class="department-icon" color="#664229">{{ getDepartmentIcon(listing.department) }}</v-icon>
                </div>
                <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px; font-weight: bold;">
                  {{ listing.label }}
                </div>
                <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">
                  <b>Department:</b> {{ listing.department }}
                </div>
                <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">
                  <b>Description:</b> {{ listing.description }}
                </div>
                <div class="text-center mt-2" style="color: #664229; padding: 10px; font-size: 18px;">
                  <b>Country of Opening:</b> {{ listing.country }}
                </div>
                <div class="text-center mt-2" style="color:#8C7251 ; padding: 10px; font-size: 18px;">
                  <b>Reporting Manager:</b> {{ listing.reportingmanager }}
                </div>
                <div class="text-center mt-3 mb-6">
                  <v-btn class="mx-auto px-4" @click="applyToAppliedRole(index)" color="#ccbbaa" style="padding: 10px 0; font-size: 18px;">Applied</v-btn>
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
export default {
  data: () => ({
    tab: 'availableRoles',
    selectedDepartment: 'All',
    selectedCountry: 'All',
    availableRoles: [
      { department: 'Engineering', label: 'Software Engineer', country: 'Singapore',reportingmanager: 'John Doe'},
      { department: 'Product Management', label: 'Product Manager', country: 'Indonesia',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      { department: 'Analytics', label: 'Data Analyst', country: 'Vietnam',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      { department: 'Sales', label: 'Sales Associate', country: 'Singapore',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      { department: 'HR', label: 'HR Coordinator', country: 'Indonesia',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      // Add more roles with department and country properties
    ],
    appliedRoles: [
      { department: 'Sales', label: 'Sales Associate', country: 'Singapore',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      { department: 'HR', label: 'HR Coordinator', country: 'Indonesia',reportingmanager: 'John Doe',description:'Lorem ipsum lorem ipsum'},
      // Add more applied roles with department and country properties
    ],
  }),
  computed: {
    departmentOptions() {
      const departments = [...new Set([...this.availableRoles, ...this.appliedRoles].map((role) => role.department))];
      return ['All', ...departments];
    },
    countryOptions() {
      const countries = [...new Set([...this.availableRoles, ...this.appliedRoles].map((role) => role.country))];
      return ['All', ...countries];
    },
    filteredAvailableRoles() {
      return this.availableRoles.filter((role) => {
        const departmentMatch = this.selectedDepartment === 'All' || role.department === this.selectedDepartment;
        const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
        return departmentMatch && countryMatch;
      });
    },
    filteredAppliedRoles() {
      return this.appliedRoles.filter((role) => {
        const departmentMatch = this.selectedDepartment === 'All' || role.department === this.selectedDepartment;
        const countryMatch = this.selectedCountry === 'All' || role.country === this.selectedCountry;
        return departmentMatch && countryMatch;
      });
    },
  },
  methods: {
    applyNow(index) {
      console.log(`Applied for ${this.filteredAvailableRoles[index].label}`);
    },
    applyToAppliedRole(index) {
      console.log(`Applied for ${this.filteredAppliedRoles[index].label}`);
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
    getReportingManager() {
      // Replace with your logic to get the reporting manager
      return 'Reporting Manager';
    },
  },
};
</script>

<style scoped>
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
