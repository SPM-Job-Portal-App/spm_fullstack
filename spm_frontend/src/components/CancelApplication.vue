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
      <h2 class="text-h5 mb-6 sheet-header">Delete Application</h2>

      <div class="text-medium-emphasis text-body-2">
        <h3 style="margin-bottom: 15px">Application for role {{ role_name }} has been deleted suceessfully</h3>
      </div>

      <v-divider class="mb-4"></v-divider>

      <div class="text-end">
        <v-btn
          class="text-none"
          :color="buttonColor"
          rounded
          variant="flat"
          width="90"
          @click="close_overlay"
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
    role_name: String,
    close_overlay: Function
  },
};
</script>

<style scoped>
.skill-row{
  list-style-type: none;
}
</style>