# 如何部署运行
* 使用git命令行输入git clone git@github.com:Elgce/bml_hw
* 打开命令行
* 下载yarn
* 下载vue-cli
* 将命令行位置跳转至文件夹位置
* 输入yarn install
* 输入yarn run serve
* 当前尚未进行封装，无需build

# 关于python环境(国内用户建议pip切换清华源)
* pip install opencv-python
* pip install tensorflow
* pip install sklearn
* 其余依赖库可以查看./backend/app.py自行安装匹配

# 关于前后端调试模式
* 首先由于跨域问题，需要下载nginx（项目使用版本：1.22.0）
* 下载完成nginx后打开安装所在文件夹，在conf/nginx.conf文件中复制进本repo中backend/nginx.conf的内容
* 回到nginx文件夹根目录，打开命令行并运行指令 ./nginx.exe并保持该终端不关闭
* yarn run serve打开前端服务
* 运行backend/app.py（建议在VScode下运行该文件，直接使用命令行运行会导致路径错误）
* 在浏览器中打开localhost:8000即可浏览效果，同时修改文件内容后可以及时预览内容

# 关于开发使用的框架或工具
* 前端框架Vue-cli
* 后端框架Flask
* UI框架Element-plus
* 跨域工具nginx(1.22.0)

# 安装或运行问题
* 联系邮箱：bqw20@mails.tsinghua.edu.cn
* 有微信可以直接通过微信联系
