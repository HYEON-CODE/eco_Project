<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <section class="home-mileage">
      <div style="text-align: center">
        <p style="font-size: 3rem; color: white">친환경 마일리지</p>
      </div>

      <div style="text-align: center; margin: 30px 0px">
        <span class="mileage">{{ usermileage }}</span
        >&nbsp;마일리지
      </div>

      <div style="margin-bottom: 20px">
        <table class="mileage-menu">
          <tbody>
            <tr>
              <td>
                <router-link to="/mileage/history">마일리지 내역</router-link>
              </td>
              <td><a href="" @click.prevent="openModal">마일리지 사용</a></td>
            </tr>
            <tr>
              <td><router-link to="/walk">친환경 걷기</router-link></td>
              <td><router-link to="/mileage/dailymission">데일리 미션</router-link></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div
        v-if="showModal"
        style="
          width: 384px;
          height: 425px;
          background-color: white;
          position: absolute;
          top: 60px;
          left: 45px;
        "
      >
        <img
          class="modal"
          src="../assets/modal/top1.png"         
          @click="closeModal"
        />
        <img
          class="modal"
          src="../assets/modal/middle1.png"
          
          @click="moveToGiftCard"
        />
        <img
          class="modal"
          src="../assets/modal/bottom1.png"
          
          @click="moveToBarCode"
        />
      </div>

      <div class="temperature">
        <div>
          <p style="display: inline-block; color: white">
            <span class="username">{{ username }}</span
            >님의 친환경 온도&nbsp;&nbsp;
          </p>
          <p style="display: inline-block; color: white">
            <span>35&#8451;</span>
          </p>
        </div>
      </div>

      <div class="sub-menus" style="margin-top: 16px">
        <div class="item">
          <img :src="require('../assets/cards/card_1.png')" alt="" />
        </div>
        <div class="item">
          <img :src="require('../assets/cards/card_2.png')" alt="" />
        </div>
        <div class="item">
          <img :src="require('../assets/cards/card_3.png')" alt="" />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import ShinhanNavigationBar from "../components/ShinhanNavigationBar.vue";
import axios from "axios";

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      showModal: false,
      username: "",
      usermileage: 0,
    };
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    moveToGiftCard() {
      this.$router.push("/mileage/giftcard");
    },
    moveToBarCode() {
      this.$router.push("/mileage/barcode");
    },
  },
  created() {
    console.log("HomeMileage created...");
    const userPk = this.$cookies.get("userPk");
    console.log("HomeMileage userPk: " + userPk);
    const that = this;
    axios
      .get("http://127.0.0.1:8000/api/member/" + userPk + "/")
      .then((response) => {
        console.log("HomeMileage response? ");
        console.log(response);
        that.usermileage = response.data.mileage;
        that.username = response.data.username;
      });
  },
};
</script>

<style scoped>
img.modal:hover {
  cursor: pointer;
}

section {
  position: relative;
}
.temperature {
  width: 412px;
  height: 52px;
  line-height: 52px;
  margin: 0 auto;
  background-color: #1e996f;
  border-radius: 20px;
}

.temperature > div {
  text-align: center;
}
.home-mileage {
  background-color: #00a54f;
}

.mileage-menu {
  margin: 0 auto;
  border-collapse: collapse;
  border-style: hidden;
}

.mileage-menu td {
  padding: 1rem;
  text-align: center;
  font-size: 30px;
}

.home-mileage > div:first-child {
  padding: 20px 0px 0px;
}

.sub-menus {
  max-height: 200px;
  display: flex;
  overflow-x: auto;
}
.sub-menus .item:first-child {
  margin-left: 20px;
}
.sub-menus .item {
  min-width: 180px;
  height: 180px;
  line-height: 180px;
  text-align: center;
  margin-right: 20px;
}

.sub-menus img {
  width: 100%;
  height: 100%;
  border-radius: 10%;
}

.username {
  font-size: 1.5rem;
}

.mileage {
  font-size: 3rem;
}
/* https://blog.hubspot.com/website/center-div-css */
</style>