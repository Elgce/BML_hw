
from urllib.robotparser import RequestRate
from flask import Flask, jsonify, request, abort, send_file,g, session
import os
import csv

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
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)
        global data_num
        data_num = data_num + 1
            

# 用于将表头重新写入用于保存数据的csv文件
def writecsvtitle():
    with open('./backend/data.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# 用于直接重置整个数据库，删除所有数据内容
def renew():
    writecsvtitle()

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

@app.route("/api/deletedata",methods=['GET','POST'])
def delete_data():
    data = request.get_json()
    name = data.get("name")
    global data_num
    data_num = data_num - 1
    print(MessageInfo)
    MessageInfo.pop(name)
    print("newone:\n")
    print(MessageInfo)
    reset_csv()
    return {"name":name}

def reset_csv():
    writecsvtitle()
    for item in MessageInfo.values():
        print(item)
        with open('./backend/data.csv', 'a+', newline='') as csvfile:
            fieldnames = ['group_id', 'name', 'version', 'num', 'data_id', 'in_state', 'specy', 'mark_state', 'clear_state']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(item)

if __name__=="__main__":
    readcsv()
    app.run(debug=True, port=5000, host= "0.0.0.0")