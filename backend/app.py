
import base64
from hashlib import new
import shutil
from flask import Flask, jsonify, request, abort, send_file,g, session
import os
import csv
import shutil

app = Flask(__name__,static_folder="../dist/",static_url_path="/")

MessageInfo = {}

data_num = 0

app.secret_key = "bighw"

def readcsv():
    with open('./backend/data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            global data_num
            data_num = data_num + 1
            MessageInfo.update({row["name"]:row})

def writecsv(data):
    with open('./backend/data.csv', 'a+', newline='') as csvfile:
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state', 'source']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
        global data_num
        data_num = data_num + 1
            

# 用于将表头重新写入用于保存数据的csv文件
def writecsvtitle():
    with open('./backend/data.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state', 'source']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# 用于直接重置整个数据库，删除所有数据内容
def renew():
    writecsvtitle()

# 用于up-load的action
@app.route("/api/call",methods=['GET','POST'])
def test():
    print(request.files.to_dict())
    file = request.files.to_dict()
    f = file["file"]
    basepath = os.path.dirname(__file__)
    name = session["name"]
    topath = "\src" + "\\" + name
    if not os.path.exists(basepath + topath):
        os.makedirs(basepath+topath)
    upload_path = basepath + topath + "\\" +f.filename
    print(upload_path)
    f.save(upload_path)
    MessageInfo[name]["source"].append(topath+"\\"+f.filename)
    print(MessageInfo[name]["source"])
    return ""

@app.route("/")
def index():
    return send_file("../dist/index.html")

# 本接口用于前端调用，给数据库增加信息条目
@app.route("/api/adddata",methods=['GET','POST'])
def add_data():
    data = request.get_json()
    group_id = data.get("group_id")
    name = data.get("name")
    version = data.get("version")
    num = data.get("num")
    data_id = data.get("data_id")
    in_state = data.get("in_state")
    specy = data.get("specy")
    mark_state = data.get("mark_state")
    clear_state = data.get("clear_state")
    sing_one = {
        "data_id": data_id,
        "group_id": group_id,
        "name": name,
        "version": version,
        "num": num,
        "in_state": in_state,
        "specy": specy,
        "mark_state": mark_state,
        "clear_state": clear_state,
        "source": [],
    }
    MessageInfo.update({data_id:sing_one})
    writecsv(sing_one)
    return MessageInfo
    
# 用于前端调用直接返回所有储存的信息
@app.route("/api/getdata")
def get_data():
    return {"MessageInfo":MessageInfo}
    
# 用于前端获取特定条目的信息
@app.route("/api/getone")
def get_one(name):
    return MessageInfo[name]

@app.route("/api/getnum")
def get_num():
    return {"data_num":data_num}

# 用于删除数据
@app.route("/api/deletedata",methods=['GET','POST'])
def delete_data():
    data = request.get_json()
    name = data.get("name")
    global data_num
    data_num = data_num - 1
    MessageInfo.pop(name)
    basepath = os.path.dirname(__file__)
    topath = basepath+"\src"+"\\"+name
    shutil.rmtree(topath, ignore_errors=True)
    reset_csv()
    return {"name":name}

    
# 用于前端获取对应的数据文件信息
@app.route("/api/get_source",methods=['GET','POST'])
def get_source():
    data = request.get_json()
    name = data.get("name")
    return {"source":MessageInfo[name]["source"]}

# 用于前端更改数据集name
@app.route("/api/changename",methods=['GET','POST'])
def change_name():
    data = request.get_json()
    new_name = data.get("new_name")
    old_name = data.get("old_name")
    basepath = os.path.dirname(__file__)
    origin_path = basepath + "\src" + "\\" + old_name
    new_path = basepath + "\src" + "\\" + new_name
    os.rename(origin_path,new_path)
    new_mes = MessageInfo[old_name]
    new_mes["name"] = new_name
    MessageInfo.pop(old_name)
    MessageInfo.update({new_mes["name"]: new_mes})
    reset_csv()
    return {"name":new_name}

def reset_csv():
    writecsvtitle()
    for item in MessageInfo.values():
        with open('./backend/data.csv', 'a+', newline='') as csvfile:
            fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state',"source"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(item)

# 通过session储存需要导入信息的内容
@app.route("/api/setsession",methods=['GET','POST'])
def set_session():
    data = request.get_json()
    name = data.get("name")
    session["name"] = name
    return {"name":name}
    
@app.route("/api/sessionname")
def get_session_name():
    return {"name":session["name"]}
    
@app.route("/api/clearsession")
def clear_session():
    session.clear()
    return {"baby":""}

# 用于复制文件夹
def copyfile(srcfile,name):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        dstpath = "./backend/src/" + name + "/"
        print(dstpath)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        fpath,fname = os.path.split(srcfile)
        shutil.copy(srcfile, dstpath + fname)

if __name__=="__main__":
    readcsv()
    app.run(debug=True, port=5000, host= "0.0.0.0")