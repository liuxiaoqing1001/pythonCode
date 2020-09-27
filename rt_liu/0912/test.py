# 字符串，列表，元组，字典

# 字符串
# 切片

# 切片类似于Java中截取字符串函数
# 切片的语法[起始:结束:步长]
# 默认的步长是1
# 注意：选取的区间属于左闭右开，结束位不包含结束位本身

print("*"*50)
name = 'abcdefghijklmn'
print(name[0])
print(name[1])
print(name[2])

print("*"*50)
print(name[0:7:2])      # 从0开始，到3-1位结束，每间隔2个字母取一个字符
print(name[0:-1])        # -1表示从倒数的第二位开始取值
print(name[:3])         # 从0开始，到3-1位结束 每间隔1个字母取一个字符
print(name[3:len(name)])  # 从第4位开始，取到字符nanme的最后一位
print(name[::])          # 取得全部的字符

# 常用字符串函数
print("*"*50)
mystr = "hello is world is a good is day"

# | find | 检测一个字符串在另一个字符串中的开始的索引位置，没找到返回 - 1，起始位置和结束位置可选 |
print(mystr.find('world', 0, len(mystr)))

# | index | 检测一个字符串在另一个字符串中的开始的索引位置，没找到会抛出异常，起始位置和结束位置可选 |
# print(mystr.index('qq', 0, len(mystr)))

# | count | 检测一下在字符串中出现的另一个字符串的个数，推荐和index函数一块使用 |
print(mystr.count('is'))

# | replace | 替换，将第个参数替换为第二个参数，替换次数为第三个参数，第三个参数可以不写，默认是全部替换 |
print(mystr.replace('is', 'sss', 2))

# | split | 切割函数，切割以后会变成列表，第一个是切割的字符，第二参数是最大切割值，第二个参数可以不写，返回一个列表 |
print(mystr.split("is"))    # 返回一个list

# | capitalize | 字符串的第一个单词首字母大写 |
print(mystr.capitalize())

# | title | 字符串中所有单词的首字母大写 |
print(mystr.title())

# | upper | 全部变大写 |
print(mystr.upper())

# | lower | 全部变小写 |
print(mystr.lower())

# | startswith | 以特定字符开头，如果是返回True, 否者返回False |
print(mystr.startswith("hello"))

# | endswith | 以特定字符结尾，如果是返回True, 否者返回False |
print(mystr.endswith("hello"))

str1 = "hello"
# | ljust | 左对齐，字符不够用空格补位 |
print(str1.ljust(20))

# | rjust | 右对齐，字符不够用空格补位 |
print(str1.rjust(20))

# | center | 剧中对齐，字符不够用空格补位 |
print(str1.center(20))

str2 = "    hahahaha    "
# | lstrip | 去掉字符串左边的空格 |
print(str2.lstrip())

# | rstrip | 去掉字符串右边的空格 |
print(str2.rstrip())

# | strip | 去掉字符串两边的空格 |
print(str2.strip())

# | partition | 分区，只分为***三个部分***，返回一个元组 |
print(mystr.partition("is"))    # ()元组   {}字典   []列表

str3 = "hello\nworld"
# | splitlines | 按行分割，返回一个包含多行的元素的列表 |
print(str3.splitlines())

str4 = "abc12"
# | isalpha | 判断字符都是字母，是返回True否则返回False |
print(str4.isalpha())

# | isdigit | 判断字符都是数字，是返回True否则返回False |
print(str4.isdigit())

# | isalnum | 判断字符都是字母和数字，是返回True否则返回False |
print(str4.isalnum())

# | isspace | 判断字符仅包含空格，是返回True否则返回False |
print(str4.isspace())

s = "_"
lists = ["bill", "gates", "lao", "wang"]
# | join | 使用特殊的连接符号将列表连接称为一个新的字符串 |
print(s.join(lists))

# 列表
# 什么是列表
# ​列表类似于Java中的ArrayList

# 定义列表的语法：
print("*"*50)
namesList = ['张三', '李四', '王五']  # 定一个列表并赋值
wordsList = []  # 定一个空的列表

