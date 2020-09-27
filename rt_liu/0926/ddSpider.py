import time
from selenium import webdriver
from lxml import etree
import urllib
import urllib.request
from selenium.webdriver.chrome.options import Options

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
# driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe") # 带有窗口界面的
myoption = Options()
myoption.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe",options=myoption)

# 访问网站
driver.get("http://book.dangdang.com/")

driver.find_element_by_id("key_S").send_keys("python")

# driver.find_element_by_class_name("button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/form/input[9]").click()

begin = 1
end = 10
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
    print("当前是第%d页，共%d页"%(begin,end))
    newPageUrl ="http://search.dangdang.com/"+"".join(page.xpath("/html/body/div[3]/div/div[3]/div[1]/div[5]/div[2]/div/ul/li[10]/a/@href"))
    list = page.xpath("//div[@class='con shoplist']/div[@id='search_nature_rg']/ul/li")

    print("开始处理数据")
    for item in list:
        pass
    print("结束处理数据")

    begin += 1

    time.sleep(2)

    driver.get(newPageUrl)

