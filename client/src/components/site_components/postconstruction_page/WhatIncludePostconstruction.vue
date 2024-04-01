<template>
  <div class="what_include_container">
    <div class="row what_include_grid">
      <WhatIncludeCol
        img_src="kitchen.svg" 
        img_header="на кухне:"
        :what_include="what_inclide_postconstruction_kitchen" 
        :can_add = "can_add_postconstruction_kitchen"
      />
      <WhatIncludeCol
        img_src="room.svg" 
        img_header="в комнатах:"
        :what_include="what_inclide_postconstruction_room" 
        :can_add = "can_add_postconstruction_room"
      />
      <WhatIncludeCol
        img_src="bathroom.svg" 
        img_header="в санузлах:"
        :what_include="what_inclide_postconstruction_bathroom" 
        :can_add = "can_add_postconstruction_bathroom"
      />
      <WhatIncludeCol
        img_src="hallway.svg"
        img_header="в прихожей:"
        :what_include="what_inclide_postconstruction_hallway"
        :can_add="can_add_postconstruction_hallway"
      />
    </div>
  </div>
</template>

<script>
import WhatIncludeCol from 'components/site_components/subcomponents/WhatIncludeCol.vue'

  export default {
    name: 'WhatIncludePostconstruction',
    components: {
      WhatIncludeCol
    },
    data() {
      return {
        what_inclide_postconstruction_kitchen: [],
        what_inclide_postconstruction_room: [],
        what_inclide_postconstruction_bathroom: [],
        what_inclide_postconstruction_hallway: [],
        can_add_postconstruction_kitchen: [],
        can_add_postconstruction_room: [],
        can_add_postconstruction_bathroom: [],
        can_add_postconstruction_hallway: []
        
      }
    },
    mounted() {
      this.$api.get("/cleaning_type/3.json")
        .then(res => {
          console.log(res.data.location[3])
          this.what_inclide_postconstruction_kitchen = res.data.location[0].include.map((i) => i)
          this.what_inclide_postconstruction_room = res.data.location[1].include.map((i) => i)
          this.what_inclide_postconstruction_bathroom = res.data.location[2].include.map((i) => i)
          this.what_inclide_postconstruction_hallway = res.data.location[3].include.map((i) => i)
          this.can_add_postconstruction_kitchen = res.data.location[0].can_add.map((i) => i)
          this.can_add_postconstruction_room = res.data.location[1].can_add.map((i) => i)
          this.can_add_postconstruction_bathroom = res.data.location[2].can_add.map((i) => i)
          this.can_add_postconstruction_hallway = res.data.location[3].can_add.map((i) => i)
        })
        .catch(err => console.log(err))  
    },
  }

</script>

<style lang="scss" scoped>

</style>