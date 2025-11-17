<template>
  <v-container>
    <h2 v-if="username">Hi {{ username }} 👋</h2>
    <h2 v-else>You are not registered 🚫</h2>

    <v-btn v-if="username" @click="logout">Logout</v-btn>
    <v-btn v-else @click="$router.push('/register')">Register</v-btn>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      username: localStorage.getItem('username')
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access')
      localStorage.removeItem('username')
      this.$router.push('/')
    }
  }
}
</script>
