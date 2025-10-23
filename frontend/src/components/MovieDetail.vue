<template>
  <v-container v-if="car">
    <v-row>
      <!-- Poster -->
      <v-col cols="12" md="4">
        <v-img :src="car.picture" aspect-ratio="2/3" contain></v-img>
      </v-col>

      <!-- Info -->
      <v-col cols="12" md="8">
        <h1>{{ car.title }}</h1>
        <p>{{ car.vid }}</p>
        <p>{{ car.year }}</p>
        <p>{{ car.whatcost }} $</p>
        <v-divider class="my-2"></v-divider>
        <p>{{ car.description }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      car: null
    }
  },
  created() {
    const id = this.$route.params.id
    axios.get(`/api/cars/${id}/`)
      .then(res => {
        this.car = res.data
      })
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 10px;
}
</style>
