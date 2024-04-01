<template>
  <div class="our_partners">
    <div class="main_h2__header_box">
      <h2 class="main_h2">НАШИ ПАРТНЁРЫ</h2>
    </div>
    <div class="row our_partners__card_container">
      <div 
        class="our_partners__card"
        v-for="n in 6" :key="n"
      ></div>
    </div>
  </div>
</template>

<script>

export default({
  name: 'OurPartners'
})
</script>

<style lang="scss">

.our_partners__card_container {
  padding-top: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.our_partners__card {
  background-color: $grey;
  height: 100px;
  width: 150px;
  border-radius: 2%;
  margin: 1%;
}
</style>