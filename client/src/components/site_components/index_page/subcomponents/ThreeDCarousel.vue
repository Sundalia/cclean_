<template>
  <div class="swiper__container">
    <swiper
      class="swiper__wrap"
      navigation
      :loop="true"
      :effect="'coverflow'"
      :grabCursor="true"
      :centeredSlides="true"
      :slidesPerView="3"
      draggable="true"
      :coverflowEffect="{
        rotate: 0,
        stretch: 0,
        depth: 30,
        modifier: 10,
        slideShadows: false,
      }"
      :pagination="true"
      :modules="modules"
    >

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-1.png"
          alt="послетроительная уборка спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">ПОСЛЕСТОИТЕЛЬНАЯ УБОРКА</h2>
            <q-btn 
              to="post_construction_cleaning"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-2.png"
          alt="поддерживающая уборка спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">ПОДДЕРЖИВАЮЩАЯ УБОРКА</h2>
            <q-btn 
              to="maintenance_cleaning"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-3.png"
          alt="генеральная уборка спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">ГЕНЕРАЛЬНАЯ УБОРКА</h2>
            <q-btn
              to="spring_cleaning" 
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-4.png"
          alt="мойка окон спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">МОЙКА ОКОН</h2>
            <q-btn 
              to="window_cleaning"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-5.png"
          alt="уборка производства спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">УБОРКА ПРОИЗВОДСТВА</h2>
            <q-btn 
              to="industrial_cleaning"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-6.png"
          alt=""
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">ГЛУБОКАЯ ЧИСТКА ПОЛА</h2>
            <q-btn 
              to="rotor"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-7.png"
          alt=""
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">УБОРКА ЯХТЫ</h2>
            <q-btn 
              to="yacht"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-8.png"
          alt="уборка загородного дома спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">УБОРКА ЗАГОРОДНОГО ДОМА</h2>
            <q-btn 
              to="cottage_cleaning"
              class="main__button"
              target="_blank"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>
    <swiper-slide class="swiper__slide">
      <q-card class="swiper__card">
        <q-img 
          class="swiper__card_img" 
          src="../../../../assets/cleaning_photos/car-9.png"
          alt="уборка офиса спб"
        ><div class="swiper__card_botom absolute-bottom text-subtitle2 text-center">
            <h2 class="swiper_h2">УБОРКА ОФИСА</h2>
            <q-btn 
              to="office_cleaning"
              target="_blank"
              class="main__button"
            >Что входит
            </q-btn>
          </div>
        </q-img>
      </q-card>
    </swiper-slide>

  </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/scss';
import 'swiper/scss/effect-coverflow';
import 'swiper/scss/navigation'
import { EffectCoverflow, Navigation } from 'swiper/modules';

  export default ({
    name: 'ThreeDCarousel',
    components: {
      Swiper,
      SwiperSlide,
    },
    setup() {
      return {
        modules: [EffectCoverflow, Navigation]
      }
    },
  })
</script>

<style lang="scss" scoped>
.swiper__wrap {
  width: 100%;
}

.swiper__card {
  min-width: 200px;
  min-height: 300px;
}

.swiper__card_img {
  min-width: 200px;
  min-height: 300px;
}

.swiper_h2 {
  font-family: 'Oswald';
  font-size: 1.5rem;
  line-height: 3rem;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
}


@media screen and (max-width: 520px) {
  .swiper_h2 {
    font-family: 'Oswald';
    font-size: 1rem;
    line-height: 2rem;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;  
  }
}

</style>