<template>
  <div class="sms_form__container">
    <q-form
      class="sms_form__form"
      @submit="onSubmit"
    >
      <EmptyHeader/>
      <q-input
        class="sms_form__input"
        input-style="text-align: center"
        label="Код из смс *"
        v-model="code"
        mask="####"
        placeholder="####"
        color="accent"
      ></q-input>
      <div class="sms_form__submit_box">
        <q-btn
          class="sms_form__submit"
          label="Войти"
          type="submit"
          color="accent"
        />
      </div>
    </q-form>
  </div>
</template>

<script>
import EmptyHeader from './subcomponents/EmptyHeader.vue'
import { ref } from 'vue'
import { useAuthStore } from "stores/authStore"


export default {
    name: 'SmsVerification',
    components: {
      EmptyHeader
    },
    setup() {
      const code = ref('')
      const store = useAuthStore()
      const verify_sms = () => store.verify_sms(code.value)

        return {
          code,

          async onSubmit() {
            await verify_sms(code.value)
          }
        }
    }
  }
</script>

<style lang="scss" scoped>
.sms_form__container {
  max-width: 700px;
  font-family: 'Comfortaa';
  background-color: $background;
  border-radius: 2%;
  padding: 2%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.sms_form__input{
  padding: 2%;
  background-color: white;
}

.sms_form__submit_box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5%;
}

.sms_form__submit {
  height: 70px;
  min-width: 150px;
}
</style>
