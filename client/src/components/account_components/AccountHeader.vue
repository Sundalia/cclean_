<template>
  <q-header class="row account_header">
      <q-toolbar class="account_header__toolbar">
        <div class="col acoount_header__customer_info">
          <div class="row account_header__customer_name">CUSTOMER NAME</div>
          <div class="row account_header__customer_phone">+7(999)99999999</div>
          <div class="row account_header__customer_mail">customer@mail.com</div>
        </div>
        <q-space/>

        <q-btn-group flat class="row account_header__toolitems">

          <q-btn flat class="row account_header__toolitem">
            <q-tooltip>
              Перейти на главную сайта
            </q-tooltip>
            <q-avatar square size="1.5rem" >
                <img class="main_header__logo_img" src="../../assets/icons/cclean_logo.svg"/> 
            </q-avatar>
            <router-link class="account_header__logo_name" to="/">
                C-CLEAN
            </router-link>
          </q-btn>

          <q-btn class="account_header__toolitem" type="a" to="support">
            <q-tooltip>
              Написать обращение в поддержку
            </q-tooltip>
            ПОДДЕРЖКА
          </q-btn>
          <q-btn class="account_header__toolitem">
            <q-tooltip>
              Выход из аккаунта
            </q-tooltip>
            ВЫЙТИ
          </q-btn>
        </q-btn-group>

        <q-btn flat icon="menu" class="q-mg-lg account_header__burger">
          <q-menu>
            <q-btn-group flat class="row account_header__toolitems">
            <q-btn flat class="row account_header__toolitem">
              <q-tooltip>
                Перейти на главную сайта
              </q-tooltip>
              <q-avatar square size="1.5rem" >
                  <img class="main_header__logo_img" src="../../assets/icons/cclean_logo.svg"/> 
              </q-avatar>
              <router-link class="account_header__logo_name" to="/">
                  C-CLEAN
              </router-link>
            </q-btn>

            <q-btn class="account_header__toolitem" type="a" to="support">
              <q-tooltip>
                Написать обращение в поддержку
              </q-tooltip>
              ПОДДЕРЖКА
            </q-btn>
            <q-btn class="account_header__toolitem">
              <q-tooltip>
                Выход из аккаунта
              </q-tooltip>
              ВЫЙТИ
            </q-btn>
          </q-btn-group>
          </q-menu>
        </q-btn>


      </q-toolbar>
  </q-header>
</template>

<script>


  export default {
    name: 'AccountHeader'
  }
</script>

<style lang="scss" scoped>
.account_header {
  background-color: $background;
}

.account_header__toolbar{
  font-family: 'Comfortaa';
  align-items: start;
}

.acoount_header__customer_info {
  color: $dark;
  margin: 2%;
  line-height: 2rem;
  font-size: 1.2rem;
}

.account_header__logo_name {
    text-decoration: none;
    color: $accent;


}

.account_header__toolitem {
  color: $dark;
  line-height: 1rem;
  font-size: 1rem;
  align-items: center;
  justify-content: center;
}

// @media screen and (min-width: 520px) {
//   .account_header__burger {
//     display: none;
//   }
// }
</style>