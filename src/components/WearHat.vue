<template>
    <div class="left">
        <div id = "select-div">
            <select v-model="selected" class="select-body">
                <option v-for="option in options" v-bind:value="option.value">
                    {{ option.text }}
                </option>
            </select>
        </div>
        <div id = "select-img">
            <img :src="getHatPath()" />
        </div>
    </div>
    <div class="left upload">
    <el-upload
      class="upload-demo"
      drag
      :data = "type"
      :headers = "headers"
      :action = "action"
      :on-success = "Success"
      :on-error = "Error"
      :on-progress = "Progress"
      list-type = "picture"
      limit = 1
    >
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将头像拖到此处，或<em>点击上传</em></div>
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
      <img :src="i" style="width:55%"/>
    </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'WearHat',
  props: {
    msg: String
  },
  data() {
    return {
      headers:{
        'Access-Control-Allow-Origin': '*',
      },
      action:"http://localhost:5000/api/wear_hat",
      resultList:[],
      selected: 'mxm',
      options: [
        { text: '暖暖毛线帽', value: 'mxm' },
        { text: '闪闪财神帽', value: 'fcm' },
        { text: '搞怪小丑帽', value: 'xcm' },
        { text: '复古贝雷帽', value: 'blm' },
        { text: '美味厨师帽', value: 'csm' },
        { text: '西域牛仔帽', value: 'nzm' },
        { text: '毕业学士帽', value: 'xsm' }
        ],
      status: "戴帽子准备"
    };
  },
  methods: {
      Success(res, file, fileList){
        this.resultList = res['result_list'] ;
        this.status = "戴好了！";
      },
      Error(err, file, fileList){
        this.resultList = [];
        alert("没戴上！");
      },
      Progress(event, file, fileList){
            this.status = "戴帽子中...";
      },
      getHatPath(){
          return "/hat/"+this.selected+".png"
      }
  },
  computed: {
    type : function() {
        return {'type':this.selected};
    },
  },

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
    width: 30%;
  }
.right {
    float: left;
    width: 36%;
}

.select-body{
    background-color: #49a0e785;
    border: none;
    color: rgb(0, 0, 0);
    padding: 10px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    margin: 4px 2px;
    cursor: pointer;
    margin-bottom: 35%;
}

.upload{
    margin-top: 10%;
}
</style>