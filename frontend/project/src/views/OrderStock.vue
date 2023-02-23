<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="top-wrap">
      <img src="../assets/re100/orderstock.png" alt="">
      <img class="buybtn" @click="confirmModalToggle" src="../assets/re100/buy2.png" alt="">
    </div>
    <span class="username">{{ username }}</span>
    <span class="accountnumber">계좌번호: {{ accountnumber }}</span>
    <span class="stockname">{{ stockname }}</span>
    <span class="stockprice">{{ stockprice }}원</span>
    <span class="stockprice-forcalc">{{ stockprice }}원</span>
    <span class="quantity">{{ orderquantity }}주</span>
    <span class="ment">지급받을 수 있는 예상 마일리지</span>
    <span class="mileage-calc">{{ calculateMileage }}</span>
    <div @click="setQuentity('plus')" class="plus"><span>+</span></div>
    <div @click="setQuentity('minus')" class="minus"><span>-</span></div>

    <div class="top-modal" v-show="showConfirmModal">
      <div style="text-align:center; font-size: 2rem">
        <span>매수 주문확인</span>
      </div>
      <div style="width: 100%; height: 0.5px; background-color: lightgray"></div>
      <div>
        <table>
          <tbody>
            <tr>
              <td class="title" style="width: 191px!important">종목이름</td>
              <td class="text">{{ stockname }}</td>
            </tr>
            <tr>
              <td class="title">주문수량</td>
              <td class="text">{{ orderquantity }}주</td>
            </tr>
            <tr>
              <td class="title">주문가격</td>
              <td class="text">{{ stockprice }}원</td>
            </tr>
            <tr>
              <td class="title">거래금액</td>
              <td class="text">{{ totalPrice }}원</td>
            </tr>
            <tr>
              <td class="title">마일리지</td>
              <td class="text">{{ calculateMileage }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="buttons" style="width: 340px; margin: 0 auto;">
        <div @click="confirmModalToggle" class="confirmdiv" style="display: inline-block; border: 1px solid gray; border-radius: 10px; width: 155px; height: 50px; position: relative">
          <span style="font-size: 1.2rem; position: absolute; left: 55px; top: 10px; font-weight: bold;">취&nbsp;소</span>
        </div>
        <div @click="confirmBuy" class="confirmdiv" style="display: inline-block; background-color: #E02D21; border-radius: 10px; width: 155px; height: 50px; float: right; position: relative;">
          <span style="font-size: 1.2rem; position: absolute; left: 55px; top: 10px; color: white; font-weight: bold;">매&nbsp;수</span>
        </div>
      </div>
    </div>

    <div class="modal" v-show="showModal">
      <div>
        <p style="color: #25BF8B; font-size: 1.5rem; font-weight: bolder; margin-left: 20px; display: inline-block;">알림</p>
        <p class="modal-close" style="float: right; display: inline-block; font-size: 1.5rem; margin-right: 20px;" @click="toggleModal">X</p>
      </div>
      <div style="width: 100%; height: 0.5px; background-color: lightgray"></div>
      <br>
      <div class="modal-content" style="margin-left: 20px; background-color: #F6F6F6; width: 91%; height: 60px">
        <p>{{ modalMessage }}</p>
      </div>      
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue';
import axios from 'axios';

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      click: false,
      username: null,
      accountnumber: null,
      stockname: null,
      stockprice: null,
      showConfirmModal: false,
      orderquantity: 1,
      calc_mileage: 0,
      showModal: false,
      modalMessage: '',
    };
  },
  methods: {
    confirmClick() {

    },
    notOrder() {

    },
    orderSuccess() {

    },
    confirmModalToggle() {
      this.showConfirmModal = !this.showConfirmModal;
    },
    checkCurrentPrice(stockName) {
      const that = this;
      axios.get('http://127.0.0.1:8000/api/stock?text=' + stockName)
        .then(response => {
          console.log(response);
          that.stockprice = response.data.current_price;
        }).catch(exception => {
          that.showModal = true;
          that.modalMessage = '해당 기업의 주가를 가져올 수 없습니다. 다른 RE100기업으로 조회해주세요.';
          that.toggleModal('redirect');
        })
    },
    getUserInfo() {
      const that = this;
      axios.get('http://127.0.0.1:8000/api/member/' + this.$cookies.get('userPk') + '/')
        .then(response => {
          that.username = response.data.username;
          that.accountnumber = response.data.account;
        })
    },
    setQuentity(type) {
      if (type == 'plus') {
        this.orderquantity++;
      } else if (type == 'minus') {
        this.orderquantity--;
      }
    },
    confirmBuy() {
      this.showConfirmModal = false;
      const that = this;
      const accessToken = this.$cookies.get('accessToken');
      axios.post('http://127.0.0.1:8000/api/mileage/', {
        user: that.$cookies.get('userPk'),
        activity: 'RE100매수',
        mileage: that.calculateMileage,
      }, {
        headers: {
          Authorization: 'JWT ' + accessToken,
        }
      }).then(result => {
        console.log('re100 매수로인해서 잘 적립됨.');
        that.modalMessage = '매수주문이 정상 체결되었습니다.'
        that.showModal = true;
      });
    },
    toggleModal(input) {
      const that = this;
      if (input === 'redirect') {
        setTimeout(() => {
          that.$router.push('/stock/re100');
        }, 2000);
      } else {
        this.showModal = false;
      }
    }
  },
  computed: {
    calculateMileage() {
      return Math.floor(this.stockprice * this.orderquantity * 0.002)
    },
    totalPrice() {
      return this.stockprice * this.orderquantity;
    }
  },
  created() {
    const stockName = this.$store.getters.getStockName;
    console.log('orderstock에서 현재 조회하고자 하는 stockname 가져오기 >> ' + stockName);
    this.stockname = stockName;
    this.checkCurrentPrice(stockName);
    this.getUserInfo();
  }
}
</script>

