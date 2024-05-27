<template>
  <div class="row main_feedback__container">

    <div class="col">

      <q-scroll-area
        class="main_feedback__scroll_area"
        :visible="true"
        :thumb-style="{background: '#FF6105', opacity: 1}"
      >
        <div v-for="n in this.feedback" :key="n">
          <FeedbackCell  :name="n.name" :stars="n.feedback_rating" :body="n.feedback_body"/>
        </div>
      </q-scroll-area>

    </div>

    <div class="col main_feedback__text_container">
      <div class="main_h2__header_box">
        <h2 class="main_h2">
          А ЗДЕСЬ ОТЗЫВЫ
        </h2>
      </div>

      <div class="main_h2__text_box">
        <p class="main_h2__text">
          Отзывами о нашей работе мы гордимся и ценим,
          они помогают нам стать лучше, ради чего в любую погоду едем даже в самые отдалённые районы делать на совесть свою работу.
          Потому наши отзывы настоящие и умеют греть наши сердечки.
        </p>
      </div>
      <div class="main_feedback__btn_container">

        <q-btn class="main__button" type="a" to="login/registration">
          ОСТАВИТЬ ОТЗЫВ
        </q-btn>
      </div>
    </div>


  </div>
</template>

<script>
import FeedbackCell from './subcomponents/FeedbackCell.vue';
import {ref} from "vue";


export default({
  name: 'MainFeedback',
  components: {
    FeedbackCell
  },
  data() {
    return {
      feedback: ref([]),
    }
  },
  beforeCreate() {
    this.$api.get('/feedback.json')
      .then(res => {
        console.log(res.data.map(i => i))
        this.feedback = res.data.map(i => i)
      })
      .catch(err => {
        console.log(err.data)
      })
  }
})
</script>

<style lang="scss" scoped>

.main_feedback__container {
  padding: 5%;
  display:grid;
  grid-template-columns: repeat(2, 1fr);
}

.main_feedback__scroll_area {
  background-color: $dark;
  height: 350px;
  width: 100%;
}

.main_feedback__text_container {
  margin-left: 5%;
}

.main_feedback__btn_container {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 5%;
}

@media screen and (max-width: 520px) {
  .main_feedback__container {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
  }

  .main_feedback__text_container{
    order: -1;
  }
}
</style>
