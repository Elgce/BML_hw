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
    <div id="left">
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span id="lefthead">MSI ML数据服务</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>数据集管理</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>数据源管理</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>标签组管理</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>在线标注</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>智能标注</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>多人标注</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>寻求标注支持</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>摄像头采集图片</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>云服务回流图片</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>清洗任务管理</span></a>
      <a href="" class="box"><i class="left_label" aria-hidden="true"></i><span>增强任务管理</span></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #left{
    margin: 0;
    padding: 0;
    margin-left: -8px;
    width: 10px;
    height: 100vh;
    display: flex;
    justify-content: top;
    align-items: center;
    flex-direction: column;
    background-color: rgb(235, 231, 231);
    transition: .3s;
  }
  .box{
    display: block;
    height: 30px;
    width: 85%;
    margin: 9px;
    border-radius: 5px;
    position: relative;
    color: black;
    font-size: 0.9rem;
  }
  #left a i{
    position: absolute;
    margin: 14px 0 0 7px;
  }
  .box span{
    position: relative;
    top: 14px;
    opacity: 0;
    float: left;
  }
  #left:hover{
    width:240px;
  }
  #left:hover span{
    opacity: 1;
  }
  #lefthead{
    font-size: 1.3rem;
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
