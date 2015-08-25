# __author__ = 'zhengmj'
# from requests import post
#
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = post("http://httpbin.org/get", params=payload)
# print(r.url)
# print(r.json)

import requests

# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36"}
# r = requests.get('http://127.0.0.1:5000/index/peterson', headers=headers)
# print r.text
# print r.status_code
# r = requests.get('http://127.0.0.1:5000/login', auth=('kk', '123456'))
# print(r.text)
# token = 'a2s6MC42NjAzMTAyNDk0MDU6MTQzOTY2MjAzNi41NQ=='
# r = requests.get('http://127.0.0.1:5000/test', params={'token': token})
# print(r.text)
r = requests.get('http://127.0.0.1:5000/client/login')
print r.text
print "============"
print r.history
print "============"
print r.url
print "============"
uri_login = r.url.split('?')[0] + '?user=kk&pw=123456'
r2 = requests.get(uri_login)
print r2.text
print "============"
print r2.url
print r2.history
print "============"
r3 = requests.get('http://127.0.0.1:5000/test', params={'token': r2.text})
print r3.text