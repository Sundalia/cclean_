import { boot } from 'quasar/wrappers'
import axios from 'axios'
import { createYmaps } from 'vue-yandex-maps'

const api = axios.create({
  baseURL: process.env.API_DEV
})

const accounts = axios.create({
  baseURL: process.env.AUTH_DEV
})

const geocoder = axios.create({
  baseURL: process.env.GEOCODE
})

export default boot(({ app }) => {

  app.config.globalProperties.$api = api
  app.config.globalProperties.$accounts = accounts
  app.config.globalProperties.$geocoder = geocoder
  app.use(createYmaps({
    apikey: '6205f264-6946-4fbc-9905-1101b7c5dd01',
    })
  )
})



export { axios, api, accounts, geocoder }
