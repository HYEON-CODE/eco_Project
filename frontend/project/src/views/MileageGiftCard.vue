<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="clickable" style="position: relative" @click="buy(1)">
      <img src="../assets/mileage/giftcard10000.png" alt="" />
      <span class="il-man">10,000</span>
    </div>
    <div class="clickable" style="position: relative" @click="buy(2)">
      <img src="../assets/mileage/giftcard30000.png" alt="" />
      <span class="sam-man">30,000</span>
    </div>
    <div class="top-wrap" style="text-align: center">
      <img src="../assets/mileage/notice2.png" alt="" />
      <img src="../assets/mileage/notice3.png" alt="">
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
import ShinhanNavigationBar from '@/components/ShinhanNavigationBar.vue';
import axios from 'axios'
export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      showModal: false,
      modalMessage: '',
    }
  },
  methods: {
    buy(id) {
      const that = this;
      let url = 'http://34.64.235.73/api/member/' + this.$cookies.get('userPk') + '/'
      axios.get(url)
        .then(response => {
          console.log(response);
          const remain = response.data.mileage;
          if (id == 1) {
            if (remain < 10000) {
              that.modalMessage = '마일리지 부족으로 구매하실 수 없습니다.'
              that.showModal = true;
            } else {
              that.minusMileage(id);
            }
          } else if (id == 2) {
            if (remain < 30000) {
              that.modalMessage = '마일리지 부족으로 구매하실 수 없습니다.'
              that.showModal = true;
            } else {
              that.minusMileage(id);
            }
          }
        });
    },
    toggleModal() {
      this.showModal = !this.showModal;
    },
    minusMileage(id) {
      const that = this;
      let price;
      const accessToken = this.$cookies.get('accessToken');
      if (id == 1) {
        price = -10000
      } else if (id == 2) {
        price = -30000
      }

      axios.post('http://34.64.235.73/api/mileage/', {
        user: that.$cookies.get('userPk'),
        activity: '투자상품권',
        mileage: price,
      }, {
        headers: {
          Authorization: 'JWT ' + accessToken,
        }
      }).then(result => {
        console.log('기프트카드 구매 잘 성공...');
        that.modalMessage = '금융투자상품권을 성공적으로 구매하였습니다.'
        that.showModal = true;
      });
    }
  },
  created() {
  }
};
</script>

<style scoped>
div.top-wrap {
  height: 180px;
  overflow: auto;
}
span {
  position: absolute;
  display: inline-block;
  font-size: 30px;
  font-weight: bolder;
  color: blue;
}
.il-man {
  top: 114px;
  right: 96px;
}

.sam-man {
  top: 114px;
  right: 96px;
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

.clickable:hover {
  cursor: pointer;
}
</style>