<template>
  <div>
    <shinhan-navigation-bar></shinhan-navigation-bar>
    <div class="title" style="text-align: center;">
      <img src="../assets/dailymission/title.png">
    </div>
    <div class="images">
      <div style="text-align: center;">
        <img class="done" v-if="doneList.indexOf(1) >= 0" src="../assets/dailymission/tumbler-done.png">
        <img class="undone" @click="doMission(1)" v-else src="../assets/dailymission/tumbler-undone.png">
      </div>
      <div style="text-align: center;">
        <img class="done" v-if="doneList.indexOf(2) >= 0" src="../assets/dailymission/recycle-done.png">
        <img class="undone" @click="doMission(2)" v-else src="../assets/dailymission/recycle-undone.png">
      </div>
      <div style="text-align: center;">
        <img class="done" v-if="doneList.indexOf(3) >= 0" src="../assets/dailymission/bus-done.png">
        <img class="undone" @click="doMission(3)" v-else src="../assets/dailymission/bus-undone.png">
      </div>
      <div style="text-align: center;">
        <img class="done" v-if="doneList.indexOf(4) >= 0" src="../assets/dailymission/shopping-done.png">
        <img class="undone" @click="doMission(4)" v-else src="../assets/dailymission/shopping-undone.png">
      </div>
    </div>
  </div>
</template>

<script>
import ShinhanNavigationBar from '../components/ShinhanNavigationBar.vue'
import axios from 'axios'

export default {
  components: {
    ShinhanNavigationBar,
  },
  data() {
    return {
      doneList: [],
    };
  },
  methods: {
    doMission(missionId) {
      console.log('doMission - missionId: ' + missionId);

      console.log('vues missionId(before setting test...): ' + this.$store.getters.getMissionId);
      this.$store.commit('setMissionId', missionId);
      console.log('vues missionId(after setting test...): ' + this.$store.getters.getMissionId);

      this.$router.push('/mission/photoupload')
    },
    checkMissionState() {
      const that = this;
      const accessToken = this.$cookies.get('accessToken');
      axios.get('http://34.64.235.73/api/mission/complete/', {
        headers: {
          Authorization: 'JWT ' + accessToken,
        },
      }).then(response => {
        console.log('유저가 완료한 일일미션 리스트 가져오기');
        console.log(response);
        response.data.forEach(mission => {
          that.doneList.push(mission.mission);
        });
      })
    }
  },
  created() {
    this.checkMissionState();
  }
}
</script>

<style scoped>
.images {
  height: 500px;
  overflow: auto;
}

.undone {
  cursor: pointer;
}

.done {
  cursor: not-allowed;
}
</style>