import datetime
import base64
from email.headerregistry import Group
from genericpath import isfile
from glob import glob
from hashlib import new
from operator import length_hint
from pydoc import describe, pager
import re
import zipfile
import shutil
from tkinter import Label
from urllib import response
from urllib.parse import quote
from urllib.robotparser import RequestRate
from flask import Flask, jsonify, request, abort, send_file,g, session,make_response,send_from_directory
import os
import csv
import shutil
import random
import cv2
import numpy as np
from tensorflow import keras
from keras.utils import to_categorical
from keras.utils import image_utils
# from image_utils import img_to_array
from sklearn.model_selection import train_test_split

app = Flask(__name__,static_folder="../dist/",static_url_path="/")

MessageInfo = {}
LabelInfo = {}

context = []
context_txt = []
context_tag = []

slices = []
colorlist = {}

label_num = 0
data_num = 0

names = []

app.secret_key = "bighw"

#定义标签组类
class labelGroup():
    name=""
    description=""
    labels=[]

groups=[]

manage_group_name=""

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

#进行机器学习
@app.route("/api/start_training",methods=['GET','POST'])
def start_training():
    data = request.get_json()
    num = data.get("num")
    train_ratio = data.get("train_ratio")
    source_txt = open('./backend/src/'+session["name"]+'/source.txt',encoding="utf-8")
    folder = os.listdir('./backend/src/'+session["name"])
    picCount=-1
    for filePath in folder:
        picCount+=1
    picName=""
    tagName=""
    tags=[]
    labels=[]
    images=[]
    turnToTag=0
    label_index=0
    for i in range(picCount):
        txt=source_txt.readline()
        turnToTag=0
        for j in range(len(txt)):
            if turnToTag==0:
                if txt[j]!=' ':
                    picName+=txt[j]
                else:
                    turnToTag=1
            else:
                if txt[j]!='\n':
                    tagName+=txt[j]
        isNew=1
        for i in range(len(tags)):
            if tags[i]==tagName:
                isNew=0
                label_index=i
        if isNew==1:
            tags.append(tagName)
            label_index=len(tags)
        labels.append(label_index)
        imgPath=os.path.join('./backend/src/'+session["name"],picName)
        image = cv2.imread(imgPath)
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, (100, 100), interpolation = cv2.INTER_AREA)
        image = image_utils.img_to_array(image)
        images.append(image)
        picName=""
        tagName=""
    images=np.array(images)
    labels=np.array(labels)
    images_train,images_test, labels_train, labels_test =train_test_split(images,labels,test_size=1-(train_ratio/100))
    images_train=keras.utils.normalize(images_train,axis=1)
    images_test=keras.utils.normalize(images_test,axis=1)
    model=keras.Sequential([keras.layers.Flatten(input_shape=(100,100,3)),keras.layers.Dense(num,activation='relu'),keras.layers.Dense(10,activation='softmax')])
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    model.fit(images_train,labels_train,epochs=10)
    _,accuracy=model.evaluate(images_test,labels_test)
    print(accuracy)
    return {"accuracy":accuracy}

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
    f_type = f.filename.split('.')
    ff_type = f_type[1]
    basepath = os.path.dirname(__file__)
    name = session["name"]
    topath = "\src" + "\\" + name
    if not os.path.exists(basepath + topath):
        os.makedirs(basepath+topath)
    
    if(ff_type=='zip'):
        zip_file = zipfile.ZipFile(f,'r')
        zip_file.extractall(basepath+topath)
        for z in zip_file.namelist():
            MessageInfo[name]["source"].append(z)
            MessageInfo[name]["num"] = int(MessageInfo[name]["num"]) + 1
            reset_csv()
        
    else:
        upload_path = basepath + topath + "\\" +f.filename
        f.save(upload_path)
        MessageInfo[name]["source"].append(f.filename)
        MessageInfo[name]["num"] = int(MessageInfo[name]["num"]) + 1
        reset_csv()
        basepath = os.path.dirname(__file__)
        path = basepath + "\src\\" + name + "\\" + "source.txt"
        if os.path.exists(path):
            with open(path,"a+",encoding="utf-8") as file_to:
                file_to.write(f.filename+"\n")
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

#给数据库增加标签组
@app.route("/api/addgroup",methods=['GET','POST'])
def add_group_data():
    data = request.get_json()
    name = data.get("name")
    isok = "no-repeat"
    global groups
    for i in range(len(groups)):
        if groups[i].name==name:
            isok = "repeat"
    if isok=="no-repeat":
        newGroup=labelGroup()
        newGroup.name=name
        newGroup.description=data.get("description")
        newGroup.labels=[]
        groups.append(newGroup)
    return {"isok":isok}

