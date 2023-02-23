<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>  
    <div class="top">
      <p style="margin-left: 25px; font-weight: bolder; font-size: 1.5rem;">친환경 마일리지</p>
      <br>
      <div class="line"></div>
    </div>

    <div style="width: 100%; height: 310px;">
    <div style="position: relative;">
      <div class="green" style="position: absolute;"></div>
      <div class="white" style="position: absolute;">
        <div style="margin-left: 45px; margin-top: 20px">
          <span class="name">{{ username }}</span>&nbsp;<span class="nim">님</span>
        </div>
        <div style="margin-left: 45px;">
          <span class="total">{{ usermileage }}</span>&nbsp;<span style="font-size: 2.5rem; font-weight: bolder; color: #25BF8B;">M</span>
        </div>
        <p style="margin-left: 45px; font-size: 1.2rem; font-weight: bold; color: #9B9B9B">만큼 환경에 기여했어요!</p>
        <router-link to="/mileage/history">
        <div class="history">
          <span>내역</span>
        </div>
        </router-link>
      </div>
    </div>
    </div>

    <div style="width: 410px; margin: 0 auto;">
      <router-link to="/walk">
        <div class="button">
          <span>친환경 걷기</span>
        </div>
      </router-link>
      <router-link to="/mileage/dailymission">
        <div class="button right"> 
          <span>데일리 미션</span>
        </div>
      </router-link>
    </div>
    <br>
    <div class="use" @click="toggleModal">
      <span>마일리지 사용하기</span>
    </div>
    <br>
    <div style="width: 100%; background-color: #E3EFEB; height: 82px; overflow:auto; color: #A4A4A4">
      <p style="margin-left: 38px;">
        마일리지는 실제 돈 단위와 동일합니다.<br>
        친환경 주식을 매수하면 0.2%의 마일리지가 적립됩니다.<br>
        바코드와 QR 코드로 마일리지를 사용해 친환경 제품을 구매해 보세요.<br>
        마일리지로 금융상품권을 구매해 보세요.
      </p>
    </div>

    <div class="modal" v-show="showModal">
      <div>
        <p style="color: #25BF8B; font-size: 1.5rem; font-weight: bolder; margin-left: 20px; display: inline-block;">마일리지 사용하기</p>
        <p class="modal-close" style="float: right; display: inline-block; font-size: 1.5rem; margin-right: 20px;" @click="toggleModal">X</p>
      </div>
      <div style="width: 100%; height: 0.5px; background-color: lightgray"></div>
      <br>
      <div class="modal-content" style="margin-left: 20px; background-color: #F6F6F6; width: 91%; height: 160px">
        <p style="font-size: 1.8rem; font-weight: bolder;">금융투자상품권<br>구매하러 가기</p>
        <span style="color: #838383">친환경 습관으로 모은 마일리지로 주식을 구매해 보세요!</span>
        <div style="width: 100%">
          <router-link to="/mileage/giftcard"><div style="float: right; margin-right: 20px; margin-top: 15px; background-color: #383EF3; color: #fff; width:80px; text-align: center; height: 25px; border-radius: 5px">바로가기</div></router-link>
        </div>
      </div>
      <br>
      <div class="modal-content" style="margin-left: 20px; background-color: #F6F6F6; width: 91%; height: 185px">
        <p style="font-size: 1.8rem; font-weight: bolder;">친환경 상품<br>구매하러 가기</p>
        <span style="color: #838383">친환경 습관으로 모은 마일리지로 친환경 상품을 구매해 보세요!</span>
        <div style="width: 100%">
          <router-link to="/mileage/barcode"><div style="float: right; margin-right: 20px; margin-top: 15px; background-color: #383EF3; color: #fff; width:80px; text-align: center; height: 25px; border-radius: 5px">바로가기</div></router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      showModal: false,
      username: '',
      usermileage: 0,
    }
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
  },
  created() {
    console.log("HomeMileage created...");
    const userPk = this.$cookies.get("userPk");
    console.log("HomeMileage userPk: " + userPk);
    const that = this;
    axios
      .get("http://34.64.235.730/api/member/" + userPk + "/")
      .then((response) => {
        console.log("HomeMileage response? ");
        console.log(response);
        that.usermileage = response.data.mileage;
        that.username = response.data.username;
      });
  },
}
</script>

<style scoped>
.top {
  margin-top: 20px;
}
.line {
  width: 100%;
  height: 0.5px;
  background-color: lightgrey;
}

.green {
  top: 60px;
  left: 30px;
  background-color: #25BF8B;
  width: 400px;
  height: 200px;
  border-radius: 20px;
  box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22);
}

.white {
  top: 60px;
  left: 51px;
  background-color: #fff;
  width: 400px;
  height: 200px;
  border-radius: 20px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}

.white:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

.name {
  font-size: 1.6rem;
  font-weight: bolder;
}

.nim {
  font-size: 1.2rem;
  font-weight: bold;
}

.total {
  font-size: 3rem;
  font-weight: bolder;
}

.history {
  position: absolute; 
  width: 90px; 
  height: 40px; 
  background-color: #EDEDED; 
  text-align: center; 
  color: #494949; 
  font-weight: bolder; 
  font-size: 1rem; 
  border-radius: 10px;
  top: 140px;
  right: 16px;
}

.history:hover {
  cursor: pointer;
}

.history > span {
  position: absolute; 
  top: 7px; 
  left: 29px;
}

.button {
  display: inline-block; 
  background-color: #e3efeb; 
  width: 190px; 
  height: 60px; 
  font-size: 1.2rem; 
  text-align: center; 
  color: #444444; 
  font-weight: bolder;
  border-radius: 15px;
  position: relative;
}

.button.right {
  float: right;
}

.button span {
  position: absolute;
  top: 15px;
  left: 50px;
}

.use {
  background-color: #5BDEB2; 
  color: #fff; 
  width: 410px; 
  margin: 0 auto; 
  height: 60px; 
  border-radius: 15px; 
  font-size: 1.5rem; 
  text-align: center; 
  position: relative; 
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}

.use:hover {
  cursor: pointer;
}

.use > span {
  position: absolute; 
  top: 12px; 
  left: 112px;
}

.modal {
  -webkit-box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  -moz-box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  border-radius: 20px;
  height: 450px;
}

.modal:before, .modal:after {
  content:"";
  position:absolute;
  z-index:-1;
  -webkit-box-shadow:0 0 20px rgba(0,0,0,0.8);
  -moz-box-shadow:0 0 20px rgba(0,0,0,0.8);
  box-shadow:0 0 20px rgba(0,0,0,0.8);
  top:0;
  bottom:0;
  left:10px;
  right:10px;
  -moz-border-radius:100px / 10px;
  border-radius:100px / 10px;
}

.modal:after {
  right:10px;
  left:auto;
  -webkit-transform:skew(8deg) rotate(3deg);
  -moz-transform:skew(8deg) rotate(3deg);
  -ms-transform:skew(8deg) rotate(3deg);
  -o-transform:skew(8deg) rotate(3deg);
  transform:skew(8deg) rotate(3deg);
}
.modal {
  -webkit-box-shadow: 0 10px 6px -6px #777;
  -moz-box-shadow: 0 10px 6px -6px #777;
  box-shadow: 0 10px 6px -6px #777;
  background: white; 
  position: absolute; 
  top: 240px; 
  left: 15px; 
  width: 450px;
}

.modal-close:hover {
  cursor: pointer;
}
</style>