<template>
        <el-container>
            <el-header>
                <Breadcrumb></Breadcrumb>
            </el-header>
            <el-divider />
            <el-main>
                <el-radio-group v-model="t_type" @change="handleradiochange" size="large" class="mytest3">
                                <el-radio-button label="all">全部({{all_num}})</el-radio-button>
                                <el-radio-button label="ed" >有标注信息({{ed_num}})</el-radio-button>
                                <el-radio-button label="to" >没有标注信息({{to_num}})</el-radio-button>
                            </el-radio-group>

                <el-button class="txt_in" @click="insert_txt">导入文本</el-button>
                <el-button class="txt_label" type="primary" @click="label_txt">标注文本</el-button>
            <div id="top_table">
                <div class="txt_list">{{name}}V1版本的文本列表</div>

                <el-popover
                    :visible="visible"
                    placement="bottom-start"
                    :width="750"

                >
         
                <div>
                    <b>导入日期&nbsp;&nbsp;&nbsp;</b>
                    <el-checkbox v-model="unlimited1" label="不限" size="large" />
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
                    <el-checkbox v-model="unlimited2" label="不限" size="large" />
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <el-date-picker
                        type="daterange"
                        range-separator="To"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期"
                    />
                </div>
             
                    <template #reference>
                        <el-button type="primary" @click="visible = !visible"   class="choose_btn">筛选&nbsp;<el-icon><ArrowDownBold /></el-icon></el-button>
                    </template>
                </el-popover>
            </div>
                <el-table
                        :data="tableData"
                        stripe="true"
                        style="width: 100%"
                        class="mytest8">
                    <el-table-column
                                    prop="num"
                                    label="序号">
                    </el-table-column>
                    <el-table-column
                                    prop="text"
                                    label="文本内容摘要">
                    </el-table-column>
                    <el-table-column label="操作">
                        <template #default="scope">
                            <el-button type="primary" @click="btn_click(scope)">查看</el-button>
                            <el-button @click="btn_delete(scope)">删除</el-button>
                        </template>
                    </el-table-column>

                </el-table>
            
                <div class="txt_num">当前数据集标注模板：短文本单标签，共有文本：{{all_num}}个</div>
            </el-main>
</el-container>

</template>

<script>
import { reactive, ref } from 'vue';
import Breadcrumb from '../BreadCrumb.vue'

    export default{
        name: 'TxtTag',
        components:{
            Breadcrumb,
        },
    data(){
        return {
            all_num: -1,
            ed_num: -1,
            to_num: -1,
            t_type: ref('all'),
            context: reactive([]),
            tableData: [],
            name:"",

        }
    },
    created(){
        this.calltxt();
    },
    methods:{
        btn_click(scope){
            console.log(scope.row["num"]);
            const data = {"page":scope.row["num"]};
            return fetch("/api/txtpagesession",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then((res) => res.json)
            .then(()=>{
                this.$router.push("/index/manage/dataset/wholetxt");
            })
        },
        handleradiochange(){
            console.log(this.t_type);
            const data = {"t_type": this.t_type};
            return fetch("/api/sessiontype",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then((res)=>res.json())
            .then(()=>{
                this.$router.push("/index/manage/dataset/txt/extract/blank");
            })
        },
        label_txt(){
            const data = {"page":1};
            return fetch("/api/txtpagesession",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then((res) => res.json)
            .then(()=>{
                this.$router.push("/index/manage/dataset/wholetxt");
            })
        },  
        btn_delete(scope){
            console.log(scope.row["text"]);
            let text = scope.row["text"];
            let num = scope.row["num"];
            const data = {"text": text,"num":num};
            return fetch("/api/deletetxt",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(()=>{
                this.$router.push('/index/manage/dataset/txt/extract/blank');
            })
        },
        insert_txt(){
            this.$router.push("/index/manage/dataset/insert");
        },
        calltxt(){
            let that = this;
            return fetch("/api/gettxtextracted").then((res) => res.json().then((j) => {
                that.context = j.context;
                that.all_num = j.all_num;
                that.to_num = j.to_num;
                that.ed_num = j.ed_num;
                that.name = j.name
                that.t_type = j.t_type;
                console.log(that.context);
                for (let item in that.context){
                    let txt = that.context[item];
                    let nu = parseInt(item) + 1;
                    let data = {"num":nu,"text":txt};
                    that.tableData.push(data);
                }
            }))
        },
    }


}
</script>

<style scoped>
    #top_table{
        position: relative;
        display: flex;
        margin-top: 20px;
    }
    .el-header{
        height: 56px;
    }
    .el-divider{
        margin:0;
    }
    .txt_list{
        position: relative;
    }
    .mytest3{
        position: relative;
        margin-left: -40px;
    }
    .txt_in{
        position: relative;
        margin-left: 880px;
    }
    .txt_label{
        position: relative;
        margin-left: 40px;
    }
    .txt_num{
        position: relative;
        font-size:15px;
        color: #8e8483;
        margin-top: 40px;
        margin-left: -1080px;
    }
    .choose_btn{
        position: relative;
        margin-left: 40px;
    }


</style>
