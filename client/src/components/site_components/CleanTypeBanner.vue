<template>
  <q-banner class="cleantype_banner">
    <RoutesHeaderItem/>
    <h1 
      class="cleantype_banner__header" 
    >{{ header }}</h1>
  </q-banner>
</template>

<script>
import RoutesHeaderItem from 'components/site_components/RoutesHeaderItem.vue'

export default {
  name: 'CleanTypeBanner',
  components: {
    RoutesHeaderItem
  },
  props: {
    header: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
.cleantype_banner {
  margin: 0;
  padding: 0;
  height: 200px;
  background-image: url("../../assets/backgrounds/cleantype_background.svg");
  background-repeat: no-repeat;
  background-position: center;
  font-family: 'Oswald';
  position:relative;
}

.cleantype_banner__header {
  margin: 5rem 10px 10px 10px;
  text-align: center;
  font-size: 2rem;
  line-height: 2.2rem;
  font-weight: bold;
  color: $accent;
  text-transform: uppercase;
}

@media screen and (max-width: 520px) {
  .cleantype_banner__header {
    font-size: 1rem;
    line-height: 1.1rem;
  }
}
</style>