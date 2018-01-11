from flask import Flask
from flask import send_file
from flask import request

import os

app = Flask(__name__)

# @app.route('/',methods=['GET', 'POST'])
# def hello_world():
#     # os.rename("/home/pramod/flaskSite/audio.py", "/home/pramod/Desktop")
#     # return 'Hello, World!'
#     return send_file('/home/pramod/flaskSite', attachment_filename='.py')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

@app.route('/audio')
def hello_world1():
    return 'Hello, World1!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username