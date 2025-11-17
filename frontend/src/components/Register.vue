<template>
  <v-container>
    <h2>Register</h2>

    <!-- If user is already registered -->
    <div v-if="isLoggedIn">
      <p>You are already registered as <strong>{{ localStorageUsername }}</strong> 🚫</p>
      <v-btn @click="$router.push('/account')">Go to Account</v-btn>
    </div>

    <!-- If not registered -->
    <div v-else>
      <v-text-field v-model="username" label="Username" />
      <v-text-field v-model="password" label="Password" type="password" />
      <v-btn @click="register">Register</v-btn>
      <p v-if="error">{{ error }}</p>
    </div>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return { username: '', password: '', error: '' }
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('username')
    },
    localStorageUsername() {
      return localStorage.getItem('username')
    }
  },
  methods: {
    register() {
      if (this.isLoggedIn) {
        this.error = 'You are already registered.'
        return
      }

      axios.post('/api/auth/register/', {
        username: this.username,
        password: this.password
      })
      .then(res => {
        localStorage.setItem('access', res.data.access)
        localStorage.setItem('username', res.data.username)
        this.$router.push('/account')
      })
      .catch(err => {
        this.error = err.response?.data?.error || 'Error'
      })
    }
  }
}
</script>
