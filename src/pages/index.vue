<template>
  <div>
    <div>
      <p class="title my-font">媒体大数据实践</p>
      <p class="subtitle my-font">&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;—— 多媒体内容理解部分</p>
      <div class="content">
        <p style="font-size:20px"><b>内容一览</b></p>
        <p><b>人脸定位：</b>提供基础人脸定位功能</p>
        <p><b>人脸匹配：</b>匹配影视剧《The Crown（王冠）》中的人物角色</p>

        <p><b>视频人脸识别：</b>识别影视剧《The Crown（王冠）》的片段</p>
      
        <p><b>人工智障戴帽子：</b>自选帽子帮您戴</p>
        <p><b>违和换脸小游戏：</b>不怕违和就来吧</p>
        <p><b>流水线化妆工厂：</b>打造专属你的“美”</p>
      </div>

    </div>
  </div>
  <div class="my-footer">
    <hr>
    <footer class="my-footer">Copyright © 2021 章颖 宋玮. All Rights Reserved</footer>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    
  },
})
</script>

<style scoped>
.title{
  padding-top: 20px;
  /* margin-top: 5%; */
  font-size: 80px;
}

.subtitle{
  margin-top: 1%;
  font-size: 60px;
}
.my-font{
  font-family: STZhongsong;
}

.content{
  font-size: 16px;
}

p{
  line-height: 0.8;
}

.my-footer{
  width: 100%;
  text-align: center;
  font-size: 14px;
  position: absolute;
  bottom: 0;
}
</style>
