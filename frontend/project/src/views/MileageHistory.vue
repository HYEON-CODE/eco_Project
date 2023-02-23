<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div style="margin-top: 30px; margin-left: 35px; position: relative">
      <span class="name">{{ username }}</span>
      <img src="../assets/mileage/currentmileage.png" alt="" />
      <span class="total">{{ usermileage }}</span>
    </div>

    <div style="margin-top: 25px; height: 385px; overflow: auto; border-radius: 20px">
      <table style="text-align: center; margin: 0 auto; width: 100%">
        <thead>
          <tr>
            <th>유형</th>
            <th>+/-</th>
            <th>일자</th>
          </tr>
        </thead>
        <tbody>          
          <tr v-for="history in historyList" :key="history.id">
            <td>{{ history.activity }}</td>
            <td>{{ history.mileage > 0 ? '+' + history.mileage : history.mileage }}</td>
            <td>{{ history.date.substr(0, 10) }}</td>
          </tr>          
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import GreenBar from '@/components/GreenBar.vue';
import ShinhanNavigationBar from '@/components/ShinhanNavigationBar.vue';
export default {
  components: {
    GreenBar,
    ShinhanNavigationBar,
  },  
  data() {
    return {
      username: '',
      usermileage: '',
      historyList: null,
    };
  },
  methods: {
    getHistory() {
      const accessToken = this.$cookies.get('accessToken');
      const that = this;
      axios.get('http://127.0.0.1:8000/api/mileage/', {
        headers: {
          Authorization: 'JWT ' + accessToken,
        }
      }).then(response => {
        console.log("MileageHistory에서 response.data(한 유저의 마일리지 전체 히스토리 조회)");
        console.log(response);
        const reversed = response.data.reverse();
        that.historyList = reversed;
      });
    },
  },
  created() {
    console.log('MileageHistory created...');
    const userPk = this.$cookies.get('userPk');
    console.log('MileageHistory userPk check: ' + userPk);
    const that = this;
    axios.get('http://127.0.0.1:8000/api/member/' + userPk + '/')
      .then(response => {
        console.log('MileageHistory 에서 username과 total마일리지를 조회');
        console.log(response);
        that.usermileage = response.data.mileage;
        that.username = response.data.username;
      });
    this.getHistory();
  },
};
</script>

<style scoped>
.name {
  top: 15px;
  left: 6px;
  position: absolute;
  font-weight: bolder;
  font-size: 1.8rem;
}

.total {
  position: absolute;
  top: 75px;
  right: 100px;
  font-size: 2.5rem;
  font-weight: bolder;
}

table thead tr th {
  font-size: 1rem;
  height: 50px;
}

table tbody tr td {
  font-size: 1rem;
  height: 30px;
}</style>