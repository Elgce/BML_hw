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
            this.$router.push("/index/menu3")
        }
    }
}
</script>
<style scoped></style>