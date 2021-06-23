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
      <div class="el-upload__text">将照片拖到此处，或<em>点击上传</em></div>
      <template #tip>
        <div class="el-upload__tip">
          只能上传 jpg 文件，且不超过 500KB
        </div>
      </template>
    </el-upload>
  </div>
  <div>
    <h1>{{status}}</h1>
      <img :src="gen_img_url(i)" v-for="i in count" style="width:100%"/>
  </div>
  <div v-for="i in resultList" class="left">
      <img :src="i.img_url" style="width:80%">
      <p class="img-title">{{i.title}}</p>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    data() {
        return {
            headers:{
                'Access-Control-Allow-Origin': '*',
            },
            action:"http://localhost:5000/api/makeup",
            resultList:[],
            status: "等待上妆"
        };
    },
    mounted () {
        
    },
    methods:{
        Success(res, file, fileList){
            console.log(res);
            this.resultList = res['result_list'] ;
            this.status = "上妆成功";
            // this.img_path = res['img_path'];
            // this.count = res['count'];
            
        },
        Error(err, file, fileList){
            this.resultList = [];
            alert("上妆失败！");
            this.status = "上妆失败";
        },
        Progress(event, file, fileList){
            this.status = "上妆中...请耐心等待";
        },
        gen_img_url(index){
            return this.img_path+(index-1).toString()+".jpg"
        },
    }
})

</script>

<style scoped>
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

.img-title{
    font-size: 40px;
    font-weight: bold;
}
</style>