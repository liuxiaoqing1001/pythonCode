#
# python的认识（了解）
# python的作者是Guido
# python的官网：www.python.org
# 在python中，井号#是注释，或者使用'''三个单引号，表示多行注释
# python中，使用缩进表示在方法体中，没有{}。
# 语法与java和javascript的综合体相似

'''

    变量和数据类型
    数字字母和下划线，并且数字不能开头
    关键字不能用
    1.对于变量名，见名知意
    2.不要用英文和中文拼音混写
    3.多写注释！！！！
    4.建议采用骆驼标记法userName

    数据类型
    1.数字类型  1.int 2.long 3.float 4.复数complex
    2.字符串类型
    3.布尔类型  boolean True和False
    4.List 列表
    5.Tuple 元组（是一个只能用来读取的列表，不能添加，删除和修改）
    6.Dictionary 字典（更接近Java中的map）

    一般是通过type()来判断变量是什么类型

    输出：
    print()
    格式化输出：
    %d 表示整数 常用
    %s 表示字符串 常用
    %c 表示字符
    %o 八进制整数
    %x 十六进制
    %X 十六进制
    %f 浮点数 常用

    输入：
    使用input函数，返回值都是字符串
    如果需要进行数学计算的话，需要转换为int或者float
    例如：
    age = int(input("请输入您的年龄:"))
    price = float(input("苹果的单价是多少:"))
    str() 转换为字符串
    list(x) 将x变成一个列表
    chr(x) 将一个整数转换为一个字符
    ord(x) 将一个字符转换为对应的整数

    运算符：
    // 求除法的整数部分
    % 求除法的余数部分
    ** 幂运算
    没有++自增运算符


'''
print(ord('A'))
print(chr(97))
a = 1
a += 1
print(a)
print(a)
print(9//2)
print(9/2)
print(9%2)
print(2**3)

age = int(input("请输入您的年龄:"))
price = float(input("苹果的单价是多少:"))
print(age+10)
print(type(price))

print("*"*50)
age = 20
name = '王大花'
print(type(12.5))
print("我名字是\t%s,\n我的年龄是%d\n"%(name,age))

print("hh")
a = 10
if a>10:
    print("hh")
elif a>2:
    print("hh")
else:
    pass
name = 'billl'
name = "gatmes"
print(0.1+0.2)

def show(name,a):
    print(name)

show(123,"哈哈哈")
