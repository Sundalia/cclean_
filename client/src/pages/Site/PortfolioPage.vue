<template>
    <q-layout>
        <q-page class="portfolio_page">
            <PortfolioMenu/>
        </q-page>
    </q-layout>
</template>

<script>
import PortfolioMenu from 'components/site_components/portfolio_page/PortfolioMenu.vue'

export default({
    name: 'PortfolioPage',
    components: {
        PortfolioMenu
    }
})
</script>
<style lang="scss" scope>
.portfolio_page {
    background-color: $background;
}
</style>