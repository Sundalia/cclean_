<template>
        <q-carousel
        v-model="slide"
        transition-prev="scale"
        transition-next="scale"
        swipeable
        animated
        autoplay
        control-color="white"
        navigation
        padding
        arrows
        height="300px"
        infinite
        class="bg-primary text-white shadow-1 rounded-borders"
      >
      <template v-slot:navigation-icon="{ active, btnProps, onClick }">
        <q-btn v-if="active" size="lg" icon="circle" color="accent" flat round dense @click="onClick" />
        <q-btn v-else size="sm" :icon="btnProps.icon" color="white" flat round dense @click="onClick" />
      </template>
      
        <q-carousel-slide 
          name="style1" 
          class="column no-wrap flex-center"
          img-src="../../../../assets/cleaning_photos/do_posle.png"
        >
          <q-btn to="portfolio">
            ПОСМОТРЕТЬ В РАЗДЕЛЕ ПОРТФОЛИО
          </q-btn>
        </q-carousel-slide>

        <q-carousel-slide 
          name="style" 
          class="column no-wrap flex-center"
          img-src="../../../../assets/cleaning_photos/do_posle.png"
        ></q-carousel-slide>

        <q-carousel-slide 
          name="style" 
          class="column no-wrap flex-center"
          img-src="../../../../assets/cleaning_photos/do_posle.png"
        ></q-carousel-slide>

      </q-carousel>
</template>

<script>
import { ref } from 'vue';

export default({
  name: 'WeDidCarousel',
  setup() {
    return {
      slide: ref('style'),
      lorem: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit.'
    }
  }
})
</script>