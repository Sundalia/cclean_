<template>
  <div class="order_h2_container">
    <h2 class="order_h2">СПИСОК МОИХ ЗАКАЗОВ</h2>
  </div>
  <div class="order_table__container">
    <q-table
      class="order_table"
      :rows="rows"
      :columns="columns"
      row-key="name"

      no-data-label="Здесть пока нет заказов, давайте это исправим в разделе Заказа"
    >
      <template v-slot:body-cell-feedback="props">
        <q-td :props="props">
          <q-btn id="btn" @click="onFeedback" :value="props.row.pk">{{ props.row }}</q-btn>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
import { api } from'src/boot/axios'
import {useAuthStore} from "stores/authStore";
import {ref} from "vue";

const store = useAuthStore()

  export default {
    name: 'OrdersTable',
    data(){
      return {
        columns: [
          {
            name: 'address',
            required: true,
            label: 'АДРЕС',
            align: 'left',
            field: row => row.address,
            format: val => `${val}`,
            sortable: true
          },
          {
            name: 'date',
            required: true,
            label: 'ДАТА',
            align: 'left',
            field: row => row.cleaning_date,
            format: val => `${val}`,
            sortable: true
          },
          {
            name: 'feedback',
            label: 'ОТЗЫВ'
          }
        ],
        rows: ref([])
      }
    },
    beforeCreate() {
      api.patch('/orders/get_users_orders/', {
        "customer" : `${store.me.id}`
      })
        .then(res => {
          console.log(res)
          this.rows = res.data.map(i => i.fields)
          console.log(this.rows)
        })
        .catch(err => console.log(err))
    },
    methods: {
      onFeedback() {
        alert("ОТЗЫВЫ В РАЗРАБОТКЕ")
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
