<template>
    <q-tabs
    class="account_tabs__desktop bg-grey"
    inline-label
    align="justify"
    indicator-color="white"
    active-class="bg-white text-accent"

  >

    <q-route-tab class="account_tabs__desktop_tab" icon="list" to="order_list">
      <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
      <label class="account_tabs__label">мои уборки</label>
    </q-route-tab>

    <q-route-tab class="account_tabs__desktop_tab" icon="task" to="order">
      <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
      <label class="account_tabs__label">заказать уборку</label>
    </q-route-tab>

    <q-route-tab class="account_tabs__desktop_tab" icon="whatshot" to="promo">
      <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
      <label class="account_tabs__label">мои купоны</label>
    </q-route-tab>

    <q-route-tab class="account_tabs__desktop_tab" icon="credit_card" to="pay">
      <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
      <label class="account_tabs__label">оплата</label>
    </q-route-tab>
  </q-tabs>
</template>

<script>
  export default {
    name: 'TabMenuDesktop'
  }
</script>

<style lang="scss" scoped>
.account_tabs__desktop_tab {
  border-radius: 0.5rem 0.5rem 0 0;
}

@media screen and (max-width: 820px) {
  .account_tabs__desktop {
    display: none;
  }
}
</style>