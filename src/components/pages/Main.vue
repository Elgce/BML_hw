<!-- 数据集展示页面 -->
<template>
    <el-container>
        <!-- 头部元素 -->
        <el-header >
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider />

        <!-- 主体部分 -->
        <el-main>
            <el-row>
                <el-col :span="2">
                    <el-button type="primary" @click="tocreate">创建数据集</el-button>
                </el-col>
                <el-col :span="2" :offset="12">
                    <el-select v-model="value" class="m-2" placeholder="数据集">
                        <el-option
                            v-for="item in options"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                        />
                    </el-select>
                </el-col>
                <el-col :span="4">
                    <el-cascader v-model="Tvalue" :options="Toptions"  placeholder="全部" @change="handleChosenChange"/>
                </el-col>
                <el-col :span="4">
                    <el-input
                        v-model="input"
                        class="w-50 m-2"
                        placeholder="输入数据集名称"
                        prefix-icon="Search"
                        @change="Searchbyname"
                    >
                    </el-input>
                </el-col>
            </el-row>
            <el-empty :image-size="250" description="空空如也" v-if="value=='open' || data_num==0">
            </el-empty>
            <div v-if="value!='open'">
            <div v-for = "(item,index) in MessageShow" :key="item.name">
            <el-divider class="between" border-style="none"></el-divider>
                <div class="table-header">
                    <div class="title">
                        <el-button class="inline-editor" link @click="show_nametxt(index)" id="edit_name">
                            <span title="name" class="inline-editor-txt">{{item["name"]}}</span>
                            <el-icon><Edit /></el-icon>
                        </el-button>
                        <el-input class="inline-editor" placeholder="请输入新名称" :id="generate_id(index)" type="text" style="width:140px;visibility: hidden" v-model="new_name" visible="false" @change="change_name(item.name)"/>
                        <span>数据集组ID:{{item["group_id"]}}</span>
                    </div>
                    <div class="op">
                        <span class="op-item">
                            <el-icon><DocumentAdd /></el-icon>
                            <span>新增版本</span>
                        </span>
                        <span class="op-item">
                            <el-icon><Menu /></el-icon>
                            <span>全部版本</span>
                        </span>
                        <el-button class="op-item" link @click="deletedata(item.name)">
                            <el-icon><Delete /></el-icon>
                            <span>删除</span>
                        </el-button>
                    </div>
                </div>

                <!-- 数据集展示部分 -->
                <el-descriptions
                    direction="vertical"
                    :column="8"
                    size="large"
                    border
                >
                    <el-descriptions-item label="版本">{{item["version"]}}</el-descriptions-item>
                    <el-descriptions-item label="数据集ID">{{item["data_id"]}}</el-descriptions-item>
                    <el-descriptions-item label="数据量">{{item["num"]}}</el-descriptions-item>
                    <el-descriptions-item label="最近导入状态">
                        <span>{{item["in_state"]}}</span>
                    </el-descriptions-item>
                    <el-descriptions-item label="标注类型">{{item["specy"]}}</el-descriptions-item>
                    <el-descriptions-item label="标注状态">{{item["mark_state"]}}</el-descriptions-item>
                    <el-descriptions-item label="清洗状态">{{item["clear_state"]}}</el-descriptions-item>
                    <el-descriptions-item label="操作">
                        <el-button type="primary" link key="label" @click="multilabel(item.name,item.specy)">查看与标注</el-button>
                        <el-button type="primary" link key="label" @click="insert(item.name)">导入</el-button>
                        <el-button type="primary" link key="delete" @click="deletedata(item.name)">删除</el-button>
                        <el-button type="primary" link key="export" @click="exportdata(item.name)">导出</el-button>
                    </el-descriptions-item>
                </el-descriptions>
            <el-divider class="between" border-style="none"></el-divider>
            </div>
            </div>
            <el-divider class="lower" border-style="none"></el-divider>

            <!-- 分页部分 -->
            <el-pagination
                v-model:currentPage="queryInfo.pagenum"
                v-model:page-size="queryInfo.pagesize"
                :page-sizes="[1, 2, 3,4, 5]"
                :background="background"
                layout="total, sizes, prev, pager, next, jumper"
                :total="data_num"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                v-if="value!='open' && data_num!=0"
                id="pagination"
            />
        </el-main>
    </el-container>
