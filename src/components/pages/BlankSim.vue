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
            this.$router.push("/index/manage/dataset/text/similarity")
        }
    }
}
</script>
<style scoped></style>