<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-collapse v-model="activeNames" @change="handleChange">
                <el-collapse-item title="标签组管理">
                    <div>
                        <el-row id="header_management">标签组管理</el-row>
                        <p id="management_text">当数据集的标签数量过多，或多个数据集需共享标签时，通过标签组管理功能可将多个常用标签创建为“标签组”进行统一管理，支持批量添加、修改、删除标签；创建成功后，在数据标注过程中可一键导入“标签组”，避免重复手动添加标签。</p>
                    </div>
                    <div>
                        <el-row id="header_handling">使用流程介绍</el-row>
                        <br>
                        <img src="../../assets/tag_group_description.png" width="600" height="39" id="pics">
                        <br>
                        <br>
                        <div id="handling_text_left">1 新建标签组</div>
                        <div id="handling_text_middle">2 管理标签组</div>
                        <div id="handling_text_right">3 调用标签组</div>
                        <br>
                        <div id="handling_datail_left">点击“创建标签组”按钮，根据需要输入标签组名称和描述。</div>
                        <div id="handling_datail_middle">支持手动或批量“添加/删除/修改”标签，您可上传csv、xls、txt格式文件批量添加标签。</div>
                        <div id="handling_datail_right">在线标注数据时，您可一键导入“标签组”，使用组内标签进行标注。</div>
                        <br>
                        <br>
                        <br>
                    </div>
                </el-collapse-item>
            </el-collapse>
            <br>
            <el-row>
                <el-button type="primary" @click="dialogVisible = true">创建标签组</el-button>
                <div id="search_tag_div">
                    <el-input v-model="tagGroupName" placeholder="输入标签组名称">
                        <template #prefix>
                            <el-icon class="el-input__icon"><search /></el-icon>
                        </template>
                    </el-input>
                </div>
            </el-row>
            <br>
            <el-descriptions
                direction="vertical"
                :column="5"
                size="large"
                border
            >
                <el-descriptions-item label="标签组名称">123</el-descriptions-item>
                <el-descriptions-item label="标签组描述">123</el-descriptions-item>
                <el-descriptions-item label="创建时间">2022-06-01 20:03:35</el-descriptions-item>
                <el-descriptions-item label="更新时间">2022-06-01 20:03:35</el-descriptions-item>
                <el-descriptions-item label="操作">
                    <el-button type="primary" link key="label" @click="multilabel(item.name)">标签管理</el-button>
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
    <el-dialog
        v-model="dialogVisible"
        title="创建标签组"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider id="dialog_divider"/>
        <el-row id="name">
            <p>标签组名称</p>
            <p id="highlight">✳</p>
            <el-input v-model="newTagName" placeholder="请输入名称" id="tag_name_input" @input="if_diableBtn"></el-input>
        </el-row>
        <br>
        <el-row id="description">
            <p>标签组描述</p>
            <el-input
                id="tag_description"
                maxlength="100"
                placeholder="请输入标签组描述"
                show-word-limit
                type="textarea"
                :rows="6"
                v-model="tagGroupDescription"
            />
        </el-row>
        <el-divider/>
        <div>
            <el-button id="complete" :disabled="disabled" type="primary">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="dialogVisible = false">取消</el-button>
        </div>
    </el-dialog>
</template>


<script>
import Breadcrumb from "../BreadCrumb.vue"
import { ref } from "vue"
    export default{
        name: "AddTag",
        components: 
        {
            Breadcrumb,
        },
        data()
        {
            return{
                dialogVisible: true,
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
                tagGroupName:ref(''),
                newTagName:ref(''),
                tagGroupDescription:ref(''),
                disabled:true
            };
        },
        methods:{
            if_diableBtn()
            {
                if(this.newTagName!="")
                {
                    this.disabled=false;
                }
                else
                {
                    this.disabled=true;
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
    #submit
    {
        position: absolute;
        top:80px;
        right:40px;
    }
    #tag_name_input
    {
        
    }
    #highlight
    {
        color:red;
        font-weight:900;
    }
    #tag_description
    {
        
    }
    #dialog_divider
    {
        margin-top:-30px;
    }
    #header_management
    {
        font-weight:900;
        text-align:left;
        font-size:16px;
    }
    #management_text
    {
        text-align:left;
        font-size:13px;
    }
    #header_handling
    {
        font-weight:900;
        text-align:left;
        font-size:16px;
    }
    #pics
    {
        position: absolute;
        left:217px;
    }
    #handling_text_left
    {
        font-weight:500;
        font-size:15px;
        position: absolute;
        left:217px;
    }
    #handling_text_middle
    {
        font-weight:500;
        font-size:15px;
        position: absolute;
        left:500px;
    }
    #handling_text_right
    {
        font-weight:500;
        font-size:15px;
        position: absolute;
        left:783px;
    }
    #handling_datail_left
    {
        font-weight:300;
        font-size:13px;
        position: absolute;
        left:217px;
        width:200px;
        text-align: left;
    }
    #handling_datail_middle
    {
        font-weight:300;
        font-size:13px;
        position: absolute;
        left:500px;
        width:200px;
        text-align: left;
    }
    #handling_datail_right
    {
        font-weight:300;
        font-size:13px;
        position: absolute;
        left:783px;
        width:200px;
        text-align: left;
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
        margin-left:960px;
    }
</style>
