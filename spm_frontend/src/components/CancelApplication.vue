<template>
  <v-overlay class="align-center justify-center">
    <v-sheet
        elevation="12"
        max-width="600"
        rounded="lg"
        width="100%"
        class="pa-4 text-center mx-auto"
      >
      <v-icon
          class="mb-5"
          color='green'
          icon="mdi-check-circle"
          size="112"
      ></v-icon>

      <h2 class="text-h5 mb-6 sheet-header">Application Cancelled Successfully</h2>

      <div class="text-medium-emphasis text-body-2">
        <h3 style="margin-bottom: 15px">Application for role {{ role_name }} has been cancelled suceessfully</h3>
      </div>

      <v-divider class="mb-4"></v-divider>

      <div class="text-end">
        <v-btn
          class="text-none"
          color="success"
          rounded
          variant="flat"
          width="90"
          @click="close_overlay"
        >
        Done
        </v-btn>
      </div>
    </v-sheet>
  </v-overlay>

</template>

<script>
export default {
  props: {
    role_name: String,
    close_overlay: Function,
    show: {
        type: Boolean,
        default: false,
      },
      icon: {
        type: String,
      },
      iconColor: {
        type: String,
      },
      iconSize: {
        type: String,
      },
      title: {
        type: String,
      },
      message: {
        type: String,
      },
      buttonColor: {
        type: String,
      },
      buttonText: {
        type: String,
      },
      route: {
        type: String,
      }
    },
  }
</script>

<style scoped>
.skill-row{
  list-style-type: none;
}
</style>