<template>
  <v-container>
    <v-row>
      <v-col
        v-for="car in Cars"
        :key="car.id"
        cols="12" sm="6" md="3"
      >
        <v-card class="hoverable" outlined @click="goToCar(car.id)">
          <!-- Poster -->
          <v-img
            :src="car.picture"
            height="350px"
            cover
          ></v-img>

          <!-- Info -->
          <v-card-text>
            <div class="car-title">{{ car.title }}</div>
            <div class="car-subtitle">{{ car.year }}, {{ car.vid }}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      Cars: []
    }
  },
  created() {
    axios.get('/api/cars/')
      .then(res => {
        this.Cars = res.data
        console.log('Все автомобили (массив объектов):')
        console.table(res.data)
        res.data.forEach((car, index) => {
          console.log(`car[${index}] все поля:`, { ...car })
        })
      })
  },
  methods: {
    goToCar(id) {
      this.$router.push(`/movie/${id}`)
    }
  }
}
</script>

<style scoped>
.car-title {
  font-weight: bold;
  font-size: 1.1rem;
  margin-top: 8px;
}
.car-subtitle {
  color: gray;
  font-size: 0.9rem;
}
</style>
