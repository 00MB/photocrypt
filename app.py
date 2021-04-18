from flask import Flask, render_template, request
from convert import ascifii
from hashlib import sha256
import os
import pymongo 
from pymongo import MongoClient
from datetime import datetime
import json 
from bson import json_util
from bson.objectid import ObjectId


cluster = MongoClient("mongodb+srv://Angel:dailyTasksAppPass@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["PhotoCrypt-DB"]
collection = db["UserCredentials"]



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.jpg")
        ascii_string = ascifii()
        os.remove("pure.jpg")
        encrypted_string = sha256(ascii_string.encode()).hexdigest()

        existingUser = list(collection.find({'username':username}))
        # print(existingUser['password'])
        if(existingUser):
            if(existingUser[0]['password'] == encrypted_string):
                return render_template('landingPage.html')
        else:
            return render_template('index.html', invalid = True)
        # print(encrypted_string)
        return render_template('index.html')
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.jpg")
        ascii_string = ascifii()
        os.remove("pure.jpg")
        encrypted_string = sha256(ascii_string.encode()).hexdigest()
        exists = list(collection.find({'username':username}))
        if(exists):
            # print("Username is already taken")
            return render_template('register.html', usernameTaken = True)
        else:
            collection.insert_one({"username":username, "password":encrypted_string})
            return render_template('index.html',createdUserLogin=username)

        # print("username: ", username, "$$ encrypted string: ", encrypted_string)

    return render_template('register.html')

@app.route('/landingPage',methods=['GET','POST'])
def landingPage():
    return render_template('landingPage.html')
