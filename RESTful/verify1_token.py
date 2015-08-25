__author__ = 'zhengmj'
from flask import Flask, request, redirect
import base64
import random
import time


app = Flask(__name__)

users = {
    "kk": [123456]
}
redirect_uri = 'http://localhost:5000/client/passport'
client_id = '123456'
users[client_id] = []
oauth_code = {}
oauth_redirect_uri = []


def get_token(uid):
    token = base64.b64encode(':'.join([str(uid), str(random.random()), str(time.time()+7200)]))
    users[uid].append(token)
    return token


def verify_token(token):
    _token = base64.b64decode(token)
    print '_token=%s' % _token
    print users.get(_token.split(':')[0])
    print users.get(_token.split(':')[0])[-1]
    if not users.get(_token.split(':')[0])[-1] == token:
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
    if str(users.get(uid)[0]) == str(pw):
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


@app.route('/client/login', methods=['POST', 'GET'])
def client_login():
    uri = 'http://localhost:5000/oauth?response_type=code&client_id=%s&redirect_uri=%s' % (client_id, redirect_uri)
    return redirect(uri)


@app.route('/oauth', methods=['POST', 'GET'])
def oauth():
    if request.args.get('user'):
        print users.get(request.args.get('user'))[0]
        print request.args.get('pw')
        if int(users.get(request.args.get('user'))[0]) == int(request.args.get('pw')) and oauth_redirect_uri:
            uri = oauth_redirect_uri[0] + '?code=%s' % gen_oauth(oauth_redirect_uri[0])
            print uri
            return redirect(uri)
    if request.args.get('code'):
        print "oauth_code:"
        print oauth_code
        if oauth_code.get(int(request.args.get('code'))) == request.args.get('redirect_uri'):
            return get_token(request.args.get('client_id'))
    if request.args.get('redirect_uri'):
        oauth_redirect_uri.append(request.args.get('redirect_uri'))
        print oauth_redirect_uri
    return "please login"


@app.route('/client/passport', methods=['POST', 'GET'])
def client_passport():
    code = request.args.get('code')
    uri = 'http://localhost:5000/oauth?grant_type=authorization_code&code=%s&redirect_uri=%s&client_id=%s' % (code, redirect_uri, client_id)
    print uri
    return redirect(uri)


def gen_oauth(uri):
    code = random.randint(0, 100000)
    oauth_code[code] = uri
    return code

if __name__ == '__main__':
    app.run()