<template>
  <div class="portfolio_card__container">

    <div class="main_h2__header_box">
      <h2 class="main_h2">
        {{ header }}
      </h2>
    </div>

    <p>DDD</p>

  </div>
</template>

<script>
  export default {
    name: 'PortfolioCard',
    props: {
      header: {
        type: String,
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>