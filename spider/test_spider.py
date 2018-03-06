import urllib.request
''' simple
response = urllib.request.urlopen("http://www.sina.com")
print(response.read())

'''

import urllib
import re
 
url = 'https://coincheckup.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    # items = re.findall(pattern,content)
    # for item in items:
    #     haveImg = re.search("img",item[3])
    #     if not haveImg:
    #         print item[0],item[1],item[2],item[4]
    print(content)
except:
	print("error")