<template>
  <div>

    <shinhan-navigation-bar></shinhan-navigation-bar>
    <loading-spinner v-if="loading"></loading-spinner>
    <div v-else>
      <div class="top">
        <p style="margin-left: 25px; font-weight: bolder; font-size: 1.5rem;">뉴스</p>
        <br>
        <div class="line" style="width: 100%; height: 0.5px; background-color: lightgray"></div>
      </div>

      <div class="first">
        <a :href="firstNews[0]" target="_blank">
        <div class="first-image" style="width: 430px; height: 250px; background-color: white; border-radius: 20px">
          <img :src="firstNews[1]" width=430 height=250 style="border-radius: 20px"> 
        </div>
        <div style="margin-left: 25px;">
          <div>
            <p class="first-text" style="font-size: 1.4rem">
              {{ firstNews[2].substr(0, 25) + '...' }}
            </p>
          </div>
          <div>
            <p class="first-content" style="font-size: 0.8rem">
              {{ firstNews[3].substr(0, 87) + '...' }}
            </p>
          </div>
        </div>
        </a>
      </div>

      <div class="line" style="width: 100%; height: 0.5px; background-color: lightgray"></div>

      <div style="overflow: auto; height: 250px;">

        <a :href="item[0]" v-for="(item, index) in newsList" :key="item[0]" target="_blank">
          <div style="position: relative; margin-top: 10px; margin-right: 15px;">
            <div style="width: 150px; height: 100px; margin-left: 25px; background-color: white; border-radius: 20px; display: inline-block">
              <img :src="item[1]" width="150" height="100">
            </div>
            <div style="position: absolute; top: -6px; left: 182px">
              <p style="font-size: 1.3rem">{{ item[2].substr(0, 28) + '...' }}</p>
              <p style="font-size: 0.8rem">{{ item[3].substr(0, 40) + '...' }}</p>
            </div>
            <div class="line" style="width: 100%; height: 0.5px; background-color: lightgray; margin-top: 5px"></div>
          </div>
        </a>  
        
    </div>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'
import LoadingSpinner from '../components/LoadingSpinner.vue'
import axios from 'axios'

export default {
  components: {
    ShinhanNavigationBar,
    LoadingSpinner,
  },
  data() {
    return {
      loading: true,
      firstNews: null,
      newsList: null,
      forloop: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    }
  },
  methods: {

  },
  created() {
    const that = this;
    axios.get('http://127.0.0.1:8000/api/news/')
      .then(response => {
        console.log('뉴스 리스트 받아온 거');
        console.log(response.data);
        that.firstNews = response.data[0];
        that.newsList = response.data.slice(1);
        that.loading = false;
      });
  },
}
</script>

<style scoped>
.first {
  margin-top: 20px;
}
.first-image {
  margin: 0 auto;
}
</style>