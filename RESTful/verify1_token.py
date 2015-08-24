__author__ = 'zhengmj'
from flask import Flask, request
import base64
import random
import time


app = Flask(__name__)

users = {
    "kk": [123456]
}


def get_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time()+7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    _token = base64.b64decode(token)
    if not users.get(_token.split(':')[0][-1]) == token:
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index/<user>', methods=['POST', 'GET'])
# @app.route('/index/<user>')
def hello_world(user):
    print request.headers
    return 'hello world %s' % user


@app.route('/login', methods=['POST', 'GET'])
def login():
    uid, pw = base64.b64decode(request.headers['Authorization'].split(' ')[-1]).split(':')
    print request.headers
    print uid, pw
    print users.get(uid)[0]
    if users.get(uid)[0] == pw:
        return get_token(uid)
    else:
        return 'error'


@app.route('/test', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        return "data"
    else:
        return 'error'


if __name__ == '__main__':
    app.run()