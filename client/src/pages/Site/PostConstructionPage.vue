<template>
    <q-layout>
        <q-page class="postconstruction_page">
            <CleanTypeBanner :header="header"/>
            <BreadCrumbs :breadcrumb="breadcrumb"/>
            <MainForm/>
            <HeaderText
                :header="headertext_header"
                :text="headertext_text"
                :subtext="headertext_subtext"
            />
            <WhatIncludePostconstruction/>
            <ConnectLinks/>
            <AppBanner/>
            <FeedBack/>

        </q-page>
    </q-layout>
</template>

<script>
import AppBanner from 'src/components/site_components/AppBanner.vue'
import BreadCrumbs from 'src/components/site_components/BreadCrumbs.vue'
import CleanTypeBanner from 'src/components/site_components/CleanTypeBanner.vue'
import ConnectLinks from 'src/components/site_components/ConnectLinks.vue'
import FeedBack from 'src/components/site_components/FeedBack.vue'
import HeaderText from 'src/components/site_components/HeaderText.vue'
import MainForm from 'src/components/site_components/MainForm.vue'
import WhatIncludePostconstruction from 'src/components/site_components/postconstruction_page/WhatIncludePostconstruction.vue'

export default({
    name: 'PostConstructionPage',
    components: {
        CleanTypeBanner,
        BreadCrumbs,
        MainForm,
        HeaderText,
        WhatIncludePostconstruction,
        ConnectLinks,
        AppBanner,
        FeedBack
    },
    data() {
        return {
            header: 'послестроительная уборка в санкт-петербурге от 5000 рублей',
            breadcrumb: 'Послестроительная',
            headertext_header: 'Что входит в послестроительную уборку',
            headertext_text: '',
            headertext_subtext: ''
        }
    },
    mounted() {
        this.$api.get("/cleaning_type/3.json")
        .then(res => {
            this.headertext_text = res.data.description
            this.headertext_subtext = res.data.subdescription
        })
        .catch(err => console.log(err))
    }
})
</script>