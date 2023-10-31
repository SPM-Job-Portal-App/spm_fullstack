<template>
  <v-overlay class="align-center justify-center">
    <v-sheet
        elevation="12"
        max-width="600"
        rounded="lg"
        width="100%"
        class="pa-4 text-center mx-auto"
      >

      <h2 class="text-h5 mb-6 sheet-header">Error</h2>

      <div class="text-medium-emphasis text-body-2">
        <h3 style="margin-bottom: 15px">Error cancelling role application</h3>
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
        Done Ready
        </v-btn>
      </div>
    </v-sheet>
  </v-overlay>

</template>

<script>
export default {
    props: {
        close_overlay: Function,
    }
}
</script>

<style scoped>
</style>