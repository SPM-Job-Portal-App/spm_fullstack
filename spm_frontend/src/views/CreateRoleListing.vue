<template>
  <v-container class="my-10 py-12 custom-container">
    <v-responsive class="text-center">
      <!-- Title -->
      <h1 style="color: #664229;">Create Role Listing</h1>

      <!-- Job title -->
      <v-row justify="center">
        <v-col cols="8">
          <v-select v-model="RoleTitle" :items="roleOptions" label="Role Title" class="mt-4"></v-select>
        </v-col>
      </v-row>

      <!-- Department -->
      <v-row justify="center">
        <v-col cols="2"></v-col>
        <v-col cols="4" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left;">Department</h3>
          </div>
          <v-radio-group v-model="SelectedDept" style="margin-left: 10px">
            <v-radio v-for="dept in deptOptions" :label="dept" :value="dept"></v-radio>
          </v-radio-group>
        </v-col>

        <v-col cols="4" class="text-center">
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
            style="width: 100%;"
          ></v-select>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>

      <!-- Country of Opening and Reporting Manager -->
      <v-row justify="center">
        <v-col cols="2"></v-col>
        <v-col cols="4" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Country of Opening</h3>
          </div>
          <v-radio-group v-model="selectedCountry" style="margin-left: 10px">
            <v-radio v-for="country in countryOptions" :label="country" :value="country"></v-radio>
          </v-radio-group>
        </v-col>

        <v-col cols="4" class="text-center">
          <div class="mb-2">
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Reporting Manager</h3>
          </div>
          <v-select
            v-model="selectedReportingManager"
            :items="reportingManagers"
            label="Select Reporting Manager"
            class="custom-select"
            outlined
            style="width: 100%;"
          ></v-select>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>

      <!-- Cancel / Confirm -->
      <v-row justify="center" class="mt-8">
        <v-btn to="/openroles/hr" style="color: #664229;" class="mr-16 my-6 custom-button" @mouseover="hoverButton('cancel')" @mouseout="resetButtonColor('cancel')" large color="#c1ad98">
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

  <!-- success message with overlay -->
  <OverlayMessage
  :show.sync="successOverlay"
  title="Application Sent Successfully"
  :message="feedbackMessage"
  buttonText="Done"
  buttonColor="success"
  icon="mdi-check-circle"
  iconColor="success"
  iconSize="112"
  @close-overlay="toggleOverlay"
  route="/openroles/hr"
  ></OverlayMessage>

  <!-- failure message with overlay -->
  <OverlayMessage
  :show.sync="failureOverlay"
  title="Application Sent Unsuccessfully"
  :message="feedbackMessage"
  buttonText="Close"
  buttonColor="red"
  icon="mdi-close-circle"
  iconColor="red"
  iconSize="112"
  @close-overlay="toggleOverlay"
  route="/openroles/hr"
  ></OverlayMessage>
</template>

<script>
import axios from'axios';
import OverlayMessage from '../components/OverlayMessage.vue';
export default {
  data() {
    return {
      RoleTitle: '',
      roleOptions: ['Manager', 'Developer', 'Designer'],
      RoleDescription: '',
      deptOptions: ['Engineering', 'Product Management', 'Analytics', 'Marketing', 'Sales', 'HR', 'Others', 'Management', 'IT', 'Design'],
      SelectedDept: null,
      skillOptions: ['Python', 'HTML', 'CSS', 'JavaScript', 'PHP', 'C#', 'Ruby', 'Angular.js', 'Vue.js', 'Leadership', 'Communication', 'Programming', 'Web Development', 'Graphic Design', 'UI/UX'],
      selectedSkills: [],
      countryOptions: ['USA', 'UK', 'Canada', 'Singapore', 'Malaysia', 'Indonesia', 'Vietnam', 'Hong Kong'],
      selectedCountry: null,
      reportingManagers: ['None', '1'],
      selectedReportingManager: null,
      loading: false,
      successOverlay: false,
      failureOverlay: false,
      feedbackMessage: '',
    };
  },
  computed: {
    isConfirmButtonEnabled() {
      const isRoleTitleValid = this.RoleTitle.length != '';
      const isDeptSelected = this.SelectedDept != null;
      const isAtLeastOneSkillSelected = this.selectedSkills.length >= 1;
      const isCountrySelected = this.selectedCountry != null;
      const isReportingManagerSelected = this.selectedReportingManager != null;
      return (
        isRoleTitleValid &&
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
    toggleOverlay(){
      this.loading = false
      this.successOverlay = false
      this.failureOverlay = false
    },
    confirmRole() {
      if (this.isConfirmButtonEnabled) {
        this.loading = true
        const listing = {
          role_name: this.RoleTitle,
          skills: this.selectedSkills.join(', '),
          country: this.selectedCountry,
          dept: this.SelectedDept,
          reporting_manager: this.selectedReportingManager == 'None' ? null : parseInt(this.selectedReportingManager),
          is_open: true
        }
        axios.post('http://localhost:5000/listing/create', listing)
          .then(
            (response)=>{
                this.successOverlay = true
                if(response.data.message) {
                    this.feedbackMessage = response.data.message
                }
                else {
                    this.feedbackMessage = "You will be contacted shortly!"
                }
                console.log(response)
            }
          )
          .catch(error => {
            this.failureOverlay = true
            if(error.response.data.message) {
                    this.feedbackMessage = error.response.data.message
                }
            else {
                this.feedbackMessage = "An error occured during the application process!"
            }
            console.error(error);
          })
      }
    },
  },
  components: {
    OverlayMessage,
  },
};
</script>

<style>
.custom-container {
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
