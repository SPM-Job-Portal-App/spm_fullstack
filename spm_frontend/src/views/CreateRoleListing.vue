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
            <v-col cols="2"></v-col>
            <v-col cols="3" class="text-center">
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

  <style>
  .custom-container {
    background-color: #eae4dd; 
    height: 80vh; 
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
  

  <script>
export default {
  data() {
    return {
      RoleTitle: '',
      RoleDescription: '',
      SelectedDept: null,
      skillOptions: ['Skill 1', 'Skill 2', 'Skill 3', 'Skill 4'],
      selectedSkills: [],
    };
  },
  computed: {
    isConfirmButtonEnabled() {
      const isRoleTitleValid = this.RoleTitle.length >= 1;
      const isRoleDescriptionValid = this.RoleDescription.length >= 1;
      const isDeptSelected = !!this.SelectedDept;
      const isAtLeastOneSkillSelected = this.selectedSkills.length >= 1;

      return (
        isRoleTitleValid &&
        isRoleDescriptionValid &&
        isDeptSelected &&
        isAtLeastOneSkillSelected
      );
    },
  },
  methods: {
    hoverButton(buttonType) {
      if (buttonType === 'cancel') {
      } else if (buttonType === 'confirm') {
      }
    },
    resetButtonColor(buttonType) {
    },
    confirmRole() {
      if (this.isConfirmButtonEnabled) {
        console.log('Role confirmed!');
      }
    },
  },
};
</script>