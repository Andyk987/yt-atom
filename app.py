from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Thank 섹스"

if __name__ == '__main__':
    app.run()