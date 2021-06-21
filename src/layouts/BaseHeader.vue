<template>
  <el-menu
    :default-active="activeIndex"
    mode="horizontal"
    @select="handleSelect"
    router
  >
    <el-menu-item v-for="(item, i) in navItems" :key="i" :index="item.index">{{
      item.name
    }}</el-menu-item>
  </el-menu>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "index",
  data() {
    return {
      activeIndex: "1",
      navItems: [
        {
          name: "首页",
          index: "/",
        },
        {
          name: "人脸定位",
          index: "/FaceLocation",
        },
        {
          name: "人脸匹配",
          index: "/FaceRecognition",
        },
        {
          name: "视频人脸识别",
          index: "/VideoFaceRe",
        },
        {
          name: "自选帽子",
          index: "/WearHat",
        },
      ],
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
  },
});
</script>
