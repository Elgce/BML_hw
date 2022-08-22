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
            this.$router.push("/index/manage/dataset/video/mark");
        }
    }
}
</script>
<style scoped></style>