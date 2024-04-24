<template>
    <q-layout>
        <q-page-container class="order_layout">
            <AccountHeader/>
            <router-view/>
            <StumbButton/>
            <TabMenuItem/>
        </q-page-container>
    </q-layout>
</template>

<script>
import TabMenuItem from 'src/components/account_components/TabMenuItem.vue'
import AccountHeader from 'src/components/account_components/AccountHeader.vue'
import StumbButton from 'src/components/account_components/StumbButton.vue'


export default({
    name: 'AccountLayout',
    components: {
        TabMenuItem,
        AccountHeader,
        StumbButton
    }
})
</script>
