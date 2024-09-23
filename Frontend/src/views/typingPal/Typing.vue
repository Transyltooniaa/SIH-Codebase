<template>
  <div class="header">
    <base-nav
    container-classes="container-fluid"
    class="navbar-top navbar-expand"
    :class="{'navbar-dark': type === 'default'}">
    <a href="#" aria-current="page" class="h4 mb-0 text-white text-uppercase d-none d-lg-inline-block active router-link-active"> {{$route.name}} </a>
    </base-nav>
      <TypingHeader></TypingHeader>
      <TypingBox></TypingBox>
  </div>
</template>

<script>

import SocialTrafficTable from '../Dashboard/SocialTrafficTable';
import TypingHeader from './TypingHeader.vue';
import TypingBox from './TypingBox.vue';
import { BaseNav, Modal } from '@/components';

export default {
  components :{
    SocialTrafficTable,
    TypingHeader,
    TypingBox,
    BaseNav,
    Modal
  }
}
</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.header{
  position: relative;
  top : 100px;
}



</style>