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
import BaseHeader from "./layouts/BaseHeader.vue";

export default defineComponent({
  name: 'App',
  components: {
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