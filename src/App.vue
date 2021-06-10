<template>
  <!-- <FaceRecognition msg="人脸定位" /> -->
  <MediaProcess/>
</template>

<script>
import FaceRecognition from './components/FaceRecognition.vue'
import MediaProcess from './components/MediaProcess.vue'

export default {
  name: 'App',
  components: {
    FaceRecognition,
    MediaProcess,
  }
}
</script>
