<template>
    <q-layout>
        <q-page>
            <OrderForm/>
        </q-page>
    </q-layout>
</template>

<script>
// import ToolbarItem from 'src/components/ToolbarItem.vue'
import OrderForm from 'src/components/account_components/OrderForm.vue'

export default({
    name: 'OrderPage',
    components: {
        OrderForm
    }
})
</script>