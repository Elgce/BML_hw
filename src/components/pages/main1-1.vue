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
                        :suffix-icon="Search"
                    />
                </el-col>
            </el-row>
            <el-empty :image-size="250" description="空空如也" v-if="value=='open' || data_num==0">
            </el-empty>
            <div v-if="value!='open'">
            <div v-for = "item in MessageInfo" :key="item.name">
            <el-divider class="between" border-style="none"></el-divider>
                <div class="table-header">
                    <div class="title">
                        <span class="inline-editor">
                            <span title="name" class="inline-editor-txt">{{item["name"]}}</span>
                            <el-icon><Edit /></el-icon>
                        </span>
                        <span>数据集组ID:{{item["data_id"]}}</span>
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
                        <el-button type="primary" link key="label" @click="multilabel">多人标注</el-button>
                        <el-button type="primary" link key="label" @click="insert">导入</el-button>
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
                :page-sizes="[1, 5, 10, 15, 20]"
                :background="background"
                layout="total, sizes, prev, pager, next, jumper"
                :total="data_num"
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                v-if="value!='open' && data_num!=0"
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
                MessageInfo: reactive({}),
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
            insert(){
                this.$router.push("/index/manage/dataset/insert")
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
            get_data(){
                this.get_datanum();
                let that = this;
                fetch("/api/getdata").then((res) => res.json().then((j)=>{
                    that.MessageInfo = j.MessageInfo
                }))
            },
            handleSizeChange(newSize){
                this.queryInfo.pagesize = newSize
            },
            handleCurrentChange(newPage){
                this.queryInfo.pagenum = newPage 
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