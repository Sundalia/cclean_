<template>
  <div class="order_h2_container">
    <h2 class="order_h2">СПИСОК МОИХ ЗАКАЗОВ</h2>
  </div> 
  <div class="order_table__container">
    <q-table
      class="order_table"
      :rows="rows"
      :columns="columns"
      no-data-label="Здесть пока нет заказов, давайте это исправим в разделе Заказа"
    ></q-table>
  </div>
</template>

<script>
  export default {
    name: 'OrdersTable',
    data() {
      return {
        rows: [],
        columns: []
      }
    }
  }
</script>

<style lang="scss" scoped>
.order_h2_container {
  display: flex;
  text-justify: center;
  width: 100%;
}

.order_h2 {
  font-family: 'Oswald';
  color: $accent;
  font-size: 2rem;
}
</style>