<style scoped>
.plus {
  background-color: red;
  top: 566px;
  left: 430px;
  background: #F8F8F8;
  font-size: 1.8rem;
  font-weight: bolder;
  width: 30px;
  height: 30px;
}

.plus:hover {
  cursor: pointer;
}

.minus {
  background-color: red;
  top: 566px;
  left: 236px;
  background: #F8F8F8;
  font-size: 1.8rem;
  font-weight: bolder;
  width: 30px;
  height: 30px; 
}

.minus:hover {
  cursor: pointer;
}

table {
  width: 340px;
}
.confirmdiv:hover {
  cursor: pointer;
}
.top-wrap {
  width: 480px;
  height: 645px;
  background-color: white;
  text-align: center;
  position: relative;
}

.buybtn {
  position: absolute;
  top: 590px;
  right: 12px;
}

.buybtn:hover {
  cursor: pointer;
}

.username,
.accountnumber,
.stockname,
.stockprice,
.stockprice-forcalc,
.quantity,
.mileage-calc,
.plus,
.minus,
.ment,
.minus {
  position: absolute;
}

.username {
  top: 0px;
  left: 0px;
  font-size: 1.5rem;
  top: 280px;
  left: 34px;
}

.accountnumber {
  top: 0px;
  left: 0px;
  font-size: 1.2rem;
  top: 285px;
  left: 225px;
}

.stockname {
  top: 148px;
  left: 55px;
  font-size: 1.5rem;
}

.stockprice {
  top: 210px;
  left: 25px;
  font-size: 2rem;
}

.stockprice-forcalc {
  top: 620px;
  right: 90px;
  font-size: 1.2rem;
}

.quantity {
  top: 572px;
  right: 123px;
  font-size: 1.2rem;
}

.mileage-calc {
  top: 500px;
  left: 194px;
  font-size: 1.5rem;
}

.ment {
  top: 470px!important;
  right: 14px!important;
  font-size: 1.3rem;
}

.text {
  text-align: right;
}

.top-modal {
  background: #fff;
  border-radius: 2px;
  display: inline-block;
  height: 375px;
  margin: 1rem;
  position: absolute;
  top: 243px;
  left: 31px;
  width: 400px;
  border-radius: 10px;
}

.top-modal {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}

.top-modal:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}

.title {
  font-size: 1.4rem;
}
td {
  height: 50px;
}

.text {
  font-size: 1.2rem;
}

table {
  margin-left: 31px;
}

.modal {
  -webkit-box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  -moz-box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  box-shadow:0 1px 4px rgba(0, 0, 0, 0.3), 0 0 40px rgba(0, 0, 0, 0.1) inset;
  border-radius: 20px;
  height: 150px;
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
  top: 330px; 
  left: 15px; 
  width: 450px;
}

.modal-close:hover {
  cursor: pointer;
}
</style>