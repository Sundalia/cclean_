<template>
  <div class="authentication_form__container">
    <q-form
      class="authentication_form__form"
      @submit="onSubmit"
    >
      <EmptyHeader/>
      <div class="row">
        <div class="authentication_form__router_tab">
          <p><router-link to="registration" class="authentication_form__router_tab_text">Регистрация</router-link></p>
        </div>
        <div class="authentication_form__router_tab_active">
          <p>Вход</p>
        </div>
      </div>
      <q-input
        class="authentication_form__input"
        input-style="text-align: center"
        label="Номер телефона *"
        v-model="phone"
        :value="phone"
        mask="+7(###)###-##-##"
        placeholder="+7(999)999-99-99"
        color="accent"
      ></q-input>

      <q-input
        class="authentication_form__input"
        input-style="text-align: center"
        label="Введите пароль *"
        v-model="password"
        :value="password"
        :type="isPassword ? 'password' : 'text'"
        lazy-rules="ondemand"
      >
        <template v-slot:append>
          <q-icon
            :name="isPassword ? 'visibility_off' : 'visibility'"
            class="cursor-pointer"
            @click="isPassword = !isPassword"
          />
        </template>
      </q-input>

      <div class="authentication_form__submit_box">
        <q-btn
          class="authentication_form__submit"
          label="Получить смс"
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
import { useAuthStore } from 'src/stores/authStore'
// import { useRouter } from 'vue-router'


  export default {
    name: 'AuthenticationForm',
    components: {
      EmptyHeader
    },
    setup() {
      // const router = useRouter()
      const store = useAuthStore()
      const login = () => store.login(phone, password)
      const phone = ref('')
      const password = ref('')
      const isPassword = ref(true)



      return {
        phone,
        password,
        isPassword,

        async onSubmit() {
          await login(phone, password)
        }
      }
    },
    methods: {

    }
  }
</script>

<style lang="scss" scoped>
.authentication_form__container {
  max-width: 700px;
  font-family: 'Comfortaa';
  background-color: $background;
  border-radius: 2%;
  padding: 2%;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.authentication_form__submit_box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5%;
}

.authentication_form__submit {
  height: 70px;
  min-width: 150px;
}

.authentication_form__input{
  padding: 2%;
  background-color: white;
}

.authentication_form__toggle_box {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Comfortaa';
  margin: 2%;
}

.authentication_form__toggle_link {
  color: $accent;
}

.authentication_form__router_tab {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: $background;
  border-radius: 2% 2% 0 0;
  height: 50px;
  max-width: 200px;
  min-width: 100px;
  color: $dark;
  padding: 2%;
}

.authentication_form__router_tab_active{
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
}

.authentication_form__router_tab_text {
  text-decoration: none;
  color: $accent;
}

.authentication_form__router_tab_text:hover {
  font-weight: bold;
}

</style>./empty_components/EmptyHeader.vue
