<template>
  <v-container>
    <h2>Login</h2>

    <!-- If user is already logged in -->
    <div v-if="isLoggedIn">
      <p>You are already logged in as <strong>{{ localStorageUsername }}</strong> ✅</p>
      <v-btn @click="$router.push('/account')">Go to Account</v-btn>
    </div>

    <!-- If not logged in -->
    <div v-else>
      <v-text-field v-model="username" label="Username" />
      <v-text-field v-model="password" label="Password" type="password" />
      <v-btn @click="login">Login</v-btn>
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
    login() {
      if (this.isLoggedIn) {
        this.error = 'You are already logged in.'
        return
      }

      axios.post('/api/auth/login/', {
        username: this.username,
        password: this.password
      })
      .then(res => {
        localStorage.setItem('access', res.data.access)
        localStorage.setItem('username', this.username)
        this.$router.push('/account')
      })
      .catch(() => {
        this.error = 'Invalid credentials'
      })
    }
  }
}
</script>
