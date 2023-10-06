<template>
  <v-container class="fill-height">
    <v-responsive class="align-center text-center fill-height">
      <v-img height="300" src="@/assets/logo.svg" />

      <div class="text-body-2 font-weight-light mb-n1">Welcome to</div>

      <h1 class="text-h2 font-weight-bold">Vuetify</h1>

      <div class="py-14" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            href="https://vuetifyjs.com/components/all/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-view-dashboard"
              size="large"
              start
            />

            Components
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            color="primary"
            href="https://vuetifyjs.com/introduction/why-vuetify/#feature-guides"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            target="_blank"
            variant="flat"
          >
            <v-icon
              icon="mdi-speedometer"
              size="large"
              start
            />

            Get Started
          </v-btn>
        </v-col>

        <v-col cols="auto">
          <v-btn
            href="https://community.vuetifyjs.com/"
            min-width="164"
            rel="noopener noreferrer"
            target="_blank"
            variant="text"
          >
            <v-icon
              icon="mdi-account-group"
              size="large"
              start
            />

            Community
          </v-btn>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="12" sm="9" md="7" lg="5">
          <v-chip
            v-for="requiredSkill in requiredSkills"
            :key="requiredSkill.name"
            :color="acquiredSkills.includes(requiredSkill.name) ? 'green' : 'red'"
            :prepend-icon="requiredSkill.icon"
            class="ma-1"
            @click="showSkillInfo(requiredSkill)"
          >
            {{ requiredSkill.name }}
          </v-chip>
        </v-col>
      </v-row>
      <v-overlay v-model="overlay" class="align-center justify-center">
        <v-card
          class="mx-auto"
          max-width="800"
          offset="256px"
        >
          <v-card-item>
            <v-card-title>
              <v-icon :icon="selectedSkill.icon"></v-icon>
              {{ selectedSkill.name }}
            </v-card-title>
          </v-card-item>
          <v-card-text>
            {{ selectedSkill.desc }}
          </v-card-text>
          <v-card-actions>
            <v-btn
              variant="text"
              color="light-blue-darken-4"
              @click="overlay = !overlay"
            >
              Close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-overlay>
    </v-responsive>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      requiredSkills: [
        {name: 'Python', icon: 'mdi-language-python', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'HTML', icon: 'mdi-language-html5', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'CSS', icon: 'mdi-language-css3', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'JavaScript', icon: 'mdi-language-javascript', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'PHP', icon: 'mdi-language-php', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'C#', icon: 'mdi-language-c', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'Ruby', icon: 'mdi-language-ruby', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'Angular.js', icon: 'mdi-angularjs', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
        {name: 'Vue.js', icon: 'mdi-vuejs', desc: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Vel possimus blanditiis, ducimus facilis provident, tempora quisquam laudantium perferendis odio dolor eligendi voluptatibus. Quidem perspiciatis expedita excepturi repellendus eum odio animi?'},
      ],
      acquiredSkills: [
        'Python',
        'Vue.js',
        'HTML',
        'CSS',
        'JavaScript'
      ],
      overlay: false,
      selectedSkill: null
    }),
    methods: {
      showSkillInfo(skill) {
        this.selectedSkill = skill
        this.overlay = true
      }
    }
  }
</script>
