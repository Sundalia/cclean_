import { defineStore } from 'pinia'
import { accounts, api } from 'src/boot/axios'
import {Notify} from "quasar"
import { ref } from 'vue'


export const useAuthStore = defineStore('authStore', {
  state: () => ({
    me: ref({
      id: '',
      username: ref(''),
      last_name: ref(''),
      mobile: ref(''),
      email: ref(''),
      password: ref(''),
      is_cleaner: ref(''),
      is_customer: ref(''),
      is_active: ref(false),
      is_verified: ref(false),
      otp: ref('')
    }),
    refresh_token: ref(''),
    access_token: ref(''),
    isAuthenticated: ref(false),
  }),
  persist: true,
  getters: {
    getMe(state){
      return state.me
    },
    getToken(state) {
      return state.refresh_token, state.access_token
    },
    getIsAuth(state) {
      return state.isAuthenticated
    }
  },

  actions: {

    async registrationCustomer(phone, name, password) {
      let cutedPhone = phone.value.replace(/[^0-9]/gi, '')
      await accounts.post('/', {
          mobile: cutedPhone,
          username: name,
          password: password,
          is_cleaner: false,
          is_customer: true
      })
        .then((res) => {
          if (res.status === 201) {
            this.me.id = res.data.id
            this.me.username = res.data.username
            this.me.last_name = res.data.last_name
            this.me.mobile = res.data.mobile
            this.me.email = res.data.email
            this.me.password = res.data.password
            this.me.is_cleaner = res.data.is_cleaner
            this.me.is_customer = res.data.is_cleaner
            this.me.is_active = res.data.is_cleaner
            this.me.is_verified = res.data.is_verified
            this.me.otp = res.data.otp
            console.log(this.me)
            Notify.create({
              color: 'accent',
              textColor: 'white',
              position: 'center',
              message: `Введите код из смс`
            })
          } else {
            console.log(res)
            Notify.create({
              color: 'red-5',
              textColor: 'white',
              position: 'center',
              message: `${res.data}`
            })
          }
        })
        .then(
            this.router.push({path: '/login/sms'})
        )
        .catch((err) => {
          const response = err.response
          if (response && response.data) {
            Notify.create({
              color: 'red-5',
              textColor: 'white',
              position: 'center',
              message: `${JSON.stringify(response.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
            })
          }
        })
    },

    async login(phone, password) {
      let cutedPhone = phone.value.replace(/[^0-9]/gi, '')
      await accounts.post(`/login/`, {
        mobile: cutedPhone,
        password: password.value
      })
        .then(res =>{
          this.me.id = res.data.id
          this.me.username = res.data.username
          this.me.last_name = res.data.last_name
          this.me.mobile = res.data.mobile
          this.me.email = res.data.email
          this.me.password = res.data.password
          this.me.is_cleaner = res.data.is_cleaner
          this.me.is_customer = res.data.is_cleaner
          this.me.is_active = res.data.is_cleaner
          this.me.is_verified = res.data.is_verified
          this.me.otp = res.data.otp
          console.log(this.me)
          this.regenerate_otp(this.me.id)
          .then(
            this.router.push('/login/sms')
          )
        })
        .catch((err) => {
          const response = err.response
          if(response && response.data) {
            console.log(response.data)
            Notify.create({
              color: 'red-5',
              textColor: 'white',
              message: `${response.data.error}`,
              position: 'center'
            })
          }
        })
    },

    async verify_sms(otp){
        await accounts.patch(`/${this.me.id}/verify_otp/`, {
          "otp": `${otp}`,
          "is_verified": "true"
        })
      .then(res =>{
        console.log(res)
        if (res.status !== 400) {
          this.refresh_token = res.data.refresh_token
          this.access_token = res.data.access_token
          console.log(this.refresh_token, this.access_token)
          api.defaults.headers.common['Authorization'] = `${this.access_token}`
          this.isAuthenticated = true
          this.router.push({path: '/account/order'})
        } else {
          Notify.create({
            color: 'red-5',
            textColor: 'white',
            position: 'center',
            message: `${JSON.stringify(res.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
          })
        }
      })
      .catch((err) => {
        console.log(err)
        const response = err.response
        if (response && response.data) {
          Notify.create({
            color: 'red-5',
            textColor: 'white',
            position: 'center',
            message: `${JSON.stringify(response.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
          })
        }
      })
    },

    async regenerate_otp(id) {
      await accounts.patch(`/${id}/regenerate_otp/`, {})
        .then(res => {
          Notify.create({
            color: 'accent',
            textColor: 'white',
            message: `${JSON.stringify(res.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
            position: 'center'
          })
        })
        .catch((err) => {
          const response = err.response
          if(response && response.data) {
            Notify.create({
              color: 'red-5',
              textColor: 'white',
              message: `${JSON.stringify(response.data).replace(/[A-Za-z{":[}.\]]/gi, '')}`,
              position: 'center'
            })
          }
        })
    },
    async logout(id, refresh_token) {
      await accounts.patch(`/${id}/logout/`, {
        "refresh_token" : `${refresh_token}`
      })
        .then(res => {
          Notify.create({
            color: 'accent',
            textColor: 'white',
            message: `${res.data.success}`,
            position: 'center'
          })
        })
        .then(
          this.router.push('/login/authentication')
        )
        .catch((err) => {
          const response = err.response
          if(response && response.data) {
            Notify.create({
              color: 'red-5',
              textColor: 'white',
              message: `${JSON.stringify(response.data).replace(/[{":[}.\]]/gi, '')}`,
              position: 'center'
            })
          }
        })
    }
  }
})