#向后端发送管理标签组
@app.route("/api/managegroup",methods=['GET','POST'])
def manage_group_data():
    data = request.get_json()
    name = data.get("name")
    isok = "not-exist"
    global groups
    global manage_group_name
    for i in range(len(groups)):
        if groups[i].name==name:
            isok = "exist"
            manage_group_name=name
    return {"isok":isok}

# 用于获取标签组信息
@app.route("/api/callGroup")
def call_group():
    tempName=[]
    tempDescription=[]
    global groups
    for i in range(len(groups)):
        tempName.append(groups[i].name)
        tempDescription.append(groups[i].description)
    return {"names":tempName,"descriptions":tempDescription}

# 用于搜索标签组信息
@app.route("/api/searchGroup",methods=['GET','POST'])
def search_group():
    # print(1)
    data = request.get_json()
    tempName=[]
    tempDescription=[]
    name = data.get("name")
    global groups
    # print(name)
    for i in range(len(groups)):
        if groups[i].name==name:
            tempName.append(groups[i].name)
            tempDescription.append(groups[i].description)
    return {"names":tempName,"descriptions":tempDescription}

# 用于搜索标签组中标签信息
@app.route("/api/searchTag",methods=['GET','POST'])
def search_tag():
    # print(1)
    data = request.get_json()
    tempName=[]
    tempDescription=[]
    name = data.get("name")
    global groups
    # print(name)
    for i in range(len(groups)):
        if groups[i].name==manage_group_name:
            for j in range(len(groups[i].labels)):
                if groups[i].labels[j]==name:
                    tempName.append(groups[i].labels[j])
    return {"names":tempName}

# 用于获取标签组标签信息
@app.route("/api/call_group_labels")
def call_group_labels():
    tempName=[]
    global groups
    global manage_group_name
    for i in range(len(groups)):
        if groups[i].name==manage_group_name:
            for j in range(len(groups[i].labels)):
                #print(groups[i].labels)
                tempName.append(groups[i].labels[j])
    return {"names":tempName}

#给数据库增加标签组中标签
@app.route("/api/add_group_tag",methods=['GET','POST'])
def add_group_tag():
    data = request.get_json()
    name = data.get("name")
    isok = "no-repeat"
    global groups
    global manage_group_name
    for i in range(len(groups)):
        if groups[i].name==manage_group_name:
            for j in range(len(groups[i].labels)):
                if groups[i].labels[j]==name:
                    isok = "repeat"
    if isok=="no-repeat":
        for i in range(len(groups)):
            if groups[i].name==manage_group_name:
                #print(i)
                groups[i].labels.append(name)
    #print(groups[1].labels)
    return {"isok":isok}

#编辑标签组
@app.route("/api/editgroup",methods=['GET','POST'])
def edit_group():
    data = request.get_json()
    form_name = data.get("form_name")
    next_name = data.get("next_name")
    description=data.get("description")
    isok = "not-exist"
    global groups
    global manage_group_name
    for i in range(len(groups)):
        if groups[i].name==form_name:
            isok="exist"
    if isok=="exist":
        for i in range(len(groups)):
            if groups[i].name==next_name:
                isok="repeat"
    if isok=="exist":
        for i in range(len(groups)):
            if groups[i].name==form_name:
                groups[i].name=next_name
                groups[i].description=description
    return {"isok":isok}

#编辑标签组中标签
@app.route("/api/editgrouptag",methods=['GET','POST'])
def edit_group_tag():
    data = request.get_json()
    form_name = data.get("form_name")
    next_name = data.get("next_name")
    isok = "not-exist"
    global groups
    global manage_group_name
    for i in range(len(groups)):
        if groups[i].name==manage_group_name:
            for j in range(len(groups[i].labels)):
                if groups[i].labels[j]==form_name:
                    isok="exist"
            if isok=="exist":
                for j in range(len(groups[i].labels)):
                    if groups[i].labels[j]==next_name:
                        isok="repeat"
            if isok=="exist":
                for j in range(len(groups[i].labels)):
                    if groups[i].labels[j]==form_name:
                        groups[i].labels[j]=next_name
    return {"isok":isok}

