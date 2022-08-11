<template>
    <span>wejqw</span>
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
            }
        },
        methods:{
            cal_session(){
                let that = this;
                return fetch("/api/sessionname").then((res) => res.json().then((j)=>{
                    that.name = j.name;
                    console.log(that.name);
                }))
            },
        }
    }
</script>


<style scoped>

</style>