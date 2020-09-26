
# 编写一个名片的管理系统：
# 要求有用户名，电话，地址，QQ号的等信息
# 现对名片的增删改查的各项操作

cardList = []
def showMenu():
    print("*"*10+"名片管理系统"+"*"*10)
    print("1.新建")
    print("2.显示")
    print("3.查询")
    print("4.退出")
    print("*"*10)

def addCard():
    name = input("请输入用户名：")
    phone = input("请输入电话：")
    qq = input("请输入QQ号：")
    address = input("请输入地址：")
    cardDict = {"name": name, "phone": phone, "qq": qq, "address": address}
    cardList.append(cardDict)
    print(">"*5+"添加成功"+"<"*5)

def showAll():
    print("-" * 25+"用-户-信-息"+"-"*25)
    if len(cardList) == 0:
        print(">"*5+"当前没有任何记录，请添加名片"+"<"*5)
    for cardDict in cardList:
        print("姓名：%s\t\t电话：%s\t\tQQ：%s\t\t地址：%s"
              %(cardDict["name"], cardDict["phone"], cardDict["qq"], cardDict["address"]))
        print("-" * 50)

def search():
    findName = input("请输入要检索的姓名:")
    for cardDict in cardList:
        if cardDict["name"] == findName:
            print("-" * 50)
            print("姓名：%s\t\t电话：%s\t\tQQ：%s\t\t地址：%s"
                  % (cardDict["name"], cardDict["phone"], cardDict["qq"], cardDict["address"]))
            dealCard(cardDict)
            break
        else:
            print(">"*5+"没有这个人"+"<"*5)

def dealCard(findDict):
    print("-"*50)
    item = input("请选择要执行的操作：1/删除 2/修改 0/返回主菜单")
    if item == "1":
        cardList.remove(findDict)
        print(">"*5+"删除成功"+"<"*5)
    elif item == "2":
        findDict["name"] = inputInfo(findDict["name"], "请输入修改后的姓名：")
        findDict["phone"] = inputInfo(findDict["phone"], "请输入修改后的电话：")
        findDict["qq"] = inputInfo(findDict["qq"], "请输入修改后的QQ号码：")
        findDict["address"] = inputInfo(findDict["address"], "请输入修改后的地址：")
        print(">"*5+"修改成功"+"<"*5)
    elif item == "0":
        print(">"*5+"返回主菜单"+"<"*5)

def inputInfo(value, massage):
    info = input(massage)
    if len(info) > 0:
        return info
    else:
        return value

showMenu()
while True:
    item = input("请选择：")
    if item in ["1", "2", "3"]:
        if item == "1":
            addCard()
        elif item == "2":
            showAll()
        elif item == "3":
            search()
    elif item == "4":
        print(">"*5+"已退出"+"<"*5)
        break
    else:
        print(">"*5+"输入错误，请重新选择"+"<"*5)
