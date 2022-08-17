<template>
    <el-main>
        <video id="myVideo" width="500" height="400" >
            <source src="../../assets/movie.mp4"  type="video/mp4">
        </video>
        <el-button color="#F56C6C" @click="classify(1)" :disabled="state!=2">第一类</el-button>
        <el-button color="#409EFF" @click="classify(2)" :disabled="state!=2">第二类</el-button>
        <el-button @click="del()" :disabled="state!=3">删除该片段</el-button>
        <div id="test" style="width:500px; height:100px; display: block;"
            @mousedown="down($event)"
            @mouseup="up($event)"
            @mousemove="move($event)">
            <div v-for="(slice,index) in slices" :key="index" 
                :class="'sl sl'+slice.type"
                :id="'sl'+index"
                :style="{left:slice.ts+'px',width:slice.te-slice.ts+'px'}"
                @mousedown="chooseSlice(index,$event)"
                @mousemove="resize(index,$event)"
                @mouseenter="addConf(index,$event)">
            </div>
            <div v-if="state==1 || state==2" id="chosen" 
                :style="{left:Math.min(start,end) + 'px',width:Math.abs(end - start) + 'px'}">
            </div>
        </div>
    </el-main>
    
</template>


<script>

export default{
    name: "AddTag",
    data(){
        return{
            slices:[],
            start:0,
            end:0,
            state:0,
            chosenIndex:-1,
            sliceConflict:-1,
        }
    },
    mounted(){


    },
    methods:{
        setVideoTime(t){
            var video = document.getElementById("myVideo")
            video.currentTime = t;
        },

        convertXtoT(x){
            var video = document.getElementById("myVideo")
            var progress = document.getElementById("test")
            var w_str = progress.style.width
            var w = w_str.substring(0,w_str.length-2)
            var l = progress.getBoundingClientRect().left
            return (x-l)/w * video.duration
        },

        nearEdge(index,x){
            var l = this.slices[index].ts
            var r = this.slices[index].te
            var dl = Math.abs(l-x)
            var dr = Math.abs(r-x)
            return dl>dr ? r : l
        },

        addConf(index,e){
            var x = this.nearEdge(index,e.x)
            if(this.state == 1){
                if(this.sliceConflict == -1){
                    this.sliceConflict = x
                }
                else if(this.sliceConflict < this.start && this.start < e.x){
                    this.sliceConflict = x
                }
                else if(this.sliceConflict > this.start && this.start > e.x){
                    this.sliceConflict = x
                }
            }
        },

        down(e){
            if(this.state == 0 || this.state == 2){
                this.start = e.x
                this.end = e.x
                this.state = 1 // 表示进入选择状态
                this.sliceConflict = -1
            }

            if(this.state == 3){
                var sl = document.getElementById('sl'+this.chosenIndex)
                sl.style.opacity = '50%'
                this.start = e.x
                this.end = e.x
                this.state = 1 // 表示进入选择状态
            }
            var t = this.convertXtoT(e.x)
            this.setVideoTime(t)
        },

        checkConflict(){
            if(this.sliceConflict != -1){
                if(this.start < this.sliceConflict && this.sliceConflict < this.end){
                    this.end = this.sliceConflict
                }
                else if(this.start > this.sliceConflict && this.sliceConflict > this.end){
                    this.end = this.sliceConflict
                }
            }
        },

        checkNear(){
            // 遍历所有区间，分别找最近的一条边
            for(var i = 0;i<this.slices.length;i++){
                var nearE = this.nearEdge(i,this.end)
                if(Math.abs(nearE - this.end) < 30){
                    this.end = nearE
                }
            }
        },

        chooseEnd(e){
            this.end = e.x
            // 1如果跨过其他区间，则只取最近一个区间
            this.checkConflict()
            // 2如果没有跨其他区间，但终点和某个区间很近，则贴上去
            this.checkNear()

            if(Math.abs(this.start - this.end) > 30){
                this.state = 2 // 表示选择完毕
            }
            else{
                this.state = 0 // 微小位移视作单机一下
            }
        },

        up(e){
            if(this.state == 1){
                this.chooseEnd(e)
            }

            else if(this.state == 4 || this.state == 5){
                this.resizeEnd(e)
            }

        },

        move(e){
            if(this.state == 1){
                this.end = e.x
                var t = this.convertXtoT(e.x)
                this.setVideoTime(t)
            }
            if(this.state == 4){
                if(e.x <= this.slices[this.chosenIndex].te - 30){
                    this.slices[this.chosenIndex].ts = e.x
                    t = this.convertXtoT(e.x)
                    this.setVideoTime(t)
                }
            } 
            if(this.state == 5){
                if(e.x >= this.slices[this.chosenIndex].ts + 30){
                    this.slices[this.chosenIndex].te = e.x
                    t = this.convertXtoT(e.x)
                    this.setVideoTime(t)
                }
            }

            // 如果进入其他slice的领地，立即

        },

        classify(type){
            var ts = Math.min(this.start,this.end)
            var te = Math.max(this.start,this.end)
            this.slices.push({ts:ts,te:te,type:type})
            this.state = 0
            this.start = 0
            this.end = 0
        },

        mouseBoundary(index,e){
            var sl = document.getElementById('sl'+index)
            var left = parseInt(sl.style.left)
            var right = left + parseInt(sl.style.width)
            if(Math.abs(e.x - left) < 10){
                return 1 // 表示左边界
            }
            else if(Math.abs(e.x - right) < 10){
                return 2 // 表示右边界
            }
            else{
                return 0 // 表示不在边界
            }
        },

        chooseSlice(index,e){
            var sl = document.getElementById('sl'+index)

            if(this.state == 0 || this.state == 2 ){
                this.state = 3
                sl.style.opacity = '100%'
                this.chosenIndex = index
                e.stopPropagation()
                e.preventDefault()
            }

            if(this.state == 3){
                e.stopPropagation()
                e.preventDefault()

                var t = this.convertXtoT(e.x)
                this.setVideoTime(t)

                // 切换片段
                if(index != this.chosenIndex){
                    var chosenSl = document.getElementById('sl'+this.chosenIndex)
                    chosenSl.style.opacity = '50%'
                    sl.style.opacity = '100%'
                    this.chosenIndex = index
                }

                var mb = this.mouseBoundary(index,e)
                if(mb == 0) return
                this.state = 3 + mb // 正在拖动,4左5右
            }
            
        },

        resizeEnd(e){
            if(this.state == 4){
                this.slices[this.chosenIndex].ts = e.x
                if(this.slices[this.chosenIndex].te - this.slices[this.chosenIndex].ts < 30){
                    this.slices[this.chosenIndex].ts = this.slices[this.chosenIndex].te - 30
                }
            }
            if(this.state == 5){
                this.slices[this.chosenIndex].te = e.x
                if(this.slices[this.chosenIndex].te - this.slices[this.chosenIndex].ts < 30){
                    this.slices[this.chosenIndex].te = this.slices[this.chosenIndex].ts + 30
                }
            } 
            this.state = 3
        },

        del(){
            this.slices.splice(this.chosenIndex,1)
            var chosenSl = document.getElementById('sl'+this.chosenIndex)
            chosenSl.style.opacity = '50%'
            this.chosenIndex = -1
            this.state = 0
        },

        resize(index,e){
            var sl = document.getElementById('sl'+index)
            // 首先判断当前段落被选中
            if(index != this.chosenIndex){
                sl.style.cursor = 'default'
                return
            }
            

            // 接着判断是否移动到了边界上
            
            if(this.mouseBoundary(index,e)){
                sl.style.cursor = 'w-resize'
            }
            else{
                sl.style.cursor = 'default'
            }

        }
    },
}
</script>


<style scoped>
#myVideo{
    display: block;
}
#progressBar{
    width: 320px;
    height: 100px;
    display: block;
}

#test{
    background-color: rgb(114, 114, 118);
}

#chosen{
    position: absolute;
    opacity: 50%;
    height: 100px;
    background-color:darkgrey
}

.sl{
    position: absolute;
    opacity: 50%;
    height: 100px;
    border:2px solid
}

.sl1{
    background-color: #F56C6C;
}

.sl2{
    background-color: #409EFF;
}
</style>