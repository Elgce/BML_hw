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
                    <el-checkbox label="" size="large" id="item_checkbox"/>
                    <!-- <div id="color_box">1</div> -->
                    &nbsp;&nbsp;
                    <el-color-picker v-model="markColor" id="mark_color"/>
                    &nbsp;&nbsp;
                    <div id="id_box">123</div>
                    <el-row id="row_of_input">
                        <el-input
                            v-model="input_id"
                            class="w-50 m-2"
                            placeholder=""
                            id="input_id"
                        />
                    </el-row>
                </el-descriptions-item>
                <el-descriptions-item label="操作">
                    <el-button id="change_btn" type="primary" link key="label" @click="change_mark">编辑</el-button>
                    <el-button id="delete_btn" type="primary" link key="delete" @click="delete_mark">删除</el-button>
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
                markColor:ref('#409EFF'),
                input_id:ref('')
            };
        },
        methods:{
            change_mark()
            {
                var change_btn=document.getElementById("change_btn");
                // var mark_color=document.getElementById("color_box");
                //var color_box=document.getElementById("color_box");
                //var item_checkbox=document.getElementById("item_checkbox");
                var id_box=document.getElementById("id_box");
                var row_of_input=document.getElementById("row_of_input");
                var delete_btn=document.getElementById("delete_btn");
                if(change_btn.innerText=="确认")
                {
                    //color_box.style.visibility='hidden';
                    //item_checkbox.style.visibility='hidden';
                    id_box.style.visibility='visible';
                    //mark_color.style.visibility='hidden';
                    row_of_input.style.visibility='hidden';
                    change_btn.innerText="编辑";
                    delete_btn.innerText="删除";
                }
                else
                {
                    //color_box.style.visibility='hidden';
                    //item_checkbox.style.visibility='hidden';
                    id_box.style.visibility='hidden';
                    //mark_color.style.visibility='hidden';
                    row_of_input.style.visibility='visible';
                    change_btn.innerText="确认";
                    delete_btn.innerText="取消";
                }
            },
            delete_mark()
            {
                var change_btn=document.getElementById("change_btn");
                // var mark_color=document.getElementById("color_box");
                //var color_box=document.getElementById("color_box");
                //var item_checkbox=document.getElementById("item_checkbox");
                var id_box=document.getElementById("id_box");
                var row_of_input=document.getElementById("row_of_input");
                var delete_btn=document.getElementById("delete_btn");
                if(change_btn.innerText=="确认")
                {
                    //color_box.style.visibility='hidden';
                    //item_checkbox.style.visibility='hidden';
                    id_box.style.visibility='visible';
                    //mark_color.style.visibility='hidden';
                    row_of_input.style.visibility='hidden';
                    change_btn.innerText="编辑";
                    delete_btn.innerText="删除";
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
    #color_box
    {
        margin-left:20px;
        background-color: #409EFF;
        color: #409EFF;
        display: inline-block;
    }
    /* #mark_color
    {
        margin-left:20px;
    } */
    #id_box
    {
        display: inline-block;
    }
    #input_id
    {
        /* width:100px; */
    }
    #row_of_input
    {
        width:400px;
        display: inline-block;
        visibility: hidden;
    }
</style>
