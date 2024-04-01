<template>
  <div class="header_text">
    <div class="main_h2__header_box">
      <h2 class="main_h2">{{ header }}</h2>
    </div>
    <div class="main_h2__text_box">
      <p class="main_h2__text">
        {{ text }}
      </p>
    </div>
    <div class="main_h2__text_box">
      <p class="header_text__subtext">
        {{ subtext }}
      </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'HeaderText',
    props: {
      header: {
        type: String,
        required: true
      },
      text: {
        type: String,
        required: true
      },
      subtext: {
        type: String
      }
    }
  }
</script>

<style lang="scss" scoped>
.header_text__subtext {
    font-family: 'Comfortaa';
    text-align: center;
    font-size: 1rem;
    padding: 0;
    color: $accent;
    font-weight: bold;
}
</style>