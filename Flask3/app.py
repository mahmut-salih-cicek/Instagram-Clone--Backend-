from asyncio import sleep
from flask import Flask, jsonify, request, app, flash , redirect, url_for
from Model.PersonModel import PersonModel
from Database import MyDatabase
import json
import werkzeug
import requests
from bs4 import BeautifulSoup





app = Flask(__name__)

MyDatabase.createDatabase()

personList = []
imgList = []


@app.route("/")
def root_folder():
    return jsonify("main root")


@app.route("/register", methods = ["POST"])
def register_folder():

    request_data = request.data  # getting the response data
    request_data = json.loads(request_data.decode('utf-8'))  # converting it from json to key value pair


    #create Field
    userName = request_data["name"]
    realName = request_data["realName"]
    email = request_data["email"]
    password = request_data["pass"]

    # Create object
    personObj = PersonModel(email,realName,password,userName)

    #Insert Database
    MyDatabase.insertDatabase(personObj.email,personObj.realName,personObj.password,personObj.userName)

    #Show Database
    #print(MyDatabase.showDatabase())

    personList.clear()
    personList.append(personObj.email)
    personList.append(personObj.password)
    personList.append(personObj.realName)
    personList.append(personObj.userName)
    return jsonify(personList)


@app.route("/signin",methods=['GET', 'POST'])
def signIn_folder():

    email = request.args.get("email")
    #password = request.args.get("password")

    return jsonify(check = MyDatabase.searchEmail(email) )


@app.route("/showData")
def showData_folder():

    veri = MyDatabase.showDatabase()
    return jsonify(data=veri)


@app.route("/upload", methods = ["POST"])
def upload():
    if(request.method == "POST"):
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save("./img/" + filename)
        return jsonify({
            "uploadMesaj" : "true"
        })



@app.route("/showImg")
def showImage():
    main_url = "http://8.tcp.ngrok.io:14054"
    re = requests.get(main_url)
    soup = BeautifulSoup(re.text, "html.parser")
    imgList.clear()
    for a in soup.find_all('a', href=True):
        print(a['href'])
        imgList.append("http://8.tcp.ngrok.io:14054/"+a['href'])
    return jsonify(img=imgList)         


   



if __name__ == "__main__":
    app.run(debug=True)