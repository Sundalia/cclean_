<template>
  <div class="order_form__container">
    <q-form
      class="order_form"
    >
      <div class="order_form__header">
        <p>закажи уборку прямо сейчас</p>
      </div>

      <div class="order_form__subrow">
        <div class="order_form__field">
          <q-select
            class="order_form__field_select"
            color="accent"
            name="cleaning_type"
            standout="bg-accent text-white"
            label="ТИП УБОРКИ *"
            v-model="cleaning_type"
            :options="cleaning_types"
            :display-value="cleaning_type.name"
            hint="Выберите тип уборки для лучшего подбора специалистов и оборудования"
            @update:modelValue="computingPrice()"
          >
            <template v-slot:option="{itemProps, opt}">
              <q-item v-bind="itemProps">
                <q-item-section>
                  <q-item-label>{{ opt.name }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-btn icon="question_mark" flat >
                    <q-popup-proxy context-menu>
                      <q-banner>{{ opt.description }}</q-banner>
                    </q-popup-proxy>
                  </q-btn>
                </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <div class="order_form__field">
          <q-select
            color="accent"
            name="furniture"
            standout="bg-accent text-white"
            label="ЗАСТАВЛЕННОСТЬ МЕБЕЛЬЮ *"
            v-model="furniture_cluttered_val"
            :options="furniture_cluttered"
            :default="furniture_cluttered[0]"
            :display-value="furniture_cluttered_val.name"
            hint="Укажите заставленность вещами чтобы мы могли понять - нужна ли дополнительно физическая сила"
            @update:model-value="computingPrice()"
          >
            <template v-slot:option="{itemProps, opt}">
              <q-item v-bind="itemProps">
                <q-item-section>
                  <q-item-label>{{ opt.name }}</q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-btn icon="question_mark" flat >
                    <q-popup-proxy context-menu>
                      <q-banner>{{ opt.description }}</q-banner>
                    </q-popup-proxy>
                  </q-btn>
                </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <div class="order_form__field">
          <q-input
            standout="bg-accent text-white"
            active-class="bg-background text-accent"
            name="square"
            color="accent"
            label="МЕТРАЖ *"
            v-model="square"
            :value="square"
            reverse-fill-mask
            placeholder="0000.00"
            hint="Если не знаете точный метраж - укажите приблизительно, это поможет рассчитать сумму заказа прямо сейчас"
            @update:model-value="computingPrice()"
            lazy-rules="ondemand"
            :rules="[
              val => val || 'Обязательно укажите метраж'
            ]"
          ></q-input>
        </div>

        <div class="order_form__field">
          <q-select
            color="accent"
            name="room_type"
            standout="bg-accent text-white"
            label="ТИП ПОМЕЩЕНИЯ *"
            v-model="room_choices_val"
            :display-value="room_choices_val.name"
            :options="room_choices"
            hint="Укажите тип помещения - это поможет нам подобрать правильные средства и технику"
            @update:model-value="computingPrice()"
          >
            <template v-slot:option="{itemProps, opt}">
              <q-item v-bind="itemProps">
                <q-item-section>
                  <q-item-label>{{ opt.name }}</q-item-label>
                </q-item-section>
              </q-item>
            </template>
          </q-select>
        </div>

        <div class="order_form__field">
          <q-select
            color="accent"
            name="pollution_degree"
            standout="bg-accent text-white"
            label="СТЕПЕНЬ ЗАГРЯЗНЕНИЯ *"
            v-model="pollution_degree_val"
            :display-value="pollution_degree_val.name"
            :options="pollution_degree"
            hint="Чтобы увидеть подробную информацию щелкните по `?` правой кнопки мыши (или долгое нажатие на мобильном устройстве)"
            @update:model-value="computingPrice()"
          >
             <template v-slot:option="{itemProps, opt}">
                <q-item v-bind="itemProps">
                  <q-item-section>
                    <q-item-label>{{ opt.name }}</q-item-label>
                  </q-item-section>
                  <q-item-section side>
                    <q-btn icon="question_mark" flat >
                      <q-popup-proxy context-menu>
                        <q-banner>{{ opt.description }}</q-banner>
                      </q-popup-proxy>
                    </q-btn>
                  </q-item-section>
                </q-item>
            </template>
          </q-select>
        </div>

        <div class="order_form__field">
          <q-file
            standout="bg-accent text-white"
            v-model="file"
            :value="file"
            label="ЗАГРУЗИТЕ ФОТО"
            hint="При желании Вы можете добавить фото для лучшего понимания с чем нужно справиться"
          >
            <template v-slot:prepend>
              <q-icon name="attach_file" />
            </template>
          </q-file>
      </div>

      <div class="order_form__field">
        <q-input
          standout="bg-accent text-white"
          color="accent"
          v-model="date"
          :value="date"
          mask="####-##-##"
          label="ДАТА УБОРКИ *"
          hint="Нажмите на иконку чтобы открыть календарь для удобного выбора даты"
          @update:model-value="computingPrice()"
          >
            <template v-slot:prepend>
              <q-icon name="event" class="cursor-pointer" size="2rem" hint="Выберите время">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-date
                    v-model="date"
                    :value="date"
                    @update:model-value="computingPrice()"
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="ГОТОВО" color="accent" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
          </template>
        </q-input>
      </div>

      <div class="order_form__field">
        <q-input
          standout="bg-accent text-white"
          color="accent"
          v-model="time"
          :rules="['time']"
          label="ВРЕМЯ УБОРКИ *"
          hint="в ночное время уборка на 20% дороже просим отнестись к этому с пониманием"
          @update:model-value="computingPrice()"
          >
            <template v-slot:prepend>
              <q-icon name="access_time" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-time
                    v-model="time"
                    format24h
                    @update:model-value="computingPrice()"
                  >
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="ГОТОВО" color="accent" flat />
                    </div>
                  </q-time>
                </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </div>

      </div>

      <div class="order_form__field">
        <q-input
          label="УКАЖИТЕ АДРЕС *"
          standout="bg-accent text-white"
          placeholder="пр.Ленина, 1"
          hint="Мы используем геокодер, укажите адрес не взирая на раскладку клавиатуры и нажмите Enter"
          v-model="address"
          :value="address"
          @change="geocodeSuggest"
          @keypress.enter.prevent="geocodeSuggest"
          input-style="text-align: center"
        >
          <q-btn
            class="order_form__field_btn"
            standout="bg-white text-black"
            label="УКАЗАТЬ НА КАРТЕ"
            color="accent"
            @click="map = true"
          >
            <q-dialog v-model="map">
              <yandex-map
                :settings="mapSettings"
                style="width: 1200px; max-width: 80vw;"
              >
                <yandex-map-default-scheme-layer/>
                <yandex-map-default-features-layer/>
                <yandex-map-controls :settings="{position: 'bottom right'}">
                  <yandex-map-geolocation-control/>
                </yandex-map-controls>
                <yandex-map-controls :settings="{position: 'right'}">
                  <yandex-map-zoom-control/>
                </yandex-map-controls>
                <yandex-map-controls :settings="{position: 'top left'}">
                  <yandex-map-entity>
                    <input
                      class="order_form__search_input"
                      v-model="suggest"
                      @input="geocodeSuggest"
                      @change="tapMarker"
                      type="text"
                      list="suggestList"
                      placeholder="Введите название"
                      autocomplete="off"
                    />
                    <datalist id="suggestList" >
                      <option v-for="i in suggestResponse" :key="i" :value="i.name"></option>
                    </datalist>
                    <q-btn
                      class="order_form__search_btn"
                      color="accent"
                      @click="tapMarker"
                      label="ok"
                      unelevated
                    />
                  </yandex-map-entity>
                </yandex-map-controls>
                <yandex-map-controls :settings="{position: 'top right'}">
                  <yandex-map-entity>
                    <q-btn
                      class="order_form__search_btn"
                      color="accent"
                      v-close-popup
                      label="готово"
                      unelevated
                    />
                  </yandex-map-entity>
                </yandex-map-controls>
                <yandex-map-default-marker v-if="this.check==true" :settings="this.mapMarker"/>
              </yandex-map>
            </q-dialog>
          </q-btn>
        </q-input>
      </div>


      <div class="order_form__field">
        <q-input
          type="textarea"
          standout="bg-accent text-white"
          label="НОМЕР КВАРТИРЫ, НАЛИЧИЕ ДОМОФОНА, ПОЖЕЛАНИЯ"
          hint="Здесь укажите ,пожалуйста, Ваши пожелания. и мы обязательно их учтём"
          v-model="comment"
          :value="comment"
          input-style="text-align: center"
        ></q-input>
      </div>

      <div class="order_form__field">
        <q-input
          color="accent"
          standout="bg-accent text-white"
          label="ПРОМОКОД"
          hint="Введите промокод при наличии"
          v-model="promocode"
          input-style="text-align: center"
          @update:model-value="computingPrice()"
        ></q-input>
      </div>

      <div class="order_form__field">
        <q-checkbox
          v-model="windows"
          label="ПОМЫТЬ ОКНА"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 500 рублей, но если в помещении окон больше двух - то расчёт производится индивидуально
        </div>
      </div>

      <div class="order_form__field">
        <q-checkbox
          v-model="linen"
          label="ПОГЛАДИТЬ БЕЛЬЁ"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 500 рублей за объём эквивалентный двум комплектам штор, если белья больше - то расчёт производится индивидуально
        </div>
      </div>

      <q-separator/>

      <div class="order_form__field">
        <q-checkbox
          v-model="microwave"
          label="ПОМЫТЬ МИКРОВОЛНОВКУ"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 400 рублей
        </div>
      </div>

      <div class="order_form__field">
        <q-checkbox
          v-model="oven"
          label="ПОМЫТЬ ДУХОВОЙ ШКАФ"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 400 рублей
        </div>
      </div>

      <div class="order_form__field">
        <q-checkbox
          v-model="fridge"
          label="ПОМЫТЬ ХОЛОДИЛЬНИК"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 400 рублей
        </div>
      </div>

       <q-separator/>

      <div class="order_form__field">
        <q-checkbox
          v-model="garbage"
          label="ВЫНЕСТИ МУСОР"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 200 рублей за объём до одного кубического метра
        </div>
      </div>

      <q-separator/>

      <div class="order_form__field">
        <q-checkbox
          v-model="deep_floor"
          label="ГЛУБОКАЯ ЧИСТКА ПОЛА"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 500 рублей за объём до 20 кв.м, если площадь больше - то расчёт и подход к выполнению рассчитываются отдельно
        </div>
      </div>

      <div class="order_form__field">
        <q-checkbox
          v-model="tile_joint"
          label="ЧИСТКА МЕЖПЛИТОЧНЫХ ШВОВ"
          @update:model-value="computingPrice()"
        />
        <div class="order_form__radio_hint">
          Это добавит к стоимости 500 рублей за объём до 20 кв.м, если площадь больше - то расчёт и подход к выполнению рассчитываются отдельно
        </div>
      </div>



      <div class="order_form__field">
        <q-input
          label="ЦЕНА"
          standout="bg-accent text-white"
          hint="Предварительная стоимость, для подтверждения заказа Вам в ближайшее время позвонит наш менеджер"
          :value="price"
          v-model="price"
          mask="### ### ###.##"
          reverse-fill-mask
          readonly
          input-style="text-align: center; color: #FF6105; font-size: 2.2rem;"
        ></q-input>
      </div>

      <div class="order_form__bottom">
        <div class="order_form__field" v-show="this.promocode !== null && this.promo_find !== 0">
          <p
            class="order_form__bottom_row"
          >
            Активирован промокод {{ this.promocode }} скидка составила:
            <span
              class="order_form__bottom_row_accent"
            >
            {{promo_markdown}}
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.promocode !== null && this.promo_find === 0">
          <p
            class="order_form__bottom_row"
          >
            Такой ПРОМОКОД не найден, проверье на правильность введенные данные
          </p>
        </div>

        <div class="order_form__field" v-show="this.windows === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость мойки двух окон :
            <span
              class="order_form__bottom_row_accent"
            >
            500
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.microwave === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость мойки микроволновой печи :
            <span
              class="order_form__bottom_row_accent"
            >
            400
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.oven === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость мойки духового шкафа :
            <span
              class="order_form__bottom_row_accent"
            >
            400
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.fridge === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость мойки холодильника :
            <span
              class="order_form__bottom_row_accent"
            >
            400
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.linen === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость глажки белья :
            <span
              class="order_form__bottom_row_accent"
            >
            500
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.garbage === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость выноса мусора :
            <span
              class="order_form__bottom_row_accent"
            >
            200
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.deep_floor === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость глубокой чистки пола :
            <span
              class="order_form__bottom_row_accent"
            >
            500
          </span>
            руб.
          </p>
        </div>

        <div class="order_form__field" v-show="this.tile_joint === true">
          <p
            class="order_form__bottom_row"
          >
            В цену включена стоимость чистки межплиточных швов :
            <span
              class="order_form__bottom_row_accent"
            >
            500
          </span>
            руб.
          </p>
        </div>

      </div>

      <div class="order_form__field">
        <q-btn
          class="order_form__submit"
          type="submit"
          label="ОТПРАВИТЬ ЗАКАЗ"
          standout="bg-accent text-white"
          color="accent"
          @click="onSubmit"
        />
      </div>

    </q-form>
  </div>
