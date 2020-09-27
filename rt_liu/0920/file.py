# 字节流
# 字符流
# 内存流
# zip流
# 7z
# rar

# 文件

# 文件是什么
# 计算机上能见到的所有内容都是文件

# 打开文件
#   open("盘符路径文件名", "文件打开方式，访问模式")

# | 访问模式 | 说明 |
# |:-----: |:-------------------------------------------: |
# | r | 以只读的形式打开文件。文件的指针放在文件的开头。默认模式。 |
# | w | 打开一个文件，用于写入，如果文件已经存在就覆盖掉，没有的话就新建。 |
# | a | 打开一个文件，用于写入，文件的指针放在文件的最后，追加模式。 |
# | rb | 以二进制的形式读取文件 |
# | wb | 以二进制的形式写入，如果文件已经存在就覆盖掉，没有的话就新建。 |
# | ab | 以二进制的形式打开一个文件，用于写入，文件的指针放在文件的最后，追加模式。 |
# | r + | 同r |
# | w + | 同w |
# | a + | 同a |
# | rb + | 同rb |
# | wb + | 同wb |
# | ab + | 同ab |

# 关闭文件
#   close()

# # 文件写
# f = open("./abc.txt", "w")  # 注意路径的斜杠  /正  \反
# f.write("哈哈哈哈哈")
# f.close()

print("*"*50)
# # 文件读
# f = open("./abc.txt", "r")
# # f.read（）方法，不指定长度，表示读取全部文件,加参数读出几个
# print(f.read(2))
# # f.readlines()表示以行的形式，一次性全部读取，返回一个列表
# print(f.readlines())
# # f.readline()表示读取一行
# print(f.readline())
# for temp in f.readlines():
#     print(temp)
# f.close()  # 文件使用完毕后记得要关闭文件

print("*"*50)
# 文件重命名
import os
# # 使用os.rename方法，记得带上盘符路径文件名
# os.rename("./abc.txt", "./cba.txt")
# # os.rename("./cba.txt", "./abc.txt")

print("*"*50)
# # 删除
# # 进行真正的删除，不会进入回收站
# os.remove("./cba.txt")
# # os.remove("./abc.txt")

print("*"*50)
# # 创建文件夹
# # 当前目录下创建一个hh的文件夹，./表示当前目录
# os.mkdir("./hh")

print("*"*50)
# # 获取当前目录
# # 打印当前目录，就是当前运行文件所在的全路径
# print(os.getcwd())

print("*"*50)
# # 切换目录
# print(os.getcwd())  # 切换当前的目录
# os.chdir("/home/liu/PycharmProjects/pythonCode/rt_liu/0926")  # 切换目录，执行动作
# print(os.getcwd())  # 切换后的目录

print("*"*50)
# # 获取目录的列表
# # listdir返回的时一个列表，获得当前目录下的所有文件和文件夹
# print(os.listdir("/home/liu/PycharmProjects/pythonCode/rt_liu"))

print("*"*50)
# # 删除文件夹
# # 删除指定的文件夹，要求这个文件夹必须是空的，里面不能有任何的文件
# os.rmdir("./hh")
