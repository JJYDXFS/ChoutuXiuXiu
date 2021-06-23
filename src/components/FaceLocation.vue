<template>
  <div class="left">
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
      <div class="el-upload__text">将图片拖到此处，或<em>点击上传</em></div>
      <template #tip>
        <div class="el-upload__tip">
          只能上传 jpg 文件，且不超过 500KB
        </div>
      </template>
    </el-upload>
  </div>
  <div class="right">
    <h1>{{status}}</h1>
    <ul v-for="i in resultList">
    <li>
      <img :src="i" style="width:60%"/>
    </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'FaceLocation',
  props: {
    msg: String
  },
  data() {
    return {
      headers:{
        'Access-Control-Allow-Origin': '*',
      },
      action:"http://localhost:5000/api/get_face_loaction",
      resultList:[],
      status:"等待定位"
    };
  },
  methods: {
      Success(res, file, fileList){
        this.resultList = res['result_list'] ;
        this.status = "定位成功"
      },
      Error(err, file, fileList){
        this.resultList = [];
        alert("识别失败！");
        this.status = "定位失败";
      },
      Progress(event, file, fileList){
        this.status = "定位中...";
      },
}
}

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
</style>