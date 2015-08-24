# __author__ = 'zhengmj'
from PIL import Image
from StringIO import StringIO
import requests
r = requests.get('http://upload.server110.com/image/20130918/222JK917-0.png')
i = Image.open(StringIO(r.content))
i.show()