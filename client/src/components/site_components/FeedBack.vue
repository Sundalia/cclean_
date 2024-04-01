<template>
  <div>
    <swiper
      class="feedback__swiper"
      :spaceBetween="30"
      :freeMode="true"
      :pagination="{
        clickable: true,
      }"
      :modules="modules"
      :breakpoints="{
        1280: {
          slidesPerView: 5,
        },
        820: {
          slidesPerView: 3
        },
        520: {
          slidesPerView: 2
        },
        320: {
          slidesPerView: 1
        }

      }"
  
    >
      <swiper-slide v-for="i in 10" :key="i">
        <FeedBackCell/>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import FeedBackCell from './subcomponents/FeedBackCell.vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { FreeMode, Pagination } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/free-mode'
import 'swiper/css/pagination'


  export default {
    name: 'FeedBack',
    components: {
      FeedBackCell,
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        
      }
    },
    setup() {
      return {
        modules: [FreeMode, Pagination],
      }
    }
  }
</script>

<style lang="scss" scoped>

.feedback__swiper{
  padding: 2%;
}

</style>