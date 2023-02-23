<template>
  <div>
  <div class="top">
    <p style="margin-left: 25px; font-weight: bolder; font-size: 1.5rem;">로그인</p>
    <br>
    <div class="line" style="width: 100%; height: 0.5px; background-color: lightgray"></div>
  </div>
  <div class="container" style="margin-top: 25px">
    <div style="text-align: center;">
      <img src="../assets/shinhancharacter/character.png" alt="">
    </div>

    <label for="uname"><b>유저네임</b></label>
    <input type="text" placeholder="유저네임을 입력하세요." name="username" id="username" required ref="username" />

    <label for="psw"><b>비밀번호</b></label>
    <input type="password" placeholder="비밀번호를 입력하세요." name="password" id="password" required ref="password" />

    <button @click="login">로그인하기</button>
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

export default {
  data() {
    return {
      modalMessage: '',
      showModal: false,
    }
  },
  methods: {
    login() {
      const username = this.$refs.username.value;
      const password = this.$refs.password.value;
      const that = this;

      axios.post('http://34.64.235.730/api/member/login/', {
        username: username,
        password: password,
      }).then(response => {
        console.log(response);
        if (response.status == 200) {
          //alert('로그인 되었습니다.');
          console.log('로그인 페이지 response.data');
          console.log(response.data);
          this.$cookies.set('accessToken', response.data.access);
          console.log('로그인 페이지에서 cookie에 accessToken이 있는지 true/false 확인.');
          console.log(this.$cookies.isKey('accessToken'));

          // 회원가입부터 진행하면 아래 코드를 실행 안 해도 상관 없으나, 로그인 부터 진행할경우 아래 코드 필요.
          axios.get('http://34.64.235.73/api/member/')
              .then(response => {
                console.log(response);
                response.data.forEach(member => {
                  if (member.username == username) {
                    this.$cookies.set('userPk', member.id);
                  }
                });
                that.showModal = true;
                that.modalMessage = "로그인 되었습니다."
              });
        } else {
          alert('로그인 실패. 유저네임 혹은 비밀번호를 확인하세요.');
        }
      }).catch(error => {
        alert('로그인 서버 오류 발생.');
      });
    },
    toggleModal() {
      this.$router.push('/account');
    }
  }
};
</script>

<style scoped>
input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

/* Set a style for all buttons */
button {
  background-color: #A3C7F7;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  font-size: 1.2rem;
}

/* Add a hover effect for buttons */
button:hover {
  opacity: 0.8;
}
/* Add padding to containers */
.container {
  padding: 16px;
}

/* The "Forgot password" text */
span.psw {
  float: right;
  padding-top: 16px;
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