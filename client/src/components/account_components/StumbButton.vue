<template>
  <div class="stumb_button__container">
    <q-btn
      class="stumb_button"
      to="account/order"
      label="РАССЧИТАТЬ СТОИМОСТЬ УБОРКИ"
    />
  </div>
</template>

<script>
  export default {
    name: 'StumbButton'
  }
</script>

<style lang="scss" scoped>
.stumb_button__container {
  display: flex;
  height: 70vh;
  justify-content: center;
  align-items: center;
}

.stumb_button {
  background: $accent;
  font-family: 'Comfortaa';
  font-size: 1rem;
  color: white;
}
</style>