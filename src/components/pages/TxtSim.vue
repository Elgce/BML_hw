<!-- 文本相似度页面 -->
<template>
        <el-container>

            <!-- 头部元素 -->
            <el-header>
                <Breadcrumb></Breadcrumb>
            </el-header>
            <el-divider />

            <!-- 主体部分 -->
            <el-main>
                <el-radio-group v-model="t_type" @change="handleradiochange" size="large" class="mytest3">
                    <el-radio-button label="all">全部({{all_num}})</el-radio-button>
                    <el-radio-button label="ed" >有标注信息({{ed_num}})</el-radio-button>
                    <el-radio-button label="to" >没有标注信息({{to_num}})</el-radio-button>
                </el-radio-group>
                <el-button class="txt_in" @click="insert_txt">导入文本</el-button>
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

                <!-- 标注表格 -->
                <el-table
                        :data="tableData"
                        :span-method="objectSpanMethod"
                        border
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
                    <el-table-column
                                    prop="label"
                                    label="标注详情">
                    </el-table-column>>
                    <el-table-column label="操作">
                        <template #default="scope">
                            <el-button @click="sim(scope)" type="success">Yes</el-button>
                            <el-button @click="nosim(scope)" type="danger">No</el-button>
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
        name: 'TxtSim',
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
            context_tag: reactive([]),
            tableData: [],
            name:"",

        }
    },
    created(){
        this.calltxt();
    },
    methods:{
        sim(scope){
            let num = scope.row["num"];
            const data = {"num":num,"label":"yes"};
            return fetch("/api/taglabelsim",{
                method: 'POST',
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then((res)=>res.json())
            .then(()=>{
                this.$router.push("/index/manage/dataset/blank/similarity");
            })
        },
        nosim(scope){
            let num = scope.row["num"];
            const data = {"num":num,"label":"no"};
            return fetch("/api/taglabelsim",{
                method: 'POST',
                headers:{
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then((res)=>res.json())
            .then(()=>{
                this.$router.push("/index/manage/dataset/blank/similarity");
            })
        },
        objectSpanMethod({row, column, rowIndex, columnIndex}){
            console.log(row);
            console.log(column);
            if(columnIndex===0 || columnIndex===3 || columnIndex===2){
                if(rowIndex % 2===0){
                    return{
                        rowspan: 2,
                        colspan: 1,
                    }
                }
                else{
                    return{
                        rowspan: 0,
                        colspan: 0,
                    }
                }
            }
        },
        handleradiochange(){
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
                this.$router.push("/index/manage/dataset/blank/similarity");
            })
        },
        btn_delete(scope){
            let text = scope.row["text"];
            let num = scope.row["num"];
            const data = {"text": text,"num":num};
            return fetch("/api/deletetxtsim",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(()=>{
                this.$router.push('/index/manage/dataset/blank/similarity');
            })
        },
        insert_txt(){
            this.$router.push("/index/manage/dataset/insert");
        },
        calltxt(){
            let that = this;
            return fetch("/api/gettxtsim").then((res) => res.json().then((j) => {
                that.context = j.context;
                that.all_num = j.all_num;
                that.to_num = j.to_num;
                that.ed_num = j.ed_num;
                that.name = j.name
                that.t_type = j.t_type;
                that.context_tag = j.context_tag;
                for (let item in that.context){
                    let txt = that.context[item][0];
                    let txtx = that.context[item][1];
                    let nu = parseInt(item) + 1;
                    let label = that.context_tag[item];
                    let s_label = "";
                    if(label==="yes"){
                        s_label = "相似";
                    }
                    else if(label===""){
                        s_label = "未标注";
                    }
                    else if(label==="no"){
                        s_label = "不相似";
                    }
                    let data = {"num":nu,"text":txt,"label":s_label};
                    let data1 = {"num":nu,"text":txtx,"label":s_label};
                    that.tableData.push(data);
                    that.tableData.push(data1);
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
