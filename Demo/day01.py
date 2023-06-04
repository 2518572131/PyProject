#爬取源代码

from urllib import response
import requests

#请求网站链接，请求响应
response=requests.get("https://so.gushiwen.cn/shiwen/")

#响应
htmlCode=response.text

print(htmlCode)