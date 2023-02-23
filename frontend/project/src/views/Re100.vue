<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="text-align: center;">
      <img src="../assets/re100/re100.png" alt="">
    </div>
    <div style="height: 328px; overflow: auto; background='red';">
      <table style="text-align: center; width: 100%">
        <thead>
          <tr>
            <th>No.</th>
            <th>기업명</th>
            <th>목표연도</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in list" :key="item.no" @click="clicked(item.name)">
            <td>{{ item.no }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.when }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';
import axios from 'axios'
export default {
  data() {
    return {
      list: [],
    }
  },
  components: {
    ShinhanNavigationBar,
  },
  methods: {
    clicked(stockName) {
      this.$store.commit('setStockName', stockName);
      console.log('re100리스트페이지에서 stockName이 잘 저장됐음? ' + this.$store.getters.getStockName);
      this.$router.push('/stock/order');
    }
  },
  created() {
    // backend에서 크롤링한 re100 기업 리스트 받아오기
    const that = this;
    axios.get('http://34.64.235.73/api/news/inner_text/')
      .then(response => {
        console.log('re100 list response.data')
        console.log(response.data)
        const resultList = response.data;
        resultList.forEach(company => {
          that.list.push({
            no: company[0],
            name: company[2],
            when: company[6].slice(0, 4),
          });
        });
      })
  },
}
</script>

<style scoped>
table thead th {
  height: 45px;
  font-size: 1rem;
}

th, td {
  width: 33.333%;
}
tbody td {
  height: 40px;
  font-size: 1rem;
}

tbody > tr:hover {
  cursor: pointer;
}
</style>