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


t = time.localtime()    # 本地时间  中国-东八区
print(time.strftime("%Y-%m-%d %H:%M:%S", t))
print(datetime.datetime.now())


# 1. 获得数据库的连接
conn = pymysql.connect(host='localhost', port=3306, db='liu_db',
                       user='liu_mysql', passwd='1234567890', charset='utf8')
cur = conn.cursor()

# sql = "insert into py_book values (uuid(),%s,%s,now())"
# param = ['Java从入门到跑路', '旺海明']
sql = "UPDATE py_book SET bookstate =%s WHERE bookid = %s"
param = [1, 'f6fadd45-0514-11eb-a520-8c164523726e']
cur.execute(sql, param)
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





# select * from py_book;
# # select UUID();
# # insert into py_book values (uuid(),%s,%s,now())
# alter table py_book add bookstate int;
# # insert into py_book values (uuid(),%s,%s,now(),1)
# # UPDATE py_book SET bookstate =%s WHERE bookid = %s
# insert into py_book values (uuid(),'python','张三',now(),0)
#
# insert into py_book values ('c31a39e3-0515-11eb-a520-8c164523726e','c语言','里斯',now(),0)