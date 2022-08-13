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
                    that.img = "http://localhost:5000/api/passfile/" + data["file_name"];
                })
            },
        }
    }
</script>


<style scoped>

</style>