from flask import Flask, render_template, request
from convert import ascifii

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get("username", False) != False:
        username = request.form['username']
        image = request.files['file']
        image.save("pure.jpg")
        ascii_string = ascifii()
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')