import urllib.request
from urllib.request import ProxyHandler

h={
    "Accept": "application/json",
     "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",}  #键值对
req= urllib.request.Request("http://httpbin.org/get",headers=h)

proxies = {"http":"180.88.111.187:3128"}
proxy_handler = ProxyHandler(proxies = proxies)
opener = urllib.request.build_opener(proxy_handler)
#r=urllib.request.urlopen(req) #传Request对象
r = opener.open(req)

print(r.read().decode())
