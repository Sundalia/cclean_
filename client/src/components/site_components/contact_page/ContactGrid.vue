<template>
  <div class="contact_grid__container">
    <div class="contact_grid">

      <div class="row contact_grid__header">
        <h3>Как с нами связаться:</h3>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Наш Телеграм-канал с новостями и промокодами:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="positive"
            icon="telegram"
            label="@CcleanSP" 
            href="https://t.me/ccleansp"
          />
        </div>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Телеграм-контакт для ответов по всем интересующим вопросам:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="positive"
            icon="telegram"
            label="@CcleanSPB" 
            href="https://t.me/CcleanSPB"
          />
        </div>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Телеграм-бот для заказа уборки:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="positive"
            icon="telegram"
            label="@CcleanSPB_bot" 
            href="https://t.me/CCleanSPB_bot"
          />
        </div>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Ватсапп-контакт для ответов по всем интересующим вопросам:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="info"
            href="https://wa.me/qr/Y4Z6OVFJ5KTPD1"
          >
              <q-avatar size="1.3rem" style="margin-right: 0.9rem;">
                <img src="../../../assets/icons/whatsapp.svg"/>
              </q-avatar>
              @CcleanSPB
          </q-btn>
        </div>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Адрес почты для отправки обращений и предложений:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="accent"
            icon="mail"
            label="ccleanspb@yandex.ru" 
            href="mailto:ccleanspb@yandex.ru"
          />
        </div>
      </div>

      <div class="row contact_grid__row">
        <div class="col contact_grid__label">
          <strong>Номер телефона:</strong>
        </div>
        <div class="col colcontact_grid__btn">
          <q-btn 
            flat 
            unelevated
            type="a" 
            text-color="accent"
            icon="phone"
            label="+79812007083" 
            href="tel:+79812007083"
          />
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: 'ContactGrid'
  }
</script>

<style lang="scss" scoped>
.contact_grid__container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5%;
  font-family: 'Comfortaa';
}

.contact_grid {
  width: 100%;
}

.contact_grid__header {
  font-family: 'Oswald' !important;
  font-size: 14px !important;
  margin: 4rem !important;
  align-items: center;
  justify-content: center;
  display: flex;
}

.contact_grid__row {
  margin: 1rem;
}

.contact_grid__label {
  color: grey;
  text-align: end;
  margin: 0.5rem;
}

.contact_grid__btn {
  margin: 0.5rem;
}
</style>