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
            <el-empty :image-size="250" description="空空如也">
            </el-empty>
        </el-main>
    </el-container>
</template>

<script>
import { ref } from "vue"
import Breadcrumb from "../BreadCrumb.vue"
    export default{
        name: "ManageDateSet",
        components:{
            Breadcrumb,
        },
        data(){
            return{
                value: ref(''),
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
            }
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