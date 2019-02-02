from flask import Flask
from utility import py as ju
import socket

app = Flask(__name__)

@app.route('//')
def index():
    return 'welcome to flask'
    return ju.Row_to_Json(rows)

@app.route('/summary')
def hello_world():
    hi=input("Hello sentence count: ")
    output=ju.summary(hi)
    return output

if __name__ == '__main__':
    app.run(debug=True, port="1111")

