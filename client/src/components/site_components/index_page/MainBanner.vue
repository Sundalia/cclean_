<template>
  <q-banner class="main_banner">
    <h1 class="main_banner__h1">
      <span class="main_banner__h1-start">ПРОФЕССИОНАЛЬНЫЕ</span><br/>
      КЛИНИНГОВЫЕ УСЛУГИ<br/> В САНКТ-ПЕТЕРБУРГЕ<br/> ОТ
      <span class="main_banner__h1-end">3000 РУБ</span>
    </h1>
      <q-btn class="col self-center main_banner__down_arrow" icon="expand_more"></q-btn>
  </q-banner>
</template>

<script>

</script>

<style lang="scss" scope>

.main_banner {
  height: 600px;
  margin: 0;
  padding: 0;
  background-image: url("../../../assets/backgrounds/main_background.svg");
  background-repeat: no-repeat;
  background-position: center;
  font-family: 'Oswald';
  position:relative;
  }

  .main_banner__h1 {
    margin-right: 5vw;
    text-align: end;
    font-size: 4rem;
    font-weight: bold;
    color: white;
  }

  .main_banner__h1-start {
    color: $accent;
  }

  .main_banner__h1-end {
    color: black;
    background-image: url("../../../assets/backgrounds/smear.svg");
    background-size: 110%;
  }

  .main_banner__down_arrow {
    background-color: $accent;
    position: absolute;
    z-index: 3;
    top: 580px;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    max-width: 60px;

  }

  @media screen and (max-width: 820px){
    .main_banner {
      height: 400px;
    }

    .main_banner__down_arrow {
      top:380px;
    }

    .main_banner__h1 {
      font-size: 3rem;
      line-height: 3.8rem;
    }
  }

  @media screen and (max-width: 560px) {
    .main_banner__h1 {
      font-size: 2rem;
      line-height: 2.6rem;
    }
  }
</style>