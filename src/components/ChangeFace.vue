<template>
  <el-upload
  ref="upload"
  :action="action"
  :on-success = "Success"
  :on-error = "Error"
  :on-progress = "Progress"
  list-type="picture-card"
  :auto-upload="false"
  limit = 2
  multiple
  >
    <template #default>
      <i class="el-icon-plus"></i>
    </template>
    <template #file="{file}">
      <div>
        <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
        <span class="el-upload-list__item-actions">
          <span
            class="el-upload-list__item-preview"
            @click="handlePictureCardPreview(file)"
          >
            <i class="el-icon-zoom-in"></i>
          </span>
          <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleDownload(file)"
          >
            <i class="el-icon-download"></i>
          </span>
          <span
            v-if="!disabled"
            class="el-upload-list__item-delete"
            @click="handleRemove(file,fileList,fileIndex)"
          >
            <i class="el-icon-delete"></i>
          </span>
        </span>
      </div>
    </template>
</el-upload>
<el-dialog v-model="dialogVisible">
  <img style="width:40%" :src="dialogImageUrl" alt="">
</el-dialog>
<el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">点击换脸</el-button>
<div>
    <h1>{{status}}</h1>
    <ul v-for="i in resultList">
    <li>
      <img :src="i" style="width:60%"/>
    </li>
    </ul>
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
        action:"http://localhost:5000/api/change_face",
        dialogImageUrl: '',
        dialogVisible: false,
        disabled: false,
        resultList: [],
        status: "等待换脸"
      };
    },
    methods: {
      submitUpload() {
        if (this.$refs.upload.uploadFiles.length<2){
          alert("必须同时上传两张图片哦！")
        }
        else{
          this.$refs.upload.submit();
        }
      },
      Success(res, file, fileList){
        this.resultList = res['result_list'];
        this.status = "换脸成功";
      },
      Error(err, file, fileList){
        this.resultList = [];
        alert("换脸失败！");
        this.status = "换脸失败";
      },
      Progress(event, file, fileList){
        this.status = "换脸中...请耐心等待";
      },
      handleRemove(file) {
        // 根据值删除数组指定元素
        // https://www.jb51.net/article/134312.htm
        Array.prototype.remove = function(val) { 
            let index = this.indexOf(val); 
            if (index > -1) { 
              this.splice(index, 1); 
            } 
        };

        this.$refs.upload.uploadFiles.remove(file);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleDownload(file) {
        // 点击下载图片
        // https://www.cnblogs.com/chao202426/p/11403713.html
        let url = file.url;                            // 获取图片地址
        let a = document.createElement('a');          // 创建一个a节点插入的document
        let event = new MouseEvent('click')           // 模拟鼠标click点击事件
        a.download = file.name                 // 设置a节点的download属性值
        a.href = url;                                 // 将图片的src赋值给a节点的href
        a.dispatchEvent(event)                        // 触发鼠标点击事件
      }
    }
})
</script>