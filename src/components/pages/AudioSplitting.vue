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
        <el-main style="overflow:hidden;">
            <!-- <el-row id="middle_btns">
                <el-radio-group v-model="radio1" size="large">
                    <el-radio-button label="全部(0)" />
                    <el-radio-button label="有标注信息(0)" />
                    <el-radio-button label="无标注信息(0)" />
                </el-radio-group>
                <div id="link">
                    <el-link type="primary" @click="dialogVisible = true">批注示例</el-link>
                </div>
            </el-row>
            <el-divider/> -->
            <el-container id="middle_data">
                <el-aside id="middle_asider">
                    <el-main height="500px" style="padding:0px;">
                        <el-row id="text_top">
                            <p id="_mark">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;音频：</p>
                            <p id="_mark_strong">{{sources[0]}}</p>
                            <!-- <el-button id="delete_btn"><el-icon><Delete/></el-icon>&nbsp;删除视频</el-button>
                            <el-popover
                                placement="bottom"
                                :width="200"
                                trigger="hover"
                            >
                                <template #reference>
                                    <el-link id="previous">上一个视频</el-link>
                                </template>
                                <p>上一个视频（翻页即保存）<el-icon><ArrowLeftBold /></el-icon></p>
                            </el-popover>
                            &nbsp;&nbsp;&nbsp;
                            <el-popover
                                placement="bottom"
                                :width="200"
                                trigger="hover"
                            >
                                <template #reference>
                                    <el-link>下一个视频</el-link>
                                </template>
                                <p>下一个视频（翻页即保存）<el-icon><ArrowRightBold /></el-icon></p>
                            </el-popover> -->
                        </el-row>
                        
                        <Audiotag ref="audio"
                            :url = "url"
                            :colorlist = "colorlist"></Audiotag>
                        <div id="empty_right" v-if="src_list.length===0">
                            暂无可用数据
                        </div>
                    </el-main>
                </el-aside>

                <el-container style="height:700px">
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
                            <el-button id="add_tagGroup" @click="addMarkGroup">添加标签组</el-button>
                            <div v-for="item in hasLabel_info" :key="item" >
                                <el-button class="labels_choice" @click="has_add_labels(item)" style="width:150px;">
                                {{item}}
                                </el-button>
                            </div>
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
                            <div v-for="(item,index) in Label_info" :key="item" class="scrollbar-demo-item">
                                <el-card shadow="hover" class="card">
                                    <div class="card_info">
                                        <!-- <el-button type="primary" text class="card_edit" @click="edit_label(item)">编辑</el-button> -->
                                        <el-button type="info" text class="card_delete" @click="delete_label(item)">删除</el-button>
                                        <p :class="'card_name label'+index" :style="getcolor(item)">{{item}}</p>
                                        <!-- <el-input type="text" id="new_name_txt" style="width:120px;visibility:hidden;" class="edit_txt" v-model="new_labelname" @change="change_name(item)"></el-input> -->
                                        <el-button type="defult" text @click="videoLabel(item)">选择</el-button>
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
</template>

<script>
import Breadcrumb from "../BreadCrumb.vue"
import Audiotag from "./AudioTag.vue"

import { reactive, ref } from "vue"

    export default
    {
        name: "MainThree",
        components: 
        {
    Breadcrumb,
    Audiotag,
},
        data()
        {
            return{
                label_num: -1,
                labelname: ref(''),
                new_labelname: ref(''),
                Label_info:reactive([]),
                hasLabel_info: reactive([]),
                src_list:reactive([]),
                sources: reactive([]),
                show_btn: false,
                dialogVisible:false,
                radio1:'全部',
                visible:false,

                input_tagName:ref(''),
                intr_date:ref(''),
                marking_date:ref(''),
                options:[
                    
                ],
                url:ref(''),
                colorlist:{},
            };
        },
        created(){
            this.get_labels();
            this.get_pics().then(this.show_pics);
            console.log(this.url)
        },
        methods:{
        //  written by bqw
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
                    console.log("!!");
                    console.log(j.labels);
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
                const data = {"newname": new_name};
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
                let that = this
                const data = {"label_name": name};
                return fetch("/api/deletelabel",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                }).then((res) => res.json().then((j)=>{
                    this.$refs.audio.delLabel(name);
                    that.colorlist = j.colorlist;
                    that.get_labels()
                }))
            },

            get_pics(){
                let that = this;
                return fetch("/api/getresources").then((res)=>res.json().then((j)=>{
                    that.sources = j.sources;
                }))
            },

            show_pics(){
                for(let item=0; item<this.sources.length;item++){
                    console.log(this.sources[item]);
                    const data = {"file_name":this.sources[item]};
                    let that = this;
                    let url = "/api/passfile/" + data["file_name"];
                    fetch(url,{
                        method: 'POST',
                        responseType: 'blob',
                        headers:{
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(data)
                    }).then(()=>{
                        let u_url = "http://localhost:5000/api/passfile/" + data["file_name"];
                        that.src_list.push(u_url);
                        this.url = u_url
                        console.log(this.url)
                    });
                }
            },

            has_add_labels(item){
                let that = this;
                const data = {"name": item};
                console.log("abd");
                console.log(data);
                return fetch("/api/addlabels",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(()=>{
                    that.get_labels();
                    that.cancel_label();
                })
            },
            add_label(){
                let that = this;
                const data = {"name": this.labelname};
                console.log("abd");
                console.log(data);
                return fetch("/api/addlabel",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(()=>{
                    that.get_labels();
                    that.cancel_label();
                })
            },
            gethas_labels(){
                let that = this;
                return fetch("/api/callGroup").then((res)=>res.json().then((j)=>{
                    that.hasLabel_info = j.names;
                    console.log(that.hasLabel_info);
                }))
            },
            get_labels(){
                let that = this;
                return fetch("/api/getlabels").then((res) => res.json().then((j)=>{
                    that.label_num = j.label_num;
                    that.Label_info = j.labels;
                    that.colorlist = j.colorlist;
                    this.gethas_labels();
                }))
            },

            create_label(){
                this.show_btn = true;
            },
            cancel_label(){
                this.show_btn = false;
            },

            //written over

            
            //添加标签组
            addMarkGroup()
            {
                this.$router.push("/index/manage/dataset/pic/addtag");
            },

            //written by syz
            getcolor(item){
                return {
                    color: this.colorlist[item]
                };
            },

            videoLabel(item){
                this.$refs.audio.mark(item);
            }
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
        margin-left:400px;
    }
    #previous
    {
        margin-left:50px;
    }
    #middle_btns
    {
        width:1300px;
    }
    #middle_data
    {
        margin-top:20px;
        width:1300px;
        height:700px;
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
        border-bottom: 0px;
    }
    #middle_footer
    {
        border:thin solid rgb(234, 229, 229);
        width:350px;
        height:550px;
        padding:0px;
    }
    #middle_asider
    {
        border:thin solid rgb(234, 229, 229);
        width:950px;
        height:700px;
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
        margin-top: -400px;
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
        margin-top: 8px;
        margin-left: 5px;
        font-weight: bold;
        width:300px;
        Text-align:left;
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
</style>
