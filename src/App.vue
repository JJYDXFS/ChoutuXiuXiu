<template>
  <el-container>
    <base-header />
    <el-main>
      <router-view />
    </el-main>
    <el-footer>
    
    </el-footer>
  </el-container>
</template>

<script>
import { defineComponent } from "vue";
// import FaceRecognition from './components/FaceRecognition.vue'
// import MediaProcess from './components/VideoFaceRe.vue'
import BaseHeader from "./layouts/BaseHeader.vue";

export default defineComponent({
  name: 'App',
  components: {
    // FaceRecognition,
    // MediaProcess,
    BaseHeader,
  }
});
</script>

<style>
body{
  background: url("/img/bg.png");
  height: 100%;
}
</style>