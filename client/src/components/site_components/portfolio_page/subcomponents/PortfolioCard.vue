<template>
  <div class="portfolio_card__container">

    <!-- <div class="row main_h2__header_box">
      <h2 class="main_h2">{{ header }}</h2>
    </div> -->

    <div class="portfolio_card__carousel_container">
      <q-carousel
        class="portfolio_card__carousel"
        swipeable
        :autoplay="autoplay"
        animated
        :model-value="slide"
        navigation
        infinite
        arrows
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
        navigation-position="bottom"
        :padding="true"
      >

      <template v-slot:navigation-icon="{ onClick, index }">
        <q-btn @click="onClick">
          <q-avatar class="portfolio_card__thumbnails" square>
            <img :src="slides[index].picture"/>
          </q-avatar>
        </q-btn>
      </template>

        <q-carousel-slide class="portfolio_card__carousel_slide" v-for="i in slides" :key="i" :name="i.name">
          <q-card class="portfolio_card__carousel_card">
            <q-img class="portfolio_card__carousel_img" :src="i.picture"/>
            <q-card-section>
              <div class="text-subtitle2">{{ i.description }}</div>
            </q-card-section>
          </q-card>
        </q-carousel-slide>
      </q-carousel>
    </div>

  </div>
</template>

<script>
import { ref } from 'vue'

  export default {
    name: 'PortfolioCard',
    props: {
      header: {
        type: String,
        required: true
      },
      slides: {
        type: Array,
        required: true
      },
      slide: {
        Type: String,
        required: true
      }
    },
    data() {
      return {
        autoplay: ref(true)
      }
    }
  }
</script>

<style lang="scss" scoped>
.main_h2 {
  color: $accent;
}

.portfolio_card__carousel {
  height: 650px;
  width: 100%;
}

.portfolio_card__carousel_slide {
  background-color: $background;
  display: flex;
  justify-content: center;
}

.portfolio_card__carousel_card {
  height: 500px;
  width: 100%;
  font-size: 1rem;
  font-family: 'Comfortaa';
  text-align: center;
}

.portfolio_card__carousel_img {
  height: 70%;
  width: 100%;
}

.portfolio_card__thumbnails {
  height: 70px;
  width: 100px;
  min-height: 50px;
  min-width: 70px;
}

</style>