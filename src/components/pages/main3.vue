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
                    <el-radio-button label="全部(0)" />
                    <el-radio-button label="有标注信息(0)" />
                    <el-radio-button label="无标注信息(0)" />
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
                        <b id="tag_column_text">标签栏</b>
                        <el-button id="add_tag">添加标签</el-button>
                        <el-popover
                            placement="bottom-end"
                            :width="20"
                            trigger="hover"
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
                        <el-input v-model="input4" class="w-50 m-2" placeholder="请输入标签名称">
                            <template #prefix>
                                <el-icon class="el-input__icon"><search /></el-icon>
                            </template>
                        </el-input>
                        <span id="tag_search_text">根据图片内容，选择标签</span>
                    </el-header>
                    <el-footer id="middle_footer">
                        <div id="empty_img_left"></div>
                        <span id="empty_text_left">暂无可用标签 ，请点击上方按钮添加</span>
                    </el-footer>
                </el-container>
                <el-aside id="middle_asider">
                    <div id="empty_right">
                        暂无可用数据
                    </div>
                </el-aside>
            </el-container>
        </el-main>
        <el-fotter>
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
        </el-fotter>
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
                ]
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
    }
    #empty_text_left
    {
        font-size:13px;
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
</style>
