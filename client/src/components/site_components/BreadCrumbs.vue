<template>
  <div class="bradcrumbs">
    <q-breadcrumbs class="text-black" active-color="accent">
      <template v-slot:separator>
        <q-icon
          size="1rem"
          name="arrow_forward"
          color="accent"
        />
      </template>

      <q-breadcrumbs-el label="Главная" to="/"/>
      <q-breadcrumbs-el>{{ breadcrumb }}</q-breadcrumbs-el>
    </q-breadcrumbs>
  </div>
</template>

<script>
  export default {
    name: 'BreadCrumbs',
    props: {
      breadcrumb: {
        type: String,
        required: true
      }
    }
  }
</script>

<style lang="scss" scoped>
.bradcrumbs {
  margin: 2%;
  padding-left: 2%;
}
</style>