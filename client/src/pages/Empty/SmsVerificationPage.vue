<template>
  <q-layout>
    <q-page class="sms_page__container">
      <SmsVerification/>
    </q-page>
  </q-layout>
</template>

<script>
import SmsVerification from 'src/components/empty_components/SmsVerification.vue'

  export default {
    name: 'SmsVerficationPage',
    components: {
      SmsVerification
    }
  }
</script>

<style lang="scss" scoped>
.sms_page__container{
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: $grey;
}
</style>