<!-- 图片展示页 -->
<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="example" type="primary" @click="dialogVisible = true">批量标注示例</el-link>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-row id="middle_btns">
                <el-radio-group v-model="t_type" size="large" @change="handleradiochange">
                    <el-radio-button label="all">全部({{all_num}})</el-radio-button>
                    <el-radio-button label="ed" >有标注信息({{ed_num}})</el-radio-button>
                    <el-radio-button label="to" >没有标注信息({{to_num}})</el-radio-button>
                </el-radio-group>
                <div id="four_btns">
                    <el-button @click="insert_pic">导入图片</el-button>
                    <el-button>质检报告</el-button>
                    <el-button @click="start_marking">开始标注</el-button>
                    <el-button>批量批注</el-button>
                </div>
            </el-row>
            <el-divider/>
            <el-row>
                <el-popover
                    :visible="visible"
                    placement="bottom-start"
                    :width="750"
                >
                <div>
                    <b>数据来源&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited1" label="不限" size="large" @change="cleanSource"/>
                    <el-checkbox v-model="source1" name="source" label="本地上传" size="large" @change="checkSource"/>
                    <el-checkbox v-model="source2" name="source" label="摄像头采集" size="large" @change="checkSource"/>
                    <el-checkbox v-model="source3" name="source" label="云服务调用数据采集" size="large" @change="checkSource"/>
                    <el-checkbox v-model="source4" name="source" label="数据清洗" size="large" @change="checkSource"/>
                    <el-checkbox v-model="source5" name="source" label="数据增强" size="large" @change="checkSource"/>
                </div>
                <div>
                    <b>导入日期&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited2" label="不限" size="large" @change="cleanIntrDate"/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-date-picker
                        v-model="intr_date"
                        type="daterange"
                        range-separator="To"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                        id="intr_date"
                        @change="checkIntrDate"
                    />
                </div>
                <div>
                    <b>标注日期&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited3" label="不限" size="large" @change="cleanMarkingDate"/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-date-picker
                        v-model="marking_date"
                        type="daterange"
                        range-separator="To"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                        @change="checkMarkingDate"
                    />
                </div>
                <div>
                    <b>标签&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited4" label="不限" size="large" @change="cleanMark" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select placeholder="请选择" size="large" @change="checkMark"></el-select>
                </div>
                    <template #reference>
                        <el-button @click="visible = !visible">筛选&nbsp;<el-icon><ArrowDownBold /></el-icon></el-button>
                    </template>
                </el-popover>
                <div id="two_btns">
                    <el-checkbox label="本页全选" size="large"/>
                    <el-button id="delete_btn" disabled><el-icon><Delete/></el-icon>&nbsp;删除</el-button>
                </div>
            </el-row>
            <el-container id="middle_data">
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
                        <span id="tag_search_text">根据图片内容，选择标签</span>
                    </el-header>
                    <el-footer id="middle_footer">
                        <el-scrollbar height="400px">
                            <div v-for="item in Label_info" :key="item" class="scrollbar-demo-item">
                                <el-card shadow="hover" class="card">
                                    <div class="card_info">
                                        <el-color-picker v-model="markColor" id="mark_color"/>
                                        &nbsp;&nbsp;
                                        <el-button type="primary" text class="card_edit" @click="edit_label(item)">编辑</el-button>
                                        <el-button type="info" text class="card_delete" @click="delete_label(item)">删除</el-button>
                                        <p class="card_name" style="visibility:visible">{{item}}</p>
                                        <el-input type="text" id="new_name_txt" style="width:120px;visibility:hidden;" class="edit_txt" v-model="new_labelname" @change="change_name(item)"></el-input>
                                    </div>
                                </el-card>
                            </div>
                        </el-scrollbar>


                        <div id="empty_img_left" v-if="label_num===0"></div>
                        <span id="empty_text_left" v-if="label_num===0">暂无可用标签 ，请点击上方按钮添加</span>
                    </el-footer>
                </el-container>
                <el-aside id="middle_asider">
                    <el-scrollbar height="390px">
                    <div id="empty_right" v-if="src_list.length===0">
                        暂无可用数据
                    </div>
                    <el-row :gutter="20"  class="el-row" type="flex" >
                    <el-col :span="4" v-for="(item,index) in src_list" :key="item" class="pic_show" >
                            <el-card class="show_pic_card">
                                <el-image
                                :src="item"
                                class="image"
                                :fit="cover"
                                />
                                <div style="padding: 14px">
                                <div class="bottom">
                                    {{context_tag[index]}}
                                </div>
                                </div>
                            </el-card>
                    </el-col>
                    </el-row>
                    </el-scrollbar>
                </el-aside>
            </el-container>
        </el-main>
        <el-footer>
            <div id="pages">
                <el-row>
                    <p id="fotter_text">每页显示&nbsp;&nbsp;&nbsp;</p>
                    <el-select v-model="value" placeholder="30" id="fotter_select">
                        <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                            :disabled="item.disabled"
                        />
                    </el-select>
                    <el-pagination id="fotter_pages" background layout="prev, pager, next" :total="1" />
                </el-row>
            </div>
        </el-footer>
    </el-container>
    <el-dialog
        v-model="dialogVisible"
        title="EasyData图像分类模板支持批量标注数据了"
        width="40%"
        :before-close="handleClose"
    >
        <el-divider id="dialog_divider"/>
        <img src="../../assets/marking_example.png" width="400" height="445">
    </el-dialog>
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
                label_num: -1,
                labelname: ref(''),
                new_labelname: ref(''),
                Label_info:reactive([]),
                src_list:reactive([]),
                sources: reactive([]),
                context_tag: reactive([]),
                all_num: -1,
                to_num: -1,
                ed_num: -1,
                t_type:ref(''),
                show_btn: false,
                dialogVisible: false,
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
                    {
                        value: '15',
                        label: '15',
                    },
                    {
                        value: '30',
                        label: '30',
                    },
                    {
                        value: '45',
                        label: '45',
                    },
                ],
                markColor:ref('#409EFF'),
            };
        },
        created(){
            this.get_labels();
            this.get_pics().then(this.show_pics);
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
                    this.$router.push("/index/manage/dataset/pic/label/blank");
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
                    this.$router.push("/index/manage/dataset/pic/label/blank");
                }))
            },
            get_pics(){
                let that = this;
                return fetch("/api/getpicsources").then((res)=>res.json().then((j)=>{
                    that.sources = j.sources;
                    that.context_tag = j.context_tag;
                    that.to_num = j.to_num;
                    that.all_num = j.all_num;
                    that.ed_num = j.ed_num;
                    that.t_type = j.t_type;
                    console.log(that.sources);
                    for(let item in that.context_tag){
                        if(that.context_tag[item]===""){
                            that.context_tag[item]="未标注";
                        }
                    }
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
                    });
                    console.log(that.src_list);
                }
            },

           
            add_label(){
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
                .then(res=>res.json())
                .then((j)=>{
                    console.log(j);
                    this.$router.push("/index/manage/dataset/pic/label/blank");
                })
            },
           
            get_labels(){
                let that = this;
                return fetch("/api/getlabels").then((res) => res.json().then((j)=>{
                    that.label_num = j.label_num;
                    that.Label_info = j.labels;
                    console.log(that.label_num);
                }))
            },
            create_label(){
                this.show_btn = true;
            },
            cancel_label(){
                this.show_btn = false;
            },
            insert_pic(){
                this.$router.push("/index/manage/dataset/insert");
            },
            handleradiochange(){
                console.log("!");
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
                    this.$router.push("/index/manage/dataset/blank/pic");
                })
            },
            //written over


            start_marking(){
                const data = {"page":1};
                return fetch("/api/txtpagesession",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then((res) => res.json)
                .then(()=>{
                    this.$router.push("/index/manage/dataset/picmarking");
                })
                
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
    #example
    {
        position: absolute;
        top:80px;
        right:120px;
    }
    #submit
    {
        position: absolute;
        top:80px;
        right:40px;
    }
    #dialog_divider
    {
        position: absolute;
        top:50px;
        left:0px;
    }
    #four_btns
    {
        position: absolute;
        left:900px;
    }
    #two_btns
    {
        position: absolute;
        right:0px;
    }
    #delete_btn
    {
        border: none;
        margin-top:-5px;
    }
    #middle_btns
    {
        width:1300px;
    }
    #middle_data
    {
        margin-top:20px;
        width:1300px;
        height:390px;
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
        height:240px;
    }
    #middle_asider
    {
        border:thin solid rgb(234, 229, 229);
        width:950px;
        height:390px;
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
    /* written by bqw */
    .card_info{
        display: flex;
        margin-top: -15px;
    }
    .el-card{
        width: 360px;
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
    .image{
        height: 80px;
        width: 80px;
    }
    .show_area{
        display: flex;
        width: 180px;
    }
    .pic_show{
        width: 180px;
    }
    .show_pic_card{
        width: 160px;
        margin-right: 240px;
    }
    .edit_txt{
        margin-left: 10px;
        margin-top: -10px;
        border-radius: 10%;
    }
    /* written over */
</style>
