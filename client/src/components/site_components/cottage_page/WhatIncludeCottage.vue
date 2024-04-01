<template>
  <div class="what_include__container">
    <div class="row what_include__grid">
      <WhatIncludeCol/>
    </div>
  </div>
</template>

<script>
import WhatIncludeCol from 'components/subcomponents/WhatIncludeCol.vue'

  export default {
    name: 'WhatIncludeCottage',
    components: {
      WhatIncludeCol
    }
  }
</script>

<style lang="scss" scoped>

</style>