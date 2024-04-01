<template>
    <div class="feedback_cell__container">
    <div class="row feedback_cell__avatar_name_col">
      <div class="col-3 feedback_cell__avatar_box">
        <q-avatar>
        <q-img src="https://cdn.quasar.dev/img/avatar.png"/>
      </q-avatar>
      </div>
      <div class="col">
        <span class="row feedback_cell__name">
          NAME
        </span>
        <div class="row">
          <q-rating size="1rem" v-model="stars" :max="5" color="accent"/>
        </div>
      </div>

    </div>
    <div class="row feedback_cell__text">
      <p>
        Первый раз воспользовалась услугой химчистки. 
        Очень понравилось и сопровождение заказа (связывались по вацап и передавали вопросы от технолога, 
        спрашивали что и как лучше сделать), и удобный сервис по приему и выдаче заказа через курьеров, 
        и качество чистки. Очень довольна и уже рекомендовала друзьям. Спасибо! Так держать 😊
      </p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

  export default {
    name: 'FeedBackCell',
    data() {
      return {
        stars: ref(4)
      }
    }
  }
</script>

<style lang="scss" scoped>

.feedback_cell__container{
  max-width: 300px;
  max-height: 270px;
  min-width: 150px;
  border-radius: 2%;
  margin: 2%;
  background-color: white;
  padding: 2%;
  overflow-y: scroll;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.feedback_cell__container::-webkit-scrollbar {
  display: none;
}

.feedback_cell__text{
  padding-top: 2%;
}

</style>