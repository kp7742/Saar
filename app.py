from flask import Flask
from flask import request
from utility import py as ju
import socket

app = Flask(__name__)

@app.route('//')
def index():
    return 'welcome to flask'
    return ju.Row_to_Json(rows)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploaded_file.txt')
        print("UPLOAD")


@app.route('/summary')
def hello_world():
   # hi=input("Hello sentence count: ")
    output=ju.summary()
    return output

if __name__ == '__main__':
    app.run(debug=True, host="192.168.137.1", port="1111")

