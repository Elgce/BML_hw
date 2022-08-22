<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider id="top_divider"/>
        <p id='welcome'>请选择参数值：</p>
        <el-divider/>
        <el-row v-loading="loading" element-loading-text="训练中...">
            <p class="text">神经元个数</p>
            <el-slider 
                v-model="num" 
                class="slider" 
                show-input 
                :min="2" 
                :max="2048"/>
        </el-row>
        <el-row v-loading="loading" element-loading-text="请稍候...">
            <p class="text">训练数占比(%)</p>
            <el-slider 
                v-model="train_ratio" 
                class="slider" 
                show-input 
                :min="60" 
                :max="90"/>
        </el-row>
        <br>
        <el-divider/>
        <el-row id="two_btns">
            <el-button type="primary" id="start_btn" size="large" @click="start_training" :disabled="disabled">开始训练</el-button>
            <el-button type="primary" id="search_btn" size="large" disabled>图像识别</el-button>
        </el-row>
    </el-container>

    <!-- 准确度对话框 -->
    <el-dialog
        v-model="accVisible"
        title="准确度"
        width="30%"
        :before-close="handleClose"
    >
        <el-divider class="dialog_divider"/>
        <el-row class="name">
            <p id="accuracy">{{accuracy}}</p>
        </el-row>
        <el-divider/>
        <div>
            <el-button :disabled="disabled" type="primary" @click="accVisible = false">确认</el-button>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <el-button @click="accVisible = false">取消</el-button>
        </div>
    </el-dialog>
</template>


<script>
import Breadcrumb from "../BreadCrumb.vue"
import { ref } from "vue"
    export default
    {
        name: "PlatformIntro",
        components: 
        {
            Breadcrumb,
        },
        data()
        {
            return{
                num:ref(0),
                train_ratio:ref(0),
                disabled:false,
                accuracy:ref(0),
                accVisible:false,
                loading:ref(false)
            };
        },
        methods:{
            start_training()
            {
                this.loading=true;
                this.disabled=true;
                const data = {
                    "num": this.num,
                    "train_ratio":this.train_ratio
                };
                return fetch("/api/start_training",{
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(data)
                })
                .then(res => res.json())
                .then((j)=>{
                    this.accuracy=j.accuracy;
                    this.disabled=false;
                    this.accVisible=true;
                    this.loading=false;
                })
            },
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
    .text
    {
        margin-left: 200px;
    }
    #welcome
    {
        /* margin-left:100px; */
        font-size: 20px;
        font-weight: 700;
    }
    .slider
    {
        margin-left: 200px;
        margin-right: 300px;
    }
    #start_btn
    {
        width:100px;
        margin-right: 100px;
    }
    #search_btn
    {
        width:100px;
        /* margin: auto;
        margin-top: 0px; */
    }
    #two_btns
    {
        margin:auto;
        margin-top:100px;
    }
    .dialog_divider
    {
        margin-top:-30px;
    }
    #accuracy
    {
        margin: auto;
    }

</style>