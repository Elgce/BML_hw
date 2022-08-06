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
                data_num:0,
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
            tocreate(){
                this.$router.push("/index/manage/dataset/create")
            },
            get_datanum(){
                let that = this;
                fetch("/api/getnum").then((res) => res.json().then((j) => {
                    that.data_num = j.data_num;
                }))
            },
            get_data(){
                let that = this;
                fetch("/api/getdata").then((res) => res.json().then((j)=>{
                    that.MessageInfo = JSON.stringify(j.MessageInfo)
                }))
            },
            handleSizeChange(newSize){
                this.queryInfo.pagesize = newSize
            },
            handleCurrentChange(newPage){
                this.queryInfo.pagenum = newPage 
            },
        },
        created() {
            this.get_datanum();
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

</style>