<template>
    <q-layout>
        <q-page-container class="order_layout">
            <AccountHeader/>
            <TabMenuDesktop/>
            <router-view/>
            <TabMenuMobile/>
        </q-page-container>
    </q-layout>
</template>

<script>
import TabMenuDesktop from 'src/components/account_components/TabMenuDesktop.vue';
import TabMenuMobile from 'src/components/account_components/TabMenuMobile.vue'
import AccountHeader from 'src/components/account_components/AccountHeader.vue'


export default({
    name: 'AccountLayout',
    components: {
        TabMenuMobile,
        AccountHeader,
        TabMenuDesktop
    }
})
</script>
