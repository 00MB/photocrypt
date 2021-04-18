from flask import Flask, render_template, request, Response
from hashlib import sha256
import os
import pymongo 
from pymongo import MongoClient
from datetime import datetime
import json 
from bson import json_util
from bson.objectid import ObjectId
import wget
from image_to_ascii import ImageToAscii

cluster = MongoClient("mongodb+srv://Angel:dailyTasksAppPass@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["PhotoCrypt-DB"]
collection = db["UserCredentials"]


app = Flask(__name__)

def getCode():
    ImageToAscii(imagePath="pure.png", outputFile="ascii.txt")
    f = open("ascii.txt", "r")
    text = f.read()
    os.remove("pure.png")
    os.remove("ascii.txt")
    return sha256(text.encode()).hexdigest()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.png")
        encrypted_string = getCode()
        existingUser = list(collection.find({'username':username}))
        if(existingUser):
            if(existingUser[0]['password'] == encrypted_string):
                return render_template('landingPage.html')
            else:
                return render_template('index.html', invalid = True)
        else:
            return render_template('index.html', invalid = True)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.png")
        encrypted_string = getCode()
        exists = list(collection.find({'username':username}))
        if(exists):
            return render_template('register.html', usernameTaken = True)
        else:
            collection.insert_one({"username":username, "password":encrypted_string})
            return render_template('index.html',createdUserLogin=username)

    return render_template('register.html')

@app.route('/<path:url>/<string:caps>/<string:chars>/<int:length>',methods=['GET','POST'])
def landingPage(url, caps, chars, length):
    image = wget.download(str(url), out = "pure.png")
    encrypted_string = getCode()[:length]
    if caps == "true":
        encrypted_string = encrypted_string[1:] + "A"
    if chars == "true":
        encrypted_string =  "!"+ encrypted_string[1:]
    resp = Response("hey")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Code'] = encrypted_string
    return resp
