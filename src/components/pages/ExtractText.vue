<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-row id="top_btns">
            <el-select v-model="value" class="m-2" placeholder="Select" id="select_data">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                />
            </el-select>
            <el-button id="ai_marking" type="success" plain>开启智能标注</el-button>
            </el-row>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-row id="middle_btns">
                <el-radio-group v-model="t_type" size="large" @change="handleradiochange">
                                <el-radio-button label="all">全部({{all_num}})</el-radio-button>
                                <el-radio-button label="ed" >有标注信息({{ed_num}})</el-radio-button>
                                <el-radio-button label="to" >没有标注信息({{to_num}})</el-radio-button>
                </el-radio-group>
                <div id="link">
                    <el-link type="primary" @click="dialogVisible = true">批注示例</el-link>
                </div>
            </el-row>
            <el-divider/>
            
            <el-container id="middle_data">
                <el-aside id="middle_asider">
                    <el-scrollbar height="500px">
                        <el-row id="text_top">
                            <!-- <p id="_mark">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;标签：</p>
                            <p id="_mark_strong">{{this_tag}}</p> -->
                            <div id="content_search">
                            <el-input type="text" v-model="input_text" class="w-50 m-2" placeholder="定位文本内容">
                            <template #prefix>
                                <el-icon class="el-input__icon"><search /></el-icon>
                            </template>
                        </el-input>
                        </div>
                            <el-popover
                                placement="bottom"
                                :width="200"
                                trigger="hover"
                            >
                                <template #reference>
                                    <el-button text id="previous" @click="previous_txt">上一篇</el-button>
                                </template>
                                <p>上一篇（翻页即保存）<el-icon><ArrowLeftBold /></el-icon></p>
                            </el-popover>
                            &nbsp;&nbsp;&nbsp;
                            <el-popover
                                placement="bottom"
                                :width="200"
                                trigger="hover"
                            >
                                <template #reference>
                                    <el-button text id="latter" @click="latter_txt">下一篇</el-button>
                                </template>
                                <p>下一篇（翻页即保存）<el-icon><ArrowRightBold /></el-icon></p>
                            </el-popover>
                        </el-row>
                        <p id="written" @click="checkChoice">
                            {{show_context}}
                        </p>
                        <div id="empty_right" v-if="all_num===0">
                            暂无可用数据
                        </div>
                    </el-scrollbar>
                </el-aside>
                <el-container>
                    <el-header id="middle_header">
                        <b v-if="show_btn===false" id="tag_column_text">标签栏</b>
                        <el-button v-if="show_btn===false" id="add_tag" @click="create_label">添加标签</el-button>
                        <el-input  v-if="show_btn===true" id="label_name" v-model="labelname" placeholder="请输入标签名字" style="margin-left:-20px;margin-top:18px;width: 240px;"/>
                        <el-button v-if="show_btn===true" type="primary" @click="add_label" link style="margin-left:5px;" >确定</el-button>
                        <el-button v-if="show_btn===true" type="info" @click="cancel_label" link style="margin-left:-2px;">取消</el-button>
                        <el-popover
                            placement="bottom-end"
                            :width="20"
                            trigger="hover"
                            v-if="show_btn===false"
                        >
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <el-button id="add_tagGroup">添加标签组</el-button>
                            <template #reference>
                                <el-button id="more_settings">···</el-button>
                            </template>
                        </el-popover>
                    </el-header>
                    <el-header id="middle_main">
                        <br>              
                        <el-input type="text" v-model="input_tagName" class="w-50 m-2" placeholder="请输入标签名称" @change="searchlabel">
                            <template #prefix>
                                <el-icon class="el-input__icon"><search /></el-icon>
                            </template>
                        </el-input>
                        <span id="tag_search_text">根据文本内容，选择唯一标签</span>
                    </el-header>
                    <el-footer id="middle_footer">
                        <el-scrollbar height="400px">
                            <div v-for="item in Label_info" :key="item" class="scrollbar-demo-item">
                                <el-card shadow="hover" class="card">
                                    <div class="card_info">
                                        <el-button type="primary" text class="card_edit" @click="edit_label(item)">编辑</el-button>
                                        <el-button type="info" text class="card_delete" @click="delete_label(item)">删除</el-button>
                                        <p class="card_name" style="visibility:visible">{{item}}</p>
                                        <el-input type="text" id="new_name_txt" style="width:120px;visibility:hidden;" class="edit_txt" v-model="new_labelname" @change="change_name(item)"></el-input>
                                        <el-button type="success" text @click="mark_text(item)">选择</el-button>
                                    </div>
                                </el-card>
                            </div>
                        </el-scrollbar>


                        <div id="empty_img_left" v-if="label_num===0"></div>
                        <span id="empty_text_left" v-if="label_num===0">暂无可用标签 ，请点击上方按钮添加</span>
                    </el-footer>
                </el-container>
                
            </el-container>
        </el-main>
    </el-container>
    <el-dialog
        v-model="dialogVisible"
        title="文本分类-单标签"
        width="40%"
        :before-close="handleClose"
    >
        <el-divider id="dialog_divider"/>
        <p>1. 如何标注: 在左侧选择唯一标签即可完成标注，切换文件可完成保存。</p>
        <p>2. 标注技巧: 对于批量文本需要标注为同一个标签的情况，可以在右侧标签区域将标签置顶。</p>
        <br>
        <img src="../../assets/text_marking_description.png" width="500" height="202">
    </el-dialog>
    <div 
        id="choose_label"
    >
        <p id="choose_label_text">
            请选择文本实体分类标签：
        </p>
        <el-divider id="choose_label_divider"/>
        <!-- <el-card shadow="hover" class="card">
            <el-button class="labels_choice" style="visibility:visible">{{item}}</el-button>
        </el-card> -->
        <el-color-picker v-model="markColor" id="mark_color"/>
        <div v-for="item in Label_info" :key="item" >
            <el-button class="labels_choice" @click="mark_text(item)">
            {{item}}
            </el-button>
        </div>
    </div>
