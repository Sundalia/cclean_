<template>
    <q-layout>
        <q-page-container class="order_layout">
            <router-view/>
            <TabMenuItem/>
        </q-page-container>
    </q-layout>
</template>

<script>
import TabMenuItem from 'src/components/account_components/TabMenuItem.vue'


export default({
    name: 'AccountLayout',
    components: {
        TabMenuItem
    }
})
</script>
