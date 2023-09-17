<template>
    <v-container class="fill-height">
      <v-responsive class="text-center fill-height">
        <!-- Title -->
        <h1>Create Job</h1>
  
        <!-- Job title -->
        <v-row justify="center">
          <v-col cols="8">
            <v-text-field
              label="Job Title"
              v-model="JobTitle"
              outlined
              class="mt-4 ml-4 mr-4"
            ></v-text-field>
          </v-col>
        </v-row>
  
        <!-- Job description -->
        <v-row justify="center">
          <v-col cols="8">
            <v-text-field
              label="Job Description"
              v-model="JobDescription"
              outlined
              class="ml-4 mr-4"
            ></v-text-field>
          </v-col>
        </v-row>
  
        <!-- Department -->
        <div>
          <v-row justify="center">
            <v-col cols="8">
                <div class="mr-12">
                    <h4 style="color:grey">Department</h4>
                  </div>
                <v-radio-group v-model="SelectedDept" style="margin-left: 10px">
                <v-radio label="Marketing" value="Marketing"></v-radio>
                <v-radio label="Finance" value="Finance"></v-radio>
                <v-radio label="Human Resources" value="Human Resources"></v-radio>
                <v-radio label="Add More Later" value="Add More Later"></v-radio>
                </v-radio-group>
            </v-col>
          </v-row>
        </div>

        <!-- Skills -->
        <div>
            <v-row justify="center">
                <v-col cols="8">
                    <v-select
                    v-model="selectedSkills"
                    :items="skillOptions"
                    label="Select required skills"
                    multiple
                    outlined
                    chips
                    small-chips
                    ></v-select>
                </v-col>
            </v-row>
          </div>

          <!-- Cancel / Confirm -->
          <v-row justify="center">
            <v-btn class="mr-6" @mouseover="hoverButton('cancel')" @mouseout="resetButtonColor('cancel')" large>
              Cancel
            </v-btn>
            <v-btn @mouseover="hoverButton('confirm')" @mouseout="resetButtonColor('confirm')" large>
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
        JobTitle: 'Enter job title',
        JobDescription: 'Enter job description',
        SelectedDept: null,

            skillOptions: [
            'Skill 1',
            'Skill 2',
            'Skill 3',
            'Skill 4',
        ],
        selectedSkills: []
      };
    },

    methods: {
    hoverButton(buttonType) {
      // Change button color on hover
      if (buttonType === 'cancel') {
        // Customize button color for 'Cancel'
        // Example: this.$refs.cancelButton.$el.style.backgroundColor = 'red';
      } else if (buttonType === 'confirm') {
        // Customize button color for 'Confirm'
        // Example: this.$refs.confirmButton.$el.style.backgroundColor = 'green';
      }
    },}

    
  };
  </script>
  