# import MySQLdb    Python3不支持MySQLdb模块，需要用pymysql替代
import datetime
import pymysql
import time

# jdbc
# 1. 加载驱动
# 2. 获得数据库的链接 connection接口
# 3. Statement
#    PrepareStatement，CallableStatement（调存储过程的）
# 4. 各种关闭（连接池）
#
# python
# 1. 获得数据库的连接
# 2. 获得执行sql语句的对象（游标指针）
# 3. 各种关闭

# 取时间
# sql命令：select NOW()

# 方法一
t = time.localtime()    # 本地时间  中国-东八区
print(time.strftime("%Y-%m-%d %H:%M:%S", t))    # 格式化时间

# 方法二
print(datetime.datetime.now())  # 取时间


# 1. 获得数据库的连接
conn = pymysql.connect(host='localhost', port=3306, db='liu_db',
                       user='liu_mysql', passwd='1234567890', charset='utf8')
cur = conn.cursor()

# 插入数据
sql = "insert into py_book values (uuid(),%s,%s,now(),0)"
param = ['py', 'join']
cur.execute(sql, param)     # cur.execute()执行sql语句
conn.commit()

# 修改数据
sql = "UPDATE py_book SET bookstate =%s WHERE bookid = %s"
param = [1, '39157aad-0551-11eb-ab8e-5800e3fd00cf']
cur.execute(sql, param)     # cur.execute()执行sql语句
conn.commit()

# 删除数据
sql = "DELETE from py_book where bookname =%s"
param = ['py']
cur.execute(sql, param)     # cur.execute()执行sql语句
conn.commit()

# 以下是查询

# 单行查询
sql = "select * from py_book where bookid = 'c31a39e3-0515-11eb-a520-8c164523726e'"
cur.execute(sql)
result = cur.fetchone()     # fetch one
print(result[1])

# 多行查询
sql = "select * from py_book"
cur.execute(sql)
result = cur.fetchall()     # fetch all
print(result[0][1])

