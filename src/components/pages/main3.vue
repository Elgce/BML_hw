<template>
    <el-contanier>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="example" type="primary" @click="dialogVisible = true">批量标注示例</el-link>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-row id="middle_btns">
                <el-radio-group v-model="radio1" size="large">
                    <el-radio-button label="全部" />
                    <el-radio-button label="有标注信息" />
                    <el-radio-button label="无标注信息" />
                </el-radio-group>
                <div id="three_btns">
                    <el-button>导入图片</el-button>
                    <el-button>质检报告</el-button>
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
                    <el-checkbox v-model="unlimited1" label="不限" size="large" @change="checkSource"/>
                    <el-checkbox name="source" label="本地上传" size="large" @change="checkSource"/>
                    <el-checkbox name="source" label="摄像头采集" size="large" @change="checkSource"/>
                    <el-checkbox name="source" label="云服务调用数据采集" size="large" @change="checkSource"/>
                    <el-checkbox name="source" label="数据清洗" size="large" @change="checkSource"/>
                    <el-checkbox name="source" label="数据增强" size="large" @change="checkSource"/>
                </div>
                <div>
                    <b>导入日期&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited2" label="不限" size="large" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-date-picker
                        type="daterange"
                        range-separator="To"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                    />
                </div>
                <div>
                    <b>标注日期&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited3" label="不限" size="large" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-date-picker
                        type="daterange"
                        range-separator="To"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                    />
                </div>
                <div>
                    <b>标签&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited4" label="不限" size="large" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-select placeholder="请选择" size="large"></el-select>
                </div>
                    <template #reference>
                        <el-button @click="visible = !visible">筛选</el-button>
                    </template>
                </el-popover>
            </el-row>
            <el-container id="middle_data">
                <el-container>
                    <el-header id="middle_header">
                        <b>标签栏</b>
                    </el-header>
                    <el-main>Main</el-main>
                    <el-footer>Footer</el-footer>
                </el-container>
                <el-aside width="1000px">Aside</el-aside>
            </el-container>
        </el-main>
    </el-contanier>
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
                dialogVisible: true,
                radio1:'全部',
                visible:false,
                unlimited1:true,
                unlimited2:true,
                unlimited3:true,
                unlimited4:true,
            };
        },
        methodes:{
            // checkSource()
            // {
            //     var source=document.getElementsByName("source");
                

            // }
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
    #three_btns
    {
        position: absolute;
        left:1010px;
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
        border:thin solid rgb(234, 229, 229);
    }
    #middle_header
    {
        border:thin solid rgb(234, 229, 229);
    }
</style>
