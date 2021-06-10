<template>
    <div>
        请输入视频路径: <input id="input-box" type="text" name="fname" placeholder="C:\\xxx\\xxx\\xxx.mp4">
        <button @click="get_img_path">切帧</button>
    </div>
    <div id="as"></div>
    <img :src="gen_img_url(i)" v-for="i in count" style="width:20px"/>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
    data() {
        return {
            img_path:"",
            movie_path:"",
            count:0,
        };
    },
    mounted () {
        
    },
    methods:{
        get_img_path(){
            this.movie_path = document.getElementById("input-box").value;
            // 192.168.0.100
            axios.get("http://localhost:5000/api/get_img_path",{ params:{ movie_path:this.movie_path} }).then((res) => {
                // console.log(res['data']['count']);
                this.count = res['data']['count'];
                this.img_path = res['data']['path'];
            });
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
