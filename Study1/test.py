# __author__ = 'zhengmj'
# import random
import re

secret_code = 'lsdkjlxxIxxsd-12ilogsdljsdlxxlovexxlj3ljsdlfjxxyouxxljql'

r = re.findall('xx(.*?)xx', secret_code)
print r
for i in r:
    print i

secret_code1 = '''lsdkjlxxI
xxlogsdljsdlxxlovexxlj3ljsdlfjxxyouxxljql'''
r1 = re.findall('xx(.*?)xx', secret_code1, re.S)
print r1


secret_code2 = 'lsdkjlxxIxxsd-12ilogsdljsdlxxlovexxlj3ljsdlfjxxyouxxljql'
r2 = re.search('xx(.*?)xx.*?xx(.*?)xx', secret_code2).group(2)
print r2
f2 = re.findall('xx(.*?)xx.*?xx(.*?)xx', secret_code2)
print f2[0][1]

secret_code3 = '123lsdjfljljlasdjf123'
r3 = re.sub('123(.*)123', '123%d123' % 789, secret_code3)
print r3

secret_code4 = 'lsdkjlxxIxxsd-12ilogsdljsdlxxlovexxlj3ljsdlfjxxyouxxljql'
pattern = 'xx(.*?)xx'
new_pattern = re.compile(pattern, re.S)
r4 = re.findall(new_pattern, secret_code4)
print r4
for each in r4:
    print each


secret_code5 = 'sdljl1214124ljljsdlfkj345234234ljl1j3451llj'
r5 = re.findall('\d+',secret_code5)
print r5
for each in r5:
    print each