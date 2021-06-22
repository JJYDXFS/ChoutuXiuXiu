<template>
  <el-upload
  ref="upload"
  :action="action"
  :on-success = "Success"
  :on-error = "Error"
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
        <!-- <span class="el-upload-list__item-actions">
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
            @click="handleRemove(file)"
          >
            <i class="el-icon-delete"></i>
          </span>
        </span> -->
      </div>
    </template>
</el-upload>
<el-dialog v-model="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog>
<el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">点击换脸</el-button>
<div>
    <h1>换脸结果</h1>
    <ul v-for="i in resultList">
    <li>
      <img :src="i" style="width:60%"/>
    </li>
    </ul>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        headers:{
          'Access-Control-Allow-Origin': '*',
        },
        action:"http://localhost:5000/api/change_face",
        dialogImageUrl: '',
        dialogVisible: false,
        disabled: false,
        resultList: []
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
        // console.log(res);
        this.resultList = res['result_list'] ;
      },
      Error(err, file, fileList){
        this.resultList = [];
        alert("识别失败！");
      },
      handleRemove(file) {
        console.log(file);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleDownload(file) {
        console.log(file);
      }
    }
  }
</script>