<template>
    <el-button @click="act"></el-button>
    <el-image v-loading="loading" :src="img"></el-image>
</template>


<script>


    export default{
        name:'MainFour',
        created(){
            this.cal_session()
        },
        data(){
            return {
                name: "",
                src_list:[],
                img: "",
                loading: false,
            }
        },
        methods:{
            cal_session(){
                let that = this;
                return fetch("/api/sessionname").then((res) => res.json().then((j)=>{
                    that.name = j.name;
                    for (let item in j.src_list){
                        let path = "..\\..\\..\\backend" + j.src_list[item];
                        path = path.replace(/\\/g,"/");
                        that.src_list.push(path);
                    }
                }))
            },
            act(){
                console.log(this.src_list);
                const data = {"file_name":"msi.jpg"};
                let that = this;
                let url = "/api/passfile/" + data["file_name"];
                return fetch(url,{
                    method: 'POST',
                    responseType: 'blob',
                    headers:{
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                }).then(() => {
                    // let src = window.URL.createObjectURL(res);
                    // this.img = src;
                    // let blob = new Blob([res]);
                    // console.log(res);
                    // console.log(res);
                    // let blob = res.blob();
                    // let binaryData = [];
                    // binaryData.push(blob);
                    // let url = URL.createObjectURL(new Blob(binaryData));
                    // console.log(url);
                    // this.img = url;
                    // const myBlob = new window.Blob([res], {type: 'image/jpeg'});
                    // const qrUrl = window.URL.createObjectURL(myBlob);
                    // console.log(qrUrl);
                    // that.src = qrUrl;
                    // that.loading = false;
                    // that.img = 'data:image/jpeg;base64,'+that.arrayBufferToBase64(res);
                    // console.log(that.img);
                    // console.log(res);
                    that.img = "http://localhost:5000/api/passfile/" + data["file_name"];
                })
            },
        }
    }
</script>


<style scoped>

</style>