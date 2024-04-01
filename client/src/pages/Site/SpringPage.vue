 <template>
    <q-layout>
        <q-page class="spring_page">
            <CleanTypeBanner :header="header"/>
            <BreadCrumbs :breadcrumb="breadcrumb"/>
            <MainForm/>
            <HeaderText 
                :header="headertext_header" 
                :text="headertext_text"
                :subtext="headertext_subtext"
            />
            <WhatIncludeSpring/>
            <ConnectLinks/>
            <AppBanner/>
            <FeedBack/>
        </q-page>
    </q-layout>
</template>

<script>
import CleanTypeBanner from 'components/site_components/CleanTypeBanner.vue'
import BreadCrumbs from 'components/site_components/BreadCrumbs.vue'
import MainForm from 'components/site_components/MainForm.vue'
import HeaderText from 'components/site_components/HeaderText.vue'
import WhatIncludeSpring from 'src/components/site_components/spring_page/WhatIncludeSpring.vue'
import ConnectLinks from 'src/components/site_components/ConnectLinks.vue'
import AppBanner from 'src/components/site_components/AppBanner.vue'
import FeedBack from 'src/components/site_components/FeedBack.vue'
import { api } from 'src/boot/axios'

export default({
    name: 'SpringPage',
    components: {
        CleanTypeBanner,
        BreadCrumbs,
        MainForm,
        HeaderText,
        WhatIncludeSpring,
        ConnectLinks,
        AppBanner,
        FeedBack
    },
    data() {
        return {
            header: 'генеральная уборка в санкт-петербурге от 5000 рублей',
            breadcrumb: 'Генеральная',
            headertext_header: 'что входит в генеральную уборку',
            headertext_text: '',
            headertext_subtext: ''
        }
    },
    mounted() {
        api.get("/cleaning_type/1.json")
        .then(res => {
            this.headertext_text = res.data.description
            this.headertext_subtext = res.data.subdescription
        })
        .catch(err => console.log(err))
    }
})
</script>

<style lang="scss" scope>
</style>