<template>
  <div class="portfolio_menu__container">

    <q-splitter
      class="portfolio_menu__splitter"
      v-model="splitterModel"
      horizontal
      :limits="[1, 5]"

    >
      <template v-slot:before>

        <q-tabs
          class="portfolio_menu__menu"
          v-model="tab"
          indicator-color="accent"
          active-color="accent"
        >
          <q-tab class="portfolio_menu__tab" name="spring" label="Генеральная" />
          <q-tab class="portfolio_menu__tab" name="maintenance" label="Поддерживающая" />
          <q-tab class="portfolio_menu__tab" name="postconstruction" label="Послестроительная" />
          <q-tab class="portfolio_menu__tab" name="industrial" label="Производственная" />
          <q-tab class="portfolio_menu__tab" name="window" label="Мойка окон" />
          <q-tab class="portfolio_menu__tab" name="cottage" label="Загородный дом" />
          <q-tab class="portfolio_menu__tab" name="office" label="Офис" />
          <q-tab class="portfolio_menu__tab" name="yacht" label="Яхта" />
          <q-tab class="portfolio_menu__tab" name="rotor" label="Глубокая чиска пола" />
        </q-tabs>
      </template>

      <template v-slot:after>
        <q-tab-panels
          class="portfolio_menu__tabs"
          v-model="tab"
          animated
          swipeable
          vertical
          transition-prev="jump-up"
          transition-next="jump-up"
        >
          <q-tab-panel name="spring">
              <PortfolioCard
                header="Генеральная уборка"
                :slides="slides"
              />
          </q-tab-panel>

          <q-tab-panel name="maintenance">
              <PortfolioCard
                header="Поддерживающая уборка"
                :slides="slides"
              />
          </q-tab-panel>

          </q-tab-panels>
      </template>

    </q-splitter>
  </div>
</template>

<script>
import { ref } from 'vue'
import PortfolioCard from 'components/site_components/portfolio_page/subcomponents/PortfolioCard.vue'

  export default {
    name: 'PortfolioMenu',
    components: {
      PortfolioCard
    },
    setup () {
      return {
        tab: ref('spring'),
        splitterModel: ref(5)
      }
    },
    data() {
      return {
        slides: [],
        header: "Генеральная уборка"
      }
    },
    beforeCreate() {
      this.$api.get('/cleaning_type/1.json')
        .then(res => {
          this.slides = res.data.portfolio.map((i) => i)
          
        })
        .catch(err => console.log(err))
        
    }
  }
</script>

<style lang="scss" scoped>
.portfolio_menu__container {
  margin-top: 3rem;
}

.portfolio_menu__menu {
  font-family: 'Oswald';
  font-size: 1.6rem;
}

.portfolio_menu__tabs {
  background-color: $background;
}

</style>