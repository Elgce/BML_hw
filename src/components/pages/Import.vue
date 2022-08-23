<template>
    <!-- 头部元素 -->
    <el-header>
        <Breadcrumb></Breadcrumb>
    </el-header>
    <el-divider />

    <!-- 数据集信息 -->
    <div class="item_heading" id="new_info">创建信息</div>
    <p class="text_left1" style="left:240px;top:170px">数据集ID</p>
    <p class="text_left1" style="left:240px;top:210px">备注</p>
    <el-row id="memo_row">
        <p id="memo_info" class="text_left1">{{memo_text}}</p>
        <button id="change_memo" @click="changing_memo"></button>
    </el-row>
    <input id="memo_input" type="text" v-model="memo_text">
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

    <!-- 导入部分 -->
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
        <option value="excel" id="excel" hidden>上传Excel文件</option>
        <option value="pic" id="txt">上传TXT文本</option>
        <option value="zip" id="zip">上传压缩包</option>
        <option>API导入</option>
    </select>
    <el-button id="uploader_pic" type="primary" @click="call_diagram_pic"><el-icon><Upload /></el-icon>上传图片</el-button>
    <el-button id="uploader_zip" type="primary" @click="call_diagram_zip"><el-icon><Upload /></el-icon>上传压缩包</el-button>
    <el-button id="uploader_txt" type="primary" @click="call_diagram_txt"><el-icon><Upload /></el-icon>上传TXT文本</el-button>
    <el-button id="uploader_excel" type="primary" @click="call_diagram_excel"><el-icon><Upload /></el-icon>上传Excel文件</el-button>
    <el-button id="uploader_video" type="primary" @click="call_diagram_video"><el-icon><Upload /></el-icon>上传视频文件</el-button>
    <el-button id="uploader_audio" type="primary" @click="call_diagram_audio"><el-icon><Upload /></el-icon>上传音频文件</el-button>
    
    <!-- 分隔符选择问题 -->
    <p class="text_left1" style="left:240px;top:810px" id="split_text">分隔符</p>
    <el-radio-group v-model="split_word" id="split_group" @change="split_change">
        <el-radio label="gn" size="large">换行符</el-radio>
        <el-radio label="dh" size="large">半角逗号</el-radio>
        <el-radio label="zbf" size="large">制表符</el-radio>
        <el-radio label="kg" size="large">空格</el-radio>
        <el-radio label="file" size="large">无</el-radio>
    </el-radio-group>
    

    <!-- 上传图片对话框 -->
    <el-dialog
        title="上传图片"
        v-model="picUpVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert 
            id="explanation_p" 
            title="对同一数据集存在多个内容完全一致的图片，将会做去重处理。为保证模型训练效果，所上传的图片应与实际业务场景的图片（光线、角度、采集设备）尽可能一致。" 
            type="warning" 
            :closable="false">
        </el-alert>
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
                <el-button @click="picUpVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="picUpVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <!-- 上传压缩包对话框 -->
    <el-dialog
        title="上传压缩包"
        v-model="picUpZipVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert 
            id="explanation_p" 
            title="对压缩包内存在多个内容完全一致的图片，将会做去重处理。为保证模型训练效果，所上传的图片应与实际业务场景的图片（光线、角度、采集设备）尽可能一致。" 
            type="warning" 
            :closable="false">
        </el-alert>
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
                <el-button @click="picUpZipVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="picUpZipVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>
    <el-dialog
        title="上传压缩包"
        v-model="textUpZipVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert 
            id="explanation_p" 
            title="1. 压缩包内的一个文本文件将作为一个样本上传，详见示例压缩包。2. 压缩包格式为zip,tar.gz格式，压缩包内文件类型支持txt，编码仅支持UTF-8" 
            type="warning" 
            :closable="false">
        </el-alert>
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
                <el-button @click="textUpZipVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="textUpZipVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <!-- 上传TXT对话框 -->
    <el-dialog
        title="上传TXT文本"
        v-model="textUpTxtVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert 
            id="explanation_p" 
            title="1. 文本将会按照您定义的分隔符拆分成多组数据，每组数据的字符数建议不超过512个字符（包括中英文、数字、符号等），超出的字符可正常保存，但可能无法参与训练。详见数据样例。2. 请确保您的数据格式准确，如果上传一个文本文件作为一个样本，请返回到导入方式上选择“上传压缩包”的方式上传数据。3. 文本文件类型支持txt，编码仅支持UTF-8，单次上传限制100个文本文件" 
            type="warning" 
            :closable="false">
        </el-alert>
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
                <el-button @click="textUpTxtVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="textUpTxtVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <!-- 上传Excel对话框 -->
    <el-dialog
        title="上传Excel文件"
        v-model="textUpExcelVisible"
    >
        <el-divider id="divider_dialog"/>
        <el-alert 
            id="explanation_p" 
            title="1. 使用第一列作为待标注文本，每行是一组样本，首行为表头默认将被忽略，每组数据文本内容的字符数不超过512个字符（包括中英文、数字、符号等），超出的字符可正常保存，但可能无法参与训练。详见数据样例。2. 文件类型支持xlsx格式，单次上传限制100个文件；文件格式示意图如下：" 
            type="warning" 
            :closable="false">
        </el-alert>
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
                <el-button @click="textUpExcelVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="textUpExcelVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <!-- 上传视频对话框 -->
    <el-dialog
        title="上传视频文件"
        v-model="videoUpVisible"
    >
        <el-divider id="divider_dialog"/>
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
                <el-button @click="videoUpVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="videoUpVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>
    <el-dialog
        title="上传压缩包"
        v-model="videoUpZipVisible"
    >
        <el-divider id="divider_dialog"/>
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
                <el-button @click="videoUpZipVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="videoUpZipVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <!-- 上传音频对话框 -->
    <el-dialog
        title="上传音频文件"
        v-model="audioUpVisible"
    >
        <el-divider id="divider_dialog"/>
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
                <el-button @click="audioUpVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="audioUpVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>
    <el-dialog
        title="上传压缩包"
        v-model="audioUpZipVisible"
    >
        <el-divider id="divider_dialog"/>
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
                <el-button @click="audioUpZipVisible=false">取消</el-button>
                <el-button id="push_file" type="primary" @click="audioUpZipVisible=false">确定</el-button>
            </span>
        </template>
    </el-dialog>

    <el-button id="submit_button" @click="back_index">确认并返回</el-button>
