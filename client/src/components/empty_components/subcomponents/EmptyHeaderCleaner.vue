<template>
  <div class="empty_header__container">
    <div class="row empty_header__logo_box">
        <q-avatar square size="4rem" >
          <img class="empty_header__logo_img" src="../../../assets/icons/cclean_logo.svg"/>
        </q-avatar>
      <h2>
        <router-link class="empty_header__logo_text" to="/">
          <q-tooltip>
            Перейти на главную сайта
          </q-tooltip>
          CCLEAN
        </router-link>
      </h2>
      </div>
      <div>
        <h3 class="empty_header__logo_subheader">ДЛЯ КЛИНЕРА</h3>
      </div>
      <div class="row empty_header__greeting_box">
        <h2 class="empty_header__greeting">Добро пожаловать в команду профессионалов, вместе к новым свершениям!</h2>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'EmptyHeaderCleaner'
  }
</script>

<style lang="scss" scoped>
.empty_header__container {
  font-family: 'Comfortaa';
  margin: 2%;
}

.empty_header__logo_box {
  display: flex;
  justify-content: center;
  align-items: center;
}

.empty_header__logo_text{
  color: $accent;
  font-weight: bold;
  font-size: 2.6rem;
  text-decoration: none;
}

.empty_header__logo_subheader{
  font-size: 1rem;
  text-align: center;
  color: $accent;
}

.empty_header__greeting_box {
  display: flex;
  justify-content: center;
  align-items: center;
}

.empty_header__greeting {
  font-size: 1.2rem;
  line-height: 1.6rem;
  text-align: center;
  margin: 2%;
}

</style>
