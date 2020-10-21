# 以下情况务必加上异常处理
# IO，数据库，多线程，网络通讯
try:
    print(10/0)
except Exception as ex:
    print(ex)
else:
    print("没有任务问题时，执行这里")
finally:
    print("我是finally")
