<template>
  <q-layout>
    <q-page class="reg_page__container">
      <RegistrationForm/>
    </q-page>
  </q-layout>
</template>

<script>
import RegistrationForm from 'components/empty_components/RegistrationForm.vue'

  export default {
    name: 'RegistrationPage',
    components: {
      RegistrationForm
    }
  }
</script>

<style lang="scss" scoped>
.reg_page__container{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: $grey;
}
</style>