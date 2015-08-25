# __author__ = 'zhengmj'
from requests import post


payload = {'key1': 'value1', 'key2': 'value2'}
r = post("http://httpbin.org/get", params=payload)
print(r.url)
print(r.json)