</template>

<script>
import { reactive, ref } from "vue"
import Breadcrumb from "../BreadCrumb.vue"
    export default{
        name: "ManageDateSet",
        components:{
            Breadcrumb,
        },
        data(){
            return{
                background :ref(true),
                queryInfo: {
                    query: '',
                    pagenum: 1,
                    pagesize: 2,
                },
                data_num: -1,
                value: ref(''),
                input: ref(''),
                new_name: ref(''),
                MessageInfo: reactive({}),
                MessageShow: reactive({}),
                MessageArray: reactive([]),
                options : [
                    {
                        value: 'my',
                        label: '我的数据集',
                    },
                    {
                        value: 'open',
                        label: '公开数据集',
                    },
                ],
                Tvalue: ref([]),
                Toptions : [
                    {
                        value: 'pic',
                        label: '图片',
                        children: [
                            {
                                value: 'pic_cla',
                                label: '图片分类',
                            },
                            {
                                value: 'pic_det',
                                label: '物体检测',
                            },
                            {
                                value: 'pic_div',
                                label: '图像分割',
                            },
                            {
                                value: 'pic_ocr',
                                label: 'OCR标注',
                            }
                        ]
                    },
                    {
                        value: 'txt',
                        label: '文本',
                        children: [
                            {
                                value: 'txt_cla',
                                label: '文本分类',
                            },
                            {
                                value: 'txt_sim',
                                label: '短文本相似度'
                            },
                            {
                                value: 'txt_cons',
                                label: '序列标注',
                            },
                            {
                                value: 'txt_extr',
                                label: '文本实体抽取',
                            },
                        ]
                    },
                    {
                        value: 'table',
                        label: '表格',
                        children: [
                            {
                                value: 'table_pre',
                                label: '表格预测',
                            },
                        ]
                    },
                    {
                        value: 'video',
                        label: '视频',
                        children: [
                            {
                                value: 'vid_ass',
                                label: '视频分类',
                            },
                            {
                                value: 'vid_spl',
                                label: '视频分割',
                            }
                        ]
                    },
                    {
                        value: 'audio',
                        label: '音频',
                        children: [
                            {
                                value: 'aud_ass',
                                label: '音频分类',
                            },
                            {
                                value: 'aud_spl',
                                label: '音频分割',
                            }
                        ]
                    }
                ]
            }
        },
        methods:{
            generate_id(index){
                return "name_"+index
            },
            exportdata(name){
                const data = {"name":name}
                return fetch("/api/setsession",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res=>res.json())
                .then(()=>{
                    this.$router.push("/index/manage/dataset/4-2");
                })
            },
            handleChosenChange(){
                let that = this;
                const data = {"specy":this.Tvalue[0],"type":this.Tvalue[1]}
                return fetch("/api/searchdata",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    that.MessageInfo = j.MessageShow;
                    that.data_num = j.data_num;
                    that.MessageArray = reactive([]);
                    for (let item in that.MessageInfo){
                        that.MessageArray.push(item);
                        if(that.MessageInfo[item]["in_state"]==="finished"){
                            that.MessageInfo[item]["in_state"] = "已完成";
                        }
                        if(that.MessageInfo[item]["specy"]==="pic"){
                            that.MessageInfo[item]["specy"] = "图片标注";
                        }
                        else if(that.MessageInfo[item]["specy"]==="txt"){
                            if(that.MessageInfo[item]["label_type"]==="txt_cla"){
                                that.MessageInfo[item]["specy"] = "文本标注";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_sim"){
                                that.MessageInfo[item]["specy"] = "文本相似度";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_extr"){
                                that.MessageInfo[item]["specy"] = "文本实体抽取";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="video"){
                            if(that.MessageInfo[item]["direction"]==="vid_ass"){
                                that.MessageInfo[item]["specy"] = "视频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="vid_spl"){
                                that.MessageInfo[item]["specy"] = "视频分割";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="audio"){
                            if(that.MessageInfo[item]["direction"]==="aud_ass"){
                                that.MessageInfo[item]["specy"] = "音频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="aud_spl"){
                                that.MessageInfo[item]["specy"] = "音频分割";
                            }
                        }
                        else{
                            that.MessageInfo[item]["specy"] = "表格标注";
                        }
                    }
                    this.handleCurrentChange(1);
                })
            },
            insert(name){
                const data = {"name": name}
                return fetch("/api/setsession",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then(()=>{
                    this.$router.push("/index/manage/dataset/insert");
                })
                
            },
            tocreate(){
                this.$router.push("/index/manage/dataset/create")
            },
            get_datanum(){
                let that = this;
                fetch("/api/getnum").then((res) => res.json().then((j) => {
                    that.data_num = j.data_num;
                    console.log(that.data_num);
                }))
            },
            multilabel(name,specy){
                const data = {"name": name}
                return fetch("/api/setsession",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then(()=>{
                    console.log(specy);
                    if(specy==="图片标注"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/menu3");
                        })
                        
                    }
                    else if(specy==="文本标注"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/text/addtag");
                        })
                    }
                    else if(specy==="文本相似度"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/text/similarity");
                        })
                    }
                    else if(specy==="视频分类"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/video/mark");
                        })
                        
                    }
                    else if(specy==="视频分割"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/video/split");
                        })
                        
                    }
                    else if(specy==="音频分类"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/audio/mark");
                        })
                        
                    }
                    else if(specy==="音频分割"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/audio/split");
                        })
                        
                    }
                    else if(specy==="文本实体抽取"){
                        const data = {"t_type": "all"};
                        fetch("/api/sessiontype",{
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(data)
                        })
                        .then((res)=>res.json())
                        .then(()=>{
                            this.$router.push("/index/manage/dataset/extracttag");
                        })
                    }
                    
                })
            },

            //搜索数据集
            Searchbyname(){
                const data = {"name":this.input};
                let that = this;
                return fetch("/api/searchname",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    that.MessageInfo = j.MessageShow;
                    that.data_num = j.data_num;
                    that.MessageArray = reactive([]);
                    for (let item in that.MessageInfo){
                        that.MessageArray.push(item);
                        if(that.MessageInfo[item]["in_state"]==="finished"){
                            that.MessageInfo[item]["in_state"] = "已完成";
                        }
                        if(that.MessageInfo[item]["specy"]==="pic"){
                            that.MessageInfo[item]["specy"] = "图片标注";
                        }
                        else if(that.MessageInfo[item]["specy"]==="txt"){
                            if(that.MessageInfo[item]["label_type"]==="txt_cla"){
                                that.MessageInfo[item]["specy"] = "文本标注";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_sim"){
                                that.MessageInfo[item]["specy"] = "文本相似度";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_extr"){
                                that.MessageInfo[item]["specy"] = "文本实体抽取";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="video"){
                            if(that.MessageInfo[item]["direction"]==="vid_ass"){
                                that.MessageInfo[item]["specy"] = "视频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="vid_spl"){
                                that.MessageInfo[item]["specy"] = "视频分割";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="audio"){
                            if(that.MessageInfo[item]["direction"]==="aud_ass"){
                                that.MessageInfo[item]["specy"] = "音频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="aud_spl"){
                                that.MessageInfo[item]["specy"] = "音频分割";
                            }
                        }
                        else{
                            that.MessageInfo[item]["specy"] = "表格标注";
                        }
                    }
                    this.handleCurrentChange(1);
                })

            },

            //改变名称
            change_name(name){
                const data = {"new_name":this.new_name,"old_name":name};
                return fetch("/api/changename",{
                    method: 'POST',
                    headers:{
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then(()=>{
                    this.$router.push("/index/manage/blank")
                })

            },
            show_nametxt(index){
                console.log(index)
                let txt = document.getElementById("name_"+index);
                if(txt.style.visibility==='visible'){
                    txt.style.visibility='hidden';
                }
                else{
                    txt.style.visibility='visible';
                    txt.style.backgroundColor="white";
                }
            },

            //获取数据
            get_data(){
                this.get_datanum();
                let that = this;
                fetch("/api/getdata").then((res) => res.json().then((j)=>{
                    that.MessageInfo = j.MessageInfo;
                    that.MessageArray = reactive([]);
                    for (let item in that.MessageInfo){
                        that.MessageArray.push(item);
                        if(that.MessageInfo[item]["in_state"]==="finished"){
                            that.MessageInfo[item]["in_state"] = "已完成";
                        }
                        if(that.MessageInfo[item]["specy"]==="pic"){
                            that.MessageInfo[item]["specy"] = "图片标注";
                        }
                        else if(that.MessageInfo[item]["specy"]==="txt"){
                            if(that.MessageInfo[item]["label_type"]==="txt_cla"){
                                that.MessageInfo[item]["specy"] = "文本标注";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_sim"){
                                that.MessageInfo[item]["specy"] = "文本相似度";
                            }
                            else if(that.MessageInfo[item]["label_type"]==="txt_extr"){
                                that.MessageInfo[item]["specy"] = "文本实体抽取";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="video"){
                            if(that.MessageInfo[item]["direction"]==="vid_ass"){
                                that.MessageInfo[item]["specy"] = "视频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="vid_spl"){
                                that.MessageInfo[item]["specy"] = "视频分割";
                            }
                        }
                        else if(that.MessageInfo[item]["specy"]==="audio"){
                            if(that.MessageInfo[item]["direction"]==="aud_ass"){
                                that.MessageInfo[item]["specy"] = "音频分类";
                            }
                            else if(that.MessageInfo[item]["direction"]==="aud_spl"){
                                that.MessageInfo[item]["specy"] = "音频分割";
                            }
                        }
                        else{
                            that.MessageInfo[item]["specy"] = "表格标注";
                        }
                    }
                    this.handleCurrentChange(1);
                }))
            },
            handleSizeChange(newSize){
                this.queryInfo.pagesize = newSize;
                this.handleCurrentChange(1);
            },
            handleCurrentChange(newPage){
                this.queryInfo.pagenum = newPage;
                let start = (this.queryInfo.pagenum - 1) * this.queryInfo.pagesize;
                let end = start + this.queryInfo.pagesize;
                if (this.MessageArray.length < end){
                    end = this.MessageArray.length;
                }
                this.MessageShow = reactive({});
                for (let i = start; i < end; i++){
                    this.MessageShow[this.MessageArray[i]]=this.MessageInfo[this.MessageArray[i]];
                }
            },

            // 用于设置页面表单的默认选项
            setvalue(){
                this.value = this.options[0].value;
            },

            //删除数据
            deletedata(name){
                let that = this;
                const d_name = {"name": name,}
                console.log(d_name)
                return fetch("/api/deletedata",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(d_name)
                })
                .then(res => res.json())
                .then(() => {
                    if(that.data_num>0){
                        that.data_num = that.data_num - 1;
                    }
                    this.$router.push("/index/manage/blank")
                })
            }
        },
        created() {
            this.setvalue();
            this.get_data();
        }

    }
</script>

<style scoped>
    .el-header  {
        height: 56px;
    }
    .el-divider{
        margin: 0;
    }
    .between{
        margin: 10px;
    }
    .lower{
        margin: 30px;
    }
    .table-header{
        display: flex;
        padding: 15px;
        border: 1px solid #eee;
        border-bottom: none;
        background-color: #f7f7f7;
        justify-content: space-between;
    }
    .table-header .title .inline-editor .el-icon{
        margin-left:10px;
        padding-bottom: -10px;
    }
    .table-header .title{
        display: flex;
        flex-direction: row;
        align-items: center;
        padding-bottom: -10px;
        font-size: 14px;
    }
    .table-header .title .inline-editor{
        margin-right: 20px;
        cursor: pointer;
        display: inline-block;
        white-space: nowrap;
    }
    .table-header .title .inline-editor-initial-txt{
        max-width: 360px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    .table-header .op{
        display: flex;
        flex-direction: row;
        align-items: flex-end;
    }
    .table-header .op .op-item{
        font-size: 14px;
        cursor: pointer;
        margin-right: 22px;
        color: #000;
        text-decoration: none;
    }
    .table-header .op .op-item span{
        font-size: 12px;
        margin-left: 3px;
    }

</style>
