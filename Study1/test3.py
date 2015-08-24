# __author__ = 'zhengmj'
import requests
url = 'https://www.baidu.com/'
r = requests.get(url)
cookies = r.cookies['BIDUPSID']
print cookies