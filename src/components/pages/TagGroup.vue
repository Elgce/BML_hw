<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>
        <el-main>
            <el-row>
                <el-button type="primary" @click="newVisible = true">添加标签</el-button>
                <el-button disabled>批量添加</el-button>
                <el-button disabled>批量修改</el-button>
                <el-button disabled>批量删除</el-button>
                <div id="search_tag_div">
                    <el-input v-model="tagName" placeholder="输入标签名称" @input="search_label">
                        <template #prefix>
                            <el-icon class="el-input__icon"><search /></el-icon>
                        </template>
                    </el-input>
                </div>
            </el-row>
            <el-divider/>
            <el-table :data="labelsData" style="width: 100%">
                <el-table-column prop="name" label="标签名称" />
                <el-table-column prop="description" label="操作">
                    <el-button type="primary" link key="label" @click="edit">编辑</el-button>
                    <el-button type="primary" link key="delete" @click="delete_">删除</el-button>
                </el-table-column>
            </el-table>
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

    <!-- 添加标签对话框 -->
    <el-dialog
        v-model="newVisible"
        title="添加标签"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>标签名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="newTagName" placeholder="请输入名称" @input="if_diableBtn"></el-input>
        </el-row>
        <el-divider/>
        <div>
            <el-button id="complete" :disabled="disabled" type="primary" @click="add_tag">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="newVisible = false">取消</el-button>
        </div>
    </el-dialog>

    <!-- 编辑标签对话框 -->
    <el-dialog
        v-model="editVisible"
        title="编辑标签"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>原标签名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="formTagName" placeholder="请输入原名称" @input="if_diableBtn2"></el-input>
        </el-row>
        <br>
        <el-row class="name">
            <p>新标签名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="nextTagName" placeholder="请输入新名称" @input="if_diableBtn2"></el-input>
        </el-row>
        <el-divider/>
        <div>
            <el-button :disabled="disabled2" type="primary" @click="edit_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="editVisible = false">取消</el-button>
        </div>
    </el-dialog>

    <!-- 删除标签对话框 -->
    <el-dialog
        v-model="deleteVisible"
        title="删除标签"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>标签名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="deleteName" placeholder="请输入名称" @input="if_diableBtn3"></el-input>
        </el-row>
        <el-divider/>
        <div>
            <el-button :disabled="disabled3" type="primary" @click="delete_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="deleteVisible = false">取消</el-button>
        </div>
    </el-dialog>
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
        created(){
            this.calldata();
        },
        data()
        {
            return{
                labelsData:[],
                newVisible:false,
                newTagName:ref(''),
                disabled:true,
                disabled2:true,
                disabled3:true,
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
                input_id:ref(''),
                editVisible:false,
                deleteVisible:false,
                formTagName:ref(''),
                nextTagName:ref(''),
                deleteName:ref('')
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
            },

            if_diableBtn2()
            {
                if(this.formTagName!=""&&this.nextTagName!="")
                {
                    this.disabled2=false;
                }
                else
                {
                    this.disabled2=true;
                }
            },

            if_diableBtn3()
            {
                if(this.deleteName!="")
                {
                    this.disabled3=false;
                }
                else
                {
                    this.disabled3=true;
                }
            },
            change_mark()
            {
                var change_btn=document.getElementById("change_btn");
                var id_box=document.getElementById("id_box");
                var row_of_input=document.getElementById("row_of_input");
                var delete_btn=document.getElementById("delete_btn");
                if(change_btn.innerText=="确认")
                {
                    id_box.style.visibility='visible';
                    row_of_input.style.visibility='hidden';
                    change_btn.innerText="编辑";
                    delete_btn.innerText="删除";
                }
                else
                {
                    id_box.style.visibility='hidden';
                    row_of_input.style.visibility='visible';
                    change_btn.innerText="确认";
                    delete_btn.innerText="取消";
                }
            },
            delete_mark()
            {
                var change_btn=document.getElementById("change_btn");
                var id_box=document.getElementById("id_box");
                var row_of_input=document.getElementById("row_of_input");
                var delete_btn=document.getElementById("delete_btn");
                if(change_btn.innerText=="确认")
                {
                    id_box.style.visibility='visible';
                    row_of_input.style.visibility='hidden';
                    change_btn.innerText="编辑";
                    delete_btn.innerText="删除";
                }
            },

            //增加标签
            add_tag()
            {
                this.newVisible=false;
                const data = {
                    "name": this.newTagName,
                };
                return fetch("/api/add_group_tag",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    if(j.isok === "repeat")
                    {
                        alert("标签名称重复!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/managegroupblank");
                    }
                })
            },

            //获取标签数据
            calldata(){
                return fetch("/api/call_group_labels").then((res)=>res.json().then((j)=>{
                    for(var i=0;i<j.names.length;i++)
                    {
                        this.labelsData.push({"name":j.names[i],});
                    }
                }))
            },

            //编辑标签
            edit()
            {
                this.editVisible=true;
            },
            edit_group()
            {
                this.editVisible=false;
                const data = {
                    "form_name": this.formTagName,
                    "next_name": this.nextTagName,
                };
                return fetch("/api/editgrouptag",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    if(j.isok === "not-exist")
                    {
                        alert("原标签名称不存在!");
                    }
                    else if(j.isok === "repeat")
                    {
                        alert("新标签名称重复!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/managegroupblank");
                    }   
                })
            },

            //删除标签
            delete_()
            {
                this.deleteVisible=true;
            },
            delete_group()
            {
                this.deleteVisible=false;
                const data = {
                    "name": this.deleteName,
                };
                return fetch("/api/deletegrouptag",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    if(j.isok === "not-exist")
                    {
                        alert("标签名称不存在!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/managegroupblank");
                    }   
                })
            },
            
            //搜素标签
            search_label()
            {
                if(this.tagName!="")
                {
                    const data = {
                        "name": this.tagName,
                    };
                    return fetch("/api/searchTag",{
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data)
                    })
                    .then(res => res.json())
                    .then((j)=>{
                        this.labelsData=[];
                        for(var i=0;i<j.names.length;i++)
                        {
                            this.labelsData.push({"name":j.names[i],});
                            //this.$router.push("/index/manage/dataset/pic/taggroupblank");
                        }
                    })
                }
                else
                {
                    return fetch("/api/call_group_labels").then((res)=>res.json().then((j)=>{
                        for(var i=0;i<j.names.length;i++)
                        {
                            this.labelsData.push({"name":j.names[i],});
                            this.$router.push("/index/manage/dataset/pic/managegroupblank");
                        }
                    }))
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
    .highlight
    {
        color:red;
        font-weight:900;
    }
    .dialog_divider
    {
        margin-top:-30px;
    }
</style>

