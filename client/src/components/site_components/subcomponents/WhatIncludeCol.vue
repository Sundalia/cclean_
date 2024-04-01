<template>
    <div class="col what_include__container">
      <div class="row what_include__image_box">
        <q-img
          :src="require(`../../../assets/backgrounds/${img_src}`)"
          class="what_include__image"
        >
          <h2 class="absolute-bottom what_include__img_h2">{{ img_header }}</h2>
        </q-img>
      </div>

      <div class="row what_include__accordion_box">
        <h2 class="what_include__accordion_h2">ВКЛЮЧЕНО В СТОИМОСТЬ</h2>
          <q-expansion-item 
            header-class="bg-grey"
            group="whatinclude"
            class="what_include__accordion" 
            v-for="i in what_include"
            :key="i"
            :label="i.name"
          >
            <q-card>
              <q-card-section>
                <q-list v-for="item in i.include_list" :key="item">
                  <q-item>{{ item }}</q-item>
                </q-list>
              </q-card-section>
            </q-card>
          </q-expansion-item> 
      </div>

      <div class="row what_include__accordion_box">
        <h2 class="what_include__accordion_h2">МОЖНО ДОБАВИТЬ</h2>
        <!-- //поставить template v-if empty -->
          <q-expansion-item 
            header-class="bg-grey"
            class="what_include__accordion"
            group="canadd" 
            v-for="i in can_add"
            :key="i"
            :label="i.name+'&nbsp;&nbsp;&nbsp;'+i.price+'р.'"
          >
            <q-card>
              <q-card-section>
                <q-list v-for="item in i.can_add_list" :key="item">
                  <q-item>{{ item }}</q-item>
                </q-list>
              </q-card-section>
            </q-card>
          </q-expansion-item> 
      </div>

    </div>
</template>

<script>
  export default {
    name: 'WhatIncludeCol',
    props: {
      img_src: {
        type: String,
        required: true
      },
      img_header: {
        type: String,
        required: true
      },
      what_include: {
        type: Array,
        required: true
      },
      can_add: {
        type: Array
      }
    }
  }
</script>

<style lang="scss" scoped>

.what_include__container{
  max-width: 400px;
  margin: 2%;
}

.what_include__image {
  text-align: center;
  height: 250px;
}

.what_include__img_h2 {
  color: white;
  font-family: 'Oswald';
  font-size: 3rem;
  padding-bottom: 2rem;
  font-weight: bold;
}

.what_include__accordion_h2{
  color: $dark;
  font-family: 'Oswald';
  font-size: 1rem;
  font-weight: bold;
  text-align: center;
  background-color: $accent;
  width: 100%;
}

.what_include__accordion_box{
  font-family: 'Comfortaa';
  font-size: 0.8rem;
  justify-content: center;
}

.what_include__accordion{
  width: 100%;
  max-width: 450px;
}

</style>