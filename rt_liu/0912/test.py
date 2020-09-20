# 字符串，列表，元组，字典

### 1.字符串

#### 1.1 切片

# 切片类似于Java中截取字符串函数
# 切片的语法[起始:结束:步长]
# 默认的步长是1
# 注意：选取的区间属于左闭右开，结束位不包含结束位本身

name = 'abcdef'
print(name[0])
print(name[1])
print(name[2])

print(name[0:3:2])  # 从第零位开始，到3-1位结束，每间隔2个字母取一个字符
print(name[0:-1])  # -1表示从倒数的第二位开始取值
print(name[:3])  # 从第零位开始，到3-1位结束 每间隔1个字母取一个字符
print(name[3:len(name)])  # 从第四位开始，取到字符nanme的最后一位
print(name[::])  # 取得全部的字符

#### 1.2 常用字符串函数

# | 函数 | 含义 |
# |:----: |:----------------------------------------------------------: |
# | find | 检测一个字符串在另一个字符串中的开始的索引位置，没找到返回 - 1，起始位置和结束位置可选 |
# | index | 检测一个字符串在另一个字符串中的开始的索引位置，没找到会抛出异常，起始位置和结束位置可选 |
# | count | 检测一下在字符串中出现的另一个字符串的个数，推荐和index函数一块使用 |
# | replace | 替换，将第个参数替换为第二个参数，替换次数为第三个参数，第三个参数可以不写，默认是全部替换 |
# | split | 切割函数，切割以后会变成列表，第一个是切割的字符，第二参数是最大切割值，第二个参数可以不写，返回一个列表 |
# | capitalize | 字符串的第一个单词首字母大写 |
# | title | 字符串中所有单词的首字母大写 |
# | upper | 全部变大写 |
# | lower | 全部变小写 |
# | startswith | 以特定字符开头，如果是返回True, 否者返回False |
# | endswith | 以特定字符结尾，如果是返回True, 否者返回False |
# | ljust | 左对齐，字符不够用空格补位 |
# | rjust | 右对齐，字符不够用空格补位 |
# | center | 剧中对齐，字符不够用空格补位 |
# | lstrip | 去掉字符串左边的空格 |
# | rstrip | 去掉字符串右边的空格 |
# | strip | 去掉字符串两边的空格 |
# | partition | 分区，只分为三个部分，返回一个元组 |
# | splitlines | 按行分割，返回一个包含多行的元素的列表 |
# | isalpha | 判断字符都是字母，是返回True否则返回False |
# | isdigit | 判断字符都是数字，是返回True否则返回False |
# | isalnum | 判断字符都是字母和数字，是返回True否则返回False |
# | isspace | 判断字符仅包含空格，是返回True否则返回False |
# | join | 使用特殊的连接符号将列表连接称为一个新的字符串 |

### 2.列表

#### 2.1 什么是列表
# ​列表类似于Java中的ArrayList

#### 2.2 定义列表的语法：

namesList = ['张三', '李四', '王五']  # 定一个列表并赋值
wordsList = []  # 定一个空的列表

print(namesList[0])  # 通过列表的索引值访问
print(namesList[1])
print(namesList[2])

# 使用for循环进行打印
for name in namesList:
    print(name)

# 使用While循环进行打印
listLength = len(namesList)
i = 0
while i < listLength:
    print(namesList[i])
    i += 1

#### 2.3 List的常用操作函数

# | 函数 | 说明 |
# |:------------------: |:----------------------------------------------------------: |
# | append(object) | 将元素添加到列表的最后，如果追加的是个列表的话，原列表保持不变 |
# | extend(object) | 将元素添加到列表的最后，如果追加的是个列表的话，则将原来的列表项变成元素，逐一追加到新列表后面 |
# | insert(index, object) | 将元素，添加到指定的位置上，index是新列表的索引值 |
# | in | 表示某一个元素在列表中 |
# | not in | 表示某个元素不在列表中 |
# | index | 某个元素在列表中的索引位置，没有找到的话，会引发异常 |
# | count | 某个元素在列表中出现的次数 |
# | del | 根据下标进行删除 |
# | pop | 删除最后一个元素 |
# | remove | 根据元素的值进行删除 |

# 添加
wordsList = []
list = [1, 2]
wordsList.append("apple")
wordsList.append(list)
wordsList.extend(list)
wordsList.insert(0, 'banana')
print(wordsList)

# 修改
wordsList[0] = 'orange'

# 查找
# in 和 not in
findName = input("随便输入个水果的名字:")
if findName in wordsList:
    print("真遗憾，居然找到了~~~！")
else:
    print("道喜，没有，娃哈哈哈哈！")

# index count
if wordsList.count(findName) >= 1:
    print(wordsList.index(findName))
else:
    print("哎呀~")

# 删除
# 通过del的方式
findName = input("随便输入个水果的名字:")
if wordsList.count(findName) >= 1:
    index = wordsList.index(findName)
    del wordsList[index]
print(wordsList)

# 通过pop的方法删除
wordsList.pop()
print(wordsList)

# 通过remove的方法删除
findName = input("随便输入个水果的名字:")
wordsList.remove(findName)
print(wordsList)

### 3.元组

# 元组和列表本质上是一样的，元组和列表只有一个却别，就是元组只能查看，增删改对于元组来说，都是不可以操作的。

tlist = tuple(wordsList)  # 将列表转成元组
print(tlist)  # 打印元组
['orange', 'apple', 'banan', 'peach']  # 列表的形态
('orange', 'apple', 'banan', 'peach')  # 元组的形态 ，是一个只读的列表，不可以进行增删改的操作，会引发异常

### 4.字典

# 4.1字典更类似于JSON
#
# 4.2字典的定义：
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}

# 4.3调用字典：
print(person["phone"])  # 根据键找到对应的value值

# 4.4字典的常用方法

# | 方法 | 说明 |
# |:---: |:------------------------: |
# | del | 删除指定的元素 |
# | clear | 删除整个字典 |
# | len | 获取字典中元素的个数 |
# | keys | 获取字典中所有的键 |
# | items | 获得字典中所有的字典的列表 |
# | | |
# | | |

# 修改字典的值
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}
person["name"] = 'tom'
print(person)

# 添加属性
# 直接写就行了
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}
person["name"] = 'tom'
person["id"] = 1000
print(person)

# 删除
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}
person["name"] = 'tom'
person["id"] = 1000
del person["sex"]  # 删除指定元素
print(person)

# clear
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}
person["name"] = 'tom'
person["id"] = 1000
del person["sex"]
print(person)

person.clear()  # 删除整个字典
print(person)

# 获取字典中元素的个数
print(len(person))

# 获取字典中所有的键列表
print(person.keys())

# 获得字典中的所有值列表
print(person.values())

# 获得字典中所有的字典的列表
print(person.items())

# 列表和字典混合使用
personList = []
person = {"name": "", "age": "", "sex": "", "phone": ""}

while True:
    person["name"] = input("请输入姓名:")
    person["age"] = input("请输入年龄:")
    person["sex"] = input("请输入性别:")
    person["phone"] = input("请输入电话:")

    personList.append(person)

    choose = input("是否继续?Y/N")
    if choose == 'n' or choose == 'N':
        break

for p in personList:
    print("姓名%s \t 年龄:%s \t 性别:%s \t 电话:%s" % (p["name"], p["age"], p["sex"], p["phone"]))
