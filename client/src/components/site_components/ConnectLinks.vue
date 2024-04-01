<template>
  <HeaderText :header="header" :text="text"/>
  <div class="row connect_links__container">
    <div class="col connect_links__btn_container">
      
      <q-btn 
        class="row connect_links__button"
        type="a"
        href="mailto:Nik123avito@yandex.ru"
        target="_blank"
      >
      <img class="connect_links__img" src="../../assets/connect_link/email_connect.svg" alt="c-clean"/>
      <p class="connect_links__text">отправить письмо</p>
    </q-btn>
    </div>

    <div class="col connect_links__btn_container">
      <q-btn 
        class="connect_links__button"
        type="a"
        href="tel:+79812007083"
        target="_blank"
      >
      <img class="connect_links__img" src="../../assets/connect_link/phone_connect.svg" alt="c-clean"/>
      <p class="connect_links__text">позвонить по телефону</p>
    </q-btn>
    </div>

    <div class="col connect_links__btn_container">
      <q-btn 
        class="connect_links__button"

      >
      <img class="connect_links__img" src="../../assets/connect_link/order_connect.svg" alt="c-clean"/>
      <p class="connect_links__text">заказать звонок</p>
    </q-btn>
    </div>

    <div class="col connect_links__btn_container">
      <q-btn 
        class="connect_links__button"
        type="a"
        href="https://t.me/ccleansp" 
        target="_blank"
      >
      <img class="connect_links__img" src="../../assets/connect_link/tg_connect.svg" alt="c-clean"/>
      <p class="connect_links__text">написать в telegram</p>
    </q-btn>
    </div>

    <div class="col connect_links__btn_container">
      <q-btn 
        class="connect_links__button"
        type="a"
        href="https://wa.me/qr/Y4Z6OVFJ5KTPD1"
        targer="_blank"
      >
      <img class="connect_links__img" src="../../assets/connect_link/wa_connect.svg" alt="c-clean"/>
      <p class="connect_links__text">написать в whatsapp</p>
    </q-btn>
    </div>

  </div>
</template>

<script>
import HeaderText from './HeaderText.vue';

  export default ({
    name: 'ConnectLinks',
    components: {
      HeaderText
    },
    data() {
      return {
        header: 'закажите уборку прямо сейчас',
        text: 'любым понравившимся способом',
        callback: ''
      }
    }
  })
</script>

<style lang="scss">
.connect_links__container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  padding: 2%;
}

.connect_links__btn_container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  padding: 2%;

}

.connect_links__button {
  background-color: $accent;
  height: 220px;
  max-width: 220px;
  color: white;
  padding: 10px;
  border-radius: 10px;
  min-width: 100px;
}

.connect_links__img {
  padding: 10px;
}

.connect_links__text {
  text-transform: uppercase;
  font-family: 'Comfortaa';
  font-weight: bold;
  max-width: 150px;
}

@media screen and (max-width: 820px) {
  .connect_links__container {
    grid-template-columns: repeat(1, 1fr);
  }

  .connect_links__button {
    width: 100%;
    font-size: 16px;
    max-width: none;
    height: 150px;

  }

  .connect_links__img {
    width: 70px;
  }
}
</style>