<template>
    <el-button @click="act"></el-button>
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
            }
        },
        methods:{
            cal_session(){
                let that = this;
                return fetch("/api/sessionname").then((res) => res.json().then((j)=>{
                    that.name = j.name;
                    that.root_dir = "../../../backend/src/"+that.name;
                    for (let item in j.src_list){
                        let path = "..\\..\\..\\backend" + j.src_list[item];
                        path = path.replace(/\\/g,"/");
                        that.src_list.push(path);
                    }
                }))
            },
            act(){
                console.log(this.src_list[0]);
            },
        }
    }
</script>


<style scoped>

</style>