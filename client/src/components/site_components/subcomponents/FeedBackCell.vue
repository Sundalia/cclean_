<template>
    <div class="feedback_cell__container">
    <div class="row feedback_cell__avatar_name_col">

      <div class="col">
        <span class="row feedback_cell__name">
          {{ name }}
        </span>
        <div class="row">
          <q-rating size="1rem" :model-value="stars" :max="5" color="accent"/>
        </div>
      </div>

    </div>
    <div class="row feedback_cell__text">
      <p>
        {{ body }}
      </p>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'FeedBackCell',
    props: {
      name: {
        type: Number,
        required: true
      },
      stars: {
        type: Number
      },
      body: {
        type: String,
        required: true
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