<template>
  <div class="app_banner__container">
    <div class="row">
      <div class="col app__banner__text_part">
        <div class="row">
          <h2 class="app_banner__header">больше возможностей в нашем приложении</h2>
        </div>
        <div class="row">
          <div class="col app_banner__app_btn_box">
            <img class="app_banner__app_btn" src="../../assets/google_play.png"/>
          </div>
          <div class="col app_banner__app_btn_box">
            <img class="app_banner__app_btn" src="../../assets/app_store.png"/>
          </div>
        </div>
      </div>
      <div class="col app_banner__img_box">
        <img class="app_banner__img" src="../../assets/app_phone.svg"/>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AppBanner'
  }
</script>

<style lang="scss" scoped>

.app_banner__container {
  background-color: $grey;
  display: flex;
  justify-content: center;
  align-items: center;
  
}

.app__banner__text_part{
  padding: 7%;
}

.app_banner__header {
  font-family: 'Oswald';
  margin: 2%;
  font-size: 2.5rem;
  line-height: 3rem;
  font-weight: bold;
  text-align: flex-start;
  text-transform: uppercase;
  color: $accent;

}

.app_banner__app_btn_box {
  display: flex;
  margin: 2%;
  justify-content: flex-start;
  max-width: 200px;
  min-width: 100px;
}

.app_banner__app_btn {
  width: 80%;
}

.app_banner__img_box {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  overflow: hidden;
  min-width: 200px;
}

.app_banner__img {
  max-height: 300px;
}

@media screen and (max-width: 520px) {
  
}

</style>