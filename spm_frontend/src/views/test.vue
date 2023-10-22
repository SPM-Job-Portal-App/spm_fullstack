<v-overlay v-model="skillsOverlay" @click="closeSkillsOverlay" class="align-center justify-center">
                  <v-sheet
                    elevation="12"
                    max-width="800"
                    rounded="lg"
                    width="100%"
                    class="pa-4 text-center mx-auto"
                    style="background-color: #eae4dd; color: #664229;"
                  >
                    <h2 class="text-h5 mb-6 sheet-header">Required Skills</h2>
                
                    <!-- Display all skills with color coding -->
                    <div class="text-medium-emphasis text-body-2">
                      <ul>
                        <li class="skill-row" v-for="skill in listing.skills" :key="skill">
                          <v-chip
                            :color="acquiredSkills.includes(skill) ? 'green' : 'red'"
                            :prepend-icon="getSkillIcon(skill)"
                            class="ma-1"
                            style="font-size: 12px;"
                          >
                            {{ skill }}
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