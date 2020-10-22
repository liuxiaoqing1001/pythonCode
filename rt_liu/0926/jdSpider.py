import pymysql
import null
from selenium import webdriver
import time
from lxml import etree
import datetime
from selenium.webdriver.chrome.options import Options


def connectionDatabase():
    conn = pymysql.connect(host='localhost', port=3306, db='jdSpider',
                           user='liu_mysql', passwd='1234567890', charset='utf8')
    return conn


def saveMoon(conn, price, manufacturer, commit):
    cur = conn.cursor()
    sql = "insert into mooncake values(uuid(), %s , %s , %s , %s)"
    param = [price, manufacturer, commit, datetime.datetime.now()]
    cur.execute(sql, param)
    conn.commit()
    print("保存完毕")
    cur.close()
    conn.close()


driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.find_element_by_id("key").send_keys("月饼")
driver.find_element_by_class_name("button").click()

begin = 1
end = 10
while begin <= end:

    driver.find_element_by_xpath('//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="J_feature"]/ul/li[1]/a').click()

    print("延迟加载开始")
    i = 300
    while i < 10000:
        js = "var q = document.documentElement.scrollTop=" + str(i)
        driver.execute_script(js)
        print("距离网页顶部的像素是%dpx" % i)
        time.sleep(1)
        i += 300
    print("延迟加载结束")

    page = etree.HTML(driver.page_source)
    print("当前是第%d页，共%d页" % (begin, end))
    a = 2 * begin + 1
    b = 1 + (begin - 1) * 50
    newPageUrl = "https://search.jd.com/Search?keyword=月饼&qrst=1&wq=月饼&stock=1&page="+str(a)+"&s="+str(b)+"&click=0"
    # newPageUrl = "http://search.jd.com/"+"".join(page.xpath("//div[@class='paging']/ul/li[@class='next']/a/@href"))
    list = page.xpath("//div[@id='J_goodsList']/ul/li/div")

    print("开始处理数据")
    try:
        for item in list:
            price = item.xpath("div[@class='p-price']/strong/i/text()")
            print(price)

            manufacturer = item.xpath("div[@class='p-shop']/span/a/@title")
            print(manufacturer)

            commit1 = item.xpath("div[@class='p-commit']/strong/a/text()")
            commit2 = item.xpath("div[@class='p-commit']/strong/text()")
            commit = commit1 + commit2
            totalCommit = ''
            for c in commit:
                totalCommit += c
            print(totalCommit)

            if price == [] or manufacturer == [] or totalCommit == []:
                price = manufacturer = totalCommit = "无"
            else:
                saveMoon(connectionDatabase(), price, manufacturer, totalCommit)
    except Exception as ex:
        print(ex)
    else:
        begin += 1
        time.sleep(2)
        driver.get(newPageUrl)
    finally:
        print("结束处理数据")

