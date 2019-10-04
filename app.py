from flask import Flask
from flask import request
from utility import py as ju
import socket

app = Flask(__name__)

@app.route('//')
def index():
    return 'Welcome to Saar App'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploaded_file.txt')
        print("UPLOAD")


@app.route('/summary')
def hello_world():
    output=ju.summary()
    return output

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="1111")

