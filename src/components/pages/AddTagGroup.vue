<template>
    <el-container>
        <!-- 上部元素 -->
        <el-header>
            <Breadcrumb></Breadcrumb>
            <el-link id="submit" type="primary">提交工单</el-link>
        </el-header>
        <el-divider id="top_divider"/>

        <!-- 主体部分 -->
        <el-main>

            <!-- 介绍部分 -->
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

            <!-- 创建及查找部分 -->
            <el-row>
                <el-button type="primary" @click="dialogVisible = true">创建标签组</el-button>
                <div id="search_tag_div">
                    <el-input v-model="tagGroupName" placeholder="输入标签组名称" @input="search_group">
                        <template #prefix>
                            <el-icon class="el-input__icon"><search /></el-icon>
                        </template>
                    </el-input>
                </div>
            </el-row>
            <el-divider/>

            <!-- 标签组数据部分 -->
            <el-table :data="groupData" style="width: 100%" row-key="name">
                <el-table-column prop="name" label="标签组名称" />
                <el-table-column prop="description" label="标签组描述" />
                <el-table-column prop="description" label="操作">
                    <el-button type="primary" link key="label" @click="manage">标签管理</el-button>
                    <el-button type="primary" link key="label" @click="edit">编辑</el-button>
                    <el-button type="primary" link key="delete" @click="delete_">删除</el-button>
                </el-table-column>
            </el-table>

            <!-- 分页部分 -->
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

    <!-- 创建标签组对话框 -->
    <el-dialog
        v-model="dialogVisible"
        title="创建标签组"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>标签组名称</p>
            <p class="highlight">✳</p>
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
            <el-button id="complete" :disabled="disabled" type="primary" @click="add_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="dialogVisible = false">取消</el-button>
        </div>
    </el-dialog>

    <!-- 标签管理对话框 -->
    <el-dialog
        v-model="manageVisible"
        title="标签管理"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>标签组名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="tagName" placeholder="请输入名称" id="tag_name_input2" @input="if_diableBtn2"></el-input>
        </el-row>
        <el-divider/>
        <div>
            <el-button id="complete" :disabled="disabled2" type="primary" @click="manage_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="manageVisible = false">取消</el-button>
        </div>
    </el-dialog>

    <!-- 编辑标签组对话框 -->
    <el-dialog
        v-model="editVisible"
        title="编辑标签组"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>原标签组名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="formTagName" placeholder="请输入原名称" @input="if_diableBtn3"></el-input>
        </el-row>
        <br>
        <el-row class="name">
            <p>新标签组名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="nextTagName" placeholder="请输入新名称" @input="if_diableBtn3"></el-input>
        </el-row>
        <br>
        <el-row>
            <p>标签组描述</p>
            <el-input
                maxlength="100"
                placeholder="请输入标签组描述"
                show-word-limit
                type="textarea"
                :rows="6"
                v-model="nextTagGroupDescription"
            />
        </el-row>
        <el-divider/>
        <div>
            <el-button :disabled="disabled3" type="primary" @click="edit_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="editVisible = false">取消</el-button>
        </div>
    </el-dialog>

    <!-- 删除标签组对话框 -->
    <el-dialog
        v-model="deleteVisible"
        title="删除标签组"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p>标签组名称</p>
            <p class="highlight">✳</p>
            <el-input v-model="deleteName" placeholder="请输入名称" @input="if_diableBtn4"></el-input>
        </el-row>
        <el-divider/>
        <div>
            <el-button :disabled="disabled4" type="primary" @click="delete_group">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="deleteVisible = false">取消</el-button>
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
                dialogVisible: false,
                groupData:[],
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
                tagName:ref(''),
                tagGroupDescription:ref(''),
                disabled:true,
                disabled2:true,
                disabled3:true,
                disabled4:true,
                group_name:ref(''),
                this_tag:ref(''),
                manageVisible:false,
                editVisible:false,
                deleteVisible:false,
                formTagName:ref(''),
                nextTagName:ref(''),
                nextTagGroupDescription:ref(''),
                deleteName:ref('')
            };
        },
        created(){
            this.calldata();
        },
        methods:{
            //管理对话框中按钮
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
                if(this.tagName!="")
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
                if(this.formTagName!=""&&this.nextTagName!="")
                {
                    this.disabled3=false;
                }
                else
                {
                    this.disabled3=true;
                }
            },

            if_diableBtn4()
            {
                if(this.deleteName!="")
                {
                    this.disabled4=false;
                }
                else
                {
                    this.disabled4=true;
                }
            },

            //新增标签组
            add_group()
            {
                const data = {
                    "name": this.newTagName,
                    "description": this.tagGroupDescription
                };
                return fetch("/api/addgroup",{
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
                        alert("标签组名称重复!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/taggroupblank");
                    }
                    this.dialogVisible=false;   
                })
            },

            //获取标签组数据
            calldata(){
                return fetch("/api/callGroup").then((res)=>res.json().then((j)=>{
                    for(var i=0;i<j.names.length;i++)
                    {
                        this.groupData.push({"name":j.names[i],"description":j.descriptions[i]});
                    }
                }))
            },

            //标签管理
            manage()
            {
                this.manageVisible=true;   
            },
            manage_group()
            {
                this.manageVisible=false;
                const data = {
                    "name": this.tagName,
                };
                return fetch("/api/managegroup",{
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
                        alert("标签组名称不存在!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/text/taggroup");
                    }   
                })
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
                    "description": this.nextTagGroupDescription
                };
                return fetch("/api/editgroup",{
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
                        alert("原标签组名称不存在!");
                    }
                    else if(j.isok === "repeat")
                    {
                        alert("新标签组名称重复!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/taggroupblank");
                    }   
                })
            },

            //删除标签组
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
                return fetch("/api/deletegroup",{
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
                        alert("标签组名称不存在!");
                    }
                    else
                    {
                        this.$router.push("/index/manage/dataset/pic/taggroupblank");
                    }   
                })
            },

            //搜素标签组
            search_group()
            {
                if(this.tagGroupName!="")
                {
                    const data = {
                        "name": this.tagGroupName,
                    };
                    return fetch("/api/searchGroup",{
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data)
                    })
                    .then(res => res.json())
                    .then((j)=>{
                        this.groupData=[];
                        for(var i=0;i<j.names.length;i++)
                        {
                            this.groupData.push({"name":j.names[i],"description":j.descriptions[i]});
                            //this.$router.push("/index/manage/dataset/pic/taggroupblank");
                        }
                    })
                }
                else
                {
                    return fetch("/api/callGroup").then((res)=>res.json().then((j)=>{
                        for(var i=0;i<j.names.length;i++)
                        {
                            this.groupData.push({"name":j.names[i],"description":j.descriptions[i]});
                            this.$router.push("/index/manage/dataset/pic/taggroupblank");
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
    .highlight
    {
        color:red;
        font-weight:900;
    }
    .dialog_divider
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
