<template>
  <q-layout>
    <q-page class="reg_page__container">
      <div>
        <RegistrationCleanerForm/>
      </div>
    </q-page>
  </q-layout>
</template>

<script>
import RegistrationCleanerForm from 'components/empty_components/RegistrationCleanerForm.vue'

  export default {
    name: 'RegistrationCleanerPage',
    components: {
      RegistrationCleanerForm
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