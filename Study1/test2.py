# __author__ = 'zhengmj'
import re
old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20
f = open('text1.html', 'r')
html = f.read()
f.close()

pattern = '<title>(.*?)</title>'
new_pattern = re.compile(pattern, re.S)
j_title = re.search(new_pattern, html).group(0)
print j_title
j_title1 = re.search(new_pattern, html).group(1)
print j_title1
j_title2 = re.search(new_pattern, html)
print j_title2
# r = re.search('<title>(.*?)</title>', html, re.S).group(1)
# print r