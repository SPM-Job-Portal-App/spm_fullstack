<template>
  <v-container class="my-10 py-12 custom-container">
    <v-responsive class="text-center">
      <!-- Title -->
      <h1 style="color: #664229;">Create Role Listing</h1>

      <!-- Job title -->
      <v-row justify="center">
        <v-col cols="8">
          <v-text-field
            label="Role Title"
            v-model="RoleTitle"
            outlined
            class="mt-4 ml-4 mr-4"
          ></v-text-field>
        </v-col>
      </v-row>

      <!-- Job description -->
      <v-row justify="center">
        <v-col cols="8">
          <v-text-field
            label="Role Description"
            v-model="RoleDescription"
            outlined
            class="ml-4 mr-4"
          ></v-text-field>
        </v-col>
      </v-row>

      <!-- Department -->
      <v-row justify="center">
        <v-col cols="3"></v-col>
        <v-col cols="2" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left;">Department</h3>
          </div>
          <v-radio-group v-model="SelectedDept" style="margin-left: 10px">
            <v-radio label="Marketing" value="Marketing"></v-radio>
            <v-radio label="Finance" value="Finance"></v-radio>
            <v-radio label="Human Resources" value="Human Resources"></v-radio>
            <v-radio label="Add More Later" value="Add More Later"></v-radio>
          </v-radio-group>
        </v-col>

        <v-col cols="5" class="text-center">
          <div class="mb-2">
            <h3 style="color: #664229; text-align: left;">Required Skills</h3>
          </div>
          <v-select
            v-model="selectedSkills"
            :items="skillOptions"
            label="Select required skills"
            multiple
            outlined
            chips
            small-chips
            class="custom-select"
          ></v-select>
        </v-col>
      </v-row>

      <!-- Country of Opening and Reporting Manager -->
      <v-row justify="center">
        <v-col cols="3"></v-col>
        <v-col cols="2" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Country of Opening</h3>
          </div>
          <v-radio-group v-model="selectedCountry" style="margin-left: 10px">
            <v-radio label="Singapore" value="Singapore"></v-radio>
            <v-radio label="Malaysia" value="Malaysia"></v-radio>
            <v-radio label="Indonesia" value="Indonesia"></v-radio>
            <v-radio label="Vietnam" value="Vietnam"></v-radio>
            <v-radio label="Hong Kong" value="Hong Kong"></v-radio>
          </v-radio-group>
        </v-col>

        <v-col cols="5" class="text-center">
          <div class="mb-2">
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Reporting Manager</h3>
          </div>
          <v-select
            v-model="selectedReportingManager"
            :items="reportingManagers"
            label="Select Reporting Manager"
            class="custom-select"
            outlined
          ></v-select>
        </v-col>
      </v-row>

      <!-- Cancel / Confirm -->
      <v-row justify="center" class="mt-8">
        <v-btn style="color: #664229;" class="mr-16 my-6 custom-button" @mouseover="hoverButton('cancel')" @mouseout="resetButtonColor('cancel')" large color="#c1ad98">
          Cancel
        </v-btn>
        <v-btn
          :style="{ backgroundColor: isConfirmButtonEnabled ? '#ccbbaa' : '#d6c8bb' }"
          class="my-6 custom-button"
          @mouseover="hoverButton('confirm')"
          @mouseout="resetButtonColor('confirm')"
          large
          :disabled="!isConfirmButtonEnabled"
          @click="confirmRole"
        >
          Confirm
        </v-btn>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      RoleTitle: '',
      RoleDescription: '',
      SelectedDept: null,
      skillOptions: ['Python','MySQL','Java','Javascript','Excel'],
      selectedSkills: [],
      selectedCountry: null,
      reportingManagers: ['Manager 1', 'Manager 2', 'Manager 3', 'Manager 4', 'Manager 5'],
      selectedReportingManager: null,
    };
  },
  computed: {
    isConfirmButtonEnabled() {
      const isRoleTitleValid = this.RoleTitle.length >= 1;
      const isRoleDescriptionValid = this.RoleDescription.length >= 1;
      const isDeptSelected = !!this.SelectedDept;
      const isAtLeastOneSkillSelected = this.selectedSkills.length >= 1;
      const isCountrySelected = !!this.selectedCountry;
      const isReportingManagerSelected = !!this.selectedReportingManager;

      return (
        isRoleTitleValid &&
        isRoleDescriptionValid &&
        isDeptSelected &&
        isAtLeastOneSkillSelected &&
        isCountrySelected &&
        isReportingManagerSelected
      );
    },
  },
  methods: {
    hoverButton(buttonType) {
      // Handle button hover styling
    },
    resetButtonColor(buttonType) {
      // Reset button color after hover
    },
    confirmRole() {
      if (this.isConfirmButtonEnabled) {
        console.log('Role confirmed!');
      }
    },
  },
};
</script>

<style>
.custom-container {
  background-color: #eae4dd;
  height: 100vh;
  margin-left: 10%;
  max-width: 80%;
  margin-right: auto;
}

.custom-button {
  background-color: #ccbbaa;
  padding: 10px 20px;
  width: 200px;
  height: 200px;
}

.custom-button-disabled {
  background-color: #ccc;
  color: #888;
}

.custom-select {
  width: 60%;
}
</style>
