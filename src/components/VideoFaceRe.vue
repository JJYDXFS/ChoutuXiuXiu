<template>
  <div class="left">
    <el-upload
      class="upload-demo"
      drag
      :headers = "headers"
      :action = "action"
      :on-success = "Success"
      :on-error = "Error"
      list-type = "picture"
      limit = 1
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <template #tip>
        <div class="el-upload__tip">
          只能上传 mp4 文件，且不超过 5MB
        </div>
      </template>
    </el-upload>
  </div>
  <div class="right">
    <h1>识别结果</h1>
    <ul v-for="i in resultList">
    <li>
      <img :src="gen_img_url(i)" v-for="i in count" style="width:20px"/>
    </li>
    </ul>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
    data() {
        return {
            headers:{
                'Access-Control-Allow-Origin': '*',
            },
            action:"http://localhost:5000/api/video_face_re",
            img_path:"",
            count:0,
        };
    },
    mounted () {
        
    },
    methods:{
        Success(res, file, fileList){
            // console.log(res);
            this.resultList = res['result_list'] ;
        },
        Error(err, file, fileList){
            this.resultList = [];
            alert("识别失败！");
        },
        gen_img_url(index){
            // console.log(index);
            // console.log(this.img_path+(index-1).toString()+".jpg");
            // return require(this.img_path+(index-1).toString()+".jpg");
            return this.img_path+(index-1).toString()+".jpg"
        },
    }
})
</script>

<style>
@import url("//unpkg.com/element-plus/lib/theme-chalk/index.css");

ul{
  list-style: none;
}
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf00;
  }
  .bg-purple {
    background: #d3dce600;
  }
  .bg-purple-light {
    background: #e5e9f200;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc00;
}
  .left{
    float: left;
    width: 50%;
  }
  .right {
    float: left;
    width: 40%;
  }
</style>