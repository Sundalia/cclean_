<template>
  <q-footer class="col footer__container">
    <div class="row footer_menu_box">

      <div class="row footer__menu">

        <div class="col footer__menu_col">

          <div class="row">
            <h2 class="footer__menu_col_header">
              c-clean
            </h2>
          </div>

          <div class="row footer__menu_col_list_container">
            <nav>
              <ul>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="contact_us">контакты</router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="support">поддержка</router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <q-btn 
                    class="footer__menu_col_list_btn"
                    target="_blank" 
                    to="vacancies"
                  >
                  стать клинером
                  </q-btn>
                </li>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="vacancies">вакансии</router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="feedback">отзывы</router-link></p>
                </li>

              </ul>
            </nav>
          </div>

        </div> 

        <div class="col footer__menu_col">

          <div class="row">
            <h2 class="footer__menu_col_header">
              услуги
            </h2>
          </div>        

          <div class="row footer__menu_col_list_container">
            <nav>
              <ul>
                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                        class="footer__menu_col_list_item_link" 
                        to="maintenance_cleaning" 
                        target="_blank"
                      >
                      поддерживающая уборка
                    </router-link>
                  </p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                        class="footer__menu_col_list_item_link" 
                        to="spring_cleaning" 
                        target="_blank"
                      >
                      генеральная уборка
                    </router-link>
                  </p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="post_construction_cleaning"
                      target="_blank"
                    >
                      послестроительная уборка
                    </router-link>
                  </p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="window_cleaning"
                      target="_blank"
                    >
                      мойка окон
                    </router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="office_cleaning"
                      target="_blank"
                    >
                      уборка офиса
                    </router-link>
                  </p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="industrial_cleaning"
                      target="_blank"
                    >
                      уборрка производства
                    </router-link>
                  </p>
                </li>


                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="cottage_cleaning"
                      target="_blank"
                    >
                      уборка загородного дома
                    </router-link>
                  </p>
                </li>


                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="yacht"
                      target="_blank"
                    >
                      уборка яхты
                    </router-link>
                  </p>
                </li>

                <li class="footer__menu_col_list_item">
                  <p>
                    <router-link 
                      class="footer__menu_col_list_item_link" 
                      to="rotor"
                      target="_blank"
                    >
                      глубокая чистка пола
                    </router-link>
                  </p>
                </li>
              </ul>
            </nav>
          </div>

        </div>

        <div class="col footer__menu_col">

          <div class="row">
            <h2 class="footer__menu_col_header">
              цены
            </h2>
          </div>

          <div class="row footer__menu_col_list_container">
            <nav>
              <ul>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="documents">документы</router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <q-btn 
                    class="footer__menu_col_list_btn"
                    target="_blank" 
                    to=""
                  >
                    заказать уборку
                  </q-btn>
                </li>

                <li class="footer__menu_col_list_item">
                  <p><router-link class="footer__menu_col_list_item_link" to="vacancies">вакансии</router-link></p>
                </li>

                <li class="footer__menu_col_list_item">
                  <img class="footer__app_btn" src="../../assets/google_play.png"/>
                </li>


                <li class="footer__menu_col_list_item">
                  <img class="footer__app_btn" src="../../assets/app_store.png"/>
                </li>

              </ul>
            </nav>
          </div>

        </div> 

        </div>

    </div>

    <div>
      <p class="footer__copyright_text_top">
        © 2024 C-Clean.
      </p>

      <q-separator color="accent"/>

      <p class="footer__copyright_text_bottom">
        Начиная использовать Сервис (его отдельные функциональности), вы принимаете Пользовательское соглашение и соглашаетесь c 
        <span class="footer__copyright_text_bottom_href">
          <router-link 
            to="portfolio" 
            target="_blank" 
            class="main_h2__text_orange"
          >
            Политикой конфиденциальности
          </router-link>
        </span>
         .
      </p>
    </div>


  </q-footer>
</template>

<script>
  export default ({

  })
</script>

<style lang="scss" scoped>
.footer__container {
  font-family: 'Comfortaa';
  padding: 2%;
  background-color: $dark;
}

.footer_menu_box {
  display: flex;
  justify-content: center;
}

.footer__menu {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.footer__menu_col{
  margin: 5%;
  padding-left: 30px;
  min-width: 200px;
}

.footer__menu_col_header {
  font-size: 1.5rem;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 1rem;
}

.footer__menu_col_list_item {
  list-style-type: none;
  font-size: 1rem;
}

.footer__menu_col_list_item :hover {
  font-weight: bold;
}

.footer__menu_col_list_item :active {
  color: $accent;
}

.footer__menu_col_list_btn {
  border-radius: 10px;
  border: 1px solid;
  padding: 5%;
  min-width: 200px;
  margin-bottom: 16px;
}

.footer__menu_col_list_item_link {
  text-decoration: none;
  color: white;
}

.footer__app_btn {
  width: 100px;
}

.footer__copyright_text_top {
  font-size: 0.7rem;
}

.footer__copyright_text_bottom {
  font-size: 0.6rem;
  text-align: center;
  text-justify: center;
}

@media screen and (max-width: 750px) {
  .footer__menu {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
  }

  .footer__menu_col {
    width: 300px;
  }
}


</style>