<template>
<p></p>
</template>
<script>
export default{
    created(){
        this.setpath()
    },
    methods:{
        setpath(){
            this.$router.push("/index/manage/dataset/pic/addtag")
        }
    }
}
</script>
<style scoped></style>