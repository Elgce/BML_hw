import datetime
import base64
from glob import glob
from hashlib import new
from operator import length_hint
from pydoc import pager
import re
import shutil
from tkinter import Label
from urllib import response
from urllib.parse import quote
from urllib.robotparser import RequestRate
from flask import Flask, jsonify, request, abort, send_file,g, session,make_response,send_from_directory
import os
import csv
import shutil

app = Flask(__name__,static_folder="../dist/",static_url_path="/")

MessageInfo = {}
LabelInfo = {}

context = []
context_txt = []
context_tag = []

label_num = 0
data_num = 0

names = []

app.secret_key = "bighw"

def readcsv():
    global names
    names = []
    with open('./backend/data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            global data_num
            data_num = data_num + 1
            names.append(row["name"])
            MessageInfo.update({row["name"]:row})

def writecsv(data):
    with open('./backend/data.csv', 'a+', newline='') as csvfile:
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state', 'source', 'direction', 'label_type', 'label_model', 'data_single', 'labels']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
        global data_num
        data_num = data_num + 1
            


# 用于将表头重新写入用于保存数据的csv文件
def writecsvtitle():
    with open('./backend/data.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state', 'source', 'direction', 'label_type', 'label_model', 'data_single', 'labels']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# 用于直接重置整个数据库，删除所有数据内容
def renew():
    writecsvtitle()

# 用于前端搜索时获取新的Message内容返回前端
@app.route("/api/searchdata",methods=['GET','POST'])
def search_data():
    global num
    num = 0
    data = request.get_json()
    specy = data.get("specy")
    label_type = data.get("type")
    Message_Show = {}
    for item in MessageInfo:
        if MessageInfo[item]["specy"]==specy and (MessageInfo[item]["label_type"]==label_type or MessageInfo[item]["direction"]==label_type):
            Message_Show.update({MessageInfo[item]["name"]:MessageInfo[item]})
            num = num + 1
    return {"MessageShow":Message_Show,"data_num":num}        
    

# 用于up-load的action
@app.route("/api/call",methods=['GET','POST'])
def test():
    file = request.files.to_dict()
    f = file["file"]
    basepath = os.path.dirname(__file__)
    name = session["name"]
    topath = "\src" + "\\" + name
    if not os.path.exists(basepath + topath):
        os.makedirs(basepath+topath)
    upload_path = basepath + topath + "\\" +f.filename
    f.save(upload_path)
    MessageInfo[name]["source"].append(f.filename)
    MessageInfo[name]["num"] = int(MessageInfo[name]["num"]) + 1
    reset_csv()
    return ""

@app.route("/")
def index():
    return send_file("../dist/index.html")

# 本接口用于前端调用，给数据库增加信息条目
@app.route("/api/adddata",methods=['GET','POST'])
def add_data():
    data = request.get_json()
    name = data.get("name")
    session["name"] = name
    isok = "no-repeat"
    if (name in names):
        isok = "repeat"
    else:
        names.append(name)
        group_id = data.get("group_id")
        version = data.get("version")
        num = data.get("num")
        data_id = data.get("data_id")
        in_state = data.get("in_state")
        specy = data.get("specy")
        mark_state = data.get("mark_state")
        clear_state = data.get("clear_state")
        
        label_type = data.get("label_type")
        label_model = data.get("label_model")
        data_single = data.get("data_single")
        direction = data.get("direction")
        
        time = datetime.datetime.now()
        group_id = (time.year%100)*10000 + time.month*100 + time.day
        data_id = time.hour*10000 + time.minute*100 + time.second
        
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
            "direction": direction,
            "label_type": label_type,
            "label_model": label_model,
            "data_single": data_single,
            "labels": [],
        }
        MessageInfo.update({name:sing_one})
        writecsv(sing_one)
    return {"isok":isok}
    
# 用于前端调用直接返回所有储存的信息
@app.route("/api/getdata")
def get_data():
    return {"MessageInfo":MessageInfo}
    
# 用于前端获取特定条目的信息
@app.route("/api/getone")
def get_one():
    name = session["name"]
    return {"data":MessageInfo[name]}

@app.route("/api/getnum")
def get_num():
    return {"data_num":data_num}

# 用于删除数据
@app.route("/api/deletedata",methods=['GET','POST'])
def delete_data():
    data = request.get_json()
    name = data.get("name")
    if name not in MessageInfo:
        return {"name":name}
    global data_num
    data_num = data_num - 1
    MessageInfo.pop(name)
    global names
    names.remove(name)
    basepath = os.path.dirname(__file__)
    topath = basepath+"\src"+"\\"+name
    shutil.rmtree(topath, ignore_errors=True)
    reset_csv()
    return {"name":name}


