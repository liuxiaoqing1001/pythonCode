import time
from selenium import webdriver
from lxml import etree
import urllib
import urllib.request

# 延迟加载
# 爬虫

# 1. lxml		    对网页进行xpath解析（html->xml）
# 2. urllib3        发送request请求 （负责图片的下载）
# 3. mysqlclient    python连接数据库的驱动
# 4. selenium       连接内容内置浏览器的驱动
# 5. chromedriver   内置浏览器，用代码控制的
# 6. 火狐浏览器      xpath的定位器
# 7. openpyxl	python读写excel文件（java读写excel文件用poi）


def savePic(imgUrl, bookid):
    # 准备头信息，告诉服务器，我是一个浏览器不是爬虫
    # 查看图片  Fn+F12  network 刷新页面    Request Headers     User-Agent
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

    # 将图片的url路径复制到浏览器的地址栏中（模拟过程）
    bookImgRequest = urllib.request.Request(imgUrl, headers=headers)

    # 将请求发送给服务器端（模拟一个回车的操作）
    fromResponseImg = urllib.request.urlopen(bookImgRequest).read()

    # 将图片保存到本地，定义路径
    bookImgSavePath = "bookimg/"+str(bookid)+".png"

    # 保存图片

    # # 方法一：
    # f = open(bookImgSavePath,"wb")
    # f.write(fromResponseImg)
    # f.close()

    # 方法二：with相当于一个生命周期
    with open(bookImgSavePath, "wb") as f:
        f.write(fromResponseImg)


# 定义使用chrome浏览器，下载chromedriver(保存至/usr/local/bin/)
driver = webdriver.Chrome()

# 访问网站  https://www.jd.com/
driver.get("http://book.dangdang.com/")

driver.find_element_by_id("key_S").send_keys("python")  # 衬衫  python

driver.find_element_by_class_name("button").click()   # 找id/class_name
# driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/input[9]").click()   # 找xml位置 火狐

# 进行延迟处理 滚动加载
print("延迟加载开始")
i = 300
while i < 16000:
    js = "var q = document.documentElement.scrollTop="+str(i)
    driver.execute_script(js)
    print("距离网页顶部的像素是%dpx"%i)
    time.sleep(1)
    i += 300
print("延迟加载结束")

# 将网页的html代码转换成为xml
# print(driver.page_source)     # 页面源码
page = etree.HTML(driver.page_source)   # 使用etree
# print(page)     # 拿到page对象0x7efe6456cfc0  上两级元素
# xpath规则：
#     从根开始（/）：/html/body/div[1]/div[3]/div/div[2]/form/input[9]
#     非根开始（//）：//div[@class='con shoplist']/div[@id='search_nature_rg']/ul/li
#     属性加@
list = page.xpath("//div[@class='con shoplist']/div[@id='search_nature_rg']/ul/li")
print(len(list))
bookid = 1
for item in list:
    # 书名
    bookname = item.xpath("p[@class='name']/a/@title")
    # print(bookname)

    # 现价
    now_price = item.xpath("p[@class='price']/span[@class='search_now_price']/text()")
    # print(now_price)

    # 原价
    price = item.xpath("p[@class='price']/span[@class='search_pre_price']/text()")
    # print(price)

    # 折扣
    discount = item.xpath("p[@class='price']/span[@class='search_discount']/text()")
    # print(discount)
    # print("-"*50)

    # 图片
    imgUrl = item.xpath("a[@class='pic']/img/@src")
    savePic("".join(imgUrl), bookid)    # "".join(imgUrl)从图片列表中取出对应图片
    bookid += 1
    print(imgUrl)
