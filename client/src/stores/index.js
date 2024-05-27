import { store } from 'quasar/wrappers'
import { createPinia } from 'pinia'
import { useAuthStore } from './authStore'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'


export default store((/* { ssrContext } */) => {
  const pinia = createPinia({
    modules: {
      useAuthStore
    }
  })

  // You can add Pinia plugins here
  // pinia.use(SomePiniaPlugin)
  pinia.use(piniaPluginPersistedstate)

  return pinia
})
