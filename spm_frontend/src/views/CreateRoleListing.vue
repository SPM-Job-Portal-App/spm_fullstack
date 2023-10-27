<template>
  <v-container class="my-10 py-12 custom-container">
    <v-responsive class="text-center">
      <!-- Title -->
      <h1 style="color: #664229;">Create Role Listing</h1>

      <!-- Job title -->
      <v-row justify="center">
        <v-col cols="8">
          <div class="mb-2">
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Role Title</h3>
          </div>
          <v-select v-model="RoleTitle" :items="roleOptions" label="Select Role Title" outlined></v-select>
        </v-col>
      </v-row>

      <!-- Country of Opening and Reporting Manager -->
      <v-row justify="center">
        <v-col cols="2"></v-col>

        <v-col cols="8" class="text-center">
          <div class="mb-2">
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Reporting Manager</h3>
          </div>
          <v-select
            v-model="selectedReportingManager"
            :items="reportingManagers"
            label="Select Reporting Manager"
            outlined
            style="width: 100%;"
          ></v-select>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>

      <!-- Department -->
      <v-row justify="center">
        <v-col cols="2"></v-col>
        <v-col cols="4" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left;">Department</h3>
          </div>
          <v-select
            v-model="SelectedDept"
            :items="deptOptions"
            label="Select Department"
            outlined
          ></v-select>
        </v-col>

        <v-col cols="4" class="text-center">
          <div>
            <h3 style="color: #664229; text-align: left; font-size: 18px;">Country of Opening</h3>
          </div>
          <v-select
            v-model="selectedCountry"
            :items="countryOptions"
            label="Select Country of Opening"
            outlined
          ></v-select>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>

      <!-- Opening and Closing date -->
      <v-row justify="center">
        <v-col cols="2"></v-col>

        <v-col cols="4" class="text-center">
          <div class="text-center">
            <h3 style="color: #664229; font-size: 18px;">Opening Date</h3>
            <VDatePicker v-model="openingDate" :disabled-dates="disabledDates" mode="date" expanded />
          </div>
        </v-col>
        <v-col cols="4" class="text-center">
          <div class="text-center">
            <h3 style="color: #664229; font-size: 18px;">Closing Date</h3>
            <VDatePicker v-model="closingDate" :disabled-dates="disabledDates" mode="date" expanded />
          </div>
        </v-col>

        <v-col cols="2"></v-col>
      </v-row>

      <!-- Cancel / Confirm -->
      <v-row justify="center" class="mt-8">
        <v-btn to="/roles/hr" style="color: #664229;" class="mr-16 my-6 custom-button" @mouseover="hoverButton('cancel')" @mouseout="resetButtonColor('cancel')" large color="#c1ad98">
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
  route="/roles/hr"
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
  route="/roles/hr"
  ></OverlayMessage>
</template>

<script>
import axios from'axios';
import OverlayMessage from '../components/OverlayMessage.vue';
export default {
  data() {
    return {
      RoleTitle: '',
      SelectedDept: null,
      SelectedCountry: null,
      roleOptions: [],
      RoleDescription: '',
      deptOptions: [
        'Design',
        'Chariman',
        'CEO',
        'Sales',
        'Solutioning',
        'Engineering',
        'HR',
        'Finance',
        'Consultancy',
        'IT'
      ],
      SelectedDept: null,
      countryOptions: ['USA', 'UK', 'Canada', 'Singapore', 'Malaysia', 'Indonesia', 'Vietnam', 'Hong Kong'],
      selectedCountry: null,
      reportingManagers: ['None'],
      reportingManagersIds: [],
      selectedReportingManager: null,
      loading: false,
      successOverlay: false,
      failureOverlay: false,
      feedbackMessage: '',
      closingDate: new Date(),
      openingDate: new Date(),
      disabledDates: this.getDisabledDates(),
    };
  },
  mounted()
  {
    axios.get('http://localhost:5000/role').then(
        (response)=>{
          for(const idx in response.data.roles){
            this.roleOptions.push(response.data.roles[idx].Role)
          }
        }
      )
    axios.get('http://localhost:5000/staff/get_staff').then(
      (response)=>{
        for(const staff of response.data.staff){
          if(staff.Role == 3){
            this.reportingManagers.push(staff['Staff Name'])
            this.reportingManagersIds[staff['Staff Name']] = staff['Staff Id']
          }
        }
      }
    )
  },
  computed: {
    isConfirmButtonEnabled() {
      const isRoleTitleValid = this.RoleTitle.length != '';
      const isDeptSelected = this.SelectedDept != null;
      const isCountrySelected = this.selectedCountry != null;
      const isReportingManagerSelected = this.selectedReportingManager != null;
      const isDatesValid = this.openingDate <= this.closingDate;
      return (
        isRoleTitleValid &&
        isDeptSelected &&
        isCountrySelected &&
        isReportingManagerSelected &&
        isDatesValid
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
    getDisabledDates(){
      const currentDate = new Date()
      currentDate.setDate(currentDate.getDate() - 1)
      return [{ start: null, end: currentDate }]
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
          country: this.selectedCountry,
          dept: this.SelectedDept,
          reporting_manager: this.selectedReportingManager == 'None' ? null : this.reportingManagersIds[this.selectedReportingManager],
          is_open: true,
          opening_date: `${this.openingDate.getFullYear()}-${this.openingDate.getMonth()+1}-${this.openingDate.getDate()}`,
          closing_date: `${this.closingDate.getFullYear()}-${this.closingDate.getMonth()+1}-${this.closingDate.getDate()}`
        }
        console.log(listing)
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
  background-color: #eae4dd;
  height: 100;
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

</style>
