from flask import Flask, render_template, request
from convert import ascifii
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("tmp/pure.jpg")
        ascifii()
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')