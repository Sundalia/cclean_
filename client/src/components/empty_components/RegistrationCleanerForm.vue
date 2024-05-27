<template>
  <div class="registration_form__container">
    <q-form
      class="registration_form__form"
      @submit="onSubmit()"
    >
      <EmptyHeaderCleaner/>
      <div class="row">
        <div class="registration_form__router_tab_active">
          <p>Регистрация</p>
        </div>
        <div class="registration_form__router_tab">
          <p>
            <router-link to="authentication" class="registration_form__router_tab_text">Вход</router-link>
          </p>
        </div>
      </div>
      <q-input
        class="registration_form__input"
        input-style="text-align: center"
        label="Номер телефона *"
        v-model="phone"
        :value="phone"
        mask="+7(###)###-##-##"
        placeholder="+7(999)999-99-99"
        lazy-rules="ondemand"
        :rules="[
          val => val && val.length > 10 || 'Проверьте на правильность номер'
        ]"
      ></q-input>

      <q-input
        class="registration_form__input"
        input-style="text-align: center"
        label="Ваше имя *"
        v-model="name"
        :value="name"
        type="text"
        placeholder="Имя"
        lazy-rules="ondemand"
        :rules="[
          val => /^[a-zA-Zа-яА-Я'][a-zA-Zа-яА-Я-' ]+[a-zA-Zа-яА-Я']?$/u.test(val) || 'Пожалуйста укажите как к Вам обращаться'
        ]"
      />
      <q-input
        class="registration_form__input"
        input-style="text-align: center"
        label="Придумайте пароль *"
        v-model="password"
        :value="password"
        :type="isPwd ? 'password' : 'text'"
        lazy-rules="ondemand"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwd ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwd = !isPwd"
          />
        </template>
      </q-input>

      <q-input
        class="registration_form__input"
        input-style="text-align: center"
        label="Подтвердите пароль *"
        v-model="password_confirm"
        :value="password_confirm"
        :type="isPwdCfm ? 'password' : 'text'"
        lazy-rules="ondemand"
      >
        <template v-slot:append>
          <q-icon
            :name="isPwdCfm ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPwdCfm = !isPwdCfm"
          />
        </template>
      </q-input>

      <div class="registration_form__toggle_box">
        <q-toggle
        class="registration_form__toggle"
        v-model="accept"
        :value="accept"
        />
        <p class="registration_form__toggle_text">Я принимаю условия&nbsp;
          <router-link
            to="/documents"
            target="_blank"
            class="registration_form__toggle_link"
          >
          Договора подряда клинера
          </router-link>
        </p>

      </div>

      <div class="registration_form__submit_box">
        <q-btn
          class="registration_form__submit"
          label="Зарегистрироваться"
          type="submit"
          color="accent"
        />
      </div>

        <div class="row registration_form__router_teb_cleaner">
          <p>
            <router-link to="registration" class="registration_form__router_tab_text">для Клиента</router-link>
          </p>
        </div>
    </q-form>
  </div>
</template>

<script>
import EmptyHeaderCleaner from './subcomponents/EmptyHeaderCleaner.vue'
import { ref } from 'vue'
import { useQuasar } from 'quasar'
import { useAuthStore } from "stores/authStore"
import { useRouter } from 'vue-router'

  export default {
    name: 'RegistrationCleanerForm',
    components: {
      EmptyHeaderCleaner
    },
    setup() {
      const $q = useQuasar()
      const router = useRouter()
      const store = useAuthStore()
      const registration = () => store.registrationCleaner(phone, name.value, password.value)
      const phone = ref('')
      const name = ref('')
      const password = ref('')
      const password_confirm = ref('')
      const accept = ref(false)
      const isPwd = ref(true)
      const isPwdCfm = ref(true)

      return {
        phone,
        name,
        password,
        password_confirm,
        accept,
        isPwd,
        isPwdCfm,

        async onSubmit() {
          if(this.accept === false) {
            $q.notify({
              color: 'red-5',
              textColor:'white',
              message: 'Нужно принять условия пользования сервисом',
              position: 'center'
            })
          } else {
            if(this.password !== this.password_confirm) {
              $q.notify({
                color: 'red-5',
                textColor:'white',
                message: 'Пароли не совпадают',
                position: 'center'
              })
            } else {
              await registration(phone, name.value, password.value)
                .then(
                  router.push({path: '/login/sms'})
                )
            }
          }
        }
      }
    },
    methods: {
    },


  }
</script>

<style lang="scss" scoped>
.registration_form__container {
  max-width: 700px;
  font-family: 'Comfortaa';
  background-color: $background;
  border-radius: 2%;
  padding: 2%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}



.registration_form__submit_box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5%;
}

.registration_form__submit {
  height: 70px;
  min-width: 150px;
}

.registration_form__input{
  padding: 2%;
  background-color: white;
}

.registration_form__toggle_box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2%;
}

.registration_form__toggle_text{
  padding: 0;
  margin: 0;
}

.registration_form__toggle_link {
  color: $accent;
}

.registration_form__router_tab {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: $background;
  border-radius: 2% 2% 0 0;
  height: 50px;
  max-width: 200px;
  min-width: 100px;
  font-family: 'Comfortaa';
  padding: 2%;
}

.registration_form__router_tab_active{
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: white;
  color: $dark;
  border-radius: 2% 2% 0 0;
  height: 50px;
  max-width: 200px;
  min-width: 100px;
  font-family: 'Comfortaa';
  padding: 2%;
  font-size: 1rem;
}

.registration_form__router_tab_text {
  text-decoration: none;
  color: $accent;
}

.registration_form__router_tab_text:hover {
  font-weight: bold;
}

.registration_form__router_teb_cleaner{
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
