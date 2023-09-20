<template>
    <v-overlay v-model="showOverlay" @click="closeOverlay" class="align-center justify-center">
      <v-sheet
        elevation="12"
        max-width="600"
        rounded="lg"
        width="100%"
        class="pa-4 text-center mx-auto"
      >
        <v-icon
          class="mb-5"
          :color="iconColor"
          :icon="icon"
          :size="iconSize"
        ></v-icon>
  
        <h2 class="text-h5 mb-6">{{ title }}</h2>
  
        <p class="mb-4 text-medium-emphasis text-body-2">
          {{ message }}
        </p>
  
        <v-divider class="mb-4"></v-divider>
  
        <div class="text-end">
          <v-btn
            class="text-none"
            :color="buttonColor"
            rounded
            variant="flat"
            width="90"
            @click="closeOverlay"
            :to="route"
          >
            {{ buttonText }}
          </v-btn>
        </div>
      </v-sheet>
    </v-overlay>
</template>

<script>
  export default {
    props: {
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
    computed: {
      showOverlay: {
        get() {
          return this.show;
        }
      },
    },
    methods: {
      closeOverlay() {
        this.$emit('close-overlay');
      },
    },
  };
</script>