</template>

<script>
import { reactive, ref } from "vue";
import Breadcrumb from "../BreadCrumb.vue"
    export default{
        name: "MainTwo",
        components: {
            Breadcrumb,
        },
        data(){
            return{
                picUpVisible: false,
                picUpZipVisible:false,
                textUpZipVisible:false,
                textUpTxtVisible:false,
                textUpExcelVisible:false,
                videoUpVisible:false,
                videoUpZipVisible:false,
                audioUpVisible:false,
                audioUpZipVisible:false,
                fileList: [],
                file: {},
                MessageInfo: reactive({}),
                memo_text:ref(''),
                split_word:ref('')
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
                    }
                    else if(that.MessageInfo["specy"]==="table"){
                        label_type.innerHTML = "表格分类";
                    }
                    else if(that.MessageInfo["specy"]==="video"){
                        label_type.innerHTML = "视频分类"
                        txt.innerHTML = "上传视频文件";
                    }
                    else if(that.MessageInfo["specy"]==="audio"){
                        label_type.innerHTML = "音频分类"
                        txt.innerHTML = "上传音频文件";
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
                    else if(that.MessageInfo["direction"]==="vid_ass"){
                        label_module.innerHTML = "视频分类";
                    }
                    else if(that.MessageInfo["direction"]==="vid_spl"){
                        label_module.innerHTML = "视频分割";
                    }
                    else if(that.MessageInfo["direction"]==="aud_ass"){
                        label_module.innerHTML = "音频分类";
                    }
                    else if(that.MessageInfo["direction"]==="aud_spl"){
                        label_module.innerHTML = "音频分割";
                    }
                    
                })
            },
            back_index(){
                return fetch("/api/clearsession").then((res) => res.json()).then(()=>{
                    this.$router.push("/index/manage/dataset");
                })
            },
            call_diagram_pic(){
                this.picUpVisible = true;
            },
            call_diagram_zip()
            {
                if(this.MessageInfo["specy"]=="pic")
                {
                    this.picUpZipVisible=true;
                }
                else if(this.MessageInfo["specy"]=="txt")
                {
                    this.textUpZipVisible=true;
                }
                else if(this.MessageInfo["specy"]=="video")
                {
                    this.videoUpZipVisible=true;
                }
                else if(this.MessageInfo["specy"]=="audio")
                {
                    this.audioUpZipVisible=true;
                }
            },
            call_diagram_txt()
            {
                this.textUpTxtVisible=true;
            },
            call_diagram_excel()
            {
                this.textUpExcelVisible=true;
            },
            call_diagram_video()
            {
                this.videoUpVisible=true;
            },
            call_diagram_audio()
            {
                this.audioUpVisible=true;
            },
            //written over

            //改变分隔符
            split_change()
            {
                const data = {
                    "txt_type": this.split_word,
                };
                return fetch("/api/settxttype",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    console.log(j);
                })
            },

            //改变备注
            changing_memo()
            {
                var change_memo_text=document.getElementById("memo_info");
                change_memo_text.style.visibility='hidden';
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='hidden';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='visible';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='visible';
            },

            //确认修改备注
            acknowleging_memo()
            {
                var change_memo_text=document.getElementById("memo_info");
                change_memo_text.style.visibility='visible';
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='visible';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='hidden';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='hidden';
            },

            //取消修改备注
            canceling_memo()
            {
                var change_memo_text=document.getElementById("memo_info");
                change_memo_text.style.visibility='visible';
                var change_memo_btn=document.getElementById("change_memo");
                change_memo_btn.style.visibility='visible';
                var change_memo_input=document.getElementById("memo_input");
                change_memo_input.style.visibility='hidden';
                var two_btns=document.getElementById("two_btns");
                two_btns.style.visibility='hidden';
            },

            //多选框改变
            select_change()
            {
                var select_fashion=document.getElementById("fashion_choice");
                var select_local=document.getElementById("local_choice");
                var upPic=document.getElementById("upload_pic");
                var submit_btn=document.getElementById("submit_button");
                var up_loader_pic = document.getElementById("uploader_pic");
                var up_loader_zip = document.getElementById("uploader_zip");
                var up_loader_txt = document.getElementById("uploader_txt");
                var up_loader_excel = document.getElementById("uploader_excel");
                var up_loader_video = document.getElementById("uploader_video");
                var up_loader_audio = document.getElementById("uploader_audio");
                var split_group = document.getElementById("split_group");
                var split_text = document.getElementById("split_text");
                if(select_fashion.value=="local"){
                    select_local.style.visibility='visible';
                    this.local_select_change();
                }
                else{
                    select_local.style.visibility='hidden';
                    upPic.style.visibility='hidden';
                    submit_btn.style.top='830px';
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    split_group.style.visibility='hidden';
                    split_text.style.visibility='hidden';
                }
            },
            local_select_change()
            {
                var upPic=document.getElementById("upload_pic");
                var select_local=document.getElementById("local_choice");
                var submit_btn=document.getElementById("submit_button");
                var up_loader_pic = document.getElementById("uploader_pic");
                var up_loader_zip = document.getElementById("uploader_zip");
                var up_loader_txt = document.getElementById("uploader_txt");
                var up_loader_excel = document.getElementById("uploader_excel");
                var up_loader_video = document.getElementById("uploader_video");
                var up_loader_audio = document.getElementById("uploader_audio");
                var split_group = document.getElementById("split_group");
                var split_text = document.getElementById("split_text");
                if(select_local.value=="pic" && this.MessageInfo["specy"]=="pic")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    up_loader_pic.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="zip" && this.MessageInfo["specy"]=="pic")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传压缩包";
                    up_loader_zip.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="zip" && this.MessageInfo["specy"]=="txt")
                {
                    upPic.style.top='810px';
                    up_loader_txt.style.top='820px';
                    split_group.style.visibility='hidden';
                    split_text.style.visibility='hidden';
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传压缩包";
                    up_loader_zip.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="pic" && this.MessageInfo["specy"]=="txt")
                {
                    split_group.style.visibility='visible';
                    split_text.style.visibility='visible';
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传TXT文本";
                    upPic.style.top='850px';
                    up_loader_txt.style.top='860px';
                    up_loader_txt.style.visibility='visible';
                    submit_btn.style.top='910px';
                }
                else if(select_local.value=="excel" && this.MessageInfo["specy"]=="txt")
                {
                    upPic.style.top='810px';
                    up_loader_txt.style.top='820px';
                    split_group.style.visibility='hidden';
                    split_text.style.visibility='hidden';
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传Excel文件";
                    up_loader_excel.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="pic" && this.MessageInfo["specy"]=="video")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传视频文件";
                    up_loader_video.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="zip" && this.MessageInfo["specy"]=="video")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传压缩包";
                    up_loader_zip.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="pic" && this.MessageInfo["specy"]=="audio")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传音频文件";
                    up_loader_audio.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else if(select_local.value=="zip" && this.MessageInfo["specy"]=="audio")
                {
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    upPic.style.visibility='visible';
                    upPic.innerText="上传压缩包";
                    up_loader_zip.style.visibility='visible';
                    submit_btn.style.top='870px';
                }
                else
                {
                    upPic.style.visibility='hidden';
                    up_loader_pic.style.visibility='hidden';
                    up_loader_zip.style.visibility='hidden';
                    up_loader_txt.style.visibility='hidden';
                    up_loader_excel.style.visibility='hidden';
                    up_loader_video.style.visibility='hidden';
                    up_loader_audio.style.visibility='hidden';
                    submit_btn.style.top='830px';
                    split_group.style.visibility='hidden';
                    split_text.style.visibility='hidden';
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
    #uploader_pic
    {
        position: absolute;
        left: 420px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #uploader_zip
    {
        position: absolute;
        left: 409px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #uploader_txt
    {
        position: absolute;
        left: 409px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #uploader_excel
    {
        position: absolute;
        left: 409px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #uploader_video
    {
        position: absolute;
        left: 409px;
        font-size: 15px;
        top:820px;
        visibility: hidden;
    }
    #uploader_audio
    {
        position: absolute;
        left: 409px;
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
    #memo_row
    {
        position:absolute;
        left:370px;
        top:213px;
        border-style:none;
    }
    #change_memo
    {
        float: left;
        background:url(../../assets/chage_memo.jpg);
        height:15px;
        width:15px;
        margin-left:-20px;
        margin-top: 16px;
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
    #split_text
    {
        visibility:hidden;
    }
    #split_group
    {
        position: absolute;
        top:817px;
        left: 420px;
        visibility: hidden;
    }
</style>
