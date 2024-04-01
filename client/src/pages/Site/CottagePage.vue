<template>
    <q-layout>
        <q-page class="cottage_page">
            <CleanTypeBanner :header="header"/>
            <BreadCrumbs :breadcrumb="breadcrumb"/>
            <MainForm/>
            <HeaderText :header="headertext_header" :text="headertext_text"/>
        </q-page>
    </q-layout>
</template>

<script>
import CleanTypeBanner from 'components/site_components/CleanTypeBanner.vue'
import BreadCrumbs from 'components/site_components/BreadCrumbs.vue'
import MainForm from 'components/site_components/MainForm.vue'
import HeaderText from 'components/site_components/HeaderText.vue'
// import WhatIncludeSpring from 'src/components/site_components/spring_page/WhatIncludeSpring.vue'
// import ConnectLinks from 'src/components/site_components/ConnectLinks.vue'
// import AppBanner from 'src/components/site_components/AppBanner.vue'
// import FeedBack from 'src/components/site_components/FeedBack.vue'


export default({
    name: 'CottagePage',
    components: {
        CleanTypeBanner,
        BreadCrumbs,
        MainForm,
        HeaderText,
        // WhatIncludeSpring,
        // ConnectLinks,
        // AppBanner,
        // FeedBack
    },
    data() {
        return {
            header: 'уборка загородного дома от 5000 рублей',
            breadcrumb: 'Загородный дом',
            headertext_header: 'Что входит в уборку загородного дома',
            headertext_text: 'ЗАПОЛНИТЬ'
        }
    }
})
</script>