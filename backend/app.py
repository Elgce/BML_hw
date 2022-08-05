from flask import Flask, jsonify, request, abort, send_file,g, session
import os

from zmq import Message

app = Flask(__name__,static_folder="../dist/",static_url_path="/")

MessageInfo = {}

data_num = 0

app.secret_key = "bighw"
@app.route("/")
def index():
    return send_file("../dist/index.html")

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
    print(MessageInfo)
    return MessageInfo
    
@app.route("/api/getdata")
def get_data():
    return MessageInfo
    
@app.route("/api/getone")
def get_one(name):
    return MessageInfo[name]




if __name__=="__main__":
    app.run(debug=True, port=5000, host= "0.0.0.0")