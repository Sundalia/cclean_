<template>
    <q-header class="routes_header">
        <q-tabs class="routes_header__tabs">
            <q-route-tab to="spring_cleaning" label="Генеральная" class="routes_header__tab"/>
            <q-route-tab to="maintenance_cleaning" label="Поддерживающая" class="routes_header__tab"/>
            <q-route-tab to="post_construction_cleaning" label="Послестроительная" class="routes_header__tab"/>
            <q-route-tab to="window_cleaning" label="Мойка окон" class="routes_header__tab"/>
            <q-route-tab to="office_cleaning" label="уборка офиса" class="routes_header__tab"/>
            <q-route-tab to="cottage_cleaning" label="Уборка загородного дома" class="routes_header__tab"/>
            <q-route-tab to="yacht" label="уборка яхты" class="routes_header__tab"/>
            <q-route-tab to="rotor" label="Глубокая чистка пола" class="routes_header__tab"/>
    </q-tabs>
    </q-header>
</template>

<script>

export default({
    name: 'RoutesHeaderItem'
})
</script>

<style lang="scss" scoped>
.routes_header {
    background-color: rgba(0, 0, 0, 0.7);
    margin-top: 50px;
}

</style>