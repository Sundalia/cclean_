<template>
  <div class="row feedback_cell__container">
    <div class="col-1 feedback_cell__avatar_col">
      <q-avatar>
        <q-img src="https://cdn.quasar.dev/img/avatar.png"/>
      </q-avatar>
    </div>
    <div class="col">
      <div class="row feedback_cell__name">
        NAME
      </div>
      <div class="row">
        <q-rating size="1rem" v-model="stars" :max="5" color="accent"/>
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
  </div>
</template>

<script>
import { ref } from 'vue';

  export default ({
    name: 'FeedbackCarouselCell',
    setup () {
      return {
        stars: ref(4)
      }
    }
  })
</script>

<style lang="scss">
.feedback_cell__container {
  background-color: white;
  max-height: 200px;
  border-radius:5px;
  padding: 5%;
  margin: 1%;
  overflow: hidden;

}

.feedback_cell__avatar_col{
  margin-right: 5%;
  width: 70px;
}

.feedback_cell__name {
  font-family: 'Comfortaa';
  font-weight: bold;
}

.feedback_cell__text {
  margin-bottom: 5%;
}
</style>