<template>
  <div>
    <OrdersTable/>
  </div>
</template>

<script>
import OrdersTable from 'src/components/account_components/OrdersTable.vue'

  export default {
    name: 'MyOrdersPage',
    components: {
      OrdersTable
    }
  }
</script>

<style lang="scss" scoped>

</style>