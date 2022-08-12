<template>
    <el-button @click="act"></el-button>
    <img src="..\\..\\..\\backend\\src\\213\\msi.jpg"/>
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
                    for (let item in j.src_list){
                        let path = "..\\..\\..\\backend" + j.src_list[item];
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