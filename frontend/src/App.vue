<template>
  <v-app>
    <v-app-bar app dark color="primary"><h1>Thesaurus</h1></v-app-bar>
    <v-main>
      <v-container align-self="center" class="mt-8">
        <v-row justify="center" class="text-center">
          <v-col>
            <h3>Python (Fast API) + Vue.js (Vuetify)</h3>
            <p>Dawid Wietrzych</p>
            <p style="word-wrap: break-word">
              The application allows you to find synonyms, antonyms and
              definitions the last word we entered into the text box
            </p>
            <v-row justify="center">
              <v-col cols="12" sm="10" md="8">
                <v-textarea
                  v-model="sentence"
                  placeholder="Start writing... (press `tab`)"
                  solo
                  color="primary"
                  background-color="secondary"
                  auto-grow
                  counter
                  clearable
                  rounded
                  v-debounce="createWordnet"
                  :autofocus="focus"
                  @keydown.tab="focus = true"
                />
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="9">
                <v-divider />
              </v-col>
            </v-row>

            <v-row justify="center" class="text-start text-capitalize" >
              <v-col cols="12" sm="10" md="8">
                <div style="height: 6vh; max-width: 80vw;" class="text-truncate">
                <h1 v-text="lastWord()" class="font-italic"/>
                </div>
                <v-card height="300" flat>
                  <v-skeleton-loader
                    v-show="loading"
                    class="mx-auto"
                    type="article@3"
                    height="360"
                  ></v-skeleton-loader>
                  <div
                    v-for="(value, key) in wordnet"
                    :key="key"
                    v-show="!loading"
                  >
                    <h2 v-text="key" />
                    <span v-text="value.length > 0 ? value.join(', ') : `No ${key}`"/>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      wordnet: {},
      sentence: "",
      focus: false,
      loading: false
    };
  },
  methods: {
    createWordnet() {
      this.loading = true;
      let word = this.lastWord();
      axios
        .post("/wordnet", { word: word })
        .then((resp) => (this.wordnet = resp.data))
        .catch((e) => console.error(e))
        .finally(() => (this.loading = false));
    },
    lastWord() {
      if (this.sentence !== null) {
        return this.sentence.split(" ").slice(-1)[0];
      }
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@600&display=swap");

.v-application {
  font-family: "Source Sans Pro", sans-serif;
}
</style>
