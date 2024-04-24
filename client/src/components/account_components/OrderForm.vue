<template>
  <div class="order_form__container">
    <q-form
      class="order_form"
      @submit="onSubmit()"
    >
      <div class="order_form__field">
        <q-select
          color="accent"
          standout
          label="ТИП УБОРКИ"
          v-model="cleaning_type"
          :value="cleaning_types"
          :options="cleaning_types"
        ></q-select>
      </div>

      <div class="order_form__field">
        <q-input
          standout
          color="accent"
          label="МЕТРАЖ"
          v-model="square"
          :value="square"
          mask="####.##"
          reverse-fill-mask
          placeholder="0000.00"
        ></q-input>
      </div>

      <div class="order_form__field">
        <q-select
          color="accent"
          standout
          label="ЗАСТАВЛЕННОСТЬ ВЕЩАМИ"
          v-model="thing_cluttered_val"
          :value="thing_cluttered"
          :options="thing_cluttered"
        ></q-select>
      </div>

      <div class="order_form__field">
        <q-select
          color="accent"
          standout
          label="4. ТИП ПОМЕЩЕНИЯ"
          v-model="room_choices_val"
          :value="room_choices"
          :options="room_choices"
        ></q-select>
      </div>

      <div class="order_form__field">
        <q-select
          color="accent"
          standout
          label="СТЕПЕНЬ ЗАГРЯЗНЕНИЯ"
          v-model="room_choices_val"
          :value="room_choices"
          :options="room_choices"
        ></q-select>
      </div>

      <div class="order_form__field">
        <q-input 
          color="accent"
          v-model="date" 
          label="ДАТА И ВРЕМЯ УБОРКИ"
          hint="в ночное время уборка на 20% дороже просим отнестись к этому с пониманием"
          >
              <template v-slot:prepend>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="date" mask="YYYY-MM-DD HH:mm">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="ГОТОВО" color="accent" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
                <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-time v-model="date" mask="YYYY-MM-DD HH:mm" format24h>
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="ГОТОВО" color="accent" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
              </q-icon>
              </template>
        </q-input>
      </div>

      <div class="order_form__field">
        <q-input label="УКАЖИТЕ АДРЕС">
          <q-btn label="УКАЗАТЬ НА КАРТЕ" color="accent" @click="map = true"/>
          <q-dialog v-model="map">
            <h1>map</h1>
          </q-dialog>
        </q-input>
      </div>

      <div class="order_form__field">
        <q-input 
          type="textarea"
          label="КОММЕНТАРИЙ"
          hint="Здесь укажите ,пожалуйста, Ваши пожелания. и мы обязательно их учтём"
        ></q-input>
      </div>

      <div class="order_form__field">
        <q-input 
          color="accent"
          standout
          label="ПРОМОКОД"
          hint="Введите промокод при наличии"
        ></q-input>
      </div>

      <div class="order_form__field">
          <q-file
            standout
            v-model="file"
            label="ЗАГРУЗИТЕ ФОТО"
            hint="При желании Вы можете добавить фото для лучшего понимания с чем нужно справиться"
          >
            <template v-slot:prepend>
              <q-icon name="attach_file" />
            </template>
          </q-file>
      </div>

      <div class="order_form__field">
        <q-radio
          v-model="windows"
          label="ПОМЫТЬ ОКНА"
        />
      </div>

      <div class="order_form__field">
        <q-input
          label="ЦЕНА"
          hint="Предварительная стоимость, для подтверждения заказа Вам в ближайшее время позвонит наш менеджер"
        ></q-input>
      </div>

    </q-form>
  </div>
</template>

<script>
import moment from 'moment'
import { ref } from 'vue'

  export default {
    name: 'OrderForm',
    data() {
      return {
        cleaning_types: [],
        cleaning_type: ref(''),
        thing_cluttered: [],
        thing_cluttered_val: ref(''),
        square: ref(''),
        room_choices: [],
        room_choices_val: ref(''),
        date: ref(moment().format("YYYY-MM-DD h:mm")),
        file: ref(null),
        windows: ref(false),
        map: ref(null)
      }
    },
    beforeCreate() {

      this.$api.get('/cleaning_type.json')
        .then(res => {
          this.cleaning_types = res.data.map((i) => i.name)
          this.cleaning_type = this.cleaning_types[0]
          console.log(this.cleaning_types)
        })
      this.$api.get('/thing_cluttered.json')
        .then(res => {
          this.thing_cluttered = res.data.map((i) => i.name)
          this.thing_cluttered_val = this.thing_cluttered[0]
        })
      this.$api.get('/orders.json')
    },
    methods: {
      onsubmit() {
        this.$api.post("/orders/", {

        })
      }
    }
  }
</script>

<style lang="scss" scoped>
.order_form__container {
  background-color: white;
}

.order_form {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  column-gap: 2rem;
  row-gap: 2rem;
}

@media screen and (max-width: 820px) {
  .order_form {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 520px) {
  .order_form {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>