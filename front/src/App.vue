<template>
  <div id="app">
    <div>
      <img :src="image" />
    </div>
    <br />
    <div>
      <v-btn name="button_1" v-if="button == false" @click="test(true)" color="primary"
        >Вкл
      </v-btn>
      <v-btn name="button_2" v-if="button == true" @click="test(false)"
        >Выкл
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  data: () => {
    return {
      button: false,
      backendUrl: process.env.VUE_APP_BACKEND_URL_API,
      image: "http://192.168.1.52:5001/video",
    };
  },
  methods: {
    test(bool) {
      fetch(`${this.backendUrl}/select`, {
        method: "POST",
        body: JSON.stringify({ key: `${bool}` }),
      }).then((response) => {
        if (response.status == 200) {
          this.button = bool;
        }
      });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
