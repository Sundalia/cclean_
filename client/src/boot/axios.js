import { boot } from 'quasar/wrappers'
import axios from 'axios'
// import { Cookies } from 'quasar'

// const csrfToken = Cookies.get('XSRF-TOKEN')

const api = axios.create({ 
  baseURL: process.env.API
})

const accounts = axios.create({
  baseURL: process.env.AUTH
})

export default boot(({ app }) => {

  app.config.globalProperties.$api = api
  app.config.globalProperties.$accounts = accounts
})


export { axios, api, accounts }
