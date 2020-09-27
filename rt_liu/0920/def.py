# 函数
# 重复多次调用的方法就是函数，重点是复用

# 定义方法
print("*"*50)


def show():
    print("hello", end="@")     # 不折行
    print("world!")


show()  # 调用方法

# 函数文档的说明
print("*"*50)


def show():

    '''
	# 这里写方法的说明，约详细越好
    :return:无
    '''
    print("hello", end="@")
    print("world!")


help(show)  # 通过help来查看函数的说明

# show()
# help(show)

# 方法的类型
print("*"*50)

# | 无参，无返回值 |
# def show2():
#     print("hh")

# | 无参，有返回值 |
# def show2():
#     return "hh"

# | 有参，无返回值 |
# def show2(a, b):
#     print(a + b)


def add(x, y):
    print(x + y)


add("hello", "world")

# | 有参，有返回值 |
# def show2(a, b):
#     return a + b


def add1(x, y):
    return x + y


add1(11, 12)

# python建议，函数与函数之间是间隔2行

# 局部变量和全局变量
print("*"*50)

# name 是一个全局变量，在方法a和方法b中都可以使用，仅限于读取，
# 如果要修改的话，需要使用global关键字
name = 'bill'


def a():
    global name
    name = 'tom'
    # x是一个局部变量，当a方法运行结束以后，x就会被销毁
    x = 100
    print(name)


def b():
    # x是一个局部变量，当b方法运行结束以后，x就会被销毁
    # 这个x与方法a中的x不是同一个变量
    x = 200
    print(name)


a()
b()


# 参数

# 缺省参数
# 默认值，缺省参数，带有默认值的参数一般是放到参数列表的最后
print("*"*50)


def personInfo(name, age=18):
    print("姓名：%s,年龄：%d" % (name, age))


personInfo("张三")
personInfo("张三", 30)

# 不定长参数
# 一个星号的参数是列表，两个星号的参数是字典
print("*"*50)


def empInfo(name, age, *bookList, **familyInfo):
    print("员工姓名:%s" % name)
    print("员工年龄:%d" % age)
    print("近期阅读的书籍:%s" % (",".join(bookList)))
    print("母上是:%s" % familyInfo["母亲"])


bookList = ['三体', 'CET4级', '时间简史', '24个比利']     # list
familyInfo = {"父亲": "张的水", "母亲": "于秀珍", "哥哥": "张二"}     # 字典
# 传值的时候，列表和字典的前面也要对应的添加对应的星号
empInfo("张三", 30, *bookList, **familyInfo)


# 返回值
# 单个返回值
print("*"*50)


def calc(a, b):
    return a + b


print(calc(1, 2))

# 多个返回值
print("*"*50)


def postion():
    return 123.234, 234.456  # 返回一个定位的精度和纬度


jingdu, weidu = postion()  # 精度和纬度接收参数
print(jingdu)
print(weidu)
# 可以理解为利用了元组


# 递归函数
# 一个自己调用自己的函数。

# 求阶乘！5!
# 5！= 1 * 2 * 3 * 4 * 5

# 采用循环的方法
print("*"*50)


def jc(num):
    i = 1
    result = 1
    while i <= num:
        result *= i
        i += 1
    return result


print(jc(5))

# 采用递归的形式，对内存有一定的压力
print("*"*50)


def jc1(num):
    if num > 1:
        result = num * jc1(num - 1)
    else:
        result = 1
    return result


print(jc1(5))

# 匿名函数(lambda)
print("*"*50)

sum = lambda x, y: x + y


def fun(x, y, opt):     # 要传进来的入表达式，想对xy做什么算术操作
    return opt(x, y)


res = fun(10, 20, lambda x, y: x - y)
print(res)

# 注意事项
# 1.函数名不要写成重复的
# 2.调用时：实参的位置要对号入座
# 3.作用域：尤其是全局变量的修改,加global
# 4.不定长的参数：传参需要加星号的不要忘了
# 5.形参：没有数据类型，一定确定好在传参数
# 6.返回值不需要声明类型，直接写return
# 7.没有花括号，注意缩进（tab键）

