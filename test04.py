import ddddocr
import requests

from bs4 import BeautifulSoup

headers={
    "Accept": "application/json",
     "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/129.0.0.0 Safari/537.36",}

proxies = {"http":"http://127.0.0.1:7890",
           "https":"http://127.0.0.1:7890"}

s=requests.Session()
login=s.get("https://www.nowapi.com/?app=account.login",headers=headers,proxies=proxies)
#print(login.text)


soup=BeautifulSoup(login.text,'html.parser')
image_url=soup.find_all(id='authCodeImg')[0]['src']

rep_code=s.get(str(image_url),headers=headers,proxies=proxies)
image_code=rep_code.content
with open('lm.jpg','wb') as f:
    f.write(image_code)



ocr=ddddocr.DdddOcr()
image=open('lm.jpg','rb').read()
result=ocr.classification(image)
print(result)

#登录
data = {'username':'syl9617016',
        'password':'syl123321',
        'authcode': result,
        'toUrl': '',
        'app': 'accountr.aja_login'
        }

r = requests.post('https://www.nowapi.com/index.php?ajax=1',headers=headers,proxies=proxies,data=data)

print(r.text)
