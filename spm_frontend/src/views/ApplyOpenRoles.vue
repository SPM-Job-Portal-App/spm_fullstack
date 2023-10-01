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
                    <!-- pre-populated skills field -->
                    <v-row>
                        <v-col cols="12" class="text-grey-lighten-1">Skills</v-col>
                        <v-col cols="12">
                            <v-chip
                                v-for="acquiredSkill in acquiredSkills"
                                :key="acquiredSkill.name"
                                :prepend-icon="acquiredSkill.icon"
                                class="ma-1"
                                disabled
                                @click="showSkillInfo(acquiredSkill)"
                            >
                                {{ acquiredSkill.name }}
                            </v-chip>
                        </v-col>
                    </v-row>
                    <!-- cover letter text field -->
                    <v-row>
                        <v-col cols="12">
                            <v-textarea
                                class="mt-6"
                                :rules="coverLetterRules"
                                clearable
                                counter
                                placeholder="Maximum 200 characters"
                                label="Cover Letter (Optional)"
                                v-model="coverLetter"
                            ></v-textarea>
                        </v-col>
                    </v-row>
                    <!-- terms and conditions checkbox -->
                    <v-row>
                        <v-col>
                            <v-checkbox
                                v-model="terms"
                                :rules="termsRules"
                                label="I agree to site terms and conditions"
                            ></v-checkbox>
                        </v-col>
                    </v-row>
                    <!-- form submit button -->
                    <v-row>
                        <v-col>
                            <v-btn @click="submitForm" :disabled="!isValid()" class="text-white" color="#ccbbaa" :loading="loading">
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
    import OverlayMessage from '../components/OverlayMessage.vue';
    import axios from 'axios'

    export default {
        data: () => ({
            firstName: 'John',
            lastName: 'Lim',
            acquiredSkills: [
                { name: 'Python', icon: 'mdi-language-python', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'HTML', icon: 'mdi-language-html5', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'CSS', icon: 'mdi-language-css3', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'JavaScript', icon: 'mdi-language-javascript', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'PHP', icon: 'mdi-language-php', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'C#', icon: 'mdi-language-c', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'Ruby', icon: 'mdi-language-ruby', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'Angular.js', icon: 'mdi-angularjs', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
                { name: 'Vue.js', icon: 'mdi-vuejs', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?' },
            ],
            coverLetterRules: [
                value => (value || '').length <= 200 || 'Max 200 characters'
            ],
            termsRules: [
                value => !!value || 'You must agree to the terms and conditions'
            ],
            coverLetter: '',
            terms: false,
            loading: false,
            successOverlay: false,
            failureOverlay: false,
            listingData: [],
            feedbackMessage: ''
        }),
        mounted() {
            // const id = this.$route.params.id;
            // axios.get(`http://localhost:5000/listing/${id}`).then(
            //     (response)=>{
            //         this.listingData = response.data;
            //         console.log(this.listingData)
            //     }
            // )
        },
        methods: {
            isValid() {
                if(this.$refs.form){
                    return this.$refs.form.validate() && this.terms
                }
            },
            submitForm() {
                if (this.isValid()) {
                    this.loading = true
                    const id = this.$route.params.id;
                    let application_data = {
                        "role_listing": id,
                        "staff_id": 1
                    }
                    axios.post('http://localhost:5000/application', application_data)
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
            toggleOverlay() {
                this.loading = false
                this.successOverlay = false
                this.failureOverlay = false
            }
        },
        components: {
            OverlayMessage,
        },
    }
</script>