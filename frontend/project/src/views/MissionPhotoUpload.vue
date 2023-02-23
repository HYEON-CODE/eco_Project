<template>
  <div>
    <green-bar></green-bar>
    <div class="top-wrap">
      <img src="../assets/missionphotoupload/greenrectangle.png" alt="" />
      <div class="mission-text">
        <p>
          <span class="mission-type">{{ missionTitle }}</span><br /><br />
          <span class="mission-description">{{ missionDescription }}</span>
        </p>
      </div>
    </div>

    <div style="margin-top: 15px">
      <div style="text-align: center">
        <label for="file-upload" class="custom-file-upload">
          여기를 클릭해서 파일을 업로드 해주세요!
        </label>
      </div>
      <input type="file" @change="onFileChange" id="file-upload" />
      <div id="preview" style="margin-top: 10px">
        <img v-if="url" :src="url" width="480" height="325" />
      </div>
    </div>

    <div class="uploadbtn" v-if="url" style="text-align: center;" @click="uploadImage">
      <img src="../assets/missionphotoupload/uploadbtn.png" alt="">
    </div>
  </div>
</template>

<script>
import GreenBar from '../components/GreenBar.vue'
import axios from 'axios'

export default {
  components: {
    GreenBar,
  },
  data() {
    return {
      url: null,
      missionTitle: null,
      missionDescription: null,
      missionType: {
      1: '분리수거',
      2: '장바구니',
      3: '텀블러',
      4: '대중교통',
      },
    };
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
    getMissionInfo(missionId) {
      const url = 'http://34.64.235.73/api/mission/';
      const that = this;
      axios.get(url + missionId + '/').
        then(response => {
          console.log(response);
          that.missionTitle = response.data.title;
          that.missionDescription = response.data.description;
        })
    },
    uploadImage() {
      const that = this;
      const missionId = this.$store.getters.getMissionId;
      console.log('missionphotoupload 페이지에서 업로드 버튼 눌렀을 때 missionId: ' + missionId);
      const accessToken = this.$cookies.get('accessToken');
      console.log('accessToken: ' + that.$cookies.get('accessToken'));
      const frm = new FormData();
      frm.append('mission', Number(missionId));

      axios.post('http://34.64.235.73/api/mission/complete/', {
          mission: Number(missionId)
        },
        {
          headers: {
            Authorization: 'JWT ' + accessToken,
          }
        }
      ).then(response => {
        console.log('uploadImage 사진 업로드 시 response');
        console.log(response);
        console.log('사진이 업로드 되었습니다.');
        //that.$router.push('/mileage/dailymission');
      }).catch(error => {
        console.log('error?');
        console.log(error);
      });


      axios.post('http://34.64.235.73/api/mileage/', {
        user: that.$cookies.get('userPk'),
        activity: '미션(' + that.missionType[missionId] + ')',
        mileage: 10,
      }, {
        headers: {
          Authorization: 'JWT ' + accessToken,
        }
      }).then(result => {
        console.log('일일미션번호?: ' + missionId + ',,, 잘 적립됨!');
        that.$router.push('/mileage/dailymission');
      });
    }
  },
  created() {
    const missionId = this.$store.getters.getMissionId;
    console.log('사진업로드페이지에서 missionId 조회: ', missionId);
    this.getMissionInfo(missionId);
  },
};
</script>

<style scoped>
input[type="file"] {
  display: none;
}
.custom-file-upload {
  border: 1px solid #ccc;
  display: inline-block;
  padding: 6px 12px;
  cursor: pointer;
  border-radius: 10px;
  margin-top: 10px;
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
.image-thumbnail {
  margin-top: 20px;
  margin-left: 16px;
  width: 450px;
  height: 360px;
  background-color: antiquewhite;
  border-radius: 20px;
}
.mission-type {
  font-size: 2rem;
  font-weight: bolder;
}

.mission-description {
  font-size: 1rem;
}
.top-wrap {
  margin-top: 20px;
  position: relative;
  text-align: center;
}
.top-wrap .mission-text {
  display: flex;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  align-items: center;
  justify-content: center;
}

.uploadbtn {
  cursor: pointer;
  margin-top: 15px;
}
</style>