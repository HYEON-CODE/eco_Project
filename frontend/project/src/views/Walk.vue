<template>
  <div>
    <green-bar></green-bar>
    <div class="box">
      <div class="percent">
        <svg>
          <circle cx="70" cy="70" r="70"></circle>
          <circle cx="70" cy="70" r="70" ref="bar"></circle>
        </svg>
        <div class="number">
          <h2>{{ percent }}<span>%</span></h2>
        </div>
      </div>
      <h2 class="text" style="text-align: center">
        <span style="color: green">환경</span>을 위해<br /><span
          style="font-size: 40px; color: green"
          >{{ walk }} / 10000</span
        ><br />걸음 걸으셨습니다!
      </h2>
    </div>

    <div class="buttons">
      <button class="oneWalk" @click="oneWalk">한 걸음 걷기</button>
      <button class="fullWalk" @click="fullWalk">
        만걸음 한 번에 걷기
      </button>
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
import axios from 'axios';
import GreenBar from '../components/GreenBar.vue';

export default {
  components: {
    GreenBar,
  },
  data() {
    return {
      percent: 0,
      walk: 0,
      showModal: false,
      modalMessage: '',
    };
  },
  mounted() {
    this.$refs.bar.style.strokeDashoffset =
      "calc(440 - (440 * (" + this.walk + "/10000) * 100) / 100)";
  },
  methods: {
    oneWalk() {
      if ((this.walk + 1) > 10000) {
        //alert('오늘은 1만 걸음을 다 채우셨습니다. 내일 걸음수가 초기화 됩니다!');
        this.modalMessage = '오늘 만걸음을 다 채우셨습니다. 내일 걸음수가 초기화 됩니다.'
        this.showModal = true;
        return;
      }
      this.walk += 1;
      if (this.walk === 10000) {
        this.addMileage();
      }
      const percent = ((this.walk / 10000) * 100).toFixed(2);
      this.percent = percent >= 100 ? 100 : percent;
      this.$refs.bar.style.strokeDashoffset =
        "calc(440 - (440 * (" + this.walk + "/10000) * 100) / 100)";
    },
    fullWalk() {
      if ((this.walk + 1) > 10000) {
        //alert('오늘은 1만 걸음을 다 채우셨습니다. 내일 걸음수가 초기화 됩니다!');
        this.modalMessage = '오늘 만걸음을 다 채우셨습니다. 내일 걸음수가 초기화 됩니다.'
        this.showModal = true;
        return;
      }
      this.walk = 10000;
      this.addMileage();
      this.percent = 100;
      this.$refs.bar.style.strokeDashoffset =
        "calc(440 - (440 * (" + this.walk + "/10000) * 100) / 100)";
    },
    addMileage() {
      const that = this;
      const userPk = this.$cookies.get('userPk');
      const activity = '하루만걸음';
      const mileage = 20;
      const accessToken = this.$cookies.get('accessToken');
      console.log('userPk: ' + userPk);
      console.log('accessToken: ' + accessToken);
      axios.post('http://127.0.0.1:8000/api/mileage/', {
          user: userPk,
          activity: activity,
          mileage: mileage,
        },
        {
          headers: {
            Authorization: 'JWT ' + accessToken,
          }
        }
      ).then(response => {
        //alert('1만 걸음 채우기 완료! 100마일리지가 적립되었습니다!');
        that.modalMessage = '만걸음 채우기 완료! 20마일리지가 적립되었습니다!'
        that.showModal = true;
      });
    },
    toggleModal() {
      this.showModal = !this.showModal;
      this.$router.push('/calendar');
    },
  },
};
</script>

<style scoped>
.buttons {
  margin-top: 65px;
}
button {
  width: 100%;
  height: 70px;
  font-size: 1.2rem;
  background-color: #25bf8b;
  color: white;
  border: 0.5px solid white;
}

button:hover {
  cursor: pointer;
}
.box {
  margin-top: 150px;
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  /* box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2); */
}
.box .percent {
  position: relative;
  width: 150px;
  height: 150px;
}
.box .percent svg {
  position: relative;
  width: 150px;
  height: 150px;
}

.box .percent svg circle {
  width: 250px;
  height: 250px;
  fill: none;
  stroke-width: 10;
  stroke: #000;
  transform: translate(5px, 5px);
  stroke-dasharray: 440;
  stroke-dashoffset: 440;
}
.box .percent svg circle:nth-child(1) {
  stroke-dashoffset: 0;
  stroke: #f3f3f3;
}

.box .percent svg circle:nth-child(2) {
  stroke-dashoffset: calc(440 - (440 * (5000 / 10000) * 100) / 100);
  stroke: #51bd73;
}
.box .percent .number {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #999;
}

.box .percent .number h2 {
  font-size: 48px;
}

.box .percent .number h2 span {
  font-size: 24px;
}

.box .text {
  padding: 10px 0 0;
  color: #999;
  font-weight: 700;
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