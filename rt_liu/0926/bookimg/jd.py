import time
from datetime import datetime
from selenium import webdriver
from lxml import etree
import selenium.webdriver.support.ui as ui

def connectionDatabase():   # 获得数据库连接
    conn = MySQLdb.connect(host='localhost', port=3306, db='jdSpider',
                           user='root', passwd='123456', charset='utf8')
    return conn


def saveMoonCake(conn, price , shopname, totalDiscuss):     # 保存月饼信息
    cur = conn.cursor()
    sql = "insert into mooncake(mooncakePrice , mooncakeManufacturer , mooncakeComment , createTime) values(%s , %s , %s , %s)"
    param = [price, shopname, totalDiscuss, datetime.now()]
    cur.execute(sql, param)
    conn.commit()
    print("保存完毕！")
    cur.close()
    conn.close()


driver = webdriver.Chrome(executable_path=r"D:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.jd.com")
driver.find_element_by_xpath("//div[@class='search-m']/div[@class='form']/input").send_keys("月饼")
driver.find_element_by_xpath("//div[@class='search-m']/div[@class='form']tton").click()

current = 1
end = 10
while current <= end:
    # 按照销量排序
    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()
    # 显示京东物流
    driver.find_element_by_xpath('//*[@id="J_feature"]/ul[1]/a').click()
    print('延迟加载开始')
    i = 300
    while i < 7600:
        js = "var q = document.documentElement.scrollTop=" + str(i)
        driver.execute_script(js)   # 执行JavaScript脚本
        print('距离顶部像素是%dpx' % i)
        time.sleep(1)
        i += 300
    print("延迟加载结束")

    page = etree.HTML(driver.page_source)
    print("当前是第%d页，共%d页" % (current, end))
    a = 2 * current + 1
    b = 1 + (current - 1) * 50
    newPageUrl = "https://search.jd.com/Search?keyword=月饼&qrst=1&wq=月饼&stock=1&page="+str(a)+"&s="+str(b)+"&click=0"
    list = page.xpath("//div[@class='ml-wrap']/div[@class='goods-list-v2 gl-type-1 J-goods-list']/ul")
    snackid = 1
    print("开始处理数据")
    for item in list:
        price1 = item.xpath("div[@class='gl-i-wrap']/div[@class='p-price']/em/text()")
        price2 = item.xpath("div[@class='gl-i-wrap']/div[@class='p-price']/i/text()")
        price = price1 + price2
        totalPrice = ''
        for p in price:
            totalPrice += p
        print("价格：")
        print(totalPrice)
        shopname = item.xpath("div[@class='gl-i-wrap']/div[@class='p-shop']/span/a/text()")
        print("厂家：")
        print(shopname)
        discuss1 = item.xpath("div[@class='gl-i-wrap']/div[@class='p-commit']/a/text()")
        discuss2 = item.xpath("div[@class='gl-i-wrap']/div[@class='p-commit']/text()")
        discuss = discuss1 + discuss2
        totalDiscuss = ''
        for name in discuss:
            totalDiscuss += name
        print(totalDiscuss)

        if totalPrice == null or shopname == [] or totalDiscuss == null:
             totalPrice = shopname = totalDiscuss = "无"
        else:
            saveMoonCake(connectionDatabase(), totalPrice, shopname, totalDiscuss)

    current += 1

    time.sleep(2)  # 减速

    driver.get(newPageUrl)