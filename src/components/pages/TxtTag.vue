<template>
    <div class="mytest1">我的数据总览 >
    </div>
     <div class="mytest2">【文本】 test/V1/查看
        </div>

    <el-radio-group v-model="radio1" size="large" class="mytest3">
                    <el-radio-button label="全部(6)" />
                    <el-radio-button label="有标注信息(6)" />
                    <el-radio-button label="无标注信息(0)" />
                </el-radio-group>

    <el-button class="mytest4">导入文本</el-button>
    <div class="mytest5">testV1版本的文本列表</div>

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
                        <el-button @click="visible = !visible"   class="mytest6">筛选&nbsp;<el-icon><ArrowDownBold /></el-icon></el-button>
                    </template>
                </el-popover>

    <div class="mytest7">当前数据集标注模板：短文本单标签，共有文本：6个</div>

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
    <el-table-column
                     prop="todo"
                     label="操作">
    </el-table-column>

</el-table>



</template>

<script>
export default{
    name: 'TxtTag',
data(){
        return {
            tableData: [
            {
                num: 1,
                text: '西瓜',
                todo:'?',

            },
            {
                num: 2,
                text: '苹果',
                todo: '?',

            },
             {
                num: 3,
                text: '香蕉',
                todo: '?',

            },
             {
                num: 4,
                text: '语文',
                todo: '?',

            },
             {
                num: 5,
                text: '数学',
                todo: '?',

            },
             {
                num: 6,
                text: '英语',
                todo: '?',

            }
            ]
        }
    }


}
</script>

<style scoped>
.mytest1{
    margin-left: 15px;
    margin-top: 25px;
    font-size:15px;
     color: #8e8483;
}
.mytest2{
   margin:5px;
    margin-top: 25px;
    margin-left:15px;
    font-size:15px;
     color: #0d0c0c;
}
.mytest3{
    position: absolute;
    margin-top:80px;
    margin-left:210px;
}
.mytest4{
    position: absolute;
    margin-top:90px;
    margin-left:1000px;
}
.mytest5{
    position:absolute;
    margin-top: 160px;
    margin-left:210px;
    font-size:15px;
     color: #0d0c0c;
}

.mytest6{
    position:absolute;
    margin-top: 155px;
    margin-left:405px;
}

.mytest7{
    position:absolute;
    margin-left: 210px;
    margin-top: 500px;
    font-size:15px;
     color: #8e8483;
}

.mytest8{
    position:absolute;
    margin-left: 210px;
    margin-top: 200px;
    font-size:15px;
     color: #8e8483;
}


</style>
