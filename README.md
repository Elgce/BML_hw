# 如何部署运行
* 下载并解压文件
* 打开命令行
* 下载yarn
* 将位置跳转至文件夹位置
* 输入yarn install
* 输入yarn run bulid、yarn run serve

# 关于前后端调试模式
* 首先由于跨域问题，需要下载nginx（最新版应该是1.22.0）
* 下载完成nginx后打开安装所在文件夹，在conf/nginx.conf文件中复制进本repo中backend/nginx.conf的内容
* 回到nginx文件夹根目录，打开命令行并运行指令 ./nginx.exe并保持该终端不关闭
* yarn run serve打开前端服务
* 运行backend/app.py
* 在浏览器中打开localhost:8000即可浏览效果，同时修改文件内容后可以及时预览内容

# 关于开发
* git clone git@github.com:Elgce/BML_hw  克隆本repo
* 每次工作前git fetch + git pull获取库的最新情况
* git checkout -b + 分支的名字，最好直接是自己名字缩写，实际命令行不含"+"
* 完成当次开发后
  * git add. 添加新写的内容
  * git commit -m "此处描述本次工作实现的功能"
  * git push（注意，直接在分支上提交）
* 登录GitHub并且进入本repo
  * 在pull requests中提交PR

# 问题
直接在微信群中联系交流
