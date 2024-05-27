import { boot } from 'quasar/wrappers'
import {useAuthStore} from "stores/authStore";

export default boot(async ({urlPath, redirect}) => {
  const store = useAuthStore()
  const isAuthenticated = store.isAuthenticated

  if (!isAuthenticated && urlPath.startsWith('/account')) {
    redirect({path: '/login/authentication'})
    return
  }

})