# 用于前端更改数据集name
@app.route("/api/changename",methods=['GET','POST'])
def change_name():
    data = request.get_json()
    new_name = data.get("new_name")
    old_name = data.get("old_name")
    global names
    
    names.pop(names.index(old_name))
    names.append(new_name)
    basepath = os.path.dirname(__file__)
    origin_path = basepath + "\src" + "\\" + old_name
    new_path = basepath + "\src" + "\\" + new_name
    if os.path.exists(origin_path):
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
            fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state',"source", 'direction', 'label_type', 'label_model', 'data_single', 'labels']
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
    name = session["name"]
    return {"name":name,"src_list":MessageInfo[name]["source"]}
    
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
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        fpath,fname = os.path.split(srcfile)
        shutil.copy(srcfile, dstpath + fname)

# 用于调用前端需要的文件并返回
@app.route("/api/passfile/<file_name>",methods=['GET','POST'])
def pass_file(file_name):
    name = session["name"]
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + file_name
    return send_file(path)

# 用于前端根据名字选取数据集
@app.route("/api/searchname",methods=['GET','POST'])
def search_name():
    data = request.get_json()
    name = data.get("name")
    if(name==""):
        return {"MessageShow":MessageInfo,"data_num":data_num}
    global num
    num = 0
    Message_Show = {}
    for item in MessageInfo:
        if MessageInfo[item]["name"]==name:
            Message_Show.update({MessageInfo[item]["name"]:MessageInfo[item]})
            num = num + 1
    return {"MessageShow":Message_Show,"data_num":num}   
    
# ---------------------------------------------------------
# Below are something about lables
# Written by bqw
# ---------------------------------------------------------
@app.route("/api/addlabel",methods=['GET','POST'])
def add_label():
    data = request.get_json()
    label_name = data.get("name")
    name = session["name"]
    MessageInfo[name]["labels"].append(label_name);
    reset_csv()
    print(MessageInfo[name]["labels"])
    return {"labels":MessageInfo[name]["labels"]}

@app.route("/api/getlabels",methods=['GET',"POST"])
def get_labels():
    name = session["name"]
    num = len(MessageInfo[name]["labels"])
    return {"labels":MessageInfo[name]["labels"],"label_num": num}

@app.route("/api/searchtagname",methods=['GET','POST'])
def search_tagname():
    name = session["name"]
    data = request.get_json()
    tagname = data.get("tagname")
    Label_show = []
    num = 0
    for item in MessageInfo[name]["labels"]:
        if item == tagname:
            Label_show.append(item)
            num = num + 1
    if tagname=="":
        Label_show = MessageInfo[name]["labels"]
        num = len(MessageInfo[name]["labels"])
    return {"labels":Label_show,'label_num': num}

@app.route("/api/getresources")
def get_resources():
    name = session["name"]
    return {"sources":MessageInfo[name]["source"]}

@app.route("/api/deletelabel",methods=['GET','POST'])
def delete_label():
    data = request.get_json()
    label_name = data.get("label_name")
    name = session["name"]
    index = MessageInfo[name]["labels"].index(label_name)
    MessageInfo[name]["labels"].pop(index)
    reset_csv()
    return {"lebel_name":label_name}

@app.route("/api/gettxt")
def get_txt():
    global context
    global context_txt
    global context_tag
    t_type = session["t_type"]
    context = []
    context_tag = []
    context_txt = []
    name = session["name"]
    sources = MessageInfo[name]["source"]
    basepath = os.path.dirname(__file__)
    all_num = 0
    to_num = 0
    ed_num = 0
    for item in sources:
        path = basepath + "\src\\" + name + "\\" + item
        with open(path,"r",encoding='utf-8') as f:
            data_list = f.readlines()
            for line in data_list:
                all_num = all_num + 1
                line = line.strip()
                datas = line.split()
                if len(datas)==2:
                    ed_num = ed_num + 1
                    if t_type=="ed" or t_type=="all":
                        context_tag.append(datas[1])
                        context.append(datas[0])
                        context_txt.append(item)
                else:
                    if t_type=="to" or t_type=="all":
                        context_tag.append("")
                        context.append(datas[0])
                        context_txt.append(item)
                    to_num = to_num + 1
                
    print(context)       
    return {"context":context,"t_type":t_type,"all_num":all_num,"name":name,"to_num":to_num,"ed_num":ed_num}
    
@app.route("/api/deletetxt",methods=['GET','POST'])
def delete_txt():
    global context_txt
    global context
    global context_tag
    data = request.get_json()
    text = data.get("text")
    name = session["name"]
    num = data.get("num")
    num = int(num) - 1
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + context_txt[num]
    if context[num]!=text:
        print("error!")
    length = len(context)
    new_context = []
    for i in range(length):
        if context_txt[i] == context_txt[num] and i!=num:
            new_context.append(context[i]+"\n")
    print(new_context)
    with open(path, 'w', encoding='utf-8') as f:
        for item in new_context:
            f.write(item)
    return {"name":name}

