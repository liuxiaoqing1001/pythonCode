# import requests
# response = requests.get('http://www.baidu.com')
# print('文本形式的网页源码')
# print(response.text)
# print('二进制流形式打印')
# print(response.content)
# print('返回JSON格式，可能抛出异常')
# print(response.json)
# print('状态码')
# print(response.status_code)
# print('请求url')
# print(response.url)
# print('头信息')
# print(response.headers)
# print('cookie信息')
# print(response.cookies)

# import requests
# payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)
# # requests.get('http://httpbin.org/get')
# # requests.post('http://httpbin.org/post')
# # requests.put('http://httpbin.org/put')
# # requests.delete('http://httpbin.org/delete')
# # requests.head('http://httpbin.org/get')
# # requests.options('http://httpbin.org/get')

# import requests
# # 发送一些编码为表单形式的数据=>非常像一个HTML表单。
# # 实现：传递一个字典给data参数,数据字典在发出请求时会自动编码为表单形式
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# import requests
# # 传递文件
# url = 'http://httpbin.org/post'
# files = {'file': open('./abc.txt', 'rb')}
# r = requests.post(url, files=files)

# # 传递字符串
# import requests
# import json
# url = 'https://baidu.com'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# #或者
# r = requests.post(url, json=payload)

# import requests
# requests.get('http://baidu.com', timeout=1)
# # 注：
# # timeout 仅对连接过程有效，与响应体的下载无关。
# # timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常。

import requests
# 防爬虫会涉及到ip限制，所以ip代理在爬虫中会常用到，还有vpn代理等等吧。
proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
requests.get('http://baidu.com', proxies=proxies)
