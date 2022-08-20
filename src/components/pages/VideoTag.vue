<template>
    <el-col align="middle" style="overflow:hidden;">
        


        <video ref="video" id="myVideo" width="800" height="450" controls
            controlslist="nodownload noplaybackrate"
            disablePictureInPicture="true"
            @timeupdate="timeupdate"
            :src = "url"
            >
        </video>

        <!-- @keyup.enter="del()" -->
        <div id="progress" style="width:800px; height:74px;"
            @mousedown="down($event)"
            @mouseup="up($event)"
            @mousemove="move($event)"
            @mouseleave="leave($event)"
            >
            <div v-for="(slice,index) in slices" :key="index" 
                :class="'sl sl'+slice.type"
                :id="'sl'+index"
                :style="{position:fixed,left:slice.ts - 2+'px',width:slice.te-slice.ts -2 +'px'}"
                @mousedown="chooseSlice(index,$event)"
                @mousemove="resize(index,$event)"
                @mouseenter="addConf(index,$event)">
            </div>
            <div v-if="state==1 || state==2" id="chosen" 
                :style="{left:Math.min(start,end) + 'px',width:Math.abs(end - start) + 'px'}">
            </div>
        </div>

        <el-button color="#F56C6C" @click="classify(1)" :disabled="state!=2">第一类</el-button>
        <el-button color="#409EFF" @click="classify(2)" :disabled="state!=2">第二类</el-button>
        <el-button @click="del()" :disabled="state!=3">删除该片段</el-button>
    </el-col>
    
</template>


<script>

export default{
    name: "AddTag",
    props:["url"],
    data(){
        return{
            slices:[],
            start:0,
            end:0,
            state:0,
            chosenIndex:-1,
            sliceConflict:-1,
            sliderTime:0
        }
    },
    mounted(){
        let that = this
        document.onkeydown = function() {            
            let key = window.event.keyCode;            
            if (key== 46) {
                that.del()
            }
        };

    },
    methods:{
        changeCurrentTime(){
            this.$refs.video.currentTime =  this.$refs.video.duration/100 * this.sliderTime
        },

        timeupdate(){
            this.sliderTime = this.$refs.video.currentTime/this.$refs.video.duration * 100
        },

        setVideoTime(t){
            var video = document.getElementById("myVideo")
            video.currentTime = t
            this.sliderTime = t/video.duration * 100
        },

        convertXtoT(x){
            var video = document.getElementById("myVideo")
            var progress = document.getElementById("progress")
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

        leave(e){
            if(this.state == 1){
                this.chooseEnd(e)
            }

            else if(this.state == 4 || this.state == 5){
                this.resizeEnd(e)
            }
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
            this.sliceConflict = -1
        },

        checkNear(x){
            // 遍历所有区间，分别找最近的一条边
            for(var i = 0;i<this.slices.length;i++){
                var nearE = this.nearEdge(i,x)
                if(Math.abs(nearE - x) < 30){
                    return nearE
                }
            }

            return x
        },

        checkSE(){
            var pr = document.getElementById('progress')
            var l = pr.getBoundingClientRect().left
            var r = pr.getBoundingClientRect().right
            if(this.start < r && r < this.end){
                this.end = r
            }
            else if(this.end < l && l < this.start){
                this.end = l
            }
        },

        chooseEnd(e){
            this.end = e.x
            // 1如果跨过其他区间，则只取最近一个区间
            this.checkConflict()
            // 2如果没有跨其他区间，但终点和某个区间很近，则贴上去
            this.end = this.checkNear(this.end)
            // 3如果超过了开头和结尾，则固定到结尾
            this.checkSE()

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

        mouseleave(e){
            var pr = document.getElementById('progress')
            var l = pr.getBoundingClientRect().left
            var r = pr.getBoundingClientRect().right
            if(e.x < l || e.x > r ){
                return true
            }
            return false 
        },

        checkConflictRe(e){
            // 检测e.x位置是否已有slice,是则返回最近一条边坐标，否则返回-1
            for(var i = 0;i<this.slices.length;i++){
                if(i == this.chosenIndex) continue
                var ts = this.slices[i].ts
                var te = this.slices[i].te
                if(e.x >= ts && e.x <= te){
                    return true
                }
            }
            return false
        },

        move(e){
            if(this.state == 1){
                this.end = e.x

                if(this.mouseleave(e)){
                    this.chooseEnd(e)
                }

                if(this.checkConflictRe(e)){
                    this.chooseEnd(e)
                }

                var t = this.convertXtoT(e.x)
                this.setVideoTime(t)
            }

            

            if(this.state == 4 || this.state == 5){
                // 出圈即停止
                if(this.mouseleave(e)){
                    this.resizeEnd(e)
                }

                // 冲突即停止
                if(this.checkConflictRe(e)){
                    this.resizeEnd(e)
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

            }
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
                if(this.mouseleave(e)) return
                if(this.checkConflictRe(e)) return
                this.state = 3 + mb // 正在拖动,4左5右
            }
            
        },

        resizeEnd(e){
            if(this.state == 4 || this.state == 5){
                var pr = document.getElementById('progress')
                var l = pr.getBoundingClientRect().left
                var r = pr.getBoundingClientRect().right

                if(this.slices[this.chosenIndex].ts <= l){
                    this.slices[this.chosenIndex].ts = l
                }
                else if(this.slices[this.chosenIndex].te >= r){
                    this.slices[this.chosenIndex].te = r
                }
            }

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
            if(this.state != 3) return
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

        },

    },
}
</script>


<style scoped>
#myVideo{
    display: block;
    object-fit:contain;
    background-color: rgb(230, 230, 230);
    margin-top: 30px;
    margin-bottom: 30px;
    border:2px solid lightgray
    
}

#progress{
    background-color: gray;
    border:2px solid lightgray
}

#chosen{
    position: absolute;
    opacity: 80%;
    height: 74px;
    background-color:darkgrey
}

.sl{
    position: absolute;
    opacity: 50%;
    height: 70px;
    border:2px solid;

}

.sl1{
    background-color: #F56C6C;
}

.sl2{
    background-color: #409EFF;
}
</style>