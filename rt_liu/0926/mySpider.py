import time
from selenium import webdriver
from lxml import etree
import urllib
import urllib.request

def savePic(imgUrl,bookid):
    # 准备头信息，告诉服务器，我是一个浏览器不是爬虫
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

    #将图片的url路径复制到浏览器的地址栏中（模拟过程）
    bookImgRequest = urllib.request.Request(imgUrl,headers=headers)

    # 将请求发送给服务器端（模拟一个回车的操作）
    fromResponseImg = urllib.request.urlopen(bookImgRequest).read()

    # 将图片保存到本地，定义路径
    bookImgSavePath = "bookimg/"+str(bookid)+".png"

    # 保存图片
    # f = open(bookImgSavePath,"wb")
    # f.write(fromResponseImg)
    # f.close()

    with open(bookImgSavePath,"wb") as f:
        f.write(fromResponseImg)


# 定义使用chrome浏览器，内置浏览器
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

# 访问网站
driver.get("http://book.dangdang.com/")

driver.find_element_by_id("key_S").send_keys("python")

# driver.find_element_by_class_name("button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/input[9]").click()

# 进行延迟处理
print("延迟加载开始")
i = 300
while i < 16000:
    js = "var q = document.documentElement.scrollTop="+str(i)
    driver.execute_script(js)
    print("距离网页顶部的像素是%dpx"%i)
    time.sleep(1)
    i+=300
print("延迟加载结束")

# 将网页的html代码转换成为xml
# print(driver.page_source)
page = etree.HTML(driver.page_source)
# print(page)
list = page.xpath("//div[@class='con shoplist']/div[@id='search_nature_rg']/ul/li")
# print(len(list))
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

    # print("="*50)

    # 图片
    imgUrl = item.xpath("a[@class='pic']/img/@src")
    savePic("".join(imgUrl),bookid)
    bookid+=1
    # print(imgUrl)