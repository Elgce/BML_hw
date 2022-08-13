<template>
  <div class="weiyang_ml">
    <div id="header">
    <nav class="top_navbar">
      <ul>
        <li id="msi">
          <a href="">
            <img src="../assets/msi.jpg" height="46" id="imgmsi"/>
          </a>
        </li>
        <li><a href="">产品介绍</a></li>
        <li><a href="">数据服务</a></li>
        <li>
          <a href="">使用文档</a>
          <ul class="hide">
            <li><a href="">平台介绍</a></li>
            <li><a href="">数据采集</a></li>
            <li><a href="">数据标注</a></li>
            <li><a href="">数据清洗</a></li>
            <li><a href="">数据增强</a></li>
            <li><a href="">联系我们</a></li>
          </ul>
        </li>
        <li id="shequ"><a href="">社区</a></li>
      </ul>
    </nav>
    </div>
    <div id="leftnav">
      
      <!-- <el-divider /> -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
      <div id="navtop" @click="toggleCollapse">
          <el-icon color="gray" ><DArrowRight /></el-icon>
          <span id="navlogo"  class="mb-2">MSIML数据服务</span>
      </div>
      <el-menu
        :default-active="$route.path"
        router 
        background-color="rgb(235, 231, 231)"
        text-color="#rgb(0,0,0)"
        class="el-menu-vertical-demo"
        mode="vertical"
        :collapse="isCollapse"
        :collapse-transition="false"
      >

        <el-divider />
        <el-sub-menu index="1">
          <template #title>
            <el-icon color="#409EFC"><Menu /></el-icon>
            <span class="submenu">数据总览</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/index/manage/dataset">数据集管理</el-menu-item>
            <el-menu-item index="/index/manage/dataset/insert">数据源管理</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
        <el-divider />
        <el-sub-menu index="2">
          <template #title>
            <el-icon color="#409EFC"><EditPen /></el-icon>
            <span class="submenu">数据标注</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="/index/menu3">标签组管理</el-menu-item>
            <el-menu-item index="/index/manage/dataset/pic/addtag">在线标注</el-menu-item>
            <el-menu-item index="/index/manage/dataset/video/addtag">智能标注</el-menu-item>
            <el-menu-item index="/index/manage/dataset/text/addtag">多人标注</el-menu-item>
            <el-menu-item index="2-5">寻求标注支持</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
        <el-divider />
        <el-sub-menu index="3">
          <template #title>
            <el-icon color="#409EFC"><PieChart /></el-icon>
            <span class="submenu">数据采集</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1">摄像头采集图片</el-menu-item>
            <el-menu-item index="3-2">云服务回流图片</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
        <el-divider />
        <el-sub-menu index="4">
          <template #title>
            <el-icon color="#409EFC"><CollectionTag /></el-icon>
            <span class="submenu">数据处理</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="4-1">清洗任务管理</el-menu-item>
            <el-menu-item index="4-2">增强任务管理</el-menu-item>
          </el-menu-item-group>
        </el-sub-menu>
      </el-menu>
      </el-aside>
    </div>
  </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      isCollapse: false
    }
  },
  methods: {
    toggleCollapse() {
      this.isCollapse = !this.isCollapse;
      document.getElementById("navlogo").style.display= this.isCollapse? "none" : "inline";
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #navtop{
    height: 50px;
  }
  .el-divider--horizontal{
    margin: 0;
    background: 0 0;
    border-top: 1px solid rgb(222, 219, 219);
  }
  #leftnav{
    background-color: rgb(235, 231, 231);
    height: 100vh;
    margin-left: -8px;
    margin-bottom: -10px;
  }
  .submenu{
    font-weight: bold;
    color: rgb(91, 92, 92);
  }
  #navtop{
    margin-top: 20px;
    margin-bottom: -15px;
  }
  .mb-2{
    text-align: left;
    margin-left: 10px;
    height: 20px;
    font-size: 1.2rem;
    font-weight: bold;
    font-family: '华文行楷','Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }
/* css style for head navigator */
  #header{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: black;
    display: flex;
    align-items: center;
    float: left;
    justify-content: space-between;
  }
  .top_navbar ul{
    display: flex;
  }
  .top_navbar ul li{
    float: left;
    font-weight: normal;
    width: 128px;
    list-style: none;
    text-align: center;
  }
  .top_navbar ul li a{
    width: 128px;
    line-height: 27px;
    font-size: auto;
    color: white;
    font-family: STHeiti, SimHei, sans-serif;
    font-size: 15px;
  }
  .top_navbar ul li a:hover{
    color: rgb(115, 149, 241);
  }
  .top_navbar ul li ul{
    background: black;
    position: absolute;
    display: none;
    text-align: center;
  }
  .top_navbar ul li ul li{
    margin-top: 20px;
    height: 40px;
    margin-left: -42px;
    float: none;
    text-align: center;
  }
  .top_navbar ul li:hover ul{
    display: block;
    width: 80px;
  }
  a{
    text-decoration: none;
  }
  #shequ{
    position: absolute;
    left: 1400px;
  }
  #msi{
    margin-top: -8px;
    margin-bottom: -80px;
    margin-left: -10px;
    margin-right: 20px;
    border-radius: 20px;
  }
  #imgmsi{
    border-radius: 23px;
  }
</style>
