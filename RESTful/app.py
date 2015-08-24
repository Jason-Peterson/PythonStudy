__author__ = 'zhengmj'
from flask import Flask, request
app = Flask(__name__)


# @app.route('/<user>', methods=['POST'])
@app.route('/index/<user>')
def hello_world(user):
    print request.headers
    return 'hello world %s' % user

if __name__ == '__main__':
    app.run()