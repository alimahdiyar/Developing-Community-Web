import Vue from 'vue'
import VueRouter from 'vue-router';
import axios from 'axios'
import VueAxios from 'vue-axios'
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
import App from './App.vue'
import { routes } from './routes';
import { rejects } from 'assert';


Vue.use(Vuex);
// Vue.use(VueResource);
Vue.use(VueAxios, axios);
Vue.use(VueRouter);

var arr = window.location.href.split("/");
var host = arr[0] + "//" + arr[2]


export const store = new Vuex.Store({
  state: {
    hostUrl: window.location.href.split("/")[0] + "//" + window.location.href.split("/")[2],
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: host + '/api/user/auth/obtain_token/',
      refreshJWT: host + '/api/user/auth/refresh_token/',
      verifyJWT: host + '/api/user/auth/verify_token/'
    },
    err: null
  },
  mutations: {
    updateToken(state, newToken) {
      localStorage.setItem('t', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      localStorage.removeItem('t');
      state.jwt = null;
    }
  },
  actions: {
    obtainToken({ commit, state }, payload) {
      axios.post(this.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.commit('updateToken', response.data.token);
          this.state.err = null;
          return Promise.resolve();
        })
        .catch((error) => {
          this.state.err = error;
          console.log("error in obtaining token");
          console.log(error);
          this.commit('removeToken');
        })
    },
    refreshToken() {
      const payload = {
        token: this.state.jwt
      }
      axios.post(this.state.endpoints.refreshJWT, payload)
        .then((response) => {
          this.commit('updateToken', response.data.token)
        })
        .catch((error) => {
          throw(error);
        })
    },
    inspectToken(){
      const token = this.state.jwt;
      if(token){
        const decoded = jwt_decode(token);
        const exp = decoded.exp
        const orig_iat = decode.orig_iat
        if(exp - (Date.now()/1000) < 1800 && (Date.now()/1000) - orig_iat < 628200){
          this.dispatch('refreshToken')
        } else if (exp -(Date.now()/1000) < 1800){
          // DO NOTHING, DO NOT REFRESH          
        } else {
          // PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
        }
      }
    }
  }
})

const router = new VueRouter({
  routes,
  mode: 'history'
});

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
