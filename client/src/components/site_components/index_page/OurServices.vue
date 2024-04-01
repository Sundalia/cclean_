<template>
  <div class="our-services__container">
    <div class="main_h2__header_box">
      <h2 class="main_h2">какие услуги мы предоставляем</h2>
    </div>
    <div class="main_h2__text_box">
      <p class="main_h2__text">
        Наши клинеры хорошо обучены, 
        отлично знают и любят своё дело и 
        потому постоянно совершенствуют свои навыки
      </p>
    </div>
    <ThreeDCarousel/>
  </div>
</template>

<script>
import ThreeDCarousel from './subcomponents/ThreeDCarousel.vue'

export default({
  name: 'OurServices',
  components: {
    ThreeDCarousel
  }
})
</script>

<style lang="scss">
.our-services__container {
  margin: 5%;
}
</style>