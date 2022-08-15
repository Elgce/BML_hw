<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-row>
                <el-button type="primary">添加标签</el-button>
                <el-button>批量添加</el-button>
                <el-button disabled>批量修改</el-button>
                <el-button disabled>批量删除</el-button>
                <div id="search_tag_div">
                    <el-input v-model="tagName" placeholder="输入标签名称">
                        <template #prefix>
                            <el-icon class="el-input__icon"><search /></el-icon>
                        </template>
                    </el-input>
                </div>
            </el-row>
            <br>
            <el-descriptions
                direction="vertical"
                :column="2"
                size="large"
                border
            >
                <el-descriptions-item label="标签名称">
                    <el-checkbox label="" size="large"/>
                    &nbsp;&nbsp;&nbsp;123
                </el-descriptions-item>
                <el-descriptions-item label="操作">
                    <el-button type="primary" link key="label" @click="insert(item.name)">编辑</el-button>
                    <el-button type="primary" link key="delete" @click="deletedata(item.name)">删除</el-button>
                </el-descriptions-item>
            </el-descriptions>
            <div id="pages">
                <el-row>
                    <p id="fotter_text">每页显示&nbsp;&nbsp;&nbsp;</p>
                    <el-select v-model="value" placeholder="10" id="fotter_select">
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
        </el-main>
    </el-container>
</template>

<script>
import Breadcrumb from "../BreadCrumb.vue"
import { ref } from "vue"
    export default
    {
        name: 'TagGroup',
        components: 
        {
            Breadcrumb,
        },
        data()
        {
            return{
                options:[
                    {
                        value: '10',
                        label: '10',
                    },
                    {
                        value: '20',
                        label: '20',
                    },
                    {
                        value: '30',
                        label: '30',
                    },
                ],
                tagName:ref(''),
            };
        },
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
    #submit
    {
        position: absolute;
        top:80px;
        right:40px;
    }
    #search_tag_div
    {
        position:absolute;
        right:0;
        width:220px;
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
        margin-top:30px;
        margin-left:860px;
    }
</style>