#向后端发送删除标签组
@app.route("/api/deletegroup",methods=['GET','POST'])
def delete_group_data():
    data = request.get_json()
    name = data.get("name")
    isok = "not-exist"
    global groups
    global manage_group_name
    global to_delete
    for i in range(len(groups)):
        if groups[i].name==name:
            isok = "exist"
            to_delete=i
    if isok=="exist":
        groups.pop(to_delete)
    
    return {"isok":isok}

#向后端发送删除标签组中标签
@app.route("/api/deletegrouptag",methods=['GET','POST'])
def delete_group_tag_data():
    data = request.get_json()
    name = data.get("name")
    isok = "not-exist"
    global groups
    global manage_group_name
    global to_delete
    for i in range(len(groups)):
        if groups[i].name==manage_group_name:
            for j in range(len(groups[i].labels)):
                if groups[i].labels[j]==name:
                    isok = "exist"
                    to_delete=j
            if isok=="exist":
                groups[i].labels.pop(to_delete)
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

# 用于复制文件夹(导出)
@app.route("/api/exportdata")
def copyfile():
    name = session["name"]
    src = "./backend/src/"+name
    src_files = os.listdir(src)
    dstpath = "./export/" + name + "/"
    if not os.path.exists(dstpath):
        os.makedirs(dstpath)
    for file_name in src_files:
        full_file_name = os.path.join(src,file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dstpath)
    return {"name":name}

# 用于储存文本抽取的样式
@app.route("/api/sendstyle",methods=["GET","POST"])
def send_style():
    page = int(session["page"]) - 1
    data = request.get_json()
    intxt = data.get("intxt")
    name = session["name"]
    global context
    global context_tag
    global context_txt
    context_tag[page] = intxt
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + context_txt[page]
    length = len(context)
    new_context = []
    for i in range(length):
        if(context_txt[i]==context_txt[page]):
            new_context.append(context[i]+" "+context_tag[i]+"\n")
    with open(path,"w",encoding='utf-8') as f:
        for item in new_context:
            f.write(item)
    return {"intxt": intxt}

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

#添加标签组
@app.route("/api/addlabels",methods=['GET','POST'])
def add_labels():
    data = request.get_json()
    group_name = data.get("name")
    name = session["name"]
    for i in range(len(groups)):
        if group_name==groups[i].name:
            MessageInfo[name]["labels"]=groups[i].labels
    reset_csv()
    print(MessageInfo[name]["labels"])


    return {"labels":MessageInfo[name]["labels"]}
    
# ---------------------------------------------------------
# Below are something about lables
# Written by bqw
# ---------------------------------------------------------
@app.route("/api/addlabel",methods=['GET','POST'])
def add_label():
    data = request.get_json()
    label_name = data.get("name")
    name = session["name"]
    MessageInfo[name]["labels"].append(label_name)
    reset_csv()
    print(MessageInfo[name]["labels"])


    return {"labels":MessageInfo[name]["labels"]}

@app.route("/api/getlabels",methods=['GET',"POST"])
def get_labels():
    name = session["name"]
    num = len(MessageInfo[name]["labels"])
    # return {"labels":MessageInfo[name]["labels"],"label_num": num}


    #----syz添加标签配色----------
    global colorlist
    colorlist = {}
    for label in MessageInfo[name]["labels"]:
        r = random.randint(100,200)
        g = random.randint(100,200)
        b = random.randint(100,200)
        if(r+g+b > 500):
            r = 500 - g - b
        color = 'rgb(' + str(r) + ',' + str(g) + ',' + str(b) + ')'
        colorlist[label] = color
    print(colorlist)
    #--------end-----------------
    # 此处额外返回了colorlist
    return {"labels":MessageInfo[name]["labels"],"label_num": num,"colorlist":colorlist}

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

    #-------删除颜色----------
    global colorlist
    colorlist.pop(label_name)
    #------------------------
    return {"lebel_name":label_name ,"colorlist":colorlist}

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
      
# 用于图片打标
@app.route("/api/tagpiclabel",methods=["GET","POST"])
def tag_piclabel():
    data = request.get_json()
    tag = data.get("tag")
    global context
    global context_tag
    global context_txt
    ind = int(session["page"]) - 1
    context_tag[ind] = tag
    name = session["name"]
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + "source.txt"
    length = len(context)
    new_context = []
    for i in range(length):
        new_context.append(context[i]+" "+context_tag[i]+"\n")
    print(new_context)
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
    print(ind)
    print(context_tag)
    return {"tag":context_tag[ind]}

