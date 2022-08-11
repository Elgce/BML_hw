<template>
    <el-container>
        <el-header>
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider />
        <el-main>
            <el-form :model="form" label-width="120px" style="max-width: 650px">
                <el-form-item label="数据集名称">
                    <el-input id="input_name" v-model="form.name" placeholder="限制50个字符以内(支持汉字、英文大小写、数字及下划线，下划线不能作为开头)"/>
                </el-form-item>
                <el-form-item label="数据类型">
                    <el-radio-group id="data_type" v-model="radio" color="blue">
                        <el-radio-button name="data_type" value="pic" label="pic" @click="set_qx_value(1)">图片</el-radio-button>
                        <el-radio-button name="data_type" value="txt" label="txt" @click="set_qx_value(2)">文本</el-radio-button>
                        <el-radio-button name="data_type" value="table" label="table" @click="set_qx_value(3)">表格</el-radio-button>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="数据集版本">
                    <el-ratio-button disabled>V1</el-ratio-button>
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="qx.quanxian===1" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio name="marking_type_pic" id="pic_assortment" label="图像分类" border @click="set_pic_value(1)"/>
                    <el-radio name="marking_type_pic" id="object" label="物体检测" border @click="set_pic_value(2)"/>
                    <el-radio name="marking_type_pic" id="split" label="图像分割" border @click="set_pic_value(3)"/>
                    <el-radio name="marking_type_pic" id="marking" label="OCR标注" border @click="set_pic_value(4)"/>
                </el-radio-group>
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="pic.quanxian===1 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="单图单标签"/>
                    <el-radio name="module" label="单图多标签"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===2 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="矩形框标注"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===3 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="实例分割"/>
                    <el-radio name="module" label="语义分割"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===4 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="非结构化文字识别"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio name="marking_type_text" id="text_assortment" label="文本分类" border @click="set_txt_value(1)"/>
                    <el-radio name="marking_type_text" id="similarity" label="文本相似度" border @click="set_txt_value(2)"/>
                    <el-radio name="marking_type_text" id="order_marking" label="序列标注" border @click="set_txt_value(3)"/>
                    <el-radio name="marking_type_text" id="extracting" label="实体抽取" border @click="set_txt_value(4)"/>
                </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===1 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="短文本单标签"/>
                    <el-radio name="module" label="短文本多标签"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===2 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="短文本相似度"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===3 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="IOB标注模式"/>
                    <el-radio name="module" label="IO标注模式"/>
                    <el-radio name="module" label="IOE标注模式"/>
                    <el-radio name="module" label="IOBES标注模式"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===4 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="文本实体抽取"/>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2 && txt.quanxian!=0" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="数据集属性">
                    <el-radio-group v-model="form.direction">
                        <el-radio name="dataPara" label="数据自动去重"/>
                        <el-radio name="dataPara" label="数据不去重"/>
                    </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===3" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="技术方向">
                    <el-radio-group v-model="form.direction">
                        <el-radio name="marking_type_table" id="predicting" label="表格预测" border/>
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
        isfull(){
            let inputName=document.getElementById("input_name");
            let dataType=document.getElementsByName("data_type");
            let markingTypePic=document.getElementsByName("marking_type_pic");
            let markingTypeText=document.getElementsByName("marking_type_text");
            let markingTypeTable=document.getElementsByName("marking_type_table");
            let module=document.getElementsByName("module");
            let dataPara=document.getElementsByName("dataPara");
            return (
                (dataType[0].checked) && ((inputName.value!=""&&markingTypePic[0]&&(module[0].checked||module[1].checked)) ||
                (inputName.value!=""&&markingTypePic[1].checked&&(module[0].checked)) || (inputName.value!=""&&markingTypePic[2]&&(module[0].checked||module[1].checked))||
                (inputName.value!=""&&markingTypePic[3]&&(module[0].checked)))
                ||
                ((dataType[1].checked&&(dataPara[0].checked||dataPara[1].checked)) && ((inputName.value!=""&&markingTypeText[0].checked&&(module[0].checked||module[1].checked))||
                (inputName.value!=""&&markingTypeText[1].checked&&(module[0].checked))||(inputName.value!=""&&markingTypeText[2].checked&&(module[0].checked||module[1].checked||module[2].checked||module[3].checked))||
                (inputName.value!=""&&markingTypeText[3].checked&&(module[0].checked))))
                || (dataType[2].checked && inputName.value!=""&&(markingTypeTable[0].checked))
                )
        },
        createdata() {
            let inputName=document.getElementById("input_name");
            if (this.isfull()){
                let name = this.form["name"];
                    let specy = this.radio;
                    const data = {
                        "data_id": name,
                        "group_id": name,
                        "name": name,
                        "version": "V1",
                        "num": 0,
                        "in_state": "finished",
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
            }
            else if(inputName.value==""){
                inputName.setAttribute("placeholder", "请输入数据集名称！");
            }
        },
        cancel(){
            this.$router.push("/index/manage/dataset")
        },
        set_qx_value(num){
            this.qx.quanxian = num;
        },
        set_pic_value(num){
            this.pic.quanxian = num;
        },

        set_txt_value(num){
            this.txt.quanxian = num;
        },
    }
}
</script>



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
    /* written by wjz */
    #placeholderChange::-webkit-input-placeholder
    {
        color: red;
    }
    #placeholderChange::-moz-placeholder
    {
        color: red;
    }
    #placeholderChange::-ms-input-placeholder
    {
        color: red;
    }
    #placeholderChange::-ms-input-placeholder
    {
        color: red;
    }
    #pic_assortment
    {
        background: url("../../assets/pic_assortment.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #object
    {
        background: url("../../assets/object.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #marking
    {
        background: url("../../assets/marking.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #split
    {
        background: url("../../assets/split.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #text_assortment
    {
        background: url("../../assets/text_assortment.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #similarity
    {
        background: url("../../assets/similarity.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #order_marking
    {
        background: url("../../assets/order_marking.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #extracting
    {
        background: url("../../assets/extracting.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #predicting
    {
        background: url("../../assets/predicting.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    /* written over */
</style>
