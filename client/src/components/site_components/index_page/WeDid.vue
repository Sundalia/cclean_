<template>
  <div class="row wedid__container">

    <div class="col wedid__text_container">
      <div class="main_h2__header_box">
        <h2 class="main_h2">
          ПОСМОТРИТЕ ЧТО МЫ УЖЕ СДЕЛАЛИ
        </h2>
      </div>
      <div class="main_h2__text_box">
        <p class="main_h2__text">
          Нет таких бытовых и строительных загрязнений, открытых человечеством, 
          с которыми мы не можем справиться, об этом свидетельствует наш опыт, 
          которым мы охотно делимся в разделе 
          <router-link 
            to="portfolio" 
            target="_blank" 
            class="main_h2__text_orange"
          >
            портфолио
          </router-link>
        </p>
      </div>
    </div>

    <div class="col wedid__carousel_container">
      <WeDidCarousel/>
    </div>

  </div>

</template>

<script>
import WeDidCarousel from './subcomponents/WeDidCarousel.vue';

export default({
  name: 'WeDid',
  components: {
    WeDidCarousel
  }
})
</script>

<style>
.wedid__container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  margin: 5%;
}

.wedid__text_container {
  padding-right: 1rem;
}

@media screen and (max-width: 820px) {
  .wedid__container{
    grid-template-columns: repeat(1, 1fr);
  }
}

</style>