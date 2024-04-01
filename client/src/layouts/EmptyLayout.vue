<template>
  <q-layout>
    <q-page-container class="empty_layout">
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>

  export default {
    name: 'EmptyLayout',
    components: {
      
    }
  }
</script>

<style lang="scss" scoped>
.empty_layout{
  background-color: $background;
}

</style>