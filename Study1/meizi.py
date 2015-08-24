# coding=utf-8
# __author__ = 'zhengmj'
import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

uri = 'http://jandan.net/ooxx/page-1520#comments'
f = requests.get(uri, headers=headers)
html = f.text
# print html
pattern = '<ol class="commentlist" style="list-style-type: none;">(.*?)</ol>'
new_pattern = re.compile(pattern, re.S)
new_html = re.search(new_pattern, html).group(1)
# print new_html
pattern1 = '<li id="comment-(\d+)">.*?<img src="(.*?)" />.*?</li>'
new_pattern1 = re.compile(pattern1, re.S)
r = re.findall(new_pattern1, new_html)
# print r
print "now download meizi pictures......."
for each in r:
    # print each[0]
    print "downloading " + each[1]
    pic_uri = requests.get(each[1], headers=headers)
    fp = open('meizipics\\' + each[0] + '.jpg', 'wb')
    fp.write(pic_uri.content)
    fp.close()