</template>

<script>
import moment from 'moment'
import {ref, toRaw} from 'vue'
import {
  YandexMap,
  YandexMapControls,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultMarker,
  YandexMapDefaultSchemeLayer,
  YandexMapEntity,
  YandexMapGeolocationControl,
  YandexMapZoomControl,
} from 'vue-yandex-maps'
import {geocoder} from 'src/boot/axios'
import {useAuthStore} from "stores/authStore"
import { Notify } from 'quasar'

export default {
    name: 'OrderForm',
    components: {
      YandexMap,
      YandexMapDefaultSchemeLayer,
      YandexMapDefaultFeaturesLayer,
      YandexMapControls,
      YandexMapGeolocationControl,
      YandexMapZoomControl,
      YandexMapEntity,
      YandexMapDefaultMarker,

    },
    data() {
      return {
        cleaning_types: ref([]),
        cleaning_type: ref(''),
        furniture_cluttered: ref([]),
        furniture_cluttered_val: ref(''),
        square: ref(''),
        room_choices: ref([]),
        room_choices_val: ref(''),
        pollution_degree: ref([]),
        pollution_degree_val: ref(''),
        promo: ref([]),
        promo_val: ref(''),
        promocode: ref(null),
        promo_find: ref(null),
        promo_markdown: ref(Number('')),
        date: ref(moment().format("YYYY-MM-DD")),
        time: ref(moment().format("HH:mm")),
        address: ref(''),
        file: ref(null),
        comment: ref(''),
        windows: ref(false),
        microwave: ref(false),
        oven: ref(false),
        garbage: ref(false),
        fridge: ref(false),
        linen: ref(false),
        deep_floor: ref(false),
        tile_joint: ref(false),
        map: ref(null),
        price: ref(Number('')),
        suggestResponse: ref([]),
        suggest: ref(''),
        check: ref(false),
        mapMarker: ref(null),
        mapSettings: {
          enterprise: false,
          coordorder: 'longlat',
          location: {
            center: [30.29, 59.92],
            zoom: 12
          }
        }
      }
    },
    beforeCreate() {
      this.$api.get('/cleaning_type.json')
        .then(res => {
          this.cleaning_types = res.data.map((i) => this.cleaning_type = i)
          console.log(this.cleaning_type)
        })
      this.$api.get('/furniture_cluttered.json')
        .then(res => {
          this.furniture_cluttered = res.data.map((i) => this.furniture_cluttered_val = i)
        })
      this.$api.get('/room_type.json')
        .then(res => {
          this.room_choices = res.data.map(i => this.room_choices_val = i)
        })
      this.$api.get('/pollution_degree.json')
        .then(res => {
          this.pollution_degree = res.data.map(i => this.pollution_degree_val = i)
        })
      this.$api.get('/promo.json')
        .then(res => {
          console.log(res)
          this.promo = res.data.map(i => this.promo_val = i)
        })
    },
    methods: {
      async geocodeSuggest() {
          this.suggest = event.target.value
          geocoder.get('', {
            params: {
              apikey: '6205f264-6946-4fbc-9905-1101b7c5dd01',
              geocode: this.suggest,
              format: 'json',
              results: 2,
              rspn: 1,
              ll: '30.29, 59.92',
              spn: '1.552069,1.400552',
            }
          })
            .then((res) => {
              this.suggestResponse =toRaw( res.data.response.GeoObjectCollection.featureMember.map(i => i.GeoObject))
              this.address = `${this.suggestResponse[0].name} ${this.suggestResponse[0].description}`
            })
        },
        tapMarker() {

          const selectedSuggest = this.suggestResponse[0]
          this.mapMarker = {
            coordinates: toRaw(selectedSuggest.Point.pos.split(' ')),
            title: selectedSuggest.name,
            subtitle: selectedSuggest.description
          }
          console.log(this.mapMarker.coordinates)
          this.mapSettings.location.center = this.mapMarker.coordinates
          this.address = selectedSuggest.name
          this.check = true

        },
        onSubmit() {
          this.$api.post('/orders.json', {
            "customer" : `${useAuthStore().me.id}`,
            "cleaning_type" : this.cleaning_type.id,
            "square" : this.square,
            "pollution_degree" : this.pollution_degree_val.id,
            "room_type" : this.room_choices_val.id,
            "cleaning_date" : this.date,
            "cleaning_time" : this.time,
            "photo" : this.file,
            "is_windows" : this.windows,
            "is_microwave" : this.microwave,
            "is_oven" : this.oven,
            "is_garbage" : this.garbage,
            "is_fridge" : this.fridge,
            "is_linen" : this.linen,
            "is_deep_floor" : this.deep_floor,
            "is_tile_joint" : this.tile_joint,
            "address" : this.address,
            "comment" : this.comment,
            "promo" : this.promo.id,
            "price" :  this.price,
          }).then(res => {
            console.log(res)

            Notify.create({
              color: 'accent',
              textColor:'white',
              message: 'Заказ успешно отправлен, для подтвержения вам в ближайшее время перезвонит наш менеджер',
              position: 'center',
              timeout: '10000'
            })
          })
            .catch(err => {
              const response = err.response

              Notify.create({
                color: 'red-5',
                textColor:'white',
                message: `${JSON.stringify(response.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
                position: 'center',
              })
            })

        },
        computingPrice() {
          const cleaning_type_price = Number(this.cleaning_type.price)
          const square_quantity = Number(this.square)
          const square_price = Number(cleaning_type_price) * Number(square_quantity)
          const furniture_cluttered_markup = Number(this.furniture_cluttered_val.markup)/100 * square_price
          const room_choises_markup = Number(this.room_choices_val.markup)/100 * square_price
          const pollution_degree_markup = Number(this.pollution_degree_val.markup)/100 * square_price
          this.promo_find  = this.promo.find(e => e.promocode === this.promocode) || 0
          this.promo_markdown = Number(this.promo_find.markup)/100 * square_price || 0
          const minutes = this.time.split(':')[0]*60+this.time.split(':')[1]*1
          const night_markup = minutes >= 1440 || minutes <= 480 ? square_price * 0.2 : 0
          const windows_markup = this.windows===true ? 500 : 0
          const microwave_markup = this.microwave === true ? 400 : 0
          const oven_markup = this.oven === true ? 400 : 0
          const fridge_markup = this.fridge === true ? 400 : 0
          const garbage_markup = this.garbage === true ? 200 : 0
          const linen_markup = this.linen === true ? 500 : 0
          const deep_floor_markup = this.deep_floor === true ? 400 : 0
          const tile_joint_markup = this.tile_joint === true ? 400 : 0
          console.log(square_price)
          this.price = (square_price + furniture_cluttered_markup + room_choises_markup + pollution_degree_markup - this.promo_markdown + night_markup + windows_markup + microwave_markup + oven_markup + fridge_markup + garbage_markup + linen_markup + deep_floor_markup + tile_joint_markup).toFixed(2)

        }
    },

  }
</script>

<style lang="scss" scoped>
.order_form__container {
  background-color: white;
  font-family: 'Comfortaa';
  display: flex;
  justify-content: center;
  align-items: center;
}

.order_form__header {
  text-align: center;
  margin: 2%;
  font-size: 2rem;
  font-family: 'Oswald';
  color: $accent;
  text-transform: uppercase;
}

.order_form {
  padding: 2%;
}

.order_form__subrow {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.order_form__field {
  margin: 1.5rem;
  padding-right: 0;
}

.order_form__search_input {
  pointer-events: all;
  height: 2.3rem;
}

.order_form__search_btn {
  pointer-events: all;
}


.order_form__field_btn {
  height: 3.4rem;
  width: 12rem;
}

.order_form__radio_hint {
  color: grey;
  font-size: 0.8rem;
  padding-left: 0.7rem;
}

.order_form__submit {
  height: 3.4rem;
  width: 100%;
}

.order_form__bottom {
  margin-top: 4rem;
  margin-bottom: 1rem;
}

.order_form__bottom_row {
  font-weight: bold;
  font-size: 1rem;
}

.order_form__bottom_row_accent {
  color: $accent;
}

@media screen and (max-width: 520px) {
  .order_form__subrow {
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>
