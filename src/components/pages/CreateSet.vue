<!-- 创建数据集页面 -->
<template>
    <el-container>
        <!-- 头部元素 -->
        <el-header>
            <Breadcrumb></Breadcrumb>
        </el-header>
        <el-divider />

        <!-- 主体部分 -->
        <el-main>

            <!-- 创建数据集的表单 -->
            <el-form :model="form" label-width="120px" style="max-width: 650px">
                <el-form-item label="数据集名称">
                    <el-input id="input_name" v-model="form.name" placeholder="限制50个字符以内(支持汉字、英文大小写、数字及下划线，下划线不能作为开头)"/>
                </el-form-item>
                <el-form-item label="数据类型">
                    <el-radio-group id="data_type" v-model="radio" color="blue">
                        <el-radio-button name="data_type" value="pic" label="pic" @click="set_qx_value(1)">图片</el-radio-button>
                        <el-radio-button name="data_type" value="txt" label="txt" @click="set_qx_value(2)">文本</el-radio-button>
                        <el-radio-button name="data_type" value="table" label="table" @click="set_qx_value(3)">表格</el-radio-button>
                        <el-radio-button name="data_type" value="video" label="video" @click="set_qx_value(4)">视频</el-radio-button>
                        <el-radio-button name="data_type" value="audio" label="audio" @click="set_qx_value(5)">音频</el-radio-button>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="数据集版本">
                    V1
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="qx.quanxian===1" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio name="marking_type_pic" id="pic_assortment" label="pic_cla" border @click="set_pic_value(1)">图像分类</el-radio>
                    <el-radio name="marking_type_pic" id="object" label="pic_det" border @click="set_pic_value(2)">物体检测</el-radio>
                    <el-radio name="marking_type_pic" id="split" label="pic_div" border @click="set_pic_value(3)">图像分割</el-radio>
                    <el-radio name="marking_type_pic" id="marking" label="pic_ocr" border @click="set_pic_value(4)">OCR标注</el-radio>
                </el-radio-group>
                </el-form-item>
            </el-form>
            <el-form id="test" v-if="pic.quanxian===1 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="ss">单图单标签</el-radio>
                    <el-radio name="module" label="sm">单图多标签</el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===2 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="rec">矩形框标注</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===3 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="insdiv">实例分割</el-radio>
                    <el-radio name="module" label="meandiv">语义分割</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="pic.quanxian===4 && qx.quanxian===1" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="recog">非结构化文字识别</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="标注类型">
                    <el-radio-group v-model="form.type">
                    <el-radio name="marking_type_text" id="text_assortment" label="txt_cla" border @click="set_txt_value(1)">文本分类</el-radio>
                    <el-radio name="marking_type_text" id="similarity" label="txt_sim" border @click="set_txt_value(2)">文本相似度</el-radio>
                    <el-radio name="marking_type_text" id="order_marking" label="txt_cons" border @click="set_txt_value(3)">序列标注</el-radio>
                    <el-radio name="marking_type_text" id="extracting" label="txt_extr" border @click="set_txt_value(4)">实体抽取</el-radio>
                </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===1 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="txt_slabel">短文本单标签</el-radio>
                    <el-radio name="module" label="txt_mlabel">短文本多标签</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===2 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="txt_sim">短文本相似度</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===3 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="txt_iob">IOB标注模式</el-radio>
                    <el-radio name="module" label="txt_io">IO标注模式</el-radio>
                    <el-radio name="module" label="txt_ioe">IOE标注模式</el-radio>
                    <el-radio name="module" label="txt_iobes">IOBES标注模式</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="txt.quanxian===4 && qx.quanxian===2" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="标注模板">
                    <el-radio-group v-model="form.model">
                    <el-radio name="module" label="txt_extr">文本实体抽取</el-radio>
                </el-radio-group>
            </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===2 && txt.quanxian!=0" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="数据集属性">
                    <el-radio-group v-model="form.single">
                        <el-radio name="dataPara" label="dir_auto">数据自动去重</el-radio>
                        <el-radio name="dataPara" label="dir_no">数据不去重</el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===3" :model="form" label-width="120px" style="max-width: 650px" :key="1">
                <el-form-item label="技术方向">
                    <el-radio-group v-model="form.direction">
                        <el-radio name="marking_type_table" id="predicting" label="table_pre" border>表格预测</el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>
            
            <el-form id="test" v-if="qx.quanxian===4" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="技术方向">
                    <el-radio-group v-model="form.direction">
                        <el-radio name="marking_type_video" id="video_assortment" label="vid_ass" border>视频分类</el-radio>
                        <el-radio name="marking_type_video" id="video_splitting" label="vid_spl" border>视频分割</el-radio>
                    </el-radio-group>
                </el-form-item>
            </el-form>

            <el-form id="test" v-if="qx.quanxian===5" :model="form" label-width="120px" style="max-width: 1550px" :key="1">
                <el-form-item label="技术方向">
                    <el-radio-group v-model="form.direction">
                        <el-radio name="marking_type_audio" id="audio_assortment" label="aud_ass" border>音频分类</el-radio>
                        <el-radio name="marking_type_audio" id="audio_splitting" label="aud_spl" border>音频分割</el-radio>
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
            single: '',
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
        //表单校验
        isfull(){
            let inputName=document.getElementById("input_name");
            let dataType=document.getElementsByName("data_type");
            let markingTypePic=document.getElementsByName("marking_type_pic");
            let markingTypeText=document.getElementsByName("marking_type_text");
            let markingTypeTable=document.getElementsByName("marking_type_table");
            let markingTypeVideo=document.getElementsByName("marking_type_video");
            let markingTypeAudio=document.getElementsByName("marking_type_audio");
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
                || 
                (dataType[2].checked && inputName.value!=""&&(markingTypeTable[0].checked))
                || 
                (dataType[3].checked && inputName.value!=""&&(markingTypeVideo[0].checked||markingTypeVideo[1].checked))
                || 
                (dataType[4].checked && inputName.value!=""&&(markingTypeAudio[0].checked||markingTypeAudio[1].checked))
                )
        },

        //创建数据集
        createdata() {
            let inputName=document.getElementById("input_name");
            if (this.isfull()){
                let name = this.form["name"];
                    let specy = this.radio;
                    let label_type = this.form["type"];
                    let label_model = this.form["model"];
                    let is_single = this.form["single"];//数据去重或不去重
                    let direction = this.form["direction"];
                    const data = {
                        "data_id": name,
                        "group_id": name,
                        "name": name,
                        "version": "V1",
                        "num": 0,
                        "in_state": "finished",
                        "specy": specy,//通过this.radio保存下创建过程中“数据类型”一栏的数据
                        "mark_state": 0,
                        "clear_state": "-",
                        "label_type": label_type,
                        "label_model": label_model,
                        "data_single": is_single,
                        "direction": direction,
                    };
                    console.log(data);
                    return fetch("/api/adddata",{
                        method: 'POST',
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data)
                    })
                    .then(res => res.json())
                    .then((j)=>{
                        if(j.isok === "repeat"){
                            alert("数据集名字重复!");
                        }
                        else{
                            this.$router.push("/index/manage/dataset/insert");
                        }
                        
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
    #video_assortment
    {
        background: url("../../assets/video_assortment.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #video_splitting
    {
        background: url("../../assets/video_splitting.png") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #audio_assortment
    {
        background: url("../../assets/audio_marking.jpg") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
    #audio_splitting
    {
        background: url("../../assets/audio_splitting.jpg") no-repeat;
        width:312px;
        height:160px;
        background-position-x:100px;
    }
</style>
