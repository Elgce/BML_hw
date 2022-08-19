<template>
    <el-header>
        <Breadcrumb></Breadcrumb>
    </el-header>
    <el-divider />
    <div class="item_heading" id="new_info">创建信息</div>
    <p class="text_left1" style="left:240px;top:170px">数据集ID</p>
    <p class="text_left1" style="left:240px;top:210px">备注</p>
    <button id="change_memo" @click="changing_memo"></button>
    <input id="memo_input" type="text">
    <div id="two_btns">
        <el-button id="memo_acknowlege" @click="acknowleging_memo">确认</el-button>
        <el-button id="memo_cancel" @click="canceling_memo">取消</el-button>
    </div>
    <p class="text_left1" style="left:240px;top:250px">历史数据</p>
    <p class="text_left2" style="left:350px;top:171px" id="data_id">123456</p>
    <p class="text_left2" style="left:350px;top:250px">暂无导入记录</p>
    <p class="text_right2" style="left:600px;top:170px">版本号</p>
    <p class="text_right2" style="left:690px;top:171px">V1</p>
    <p class="item_heading" id="mark_info">标注信息</p>
    <p class="text_left1" style="left:240px;top:340px">标注类型</p>
    <p class="text_left1" style="left:240px;top:380px">数据总量</p>
    <p class="text_left1" style="left:240px;top:420px">标签个数</p>
    <p class="text_left1" style="left:240px;top:460px">大小</p>
    <p class="text_left2" style="left:350px;top:340px" id="label_type">图像分类</p>
    <p class="text_left2" style="left:350px;top:381px">0</p>
    <p class="text_left2" style="left:350px;top:421px">0</p>
    <p class="text_left2" style="left:350px;top:461px">0M</p>
    <p class="text_right1" style="left:600px;top:343px">标注模块</p>
    <p class="text_right1" style="left:600px;top:383px">已标注</p>
    <p class="text_right1" style="left:600px;top:423px">待确认</p>
    <p class="text_right2" style="left:690px;top:344px" id="label_module">单图单标签</p>
    <p class="text_right2" style="left:690px;top:385px">0</p>
    <p class="text_right2" style="left:690px;top:425px">0</p>
    <p class="item_heading" id="data_cle">数据清洗</p>
    <p class="text_left1" style="left:240px;top:550px">暂未做过数据清洗任务</p>
    <p class="item_heading" id="data_enhan">数据增强</p>
    <p class="text_left1" style="left:240px;top:640px">暂未做过数据增强任务</p>
    <p class="item_heading" id="data_intro">导入数据</p>
    <p class="text_left1" style="left:240px;top:810px" id="upload_pic">上传图片</p>
    <p class="text_left1" style="left:240px;top:730px">数据标注状态</p>
    <form id="markingInfo_radio_group">
        <input type="radio" value="no_marking_info" name="marking_info">无标注信息&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="radio" value="_marking_info" name="marking_info">有标注信息
    </form>
    <p class="text_left1" style="left:240px;top:770px">导入方式</p>
    <select id="fashion_choice" @change="select_change">
        <option value="" disabled selected hidden>请选择</option>
        <option value="local">本地导入</option>
        <option>BOS目录导入</option>
        <option>分享链接导入</option>
        <option>平台已有数据集</option>
        <option id="camera_data">摄像头采集数据</option>
        <option id="cloud_data">云服务回流数据</option>
    </select>
    <select id="local_choice" @change="local_select_change">
        <option value="" disabled selected hidden>请选择</option>
        <option id="excel" hidden>上传Excel文件</option>
        <option value="pic" id="txt">上传TXT文本</option>
        <option>上传压缩包</option>
        <option>API导入</option>
    </select>
    <!-- written by bqw -->
    <el-button id="uploader" type="primary" @click="call_diagram"><el-icon><Upload /></el-icon>上传图片</el-button>
    <el-dialog
        title="上传图片"
        v-model="dialogVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert id="explanation_p" title="对同一数据集存在多个内容完全一致的图片，将会做去重处
        理。<br>为保证模型训练效果，所上传的图片应与实际业务场景的图片（光线、角度、采集设备）尽可能
        一致。" type="warning" :closable="false"></el-alert>
        <el-upload
            class="upload-demo"
            drag
            action="/api/call"
            multiple
        >
         
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
            Drop file here or <em>click to upload</em>
            </div>
            <template #tip>
            <div class="el-upload__tip">
                files with a size less than 500kb
            </div>
            </template>
        </el-upload>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="dialogVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>
    <!-- written over -->

    <el-button id="submit_button" @click="back_index">确认并返回</el-button>
</template>

