# coding=utf-8
import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}




class spider(object):
    def __init__(self):
        print u'开始爬取美女图片'

    def getsource(self, url, headers):
        html = requests.get(url, headers=headers).text
        return html

    def changepages(self, url, total_page):
        link_group = []
        pattern = 'page-(\d+)#comments'
        new_pattern = re.compile(pattern)
        now_page = int(re.search(new_pattern, url).group(1))
        # print now_page
        for i in range(now_page, total_page+1):
            link = re.sub('page-\d+#comments', 'page-%d#comments' % i, url)
            link_group.append(link)
        return link_group

    def gen_pic_url(self, html):
        pattern = '<ol class="commentlist" style="list-style-type: none;">(.*?)</ol>'
        new_pattern = re.compile(pattern, re.S)
        new_html = re.search(new_pattern, html).group(1)
        # print new_html
        pattern1 = '<li id="comment-\d+">.*?<img src="(.*?)" .*?</li>'
        new_pattern1 = re.compile(pattern1, re.S)
        r_pic = re.findall(new_pattern1, new_html)
        return r_pic

    # def split_pic_name(self, pic_url):
    #     pic_name = pic_url.split('/')[-1]
    #     return pic_name

    def download_pic(self, list_pic, headers):
        # print list_pic
        for each in list_pic:
            print "正在下载：" + str(each)
            pic_name = each.split('/')[-1]
            pic_uri = requests.get(each, headers=headers)
            fp = open('meizipics1\\' + pic_name, 'wb')
            fp.write(pic_uri.content)
            fp.close()

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/page-1100#comments'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    meinvspider = spider()
    all_links = meinvspider.changepages(url, 1102)
    for link in all_links:
        html = meinvspider.getsource(link, headers)
        all_pic_url = meinvspider.gen_pic_url(html)
        meinvspider.download_pic(all_pic_url, headers)


