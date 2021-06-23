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
          name: "人工智障戴帽子",
          index: "/WearHat",
        },
        {
          name: "违和换脸小游戏",
          index: "/ChangeFace",
        },
        {
          name: "流水线化妆工厂",
          index: "/Makeup",
        },
      ],
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    },
  },
});
</script>
