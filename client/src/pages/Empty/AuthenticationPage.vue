<template>
  <q-layout>
    <q-page class="auth_page__container">
      <AuthenticationForm/>
    </q-page>
  </q-layout>
</template>

<script>
import AuthenticationForm from 'components/empty_components/AuthenticationForm.vue'

  export default {
    name: 'AuthenticationPage',
    components: {
      AuthenticationForm
    }
  }
</script>

<style lang="scss" scoped>
.auth_page__container{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: $grey;
}

</style>