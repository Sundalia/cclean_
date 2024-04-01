<template>
    <q-layout>
        <q-page class="maintenance_page">
            <CleanTypeBanner :header="header"/>
            <BreadCrumbs :breadcrumb="breadcrumb"/>
            <MainForm/>
            <HeaderText 
                :header="headertext_header"
                :text="headertext_text"
                :subtext="headertext_subtext"
            />
            <WhatIncludeMaintenance/>
            <ConnectLinks/>
            <AppBanner/>
            <FeedBack/>
        </q-page>
    </q-layout>
</template>

<script>
import { api } from 'src/boot/axios'
import AppBanner from 'src/components/site_components/AppBanner.vue'
import BreadCrumbs from 'src/components/site_components/BreadCrumbs.vue'
import CleanTypeBanner from 'src/components/site_components/CleanTypeBanner.vue'
import FeedBack from 'src/components/site_components/FeedBack.vue'
import HeaderText from 'src/components/site_components/HeaderText.vue'
import MainForm from 'src/components/site_components/MainForm.vue'
import WhatIncludeMaintenance from 'src/components/site_components/maintenance_page/WhatIncludeMaintenance.vue'
import ConnectLinks from 'src/components/site_components/ConnectLinks.vue'



export default({
    name: 'MaintenancePage',
    components: {
        CleanTypeBanner,
        BreadCrumbs,
        MainForm,
        HeaderText,
        WhatIncludeMaintenance,
        ConnectLinks,
        AppBanner,
        FeedBack
    },
    data() {
        return {
            header: 'поддерживающая уборка в санкт-петербурге от 2500 рублей',
            breadcrumb: 'Поддерживающая',
            headertext_header: 'Что входит в поддерживающую уборку',
            headertext_text: '',
            headertext_subtext: ''
        }
    },
    mounted() {
        api.get("/cleaning_type/2.json")
        .then(res => {
            this.headertext_text = res.data.description
            this.headertext_subtext = res.data.subdescription
        })
        .catch(err => console.log(err))
    }
})
</script>
<style lang="scss" scoped>
</style>