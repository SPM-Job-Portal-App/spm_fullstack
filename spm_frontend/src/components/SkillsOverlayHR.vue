<template>
    <v-overlay class="align-center justify-center">
      <v-sheet
        elevation="12"
        max-width="800"
        rounded="lg"
        width="100%"
        class="pa-4 text-center mx-auto"
        style="background-color: #eae4dd; color: #664229;"
      >
        <h2 class="text-h5 mb-6 sheet-header">Required Skills</h2>
  
        <div class="text-medium-emphasis text-body-2">
          <h3 style="margin-bottom: 15px">Skills match: {{ calculateSkillPercentage(listingData.skills) }}</h3>
          <p>A red highlight indicates that you do not possess this skill</p>
          <p>A green highlight indicates that you possess this skill</p>
          <ul style="margin-top: 15px">
            <li class="skill-row" v-for="skill in getListingSkills()" :key="skill">
              <v-chip
                :prepend-icon="getSkillIcon(skill)"
                class="ma-1"
                style="font-size: 12px;"
              >
              {{skill}}
              </v-chip>
            </li>
          </ul>
        </div>
  
        <v-divider class="mb-4"></v-divider>
  
        <div class="text-end">
          <v-btn
            class="text-none"
            :color="buttonColor"
            rounded
            variant="flat"
            width="90"
            @click="closeSkillsOverlay"
          >
            Close
          </v-btn>
        </div>
      </v-sheet>
    </v-overlay>
  </template>
  
  <script>
  export default {
    props: {
      listingData: Object,
      closeSkillsOverlay: Function,
      getSkillIcon: Function,
      acquiredSkills: Array,
      calculateSkillPercentage: Function
    },
    methods: {
      getListingSkills(){
        const requiredSkillsArr = this.listingData.skills.split(',').map(item => item.trim());
        return requiredSkillsArr
      }
    }
  };
  </script>
  
  <style scoped>
  .skill-row{
    list-style-type: none;
  }
  </style>