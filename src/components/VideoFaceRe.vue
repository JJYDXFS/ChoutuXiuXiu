<template>
  <div>
    <el-upload
      class="upload-demo"
      drag
      :headers = "headers"
      :action = "action"
      :on-success = "Success"
      :on-error = "Error"
      :on-progress = "Progress"
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
  <div>
    <h1>{{status}}</h1>
      <img :src="gen_img_url(i)" v-for="i in count" style="width:100%"/>
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
            status:"等待识别"
        };
    },
    mounted () {
        
    },
    methods:{
        Success(res, file, fileList){
            // console.log(res);
            // this.resultList = res['result_list'] ;
            this.img_path = res['img_path'];
            this.count = res['count']
            this.status = "识别成功"
        },
        Error(err, file, fileList){
            this.resultList = [];
            alert("识别失败！");
            this.status = "识别失败";
        },
        Progress(event, file, fileList){
            this.status = "识别中...";
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