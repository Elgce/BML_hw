<template>
    <el-container>
        <el-header >
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider />
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
                    <el-cascader v-model="Tvalue" :options="Toptions"  placeholder="全部"/>
                </el-col>
                <el-col :span="4">
                    <el-input
                        v-model="input"
                        class="w-50 m-2"
                        placeholder="输入数据集名称或ID"
                        prefix-icon="Search"
                    >
                    </el-input>
                </el-col>
            </el-row>
            <el-empty :image-size="250" description="空空如也" v-if="value=='open' || data_num==0">
            </el-empty>
            <div v-if="value!='open'">
            <div v-for = "item in MessageShow" :key="item.name">
            <el-divider class="between" border-style="none"></el-divider>
                <div class="table-header">
                    <div class="title">
                        <el-button class="inline-editor" link @click="show_nametxt" id="edit_name">
                            <span title="name" class="inline-editor-txt">{{item["name"]}}</span>
                            <el-icon><Edit /></el-icon>
                            
                        </el-button>
                        <el-input class="inline-editor" placeholder="请输入新名称" id="name_input" type="text" style="width:140px;visibility: hidden" v-model="new_name" visible="false" @change="change_name(item.name)"/>
                    
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
                        <!-- <i v-if="{{item[in_state]}}=='finiesd'" class="greendot"></i> -->
                        
                    </el-descriptions-item>
                    <el-descriptions-item label="标注类型">{{item["specy"]}}</el-descriptions-item>
                    <el-descriptions-item label="标注状态">{{item["mark_state"]}}</el-descriptions-item>
                    <el-descriptions-item label="清洗状态">{{item["clear_state"]}}</el-descriptions-item>
                    <el-descriptions-item label="操作">
                        <el-button type="primary" link key="label" @click="multilabel(item.name)">多人标注</el-button>
                        <el-button type="primary" link key="label" @click="insert(item.name)">导入</el-button>
                        <el-button type="primary" link key="delete" @click="deletedata(item.name)">删除</el-button>
                    </el-descriptions-item>
                </el-descriptions>
            <el-divider class="between" border-style="none"></el-divider>
            </div>
            </div>
            <el-divider class="lower" border-style="none"></el-divider>
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
                                value: 'clapic',
                                label: '图片分类',
                            },
                            {
                                value: 'tach',
                                label: '物体检测',
                            },
                            {
                                value: 'cut',
                                label: '图像分割',
                            },
                            {
                                value: 'OCR',
                                label: 'OCR标注',
                            }
                        ]
                    },
                    {
                        value: 'tex',
                        label: '文本',
                        children: [
                            {
                                value: 'clasi',
                                label: '文本分类',
                            },
                            {
                                value: 'accor',
                                label: '短文本相似度'
                            },
                            {
                                value: 'label',
                                label: '序列标注',
                            },
                            {
                                value: 'get',
                                label: '文本实体抽取',
                            },
                        ]
                    },
                    {
                        value: 'tab',
                        label: '表格',
                        children: [
                            {
                                value: 'pred',
                                label: '表格预测',
                            },
                            {

                            }
                        ]
                    }
                ]
            }
        },
        methods:{
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
            multilabel(name){
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
                    this.$router.push("/index/manage/test");
                })
            },
            change_name(name){
                // let that = this;
                const data = {"new_name":this.new_name,"old_name":name}
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
            show_nametxt(){
                let txt = document.getElementById("name_input");
                if(txt.style.visibility==='visible'){
                    txt.style.visibility='hidden';
                }
                else{
                    txt.style.visibility='visible';
                    txt.style.backgroundColor="white";
                }
            },
            get_data(){
                this.get_datanum();
                let that = this;
                fetch("/api/getdata").then((res) => res.json().then((j)=>{
                    that.MessageInfo = j.MessageInfo;
                    // console.log(that.MessageInfo.value());
                    for (let item in that.MessageInfo){
                        that.MessageArray.push(item);
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
                    // this.$router.push("/index/manage/dataset")
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