<script>
import { reactive } from "vue";
import Breadcrumb from "../BreadCrumb.vue"
    export default{
        name: "MainTwo",
        components: {
            Breadcrumb,
        },
        data(){
            return{
                dialogVisible: false,
                fileList: [],
                file: {},
                MessageInfo: reactive({}),
            };
        },
        created(){
            this.get_data();
        },
        methods:{
            //written by bqw
            get_data(){
                let that = this;
                return fetch("/api/getone").then((res) => res.json())
                .then((j)=>{
                    console.log(j.data);
                    that.MessageInfo = j.data;
                    let data_id = document.getElementById("data_id");
                    data_id.innerHTML = that.MessageInfo["data_id"];
                    let label_type = document.getElementById("label_type");
                    var camera_data=document.getElementById("camera_data");
                    var cloud_data=document.getElementById("cloud_data");
                    var excel=document.getElementById("excel");
                    var txt=document.getElementById("txt");
                    var upload_pic=document.getElementById("upload_pic");
                    var uploader=document.getElementById("uploader");
                    if(that.MessageInfo["specy"]==="pic"){
                        label_type.innerHTML = "图像分类";
                        txt.innerHTML = "上传图片";
                    }
                    else if(that.MessageInfo["specy"]==="txt"){
                        label_type.innerHTML = "文本分类";
                        cloud_data.hidden=true;
                        camera_data.hidden=true;
                        excel.hidden=false;
                        upload_pic.innerHTML = "上传TXT文本";
                        uploader.innerHTML = "上传TXT文本";
                    }
                    else if(that.MessageInfo["specy"]==="table"){
                        label_type.innerHTML = "表格分类";
                    }
                    let label_module = document.getElementById("label_module");
                    if(that.MessageInfo["label_model"]==="ss"){
                        label_module.innerHTML = "单图单标签";
                    }
                    else if(that.MessageInfo["label_model"]==="sm"){
                        label_module.innerHTML = "单图多标签";
                    }
                    else if(that.MessageInfo["label_model"]==="rec"){
                        label_module.innerHTML = "矩形框标注";
                    }
                    else if(that.MessageInfo["label_model"]==="insdiv"){
                        label_module.innerHTML = "实例分割";
                    }
                    else if(that.MessageInfo["label_model"]==="meandiv"){
                        label_module.innerHTML = "语义分割";
                    }
                    else if(that.MessageInfo["label_model"]==="recog"){
                        label_module.innerHTML = "非结构化文字识别";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_slabel"){
                        label_module.innerHTML = "短文本单标签";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_mlabel"){
                        label_module.innerHTML = "短文本多标签"
                    }
                    else if(that.MessageInfo["label_model"]==="txt_sim"){
                        label_module.innerHTML = "短文本相似度";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_iob"){
                        label_module.innerHTML = "IOB标注模式";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_io"){
                        label_module.innerHTML = "IO标注模式";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_ioe"){
                        label_module.innerHTML = "IOE标注模式";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_iobes"){
                        label_module.innerHTML = "IOBES标注模式";
                    }
                    else if(that.MessageInfo["label_model"]==="txt_extr"){
                        label_module.innerHTML = "文本实体抽取";
                    }
                })
            },
            back_index(){
                return fetch("/api/clearsession").then((res) => res.json()).then(()=>{
                    this.$router.push("/index/manage/dataset");
                })
            },
            call_diagram(){
                this.dialogVisible = true;
            },
            //written over

            //written by wjz
            changing_memo()
            {
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='hidden';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='visible';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='visible';
            },
            acknowleging_memo()
            {
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='visible';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='hidden';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='hidden';
            },
            canceling_memo()
            {
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='visible';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='hidden';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='hidden';
            },
            select_change()
            {
                var select_fashion=document.getElementById("fashion_choice");
                var select_local=document.getElementById("local_choice");
                var upPic=document.getElementById("upload_pic");
                var submit_btn=document.getElementById("submit_button");
                var up_loader = document.getElementById("uploader");
                if(select_fashion.value=="local")
                {
                    select_local.style.visibility='visible';
                    this.local_select_change();
                }
                else
                {
                    select_local.style.visibility='hidden';
                    upPic.style.visibility='hidden';
                    submit_btn.style.top='830px';
                    up_loader.style.visibility='hidden';
                }
            },
            local_select_change()
            {
                var upPic=document.getElementById("upload_pic");
                var select_local=document.getElementById("local_choice");
                var submit_btn=document.getElementById("submit_button");
                var up_loader = document.getElementById("uploader");
                if(select_local.value=="pic")
                {
                    upPic.style.visibility='visible';
                    up_loader.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else
                {
                    upPic.style.visibility='hidden';
                    up_loader.style.visibility='hidden';
                    submit_btn.style.top='830px';
                }
            }
        }
    }

</script>

<style scoped>
    .el-header  
    {
        height: 56px;
    }
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
        top:140px;
    }
    #mark_info
    {
        left:230px;
        top:300px;
    }
    #data_cle
    {
        left:230px;
        top:510px;
    }
    #data_enhan
    {
        left:230px;
        top:600px;
    }
    #data_intro
    {
        left:230px;
        top:690px;
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
    .el-divider
    {
        position:absolute;
        top:92px;
        left:200px;
    }
    #markingInfo_radio_group
    {
        position:absolute;
        font-size:15px;
        left:420px;
        top:747px
    }
    #fashion_choice
    {
        position:absolute;
        font-size:15px;
        left:420px;
        width:200px;
        top:787px;
    }
    #local_choice
    {
        position:absolute;
        font-size:15px;
        left:620px;
        top:787px;
        visibility: hidden;
    }
    #uploader{
        position: absolute;
        left: 420px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #submit_button
    {
        position:absolute;
        font-size:15px;
        left:420px;
        top:830px;
    }
    #change_memo
    {
        position:absolute;
        background:url(../../assets/chage_memo.jpg);
        height:15px;
        width:15px;
        left:350px;
        top:230px;
        border-style:none;
    }
    #memo_input
    {
        height:15px;
        width:200px;
        position:absolute;
        top:230px;
        left:350px;
        visibility:hidden;
    }
    #memo_acknowlege
    {
        position:absolute;
        border-style:none;
        height:19px;
        width:50px;
        left:0px;
    }
    #memo_cancel
    {
        position:absolute;
        border-style:none;
        height:19px;
        width:50px;
        right:0px;
    }
    #two_btns
    {
        position:absolute;
        top:230px;
        left:558px;
        font-size:12px;
        height:19px;
        width:100px;
        border-style:solid;
        border-width:1px;
        visibility:hidden;
    }
    #upload_pic
    {
        visibility: hidden;
    }
    #divider_dialog
    {
        position: absolute;
        left:0px;
        top:40px;
    }
    #explanation_p
    {
        background-color: bisque;
        color: orange;
    }
</style>
