<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height custom-box">
      <h1 class="text-h5 font-weight-bold mb-5">Welcome to the Job Application Portal</h1>
      <p> The job application portal for staff to apply for the role that
      they would like to apply for and to be able to see their match based on their current skill set which
      they have gained and stored in LJPS with the skill set of that role. HR and the recruiting manager will
      then be able to see the skills set of the applicants based on the courses that they have taken with the
      skills set added into their profile by the L&D team. The HR team will be able to list out the open roles.
      </p>
      <v-form ref="form" class="mt-5">
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="staffId"
              label="Staff ID"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="password"
              label="Password"
              type="password"
              required
            ></v-text-field>
          </v-col>
        </v-row>
        <div class="d-flex justify-center">
          <v-btn
            color="success"
            class="mt-4 w-25"
            @click="submitForm"
            :loading="loading"
          >
            Login
          </v-btn>
        </div>
        <div class="d-flex justify-center mt-5">
          <p class="text-disabled">You are currently logged in as staff ID {{ initialStaffId }} with role {{ roles[initialStaffRole] }}</p>
        </div>
      </v-form>
      <!-- success message with overlay -->
      <OverlayMessage
        :show.sync="successOverlay"
        title="Login Successful"
        :message="feedbackMessage"
        buttonText="Done"
        buttonColor="success"
        icon="mdi-check-circle"
        iconColor="success"
        iconSize="112"
        @close-overlay="toggleOverlay"
        route="/"
      ></OverlayMessage>
      <!-- failure message with overlay -->
      <OverlayMessage
        :show.sync="failureOverlay"
        title="Login Unsuccessful"
        :message="feedbackMessage"
        buttonText="Close"
        buttonColor="red"
        icon="mdi-close-circle"
        iconColor="red"
        iconSize="112"
        @close-overlay="toggleOverlay"
        route="/"
      ></OverlayMessage>
    </v-responsive>
  </v-container>
</template>

<script>
  import OverlayMessage from '../components/OverlayMessage.vue';
  import axios from 'axios'

  export default {
    data: () => ({
      staffId: '',
      initialStaffId: '',
      initialStaffRole: '',
      password: '',
      loading: false,
      successOverlay: false,
      failureOverlay: false,
      feedbackMessage: '',
      roleId: '',
      object: '',
      roles: {1: "Admin", 2: "User", 3: "Manager", 4: "HR"},
      staffRole: ''
      // staffIdRules: [
      //   v => (v || '').length > 0 || 'Staff ID is required',
      // ],
      // passwordRules: [
      //   v => (v || '').length > 0 || 'Password is required',
      // ],
    }),
    mounted() {
      if(this.$cookies.get('staffId')){
        this.staffId = this.$cookies.get('staffId')
        this.initialStaffId = this.staffId
      }
      if(this.$cookies.get('roleId')){
        this.roleId = this.$cookies.get('roleId')
      }
      if(this.$cookies.get('staffRole')){
        this.staffRole = this.$cookies.get('staffRole')
        this.initialStaffRole = this.staffRole
      }
    },
    methods: {
      submitForm () {
        this.loading = true
        axios.get(`http://localhost:5000/staff/get_staff_by_id/${this.staffId}`)
        .then(
          (response)=>{
            console.log(response.data)
            this.object = response.data
            if(this.$cookies.get('roleId') && response.data){
              this.$cookies.set('staffId', this.staffId, { expires: '1D', path: '/' });
              this.$cookies.set('staffRole', this.object.role, { expires: '1D', path: '/' });
              this.initialStaffId = this.staffId
              this.initialStaffRole = this.object.role
              this.successOverlay = true
              this.feedbackMessage = `Welcome ${response.data.staff_first_name}`
            }
          }
        )
        .catch(
          (error)=>{
            console.log(error)
            this.failureOverlay = true
            this.feedbackMessage = 'User does not exist'
          }
        )
      },
      // isValid() {
      //   if(this.$refs.form){
      //       return this.$refs.form.validate()
      //   }
      // },
      toggleOverlay() {
        this.loading = false
        this.successOverlay = false
        this.failureOverlay = false
      },
    },
    components: {
        OverlayMessage,
    },
  }
</script>

<style scoped>
  .custom-box {
    padding: 20%;
  }
</style>