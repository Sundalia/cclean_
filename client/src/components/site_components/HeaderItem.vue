<template>
    <q-header class="row main_header">
        <q-page-sticky expand position="top">
            <q-toolbar>

                <q-btn flat round dense icon="menu" class="q-mr-lg main_header__burger">
                    <q-menu class="main_header__burger_menu">

                        <q-expansion-item
                            label="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Услуги"
                            expand-separatior
                            :header-style="{textAlign: 'center'}"
                            class="main_header__burger_menu_expansion"
                        >
                            <q-tabs vertical class="main_header__burger_menu_tabs">
                                <q-route-tab to="spring_cleaning" label="Генеральная" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="maintenance_cleaning" label="Поддерживающая" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="post_construction_cleaning" label="Послестроительная" class="main_header__burger_menu_tab"/>
                                <q-separator/>
                                <q-route-tab to="industrial_cleaning" label="Производство" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="office_cleaning" label="Офис" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="cottage_cleaning" label="Загородный дом" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="yacht" label="Яхта" class="main_header__burger_menu_tab"/>
                                <q-separator/>
                                <q-route-tab to="rotor" label="Глубокая чистка пола" class="main_header__burger_menu_tab"/>
                                <q-route-tab to="window_cleaning" label="Мойка окон" class="main_header__burger_menu_tab"/>
                            </q-tabs>
                        </q-expansion-item>

                        <q-tabs vertical class="main_header__burger_menu_tabs">
                            <q-separator/>
                            <q-route-tab to="portfolio" label="Портфолио" class="main_header__burger_menu_tab"/>
                            <q-route-tab to="contact_us" label="Контакты" class="main_header__burger_menu_tab"/>
                            <q-route-tab to="vacancies" label="Вакансии" class="main_header__burger_menu_tab"/>
                            <q-route-tab to="documents" label="Оферта" class="main_header__burger_menu_tab"/>
                            <q-separator/>
                            <q-route-tab to="account/order" label="Личный кабинет" class="main_header__burger_menu_tab"/>
                            <q-separator/>
                            <q-btn-group flat class="main_header__social_links_group_burger">

                                <q-btn 
                                    class="main_header__social_links_burger"
                                    type="a" 
                                    size="md"
                                    href="tel:+79812007083" 
                                    target="_blank"
                                    rounded
                                >
                                    <q-avatar>
                                        <img src="../../assets/icons/call_us.svg" style="width: 20px;"/>
                                    </q-avatar>
                                    <q-tooltip>
                                        Позвонить нам
                                    </q-tooltip>
                                </q-btn>

                                <q-btn 
                                    class="main_header__social_links_burger"
                                    type="a"
                                    size="md"
                                    href="https://t.me/ccleansp" 
                                    target="_blank"
                                    rounded
                                >
                                    <q-avatar class="">
                                        <img src="../../assets/icons/telegram.svg" style="width: 20px;"/>
                                    </q-avatar>
                                    <q-tooltip>
                                        Написать в Telegram
                                    </q-tooltip>
                                </q-btn>

                                <q-btn 
                                    class="main_header__social_links_burger"
                                    type="a" 
                                    size="md"
                                    href="https://wa.me/qr/Y4Z6OVFJ5KTPD1" 
                                    target="_blank"
                                    rounded
                                >
                                    <q-avatar class="">
                                        <img src="../../assets/icons/whatsapp.svg" style="width: 20px;"/>
                                    </q-avatar>
                                    <q-tooltip>
                                        Написать в Whatsapp
                                    </q-tooltip>
                                </q-btn>

                            </q-btn-group>
                            
                        </q-tabs>
                    </q-menu>
                </q-btn>

                <q-toolbar-title class="row main_header__logo">
                    <q-avatar square size="30px" >
                        <img class="main_header__logo_img" src="../../assets/icons/cclean_logo.svg"/> 
                    </q-avatar>
                    <router-link class="main_header__logo_name" to="/">
                        C-CLEAN
                    </router-link>
                </q-toolbar-title>

                <q-space/>

                <q-btn-group flat rounded class="main_header__social_links_group">

                    <q-btn 
                        class="main_header__social_links"
                        type="a" 
                        size="md"
                        href="tel:+79812007083" 
                        target="_blank"
                        rounded
                    >
                        <q-avatar>
                            <img src="../../assets/icons/call_us.svg" style="width: 20px;"/>
                        </q-avatar>
                        <q-tooltip>
                            Позвонить нам
                        </q-tooltip>
                    </q-btn>

                    <q-btn 
                        class="main_header__social_links"
                        type="a"
                        size="md"
                        href="https://t.me/ccleansp" 
                        target="_blank"
                        rounded
                    >
                        <q-avatar class="">
                            <img src="../../assets/icons/telegram.svg" style="width: 20px;"/>
                        </q-avatar>
                        <q-tooltip>
                            Написать в Telegram
                        </q-tooltip>
                    </q-btn>

                    <q-btn 
                        class="main_header__social_links"
                        type="a" 
                        size="md"
                        href="https://wa.me/qr/Y4Z6OVFJ5KTPD1" 
                        target="_blank"
                        rounded
                    >
                        <q-avatar class="">
                            <img src="../../assets/icons/whatsapp.svg" style="width: 20px;"/>
                        </q-avatar>
                        <q-tooltip>
                            Написать в Whatsapp
                        </q-tooltip>
                    </q-btn>

                </q-btn-group>
                
                <q-btn 
                    size="sm"
                    flat 
                    rounded 
                    type="a" 
                    to="login/authentication" 
                >
                    <q-avatar square>
                        <img src="../../assets/icons/login.svg" style="width: 20px;"/>
                    </q-avatar>
                    <q-tooltip>
                        Личный кабинет
                    </q-tooltip>
                </q-btn>

            </q-toolbar>

        </q-page-sticky>
    </q-header>
</template>

<script>



export default({
    name: 'HeaderItem',
    components: {

    }
})
</script>

<style lang="scss" scoped>

.main_header {
    color: $accent;
    background: transparent;
    font-family: 'Comfortaa';
    max-width: 1920px !important;
    margin: auto;
}

.main_header__burger {
    max-width: 50px;
    margin-left: 2%;
}

.main_header__burger_menu {
    max-width: 300px;
    font-family: 'Comfortaa';
}

.main_header__burger_menu_expansion{
    text-transform: uppercase;
    font-family: 'Oswald';
    font-weight: bold;
    text-justify: center;
    color: $dark;
}

.main_header__burger_menu_tabs {
    min-width: 250px;
    font-family: 'Oswald';
}

.main_header__social_links_burger {
    display: none;
}

.main_header__logo {
    width: 200px;
    min-width: 150px;
    padding: 0;
    font-weight: bold;
    line-height: 2rem;
}

.main_header__logo_name {
    text-decoration: none;
    color: $accent;
}

.main_header__social_links_group {
    margin-right: 5%;
}


@media screen and (max-width: 820px) {
.main_header__social_links {
    display: none;
}

.main_header__social_links_burger {
    display: flex;
}
}


</style>