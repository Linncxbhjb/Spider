import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

headers={
    "Accept": "application/json",
     "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",}
data = {'username':'longmao',
        'password':'123456'}

def getHtml():
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
       try:
           r = requests.post('http://httpbin.org/post', headers=headers, proxies={"http": "http://{}".format(proxy)}, data=data)

        # 使用代理访问
           return r
       except Exception:
          retry_count -= 1
# 删除代理池中代理
    delete_proxy(proxy)

r = getHtml()
print(r.text)
