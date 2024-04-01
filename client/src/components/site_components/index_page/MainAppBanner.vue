<template>
  <div class="row main_app_banner__container">

    <div class="col-8 main_app_banner__wordpart_container">
      <div class="row main_app_banner__header_container">
        <h2 class="main_app_banner__header">полный контроль над уборкой</h2>
      </div>
      <div class="main_app_banner__text_box">
        <p class="main_app_banner__text">
          В нашем приложении вы сможете:
        </p>
        <ul class="main_app_banner__text_list">
          <li>отслеживать статус уборки и получать полный отчёт по окончании</li>
          <li>выбирать клинеров по своим предпочтениям</li>
          <li>заказывать отчётные документы и производить оплату безналично</li>
          <li>забирать самые крутые промокоды  на уборку</li>
        </ul>
      </div>
      <div class="row main_app_banner__app_btn_box">
        <div class="col main_app_banner__app_btn_box">
          <img class="main_app_banner__app_btn" src="../../../assets/google_play.png"/>
        </div>
        <div class="col main_app_banner__app_btn_box">
          <img class="main_app_banner__app_btn" src="../../../assets/app_store.png"/>
        </div>
      </div>
    </div>
    <div class="col main_app_banner__img_box">
      <img class="main_app_banner__img" src="../../../assets/app_phone.svg"/>
    </div>

  </div>
</template>

<script>
  export default ({
    name: 'MainAppBanner'
  })
</script>

<style lang="scss" scoped>

.main_app_banner__container {
  justify-content: center;
}

.main_app_banner__wordpart_container {
  padding: 5%;
}

.main_app_banner__header_container {
  display: flex;
  justify-content: flex-start;
  padding-bottom: 3rem;
  color: $accent;
}

.main_app_banner__header {
  font-family: 'Oswald';
  font-size: 3rem;
  line-height: 3.6rem;
  font-weight: bold;
  text-align: flex-start;
  text-transform: uppercase;
}

.main_app_banner__text_box {
  font-family: 'Comfortaa';
  font-size: 1rem;
  padding-bottom: 3rem;
}

.main_app_banner__text_list {
  padding-left: 3rem;
}

.main_app_banner__img_box {
  justify-content: flex-end;
  align-items: flex-end;
  overflow: hidden;
}

.main_app_banner__img {
  max-height: 500px;
}

.main_app_banner__app_btn_box {
  display: flex;
  justify-content: flex-start;
  max-width: 600px;
}

.main_app_banner__app_btn {
  width: 80%;
}

@media screen and (max-width: 820px) {
  .main_app_banner__container {
    display: grid;
    grid-template-columns: repeat(1);
  }

  .main_app_banner__wordpart_container{
    width: 100%;
    justify-content: center;
  }

  .main_app_banner__img_box {
    width: 100%;
    justify-content: center;
    padding: 0;
  }
}
</style>