# 用于设置文本视图需要的种类
@app.route("/api/sessiontype",methods=["GET","POST"])
def session_type():
    data = request.get_json()
    t_type = data.get("t_type")
    session["t_type"] = t_type
    session["page"] = 1
    return {"t_type":t_type}

# 用于文本抽取获取文本信息
@app.route("/api/gettxtextracted")
def get_txtextracted():
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
                if len(datas)>1:
                    ed_num = ed_num + 1
                    if t_type=="ed" or t_type=="all":
                        d_data = ""
                        for i in range(len(datas)):
                            if(i!=0):
                                d_data = d_data + datas[i] + " "
                        context_tag.append(d_data)
                        context.append(datas[0])
                        context_txt.append(item)
                else:
                    if t_type=="to" or t_type=="all":
                        context_tag.append("")
                        context.append(datas[0])
                        context_txt.append(item)
                    to_num = to_num + 1
    print(context_tag)               
    return {"context_tag":context_tag,"context":context,"t_type":t_type,"all_num":all_num,"name":name,"to_num":to_num,"ed_num":ed_num}

# 用于文本实体数据页面获取文本信息
@app.route("/api/gettxtextract")
def get_txtextract():
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
                if len(datas)>1:
                    ed_num = ed_num + 1
                    if t_type=="ed" or t_type=="all":
                        context_tag.append("")
                        context.append(datas[0])
                        context_txt.append(item)
                elif len(datas)==2:
                    if t_type=="to" or t_type=="all":
                        context_tag.append("")
                        context.append(datas[0])
                        context_txt.append(item)
                    to_num = to_num + 1
                else:
                    print("datas")
                   
    return {"context_tag":context_tag,"context":context,"t_type":t_type,"all_num":all_num,"name":name,"to_num":to_num,"ed_num":ed_num}

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

# 保存视频的切片信息
@app.route("/api/setvideospl",methods=["GET","POST"])
def setVideoSpl():
    global slices
    slices = []
    slices = request.get_json().get("slices")
    # 将slices中的信息写进txt中
    basepath = os.path.dirname(__file__)
    name = session["name"]
    path = basepath + "\src\\" + name + "\\" + 'source.txt'
    with open(path,"w",encoding='utf-8') as f:
        for item in slices:
            f.write(str(item['ts'])+' '+str(item['te'])+' '+str(item['type'])+"\n")
    return {"slices":slices}

# 获取视频的切片信息
@app.route("/api/getvideospl",methods=["GET","POST"])
def getVideoSpl():
    global slices
    slices = []
    basepath = os.path.dirname(__file__)
    name = session["name"]
    path = basepath + "\src\\" + name + "\\" + "source.txt"
    if os.path.exists(path):
        with open(path,"r",encoding="utf-8") as f:
            data_list = f.readlines()
            for line in data_list:
                line = line.strip()
                line_list = line.split(" ")
                ts = eval(line_list[0])
                te = eval(line_list[1])
                type = line_list[2]
                slices.append({"ts":ts,"te":te,"type":type})
    else:
        open(path,'w')
    return {"slices":slices}

@app.route("/api/getpicsources")
def get_picsources():
    global context
    global context_tag
    global context_txt
    t_type = session["t_type"]
    context = []
    context_tag = []
    context_txt = []
    name = session["name"]
    basepath = os.path.dirname(__file__)
    path = basepath + "\src\\" + name + "\\" + "source.txt"
    all_num = 0
    to_num = 0
    ed_num = 0
    if not os.path.exists(path):
        with open(path,"w",encoding="utf-8") as f:
            for item in MessageInfo[name]["source"]:
                f.write(item+"\n")
                all_num = all_num + 1
                to_num = to_num + 1
                context.append(item)
                context_tag.append("")
    else:
        with open(path,"r",encoding="utf-8") as f:
            data_list = f.readlines()
            for line in data_list:
                all_num = all_num + 1
                line = line.strip()
                datas = line.split()
                if len(datas)==1:
                    to_num = to_num + 1
                    if t_type=="to" or t_type=="all":
                        context_tag.append("")
                        context.append(datas[0])
                else:
                    ed_num = ed_num + 1
                    if t_type=="ed" or t_type=="all":
                        print(datas)
                        context_tag.append(datas[1])
                        context.append(datas[0])
    return {"t_type":t_type,"sources":context,"context_tag":context_tag,"all_num":all_num,"to_num":to_num,"ed_num":ed_num}

if __name__=="__main__":
    renew()
    readcsv()
    app.run(debug=True, port=5000, host= "0.0.0.0")