</template>

<script>
import Breadcrumb from "../BreadCrumb.vue"
import { reactive, ref } from "vue"
    export default
    {
        name: "MainThree",
        components: 
        {
            Breadcrumb,
        },
        data()
        {
            return{
                context: reactive([]),
                all_num: -1,
                ed_num: -1,
                to_num: -1,
                t_type: ref("all"),
                name : ref(''),
                page : -1,
                show_context: ref(''),
                this_tag: ref('请在右侧选择标签'),
                input_text:ref(''),
                start_end: reactive([]),
                context_tag: reactive([]),

                labelname: ref(''),
                new_labelname: ref(''),
                Label_info:reactive([]),
                sources: reactive([]),
                show_btn: false,
                dialogVisible:false,
                radio1:'全部',
                visible:false,
                unlimited1:true,
                unlimited2:true,
                unlimited3:true,
                unlimited4:true,
                source1:false,
                source2:false,
                source3:false,
                source4:false,
                source5:false,
                input_tagName:ref(''),
                intr_date:ref(''),
                marking_date:ref(''),
                options:[
                    
                ],
                markColor:ref('#FFCC22'),
            };
        },
        created(){
            this.calltxt().then(this.get_labels()).then(this.callpage());
            
        },
        methods:{
        //  written by bqw
            handleradiochange(){
                console.log(this.t_type);
                const data = {"t_type": this.t_type};
                return fetch("/api/sessiontype",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then((res)=>res.json())
                .then(()=>{
                    this.$router.push("/index/manage/dataset/txt/extracted/blank");
                })
            },
            
            latter_txt(){
                return fetch("/api/nextpage").then((res)=>res.json().then((j)=>{
                    let passa = j.page;
                    if(passa==="fail"){
                        alert("已是最后一页!");
                    }
                    else{
                        this.$router.push("/index/manage/dataset/txt/extracted/blank");
                    }
                }))
            },
            previous_txt(){
                return fetch("/api/prepage").then((res)=>res.json().then((j)=>{
                    let passa = j.page;
                    if(passa==="fail"){
                        alert("已是第一页!");
                    }
                    else{
                        this.$router.push("/index/manage/dataset/txt/extracted/blank");
                    }
                }))
            },
            callpage(){
                let that = this;
                return fetch("/api/txtgetpage").then((res)=>res.json().then((j)=>{
                    that.page = j.page;
                    let page = parseInt(that.page) - 1;
                    if(that.context_tag[page]==""){
                        that.show_context = that.context[page];
                    }
                    else{
                        console.log(that.context_tag[page])
                        let writter = document.getElementById("written");
                        writter.innerHTML = that.context_tag[page];
                    }
                    
                }))
            },
            calltxt(){
                let that = this;
                return fetch("/api/gettxtextracted").then((res) => res.json().then((j) => {
                    that.context = j.context;
                    that.context_tag = j.context_tag;
                    that.all_num = j.all_num;
                    that.name = j.name;
                    that.to_num = j.to_num;
                    that.ed_num = j.ed_num;
                    that.t_type = j.t_type;
                }))
            },
            searchlabel(){
                let data = {"tagname":this.input_tagName};
                let that = this;
                return fetch("/api/searchtagname",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    // that.Label_info = j.labels;
                    that.Label_info = reactive([]);
                    if(j.label_num!=0){
                        for(let item in j.labels){
                            that.Label_info.push(j.labels[item]);
                        }
                    }
                    else{
                        alert("没有此名称的标签!");
                    }
                    console.log(that.Label_info);
                    that.label_num = j.label_num;
                })
            },
            change_name(name){
                let new_name= this.new_labelname;
                this.delete_label(name);
                const data = {"name": new_name};
                return fetch("/api/addlabel",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res=>res.json())
                .then((j)=>{
                    console.log(j);
                    this.$router.push("/index/manage/dataset/txt/extracted/blank");
                })
            },
            edit_label(name){
                console.log(name);
                let std = document.getElementById("new_name_txt");
                if(std.style.visibility==='hidden'){
                    std.style.visibility='visible';
                    std.style.backgroundColor="rgb(221, 218, 218)";
                }
                else{
                    std.style.visibility='hidden';
                }
            },
            delete_label(name){
                const data = {"label_name": name};
                return fetch("/api/deletelabel",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then((res)=>res.json()
                .then(()=>{
                    this.$router.push("/index/manage/dataset/txt/extracted/blank");
                }))
            },

           
            add_label(){
                const data = {"name": this.labelname};
                return fetch("/api/addlabel",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res=>res.json())
                .then((j)=>{
                    console.log(j);
                    this.$router.push("/index/manage/dataset/txt/extracted/blank");
                })
            },
           
            get_labels(){
                let that = this;
                return fetch("/api/getlabels").then((res) => res.json().then((j)=>{
                    that.label_num = j.label_num;
                    that.Label_info = j.labels;
                }))
            },
            create_label(){
                this.show_btn = true;
            },
            cancel_label(){
                this.show_btn = false;
            },
            //written over


            checkChoice()
            {
                var selection=window.getSelection();
                var selectionStr=selection.toString();
                if(selectionStr!="")
                {
                    var choose_label=document.getElementById("choose_label");
                    choose_label.style.visibility='visible';
                    var e = window.event;
                    var scrollx = document.documentElement.scrollLeft || document.body.scrollTop;
                    var scrolly= document.documentElement.scrollTop || document.body.scrollTop;
                    var x = e.pageX || e.clientX + scrollx;
                    var y = e.pageY || e.clientY + scrolly;
                    x+=20;
                    y+=20;
                    choose_label.style.top=String(y)+'px';
                    choose_label.style.left=String(x)+'px';
                }
            },
            cleanSource()
            {
                if(this.unlimited1==true)
                {
                    this.source1=false;
                    this.source2=false;
                    this.source3=false;
                    this.source4=false;
                    this.source5=false;
                }
            },
            checkSource()
            {
                var source=document.getElementsByName("source");
                if(this.unlimited1==true)
                {
                    if(source[0].checked||source[1].checked||source[2].checked||source[3].checked||source[4].checked)
                    {
                        this.unlimited1=false;
                    }
                }
                else
                {
                    if(!(source[0].checked||source[1].checked||source[2].checked||source[3].checked||source[4].checked))
                    {
                        this.unlimited1=true;
                    }
                }
            },
            checkIntrDate()
            {
                if(this.intr_date==null)
                {
                    this.unlimited2=true;
                }
                else
                {
                    this.unlimited2=false;
                }
            },
            cleanIntrDate()
            {
                if(this.unlimited2!=false)
                {
                    this.intr_date=null
                }
            },
            checkMarkingDate()
            {
                if(this.marking_date==null)
                {
                    this.unlimited3=true;
                }
                else
                {
                    this.unlimited3=false;
                }
            },
            cleanMarkingDate()
            {
                if(this.unlimited3!=false)
                {
                    this.marking_date=null
                }
            },
            //written by bqw
            mark_text(item)
            {
                console.log(item)
                var selection=window.getSelection();
                var range = selection.getRangeAt(0);

                var selectionContents = range.extractContents();
                var span = document.createElement("span");
                span.style="text-decoration:underline";
                span.style.color = this.markColor;
                span.appendChild(selectionContents);
                let tag = document.createElement("span");
                tag.style.backgroundColor = this.markColor;
                tag.style.color = "black";
                tag.innerHTML = item;
                span.appendChild(tag); 

                range.insertNode(span);

                let written = document.getElementById("written");
                var choose_label=document.getElementById("choose_label");
                choose_label.style.visibility='hidden';
                let intxt = written.innerHTML;
                console.log(intxt);
                const data = {"intxt": intxt};
                return fetch("/api/sendstyle",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then((res)=>res.json())
                .then(()=>{
                    this.$router.push("/index/manage/dataset/txt/extracted/blank");
                })

            },

            //written over
        }
    }


</script>

<style scoped>
    .el-header 
    {
        height: 56px;
    }
    #top_divider
    {
        position:absolute;
        top:92px;
        left:200px;
    }
    #ai_marking
    {
        margin-left:20px;
    }
    #top_btns
    {
        position: absolute;
        right:30px;
        margin-top: -20px;
    }
    #dialog_divider
    {
        position: absolute;
        top:50px;
        left:0px;
    }
    #link
    {
        position: absolute;
        left:1200px;
        margin-top: 20px;
    }
    #two_btns
    {
        position: absolute;
        right:0px;
    }
    #text_top
    {
        background-color: rgb(243, 244, 243);
    }
    #_mark
    {
        font-size:13px;
    }
    #_mark_strong
    {
        font-weight:700;
        font-size:13px;
    }
    #delete_btn
    {
        border: none;
        background-color: rgb(243, 244, 243);
        margin-top: 5px;
        margin-left:500px;
    }
    #latter{
        margin-left: -10px;
        margin-top: 5px;
    }
    #previous
    {
        margin-left:430px;
        margin-top:5px;
    }
    #middle_btns
    {
        width:1300px;
    }
    #middle_data
    {
        margin-top:20px;
        width:1300px;
        height:500px;
    }
    #middle_header
    {
        border:thin solid rgb(234, 229, 229);
        width:350px;
        height:70px;
    }
    #tag_column_text
    {
        line-height:70px;
    }
    #add_tag
    {
        margin-left:100px;
        background-color: rgb(0, 110, 254);
        color: white;
    }
    #more_settings
    {
        margin-left:0px;
        background-color: rgb(0, 110, 254);
        color: white;
    }
    #add_tagGroup
    {
        border: none;
    }
    #middle_main
    {
        border:thin solid rgb(234, 229, 229);
        width:350px;
        height:80px;
    }
    #middle_footer
    {
        border:thin solid rgb(234, 229, 229);
        width:350px;
        height:350px;
    }
    #middle_asider
    {
        border:thin solid rgb(234, 229, 229);
        width:950px;
        height:500px;
    }
    #tag_search_text
    {
        font-size:12px;
        color:grey;
        font-weight:300;
    }
    #empty_img_left
    {
        background:url(../../assets/empty.png);
        height:170px;
        width:167px;
        margin:auto;
        margin-top: -200px;
    }
    #empty_text_left
    {
        font-size:13px;
        margin-top: -100px;

    }
    .card{
        height: 40px;
    }
    #empty_right
    {
        background:url(../../assets/empty.png) no-repeat;
        height:170px;
        width:290px;
        margin:auto;
        font-size:15px;
        text-align:right;
        line-height:170px;
        margin-top: 100px;
    }
    .scrollbar-demo-item{
        display: flex;
    }
    #fotter_text
    {
        margin-top:0px;
        line-height:30px;
    }
    #fotter_select
    {
        margin-top:0px;
    }
    #fotter_pages
    {
        margin-left:10px;
        margin-top:-12px;
    }
    #pages
    {
        position: absolute;
        right:50px; 
    }
    .card_info{
        display: flex;
        margin-top: -15px;
    }
    .card_name{
        margin-top: 6px;
        margin-left: 5px;
    }
    .card_edit{
        margin-left: -20px;
    }
    .card_delete{
        margin-left: -5px;
    }
    .el-card{
        width: 360px;
    }
    .written{
        font-size: 20px;
        vertical-align: center;
        text-align: center;
    }
    #choose_label
    {
        visibility: hidden;
        position: absolute;
        box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.3); 
    }
    #choose_label_text
    {
        font-weight: 300;
        font-size: 13px;
        line-height: 13px;
    }
    #choose_label_divider
    {
        margin-top: -5px;
    }
    .labels_choice
    {
        font-size: 13px;
        width:120px;
        border: none;
    }
    #content_search
    {
        width:300px;
        margin-left:20px;
        margin-top:2px;
    }
</style>