print(namesList[0])  # 通过列表的索引值访问
print(namesList[1])
print(namesList[2])

# 使用for循环进行打印
print("*"*50)
for name in namesList:
    print(name)

# 使用While循环进行打印
print("*"*50)
# len求字符串的长度，也可以求列表中元素的个数
listLength = len(namesList)
i = 0
while i < listLength:
    print(namesList[i])
    i += 1

# List的常用操作函数

# ()元组 {}字典 []list

# 添加 append,extend,insert
print("*"*50)
wordsList = []

# | append(object) | 将元素添加到列表的最后，如果追加的是个列表的话，原列表保持不变 |
list1 = [1, 2]
wordsList.append("apple")
print(wordsList)
wordsList.append(list1)     # 加入一个list
print(wordsList)
print(wordsList[1][1])

# | extend(object) | 将元素添加到列表的最后，如果追加的是个列表的话，则将原来的列表项变成元素，逐一追加到新列表后面 |
list2 = ['a', 'b']
wordsList.extend(list2)     # 加入原来列表的内容
print(wordsList)

# | insert(index, object) | 将元素，添加到指定的位置上，index是新列表的索引值 |
wordsList.insert(0, 'banana')
print(wordsList)

# 修改
print("*"*50)
wordsList[0] = 'orange'
print(wordsList)    # 覆盖

# 查找
# | in | 表示某一个元素在列表中 |
# | not in | 表示某个元素不在列表中 |
print("*"*50)
findName = input("随便输入个水果的名字:")
if findName in wordsList:
    print("真遗憾，居然找到了~~~！")
else:
    print("道喜，没有，娃哈哈哈哈！")

# | index | 某个元素在列表中的索引位置，没有找到的话，会引发异常 |
# | count | 某个元素在列表中出现的次数 |
# index count
if wordsList.count(findName) >= 1:
    print(wordsList.index(findName))
else:
    print("哎呀~")

# 删除
# | del | 根据下标进行删除 |
print("*"*50)
findName = input("随便输入个水果的名字:")
if wordsList.count(findName) >= 1:
    index = wordsList.index(findName)
    del wordsList[index]
print(wordsList)

# | pop | 删除最后一个元素 |
wordsList.pop()
print(wordsList)

# | remove | 根据元素的值进行删除 |
findName = input("随便输入个水果的名字:")
wordsList.remove(findName)
print(wordsList)


# 元组
# 元组和列表本质上是一样的
# 元组和列表只有一个区别：
#   元组只能查看，增删改对于元组来说，都是不可以操作的。

print("*"*50)
# 将列表转成元组tuple
tlist = tuple(wordsList)
print(tlist)  # 打印元组
# ['orange', 'apple', 'banan', 'peach']  # 列表的形态
# ('orange', 'apple', 'banan', 'peach')  # 元组的形态 ，是一个只读的列表，不可以进行增删改的操作，会引发异常

# 字典

# 字典更类似于JSON
#
# 字典的定义：
print("*"*50)
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}

# 调用字典：
print(person["phone"])  # 根据键找到对应的value值

# 4.4字典的常用方法

print("*"*50)
# 删除
# | del | 删除指定的元素 |
person["name"] = 'tom'
person["id"] = 1000
del person["sex"]  # 删除指定元素
print(person)

# | clear | 删除整个字典 |
person.clear()  # 删除整个字典
print(person)

print("*"*50)
# | len | 获取字典中元素的个数 |
person = {"name": "bill", "age": 20, "sex": True, "phone": "13888888888"}
print(len(person))

# | keys | 获取字典中所有的键 |
print(person.keys())

# 获得字典中的所有值列表
print(person.values())

# | items | 获得字典中所有的字典的列表 |
print(person.items())

# 修改字典的值
person["name"] = 'tom'
print(person)

# 添加属性
# 直接写就行了
person["name"] = 'tom'
person["id"] = 1000
print(person)


# 列表和字典混合使用
print("*"*50)
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
