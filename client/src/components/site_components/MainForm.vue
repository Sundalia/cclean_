<template>
  <div class="main_form__container">
    <div class="main_form_box">
      <q-form
      class="row main_form"
      @submit="onSubmit"
    >
      <div class="main_form__item">
        <q-select 
          color="dark"
          bg-color="accent"
          standout 
          v-model="clean_type_val"
          :value="clean_type"
          :options="clean_type"
        ></q-select>
      </div>

      <div class="row main_form__item">
        <q-btn
          unelevated
          class="main_form__item_btn_minus" 
          @click.stop.prevent=decrementRoom()
          color="accent"
          text-color="black"
          bg-color="accent"
          size="20px"
        >-</q-btn>

        <q-input
          bg-color="grey"
          class="main_form__item_input"
          input-style="text-align: center"
          v-model="counter_room"
          :value ="counter_room"
          label="&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Сколько комнат:"
          mask="#"
          fill-mask="0"
          :min="min" 
          :max="max"
        ></q-input>

        <q-btn 
          unelevated
          class="main_form__item_btn_plus"
          color="accent"
          text-color="black"
          size="20px"
          @click.stop.prevent=incrementRoom()
        >+</q-btn>
      </div>

      <div class="row main_form__item">
        <q-btn
          unelevated
          class="main_form__item_btn_minus" 
          @click.stop.prevent=decrementToilet()
          color="accent"
          text-color="black"
          size="20px"
        >-</q-btn>

        <q-input
          bg-color="grey"
          class="main_form__item_input"
          input-style="text-align: center "
          v-model="counter_toilet"
          :value="counter_toilet"
          label="&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Сколько санузлов:"
          mask="#"
          fill-mask="0"
          :min="min" 
          :max="max"
          lazy_rules="ondemand"
        ></q-input>

        <q-btn 
          unelevated
          class="main_form__item_btn_plus"
          color="accent"
          text-color="black"
          size="20px"
          @click.stop.prevent=incrementToilet()
        >+</q-btn>
      </div>

      <div class="main_form__item">
        <q-input
          input-style="text-align: center "
          bg-color="grey"
          :value="phone"
          v-model="phone"
          mask="+7(###)###-##-##"
          placeholder="+7(999)999-99-99"
          lazy-rules="ondemand"
          :rules="[
            val => val && val.length > 10 || 'Проверьте на правильность номер'
          ]"
        ></q-input>
      </div>

      <div class="main_form__item_submit">
        <q-btn
          unelevated
          class="main_form__item_submit_btn"
          color="accent"
          text-color="black"
          type="submit"
        >
          РАССЧИТАТЬ
        </q-btn>
      </div>

    </q-form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { api } from 'src/boot/axios'
import { useQuasar } from 'quasar'

export default({
  name: 'MainForm',
  setup() {
    const $q = useQuasar()

    const clean_type = [
        'Генеральная', 
        'Поддерживающая', 
        'Послестроительная', 
        'Мойка окон', 
        'Уборка офиса', 
        'Загородный дом', 
        'Уборка яхты',
        'Глубокая чистка пола'
      ]
      const clean_type_val = ref("Генеральная")
      const counter_room = ref(1)
      const counter_toilet = ref(1)
      const min = 1
      const max = 9
      const phone = ref('')

    return {
      clean_type,
      clean_type_val,
      counter_room,
      counter_toilet,
      min,
      max,
      phone,
      onSubmit() {
        let cutedPhone = phone.value.replace(/[^0-9+]+/gi, '')
        $q.notify({
          position: 'center',
          color: 'accent',
          textColor: 'white',
          message: 'Запрос отправлен, ожидайте звонка в ближайшее время'
        })
        api.post("/leads/", {
          cleaning_type: clean_type_val.value,
          counter_room: counter_room.value,
          counter_toilet: counter_toilet.value,
          phone_number: cutedPhone
        })
        .catch((err) => {
          $q.notify({
            color: 'red',
            textColor: 'white',
            position: 'center',
            message: `${JSON.stringify(err.response.data).replace(/[`",.<>\\{\\}\\[\]]/gi, '')}`
          })
        })
          clean_type.value ='Генеральная'
          counter_room.value = 1
          counter_toilet.value = 1
          phone.value = ''

      }
    }
  },
  methods: {
    decrementRoom() {
      this.counter_room = this.counter_room === this.min ? this.min : this.counter_room -1
    },
    incrementRoom() {
      this.counter_room = this.counter_room === this.max ? this.max : this.counter_room +1
    },
    decrementToilet() {
      this.counter_toilet = this.counter_toilet === this.min ? this.min : this.counter_toilet -1
    },
    incrementToilet() {
      this.counter_toilet = this.counter_toilet === this.max ? this.max : this.counter_toilet +1
    }
  }
})
</script>

<style lang="scss" scoped>
.main_form__container {
  display: flex;
  justify-content: center;
  padding: 2%;
  margin: 50px;
}

.main_form {
  font-family: 'Comfortaa';
  justify-content: center;
  align-items: start;
}

.main_form__item {
  margin: 10px;
  min-width: 300px;
  border-radius: 5%;

}

.main_form__item_btn_minus {
  border-radius: 5% 0 0 5%;
  height: 56px;
  width: 50px;
}

.main_form__item_input{
  min-width: 200px;
}

.main_form__item_btn_plus {
  border-radius: 0 5% 5% 0;
  height: 56px;
  width: 50px;
  box-shadow: none !important;
}

.main_form__item_submit {
  margin: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.main_form__item_submit_btn {
  min-width: 300px;
  height: 56px;
}

// @media screen and (max-width: 820px) {
// }

</style>