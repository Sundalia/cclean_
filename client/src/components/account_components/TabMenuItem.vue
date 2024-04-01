<template>
  <q-page-sticky
    class="account_tabs__container"
    position="bottom"
  >
    <q-tabs
        class="account_tabs text-grey shadow-2"
        inline-label
        switch-indicator
        indicator-color="white"
        active-color="white"
      >

      <q-route-tab class="account_tabs__tab" icon="list" to="order_list">
        <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
        <label class="account_tabs__label">мои уборки</label>
      </q-route-tab>

      <q-route-tab class="account_tab__tab" icon="task" to="order">
        <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
        <label class="account_tabs__label">заказать уборку</label>
      </q-route-tab>

      <q-route-tab class="account_tab__tab" icon="whatshot" to="promo">
        <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
        <label class="account_tabs__label">мои купоны</label>
      </q-route-tab>

      <q-route-tab class="account_tab__tab" icon="credit_card" to="pay">
        <q-badge class="account_tabs__badge" color="red" floating>1</q-badge>
        <label class="account_tabs__label">оплата</label>
      </q-route-tab>
      

    </q-tabs>
  </q-page-sticky>
</template>

<script>
  export default {
    name: 'TabMenuItem'
  }
</script>

<style lang="scss" scoped>
.account_tabs {
  font-family: 'Oswald';
  background-color: $accent;
  color: white;

}

.account_tabs__label {
  padding-left: 5%;
}

@media screen and (max-width: 820px) {
  .account_tabs__label {
    display: none;
  }
}

</style>