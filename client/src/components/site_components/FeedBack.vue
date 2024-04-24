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
      <swiper-slide v-for="i in feedback" :key="i">
        <FeedBackCell
          :name="i.name"
          :stars="i.feedback_rating"
          :body="i.feedback_body"
        />
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
import { ref } from 'vue'


  export default {
    name: 'FeedBack',
    components: {
      FeedBackCell,
      Swiper,
      SwiperSlide
    },
    data() {
      return {
        feedback: ref([]),
      }
    },
    setup() {
      return {
        modules: [FreeMode, Pagination],
      }
    },
    beforeCreate() {
      this.$api.get('/feedback.json')
        .then(res => {
          console.log(res.data.map(i => i.feedback_rating))
          this.feedback = res.data.map(i => i)
        })
        .catch(err => {
          console.log(err.data)
        })
    }
  }
</script>

<style lang="scss" scoped>

.feedback__swiper{
  padding: 2%;
}

</style>