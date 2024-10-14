import urllib.request
import pymysql
from bs4 import BeautifulSoup
from requests import session

start = 0
for i in range(0,11):  #for循环十个页面
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='@Rjl890411',
                                 database='spider',
                                 cursorclass=pymysql.cursors.DictCursor)

    h = {
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36 (HTML,like Gecko)Chrome/124.0.0.0 Safari/537.36"
    }
    req = urllib.request.Request(f'https://movie.douban.com/top250?start={start}&filter=', headers=h)
    r = urllib.request.urlopen(req)
    html_doc = r.read().decode()

    # 使用bs4或者正则表达式解析数据
    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all("div", class_="item")  # 获取第一页每个电影的div,div叫item
    # infos=soup.find_all("div",class_="info")
    # find_all找列表，find找一个

    
    # 遍历列表
    with connection:
        for item in items:
            # img=item.find("div",class_="pic").a.img
            pic_div = item.find("div", class_="pic")
            img = pic_div.a.img
            name = img['alt']  # 取出img里的alt   #电影名
            url = img['src']  # 网址

            hd = item.find("div", class_="hd")
            English = hd.find_all("span")  # 找出hd下的所以span标签
            title_english = English[1].text
            other = hd.find("span", class_="other").text

            bd = item.find("div", class_="bd")
            dictor = item.find("div", class_="bd").p.text.strip()  # 导演

            star = bd.find("div", class_="star")
            score = star.find("span", class_="rating_num").text  # 评分

            comments = star.find_all("span")
            comment = comments[3].text  #索引从0开始
            summary = bd.find("span", class_="inq")  # 简介

            if summary is not None:
                summary = bd.find("span", class_="inq").text
            else:
                summary = bd.find("span", class_="inq")

                # 存储数据
            with connection.cursor() as cursor:  # 游标
                sql = ("INSERT INTO `movie_info`(`name`,`url`,`title_english`,"
                       "`other`,`dictor`,`score`,`comment`,`summary`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(sql, (name, url, title_english, other, dictor, score, comment, summary))
        connection.commit()

    start = start + 25 #每个页面的start加25
    '''
    https://movie.douban.com/top250?start=25&filter=
    https://movie.douban.com/top250?start=50&filter=
    https://movie.douban.com/top250?start=75&filter=
    '''
