

<template>
    <v-container class="fill-height">
        <v-responsive class="align-center text-center fill-height">

                <!-- Apply for role listing form -->
                <v-sheet max-width="600" class="mx-auto">
                <h4 class="text-h5 font-weight-bold mb-4">Apply for role listing</h4>
                <p class="mb-4"><v-icon icon="mdi-face-man"></v-icon> Your profile will be automatically sent as part of the application!</p>
                <v-form ref="form">
                    <!-- pre-populated name fields -->
                    <v-row>
                        <v-col cols="6">
                            <v-text-field
                            v-model="firstName"
                            label="First name"
                            disabled
                            ></v-text-field>
                        </v-col>
                        <v-col cols="6">
                            <v-text-field
                            v-model="lastName"
                            label="Last name"
                            disabled
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <!-- pre-populated country and dept fields -->
                    <v-row>
                        <v-col cols="6">
                            <v-text-field
                            v-model="country"
                            label="Country"
                            disabled
                            ></v-text-field>
                        </v-col>
                        <v-col cols="6">
                            <v-text-field
                            v-model="deparment"
                            label="Department"
                            disabled
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <!-- pre-populated email fields -->
                    <v-row>
                        <v-col cols='12'>
                            <v-text-field
                            v-model="email"
                            label="Email"
                            disabled
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <!-- pre-populated skills field -->
                    <v-row>
                        <v-col cols="12" class="text-grey-lighten-1">Skills</v-col>
                        <v-col cols="12">
                            <v-chip
                                v-if="acquiredSkills.length != 0"
                                v-for="acquiredSkill in acquiredSkills"
                                :key="acquiredSkill"
                                :prepend-icon="getSkillIcon(acquiredSkill)"
                                class="ma-1"
                                disabled
                                @click="showSkillInfo(acquiredSkill)"
                            >
                                {{ acquiredSkill }}
                            </v-chip>
                            <v-chip
                                v-else
                                class="ma-1"
                                disabled
                            >
                                None
                            </v-chip>
                        </v-col>
                    </v-row>
                    <!-- form submit button -->
                    <v-row>
                        <v-col>
                            <v-btn @click="submitForm" class="text-white" color="#ccbbaa" :loading="loading">
                                Apply
                                <v-icon icon="mdi-chevron-right" end></v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                </v-form>
                </v-sheet>

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
                    route="/openroles/staff"
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
                    route="/openroles/staff"
                ></OverlayMessage>

        </v-responsive>
      </v-container>
</template>

<script>
const isProduction = import.meta.env.PROD;
   if(isProduction){
    var apiUrl = "http://spm-backend-lb-780988294.ap-southeast-1.elb.amazonaws.com"
  }
  else{
    var apiUrl = "http://localhost:5000"
  }

    import OverlayMessage from '../components/OverlayMessage.vue';
    import axios from 'axios'

    export default {
        data: () => ({
            firstName: '',
            lastName: '',
            email: '',
            country: '',
            deparment: '',
            id: '',
            acquiredSkills: [],
            loading: false,
            successOverlay: false,
            failureOverlay: false,
            listingData: [],
            feedbackMessage: ''
        }),
        mounted() {
            this.id = this.$cookies.get('staffId')
            axios.get(`${apiUrl}/staff/get_staff_by_id/${this.id}`).then(
                (response)=>{
                    this.firstName = response.data.staff_first_name;
                    this.lastName = response.data.staff_last_name;
                    this.email = response.data.email;
                    this.country = response.data.country;
                    this.deparment = response.data.dept;
                }
            )
            if(this.id) {
                axios.get(`${apiUrl}/staffskill/get_staff_skills/${this.id}`).then(
                    (response)=>{
                        this.acquiredSkills = response.data;
                    }
                )
            }
        },
        methods: {
            submitForm() {
                this.loading = true
                const id = this.$route.params.id;
                let application_data = {
                    "role_listing": id,
                    "staff_id": this.id
                }
                axios.post(`${apiUrl}/application`, application_data)
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
            },
            toggleOverlay() {
                this.loading = false
                this.successOverlay = false
                this.failureOverlay = false
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
        components: {
            OverlayMessage,
        },
    }
</script>