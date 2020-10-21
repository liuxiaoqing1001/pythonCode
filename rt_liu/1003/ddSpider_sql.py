import time
from selenium import webdriver
from lxml import etree
import urllib
import urllib.request
from selenium.webdriver.chrome.options import Options
import pymysql

# 多页爬虫

# 数据库
# 获得数据库的连接
def connectionDatabase():
    conn = pymysql.connect(host='localhost', port=3306, db='liu_db',
                           user='liu_mysql', passwd='1234567890', charset='utf8')
    return conn


# 保存图书信息
def saveBook(conn, bookname, autor, price, nowPrice, discount, press):
    cur = conn.cursor()
    sql = ""
    param = [bookname, autor, price, nowPrice, discount, press]
    cur.execute(sql, param)
    conn.commit()
    print("保存完毕")


# def savePic(imgUrl, bookid):
#     # 准备头信息，告诉服务器，我是一个浏览器不是爬虫
#     # 查看图片  Fn+F12  network 刷新页面    Request Headers     User-Agent
#     headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
#
#     # 将图片的url路径复制到浏览器的地址栏中（模拟过程）
#     bookImgRequest = urllib.request.Request(imgUrl, headers=headers)
#
#     # 将请求发送给服务器端（模拟一个回车的操作）
#     fromResponseImg = urllib.request.urlopen(bookImgRequest).read()
#
#     # 将图片保存到本地，定义路径
#     bookImgSavePath = "bookimg/"+str(bookid)+".png"
#
#     # 保存图片
#     # # 方法一：
#     # f = open(bookImgSavePath,"wb")
#     # f.write(fromResponseImg)
#     # f.close()
#
#     # 方法二：with相当于一个生命周期
#     with open(bookImgSavePath, "wb") as f:
#         f.write(fromResponseImg)


# 定义使用chrome浏览器，下载chromedriver(保存至/usr/local/bin/)
# driver = webdriver.Chrome()     # 带有窗口界面的（跳出浏览器）

# 不带窗口的
myoption = Options()
myoption.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver", options=myoption)


# 访问网站
driver.get("http://book.dangdang.com/")

driver.find_element_by_id("key_S").send_keys("python")  # 衬衫  python

# driver.find_element_by_class_name("button").click()   # 找id/class_name
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/input[9]").click()   # 找xml位置    火狐

begin = 1
end = 10
# connectionDatabase()
while begin <= end:
    # 进行延迟处理
    print("延迟加载开始")
    i = 300
    while i < 16000:
        js = "var q = document.documentElement.scrollTop=" + str(i)
        driver.execute_script(js)
        print("距离网页顶部的像素是%dpx" % i)
        time.sleep(1)
        i += 300
    print("延迟加载结束")

    page = etree.HTML(driver.page_source)
    print("当前是第%d页，共%d页" % (begin, end))
    newPageUrl = "http://search.dangdang.com/"+"".join(page.xpath("/html/body/div[3]/div/div[3]/div[1]/div[5]/div[2]/div/ul/li[10]/a/@href"))
    list = page.xpath("//div[@class='con shoplist']/div[@id='search_nature_rg']/ul/li")

    print("开始处理数据")
    for item in list:
        pass
        # saveBook(conn, bookname, autor, price, nowPrice, discount, press)
    print("结束处理数据")

    begin += 1

    time.sleep(2)   # 等一会儿  爬的快会死

    driver.get(newPageUrl)

