from openpyxl import Workbook
import pymysql
import datetime

# openpyxl python读写excel文件
# 写入
# 从数据库取值写入excel

# 定一个工作簿
wb = Workbook()

# 定义一个sheet页对象
sheet = wb.create_sheet("书名", 0)
conn = pymysql.connect(host='localhost', port=3306, db='liu_db',
                       user='liu_mysql', passwd='1234567890', charset='utf8')
cur = conn.cursor()

sql = "select * from py_book"
cur.execute(sql)
result = cur.fetchall()
sheet.append(['编号', '书名', '作者', '爬取时间'])
i = 0
print(result)

# 向excel加入数据1
while i < len(result):
    # 写入sheet页
    sheet.append([result[i][0], result[i][1], result[i][2]])
    i += 1

# # 向excel加入数据2
# index = chr(68) + str(5)
# sheet[index] = datetime.datetime.now()    # sheet['D6'] = datetime.datetime.now()

# 保存工作簿
wb.save("books.xlsx")
