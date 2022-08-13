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
            <el-input v-model="input4" placeholder="请输入名称" id="tag_name_input"></el-input>
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
            />
        </el-row>
        <el-divider/>
        <div>
            <el-button disabled>确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button>取消</el-button>
        </div>
    </el-dialog>
</template>


<script>
import Breadcrumb from "../BreadCrumb.vue"
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
    #tag_name_input
    {
        width:50px;
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
</style>