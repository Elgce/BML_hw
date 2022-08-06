<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider />
        <el-main>
            <el-form :model="form" label-width="120px" style="max-width: 650px">
                <el-form-item label="数据集名称">
                    <el-input v-model="form.name" placeholder="限制50个字符以内(支持汉字、英文大小写、数字及下划线，下划线不能作为开头)"/>
                </el-form-item>
                <el-form-item label="数据类型">
                    <el-radio-group v-model="radio" color="blue">
                        <el-radio-button label="pic" @click="topic">图片</el-radio-button>
                        <el-radio-button label="txt" @click="totxt">文本</el-radio-button>
                        <el-radio-button label="table" @click="totab">表格</el-radio-button>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="数据集版本">
                    <el-ratio-button disabled>V1</el-ratio-button>
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio label="图像分类" @click="fenlei"/>
                    <el-radio label="物体检测" @click="jiance"/>
                    <el-radio label="图像分割" @click="fenge"/>
                    <el-radio label="OCR标注" @click="biaozhu"/>
                </el-radio-group>
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="pic.quanxian===1 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="单图单标签"/>
                    <el-radio label="单图多标签"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===2 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="矩形框标注"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===3 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="实例分割"/>
                    <el-radio label="语义分割"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===4 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="非结构化文字识别"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio label="文本分类" @click="leifen"/>
                    <el-radio label="短文本相似度" @click="xiangsi"/>
                    <el-radio label="序列标注" @click="xulie"/>
                    <el-radio label="文本实体抽取" @click="chouqu"/>
                </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===1 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="短文本单标签"/>
                    <el-radio label="短文本多标签"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===2 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="短文本相似度"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===3 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="IOB标注模式"/>
                    <el-radio label="IO标注模式"/>
                    <el-radio label="IOE标注模式"/>
                    <el-radio label="IOBES标注模式"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===4 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio label="文本实体抽取"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2 && txt.quanxian!=0" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="数据集属性">
                    <el-radio-group v-model="form.direction">
                        <el-radio label="数据自动去重"/>
                        <el-radio label="数据不去重"/>
                    </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===3" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="技术方向">
                    <el-radio-group v-model="form.direction">
                        <el-radio label="表格预测"/>
                    </el-radio-group>
                </el-form-item>
            </el-form>
            
            <el-row class="mb-4">
                <el-button type="primary" @click="createdata">创建并导入</el-button>
                <el-button type="success">完成创建</el-button>
                <el-button type="warning" @click="cancel">取消</el-button>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>
import Breadcrumb from "../BreadCrumb.vue"
import { reactive } from 'vue'
import { ref } from 'vue'

export default{
    components: {
        Breadcrumb,
    },
    setup(){
        let form = reactive({
            name: '',
            type: '',
            model: '',
            direction: '',
        });
        let qx = reactive({
            quanxian : 0,
        });
        let txt = reactive({
            quanxian : 0,
        });
        let pic = reactive({
            quanxian: 0,
        })
        let bqw = 1;
        let radio = ref('');
        return{
            form,
            bqw,
            radio,
            qx,
            txt,
            pic,
        }
    },
    methods: {
        createdata() {
            let name = this.form["name"];
            let specy = this.radio;
            const data = {
                "data_id": name,
                "group_id": name,
                "name": name,
                "version": "V1",
                "num": 0,
                "in_state": "已完成",
                "specy": specy,
                "mark_state": 0,
                "clear_state": "-",
            }
            return fetch("/api/adddata",{
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(()=>{
                this.$router.push("/index/manage/dataset")
            })
        },
        cancel(){
            this.$router.push("/index/manage/dataset")
        },
        topic (){
            this.qx.quanxian = 1;
        },
        totxt (){
            this.qx.quanxian = 2;
        },
        totab (){
            this.qx.quanxian = 3;
        },
        fenlei (){
            this.pic.quanxian = 1;
        },
        jiance (){
            this.pic.quanxian = 2;
        },
        fenge (){
            this.pic.quanxian = 3;
        },
        biaozhu () {
            this.pic.quanxian = 4;
        },
        leifen () {
            this.txt.quanxian = 1;
        },
        xiangsi() {
            this.txt.quanxian = 2;
        },
        xulie () {
            this.txt.quanxian = 3;
        },
        chouqu () {
            this.txt.quanxian = 4;
        }
    }
}
</script>

<!-- <script setup>
import Breadcrumb from "../BreadCrumb.vue"
import { reactive } from 'vue'
import {ref} from 'vue'
import {useRouter} from 'vue-router'

const form = reactive({
  name: '',
  type: '',
  model: '',
  direction: '',
})

const radio = ref('')
let bqw = 0
const createdata = () => {
    bqw = bqw + 1
    const data = {
        "data_id": bqw.toString(),
        "group_id": "group_id",
        "name": "name",
        "version": "version",
        "num": "num",
        "in_state": "in_state",
        "specy": "specy",
        "mark_state": "mark_state",
        "clear_state": "clear_state",
    }
    return fetch("/api/adddata",{
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(()=>{
        const router = useRouter();
        router.push({
            path:"/index/manage/dataset",
        })
    })
}

const qx = reactive({
    quanxian: 0,
})
const topic = ()=>{
    qx.quanxian = 1;
}
const totxt = ()=>{
    qx.quanxian = 2;
}
const totab = ()=>{
    qx.quanxian = 3;
}

const pic = reactive({
    quanxian: 0,
})
const fenlei = () =>{
    pic.quanxian = 1;
}
const jiance = () =>{
    pic.quanxian = 2;
}
const fenge = () =>{
    pic.quanxian = 3;
}
const biaozhu = () =>{
    pic.quanxian = 4;
}

const txt = reactive({
    quanxian: 0,
})
const leifen = () => {
    txt.quanxian = 1;
}
const xiangsi = () => {
    txt.quanxian = 2;
}
const xulie = () => {
    txt.quanxian = 3;
}
const chouqu = () => {
    txt.quanxian = 4;
}

</script> -->


<style scoped>
    .el-header  {
        height: 56px;
    }
    .el-divider{
        margin: 0;
    }
    .mb-4{
        margin-left: 120px;
    }
    .mb-4 .el-button{
        width: 110px;
    }
</style>