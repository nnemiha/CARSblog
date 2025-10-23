<template>
  <v-app>
      <v-app-bar app>
        <v-toolbar-title @click="$router.push('/')">TopCarsEver</v-toolbar-title>
        <v-spacer />
        <v-btn text @click="$router.push('/forum')">Главная страница</v-btn>
        <v-btn text @click="$router.push('/')">Форум</v-btn>
        <v-btn text @click="$router.push('/login')">Логин</v-btn>
        <v-btn text @click="$router.push('/register')">Регистрация
        </v-btn>
        <v-btn text @click="$router.push('/account')">Аккаунт</v-btn>
      </v-app-bar>


    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  .v-toolbar-title {
    cursor: pointer;
  }
</style>