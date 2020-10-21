import zipfile

z = zipfile.ZipFile('hh1.zip', 'w')
try:
    z.write("books1.xlsx")
    z.write('ddSpider1.py')
    z.write('demo1.py')
except Exception as ex:
    print(ex)
else:
    z.close()
finally:
    print("运行完毕")
