#
# python的认识（了解）
# python的作者是Guido
# python的官网：www.python.org
# 在python中，井号#是注释，或者使用'''三个单引号，表示多行注释
# python中，使用缩进表示在方法体中，没有{}
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
        2.字符串类型 string
        3.布尔类型  boolean True和False
        4.List 列表
        5.Tuple 元组（是一个只读的列表，不能添加，删除和修改）
        6.Dictionary 字典（更接近Java中的map）

    一般是通过type()来判断变量是什么类型
        price = float(input("苹果的单价是多少:"))
        print(type(price))

    标识符
        就是变量名：数字，字母和下划线组成，并且不能用数字开头。
        ​起名的原则：见名知意
        ​命名法：骆驼命名法，第一个单词的首字母小写，从第二个单词开始每个单词的首字母都是大写

    ​关键字：
        def ,if, try, pass....等都是不可以用的

    输出：print("打印信息")，格式化输出，
        print("姓名:%s,年龄是%d,身高是%f" % ('张三', 23, 193))

    | 符号 | 说明 |
    |:---:|:---------------------------------: |
    | % s | 字符串 |
    | % d | 整型 |
    | % f | float类型 |
    | % c | 字符 |
    | % i | 十进制整型 |
    | % o | 八进制整数 |
    | % x % X | x的大小写决定16进制中的字母的大小写 |

    输出时需要缩进或者换行的 \t和 \n符号
        缩进: print("张三\t李四")    一行打印，但是有一个tab的空格
        换行: print("张三\n李四")    分两行打印

    | 函数 | 说明 |
    |:-----: |:---------------------: |
    | int() | 转整数 |
    | float() | 转小数 |
    | str() | 转成字符串 |
    | chr() | 将整数转成字符(ASCII码) |
    | ord() | 将字符转成整数(ASCII码) |

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
            str()   转换为字符串
            list(x) 将x变成一个列表
            chr(x)  将一个整数转换为一个字符
            ord(x)  将一个字符转换为对应的整数

    运算符：
        //  求除法的整数部分
        %   求除法的余数部分
        **  幂运算
        没有++自增运算符

        无&&
        只有  | and | 与 |
             | or  | 或 |
            | not | 非 |

    比较运算符：
        ==,!=,>,<,<>(检查两个操作的数值是否相同，不等返回真)

    判断语句
    ```python
        if 条件:
            # 使用tab缩进，无{}
            pass
        elif 条件:
            pass
        else:
            pass
    ```

    循环
    ```python
        name = 'hello world'

        # for 循环更类似于foreach的迭代循环
        for n in name:
            print(n)

        # python的循环主要是while
        while 条件:
            pass
        break   # 停止当前的循环
        continue    #停止当次的循环
    ```

'''

# 数据类型转换
# int(),float(),str()
# ord()将字符转成整数(ASCII码)
# chr()将整数转成字符(ASCII码)
print("*"*50)
print(ord('A'))
print(chr(97))

# 没有a++, a--
print("*"*50)
a = 1
a += 1
print(a)

# 运算符
print("*"*50)
print(9//2)
print(9/2)
print(9%2)
print(2**3)

# 输入输出
print("*"*50)
age = int(input("请输入您的年龄:"))    # 类型转换
price = float(input("苹果的单价是多少:"))
print(age+10)
print(type(price))

print("*"*50)
age = 20
name = '王大花'
print(type(12.5))
print("我名字是%s,我的年龄是%d" % (name, age))    # 正确语法
print("我名字是", name, ",我的年龄是%d", age)    # 会带空格 不可取
print("我名字是"+str(name)+",我的年龄是"+str(age))    # 转成字符串 繁琐
# # print("我名字是"+name+"我的年龄是"+age)   在python中是错误语法

# 判断语句
print("*"*50)
a = 10
if a > 10:
    print("hh")
elif a > 2:
    print("hh")
else:
    # 占位符号
    pass
name = 'billl'
name = "gatmes"
print(0.1+0.2)  #0.30000000000000004

# 循环
print("*"*50)
i = 0
while i < 10:
   print("h"*i)
   i += 1
print("*"*50)
name = 'xiaoqing liu 7073'
print("切片", name[0])  # 切片
for n in name:
    print(n)

# 函数
print("*"*50)


def show(name, a):
    print(name)


show(123, "哈哈哈")

