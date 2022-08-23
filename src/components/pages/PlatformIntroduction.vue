<template>
<el-main>
<p class="index">帮助文档 > MSI ML数据标注平台</p>
<p class="title">什么是MSI ML</p>
<p class="update-time">更新时间：2022-08-24</p>

<p class="intro">MSIML 数据标注平台是一个面向企业和个人开发者的机器学习集成开发环境，具有文本标注、文本相似度判断、文本抽取、图片标注、视频分段、视频分类等数据打标功能，为经典机器学习和深度学习提供了从数据处理、模型训练、模型管理到模型推理的全生命周期管理服务，帮助用户更快的构建、训练和部署模型。</p>
<ul class="chart">
		<li>文本标注
            <div>MSIML支持用户以txt文本与zip压缩包（注意：只能对原始的文件们进行压缩，不能对一个装有文件的文件夹压缩，下同）的形式导入数据。用户可自定义标签，并对数据以标签的形式分类。</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图1.文本标注创建界面</div>
        </li>
		<li>文本相似度（短文本匹配）
            <div>MSIML支持用户以txt格式与zip压缩包导入数据。文本文件内数据格式要求为"文本内容\n"（即每行一个未标注样本，使用回车换行），每一行表示一组数据。用户可对每组数据进行判断，打标“相似”或“不相似”，或删除本组数据。</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图2.文本相似度判断界面</div>
        </li>
		<li>文本实体抽取
            <div>MSIML支持用户以txt格式与zip压缩包导入数据。用户可自定义标签，并对文本中的某些段落利用标签作标记。标签的颜色可由用户自定义。</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图3.文本实体抽取处理界面</div>
        </li>
        <li>图片标注
            <div>MSIML支持用户以png形似或zip压缩包导入图片。用户可自定义标签，并标记对应的图片</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图4.图片标注界面</div>
        </li>
        <li>视频分类
            <div>MSIML支持用户以txt格式与zip压缩包导入数据。用户可自定义标签，并对文本中的某些段落利用标签作标记。标签的颜色可由用户自定义。</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图5.视频分类界面</div>
        </li>
        <li>视频分段
            <div>MSIML支持用户以txt格式与zip压缩包导入数据。用户可自定义标签，并对文本中的某些段落利用标签作标记。标签的颜色可由用户自定义。</div>
            <img src="../../assets/fenlei.png" width="800" height="350">
            <div class="mark">图6.视频分段界面</div>
        </li>
	</ul>
</el-main>
</template>


<script>
    export default
    {
        name: "PlatformIntro",
        data()
        {
            return{
                
            };
        },
        methods:{

        }
    }


</script>


<style scoped>
.index{
    position:absolute;
    font-size: 16px;
    color:black;
    margin-left: 220px;
}

.title{
    position:absolute;
    font-size: 28px;
    color:black;
    margin-top:60px;
    margin-left: 220px;
}
.update-time{
    position:absolute;
    font-size: 14px;
    color:grey;
    margin-top:105px;
    margin-left: 220px;
}

.intro{
    position:absolute;
    text-align: left;
    text-align: justify;
    width: 800px;
    font-size: 16px;
    color:black;
    margin-top:140px;
    margin-left: 220px;
}

.chart{
    position:absolute;
    font-size: 18px;
    width: 800px;
    text-align: left;
    color:black;
    margin-top:240px;
    margin-left: 220px;
}

div{
    font-size:14px;
    margin: 15px;
}

.mark{
    font-size:14px;
    text-align: center;
    margin: 15px;
}
li{
    margin:15px;
}
</style>
