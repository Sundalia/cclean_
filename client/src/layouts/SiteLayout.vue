<template>
  <q-layout>
    <q-page-container class="site_layout">
      <header-item/>
      <router-view/>
      <footer-item/>
    </q-page-container>
  </q-layout>
</template>

<script>
import HeaderItem from 'src/components/site_components/HeaderItem.vue'
import FooterItem from 'src/components/site_components/FooterItem.vue'

export default({
  name: 'SiteLayout',
  components: {
    HeaderItem,
    FooterItem,
}
})
</script>

<style lang="scss" scope>

.site_layout {
  background-color: $background;
  max-width: 1920px;
  margin: 0 auto;
}

.main_h2__header_box {
  display: flex;
  justify-content: center;
  width: 100%;
}
  
.main_h2 {
  font-family: 'Oswald';
  font-size: 1.5rem;
  line-height: 1.6rem;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  margin: 2%;
}

.main_h2__text_box {
  display: flex;
  text-align: center;
  justify-content: center;
  margin: 2%;

}

.main_h2__text {
  font-family: 'Comfortaa';
  text-align: center;
  font-size: 1rem;
  padding: 0;
}

.main_h2__text_orange {
  color: $accent;
}

.main__button {
  background-color: $accent;
  color: white;
  font-family: 'Comfortaa';
  font-weight: bold;
  width: 70%;
}

.what_include_container{
  display: flex;
  justify-content: center;
  margin: 2%;
}

.what_include_grid{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  width: 100%;
}

@media screen and (max-width: 820px){
  .what_include_grid{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

@media screen and (max-width: 520px){
  .what_include_grid{
    display: grid;
    grid-template-columns: repeat(1, 1fr);
  }
}
</style>