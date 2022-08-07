<template>
    <div class="item_heading" id="new_info">创建信息</div>
    <p class="text_left1" style="left:240px;top:120px">数据集ID</p>
    <p class="text_left1" style="left:240px;top:160px">备注</p>
    <button id="change_memo"></button>
    <p class="text_left1" style="left:240px;top:200px">历史数据</p>
    <p class="text_left2" style="left:350px;top:121px">123456</p>
    <p class="text_left2" style="left:350px;top:200px">暂无导入记录</p>
    <p class="text_right2" style="left:600px;top:120px">版本号</p>
    <p class="text_right2" style="left:690px;top:121px">V1</p>
    <p class="item_heading" id="mark_info">标注信息</p>
    <p class="text_left1" style="left:240px;top:290px">标注类型</p>
    <p class="text_left1" style="left:240px;top:330px">数据总量</p>
    <p class="text_left1" style="left:240px;top:370px">标签个数</p>
    <p class="text_left1" style="left:240px;top:410px">大小</p>
    <p class="text_left2" style="left:350px;top:290px">图像分类</p>
    <p class="text_left2" style="left:350px;top:331px">0</p>
    <p class="text_left2" style="left:350px;top:371px">0</p>
    <p class="text_left2" style="left:350px;top:411px">0M</p>
    <p class="text_right1" style="left:600px;top:293px">标注模块</p>
    <p class="text_right1" style="left:600px;top:333px">已标注</p>
    <p class="text_right1" style="left:600px;top:373px">待确认</p>
    <p class="text_right2" style="left:690px;top:294px">单图单标签</p>
    <p class="text_right2" style="left:690px;top:335px">0</p>
    <p class="text_right2" style="left:690px;top:375px">0</p>
    <p class="item_heading" id="data_cle">数据清洗</p>
    <p class="text_left1" style="left:240px;top:500px">暂未做过数据清洗任务</p>
    <p class="item_heading" id="data_enhan">数据增强</p>
    <p class="text_left1" style="left:240px;top:590px">暂未做过数据增强任务</p>
    <p class="item_heading" id="data_intro">导入数据</p>
    <p class="text_left1" style="left:240px;top:680px">数据标注状态</p>
    <form id="markingInfo_radio_group">
        <input type="radio" value="no_marking_info" name="marking_info">无标注信息&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="radio" value="_marking_info" name="marking_info">有标注信息
    </form>
    <p class="text_left1" style="left:240px;top:720px">导入方式</p>
    <select id="fashion_choice">
        <option value="" disabled selected hidden>请选择</option>
        <option>本地导入</option>
        <option>BOS目录导入</option>
        <option>分享链接导入</option>
        <option>平台已有数据集</option>
        <option>摄像头采集数据</option>
        <option>云服务回流数据</option>
    </select>
    <button id="submit_button">确认并返回</button>
</template>

<script>
    export default{
        name: "MainTwo"
    }
    // var change_memo_btn=document.getElementById("change_memo");
    // change_memo_btn.onclick=function(){
    //     this.style.visibility='hidden';
    // }
</script>

<style scoped>
    .item_heading
    {
        position:absolute;
        padding-left: 6px;
        border-left: 4px solid;
        height:22px;
        font-weight:700;
        font-size:15px;
    }
    #new_info
    {
        left:230px;
        top:90px;
    }
    #mark_info
    {
        left:230px;
        top:250px;
    }
    #data_cle
    {
        left:230px;
        top:460px;
    }
    #data_enhan
    {
        left:230px;
        top:550px;
    }
    #data_intro
    {
        left:230px;
        top:640px;
    }
    .text_left1
    {
        position:absolute;
        font-size:15px;
        font-weight:300;
    }
    .text_right1
    {
        position:absolute;
        font-size:15px;
        font-weight:300;
    }
    .text_left2
    {
        position:absolute;
        font-size:15px;
    }
    .text_right2
    {
        position:absolute;
        font-size:15px;
    }
    #markingInfo_radio_group
    {
        position:absolute;
        font-size:15px;
        left:420px;
        top:697px
    }
    #fashion_choice
    {
        position:absolute;
        font-size:15px;
        left:420px;
        top:737px;
    }
    #submit_button
    {
        position:absolute;
        font-size:15px;
        left:420px;
        top:790px;
    }
    #change_memo
    {
        position:absolute;
        background:url(../../assets/chage_memo.jpg);
        height:15px;
        width:15px;
        left:350px;
        top:180px;
    }
</style>