# 用于文本相似度删除数据
@app.route("/api/deletetxtsim",methods=['GET','POST'])
def delete_txtsim():
    global context_txt
    global context
    global context_tag
    data = request.get_json()
    text = data.get("text")
    name = session["name"]
    num = data.get("num")
    num = int(num) - 1
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + context_txt[num]
    if context[num][0]!=text:
        print("error!")
    length = len(context)
    new_context = []
    for i in range(length):
        if context_txt[i] == context_txt[num] and i!=num:
            new_context.append(context[i][0]+" "+context[i][1]+" "+context_tag[i]+"\n")
    print(new_context)
    with open(path, 'w', encoding='utf-8') as f:
        for item in new_context:
            f.write(item)
    return {"name":name}

# 用于文本页面跳转时确定谁是第一个展示的文本标签
@app.route("/api/txtpagesession",methods=['GET','POST'])
def txt_pagesession():
    data = request.get_json()
    page = data.get("page")
    session["page"] = page
    return {"page":page}

# 用于获取页面配置的数据
@app.route("/api/txtgetpage")
def txt_getpage():
    return {"page":session["page"]}

@app.route("/api/prepage")
def pre_page():
    page = int(session["page"]) - 1
    if page > 0 :
        session["page"] = page
        return {"page":page}
    else:
        return {"page":"fail"}

@app.route("/api/nextpage")
def next_page():
    page = int(session["page"]) + 1
    global context
    length = len(context)
    if page <= length:
        session["page"] = page
        return {"page":page}
    else:
        return {"page":"fail"}

# 用于文本打标签并保存
@app.route("/api/taglabel",methods=["GET","POST"])
def tag_label():
    data = request.get_json()
    tag = data.get("tag")
    global context
    global context_tag
    global context_txt
    ind = int(session["page"]) - 1
    context_tag[ind] = tag
    name = session["name"]
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + context_txt[ind]
    length = len(context)
    new_context = []
    for i in range(length):
        if(context_txt[i]==context_txt[ind]):
            new_context.append(context[i]+" "+context_tag[i]+"\n")
    with open(path, 'w', encoding='utf-8') as f:
        for item in new_context:
            f.write(item)
    return {"tag":tag}
      
# 用于文本相似度打标签并保存
@app.route("/api/taglabelsim",methods=["GET","POST"])
def tag_labelsim():
    data = request.get_json()
    tag = data.get("label")
    global context
    global context_tag
    global context_txt
    inx = data.get("num")
    ind = int(inx) - 1
    context_tag[ind] = tag
    name = session["name"]
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + context_txt[ind]
    length = len(context)
    new_context = []
    print(context)
    print(context_tag)
    print(context_txt)
    for i in range(length):
        if(context_txt[i]==context_txt[ind]):
            new_context.append(context[i][0]+" "+context[i][1]+" "+context_tag[i]+"\n")
    with open(path, 'w', encoding='utf-8') as f:
        for item in new_context:
            f.write(item)
    return {"tag":tag}
      
        
# 用于获取文本编辑时当前页面的标签信息
@app.route("/api/calltag")
def call_tag():
    global context_tag
    ind = int(session["page"]) - 1
    return {"tag":context_tag[ind]}

# 用于设置文本视图需要的种类
@app.route("/api/sessiontype",methods=["GET","POST"])
def session_type():
    data = request.get_json()
    t_type = data.get("t_type")
    session["t_type"] = t_type
    session["page"] = 1
    return {"t_type":t_type}

# 用于文本相似度获取文本
@app.route("/api/gettxtsim")
def get_txtsim():
    global context
    global context_txt
    global context_tag
    t_type = session["t_type"]
    context = []
    context_tag = []
    context_txt = []
    name = session["name"]
    sources = MessageInfo[name]["source"]
    basepath = os.path.dirname(__file__)
    all_num = 0
    to_num = 0
    ed_num = 0
    for item in sources:
        path = basepath + "\src\\" + name + "\\" + item
        with open(path,"r",encoding='utf-8') as f:
            data_list = f.readlines()
            for line in data_list:
                all_num = all_num + 1
                line = line.strip()
                datas = line.split()
                if len(datas)==3:
                    ed_num = ed_num + 1
                    if t_type=="ed" or t_type=="all":
                        context_tag.append(datas[2])
                        context.append([datas[0],datas[1]])
                        context_txt.append(item)
                else:
                    if t_type=="to" or t_type=="all":
                        context_tag.append("")
                        context.append([datas[0],datas[1]])
                        context_txt.append(item)
                    to_num = to_num + 1
                   
    return {"context_tag":context_tag,"context":context,"t_type":t_type,"all_num":all_num,"name":name,"to_num":to_num,"ed_num":ed_num}

if __name__=="__main__":
    # renew()
    readcsv()
    app.run(debug=True, port=5000, host= "0.0.0.0")