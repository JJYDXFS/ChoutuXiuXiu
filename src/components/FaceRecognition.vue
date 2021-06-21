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
        只能上传 jpg 文件，且不超过 500KB
      </div>
    </template>
  </el-upload>
  </div>
  <div class="right">
    <h1>匹配结果</h1>
    <ul v-for="i in resultList">
    <li>
      <img :src="i" style="width:45%"/>
    </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'FaceRecognition',
  props: {
    msg: String
  },
  data() {
    return {
      headers:{
        'Access-Control-Allow-Origin': '*',
      },
      action:"http://localhost:5000/api/get_face_recognition",
      resultList:[]
    };
  },
  methods: {
      Success(res, file, fileList){
        // console.log(res);
        this.resultList = res['result_list'] ;
      },
      Error(err, file, fileList){
        this.resultList = [];
        alert("识别失败！");
      }
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