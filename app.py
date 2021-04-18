from flask import Flask, render_template, request
from convert import ascifii
from hashlib import sha256

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.jpg")
        ascii_string = ascifii()
        encrypted_string = sha256(ascii_string.encode()).hexdigest()
        print(encrypted_string)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.jpg")
        ascii_string = ascifii()
        encrypted_string = sha256(ascii_string.encode()).hexdigest()
    return render_template('register.html')