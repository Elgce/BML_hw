<template>
    <span>Hello</span>
    <video id="myVideo" width="320" height="240" controls>
        <source src="../../assets/movie.mp4"  type="video/mp4">
    </video>
    <progress id="progressBar" value="0" max="100"></progress>
</template>


<script>
export default{
    name: "AddTag",
    mounted(){
        var video = document.getElementById("myVideo");
        var progress = document.getElementById("progressBar");
        video.ontimeupdate = function() {
            progress.value = 100 * video.currentTime / video.duration;
        }

    }
}
</script>


<style scoped>
#progressBar{
    width: 320px;
    height: 20px;
}
</style>