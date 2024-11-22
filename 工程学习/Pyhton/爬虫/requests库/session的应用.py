# Session对象可以用于保持会话状态，例如在多个请求之间共享cookies。
import requests
# 先实例化一个对象
session = requests.session()

url = "https://www.bx33661.com/"
# 后面用法和直接使用requests一样了
json_data = {
    "name":"bx",
    "age":"18"
}

response = session.get(url)  # get请求
response = session.post(url, json=json_data)  # post请求
result = response.json()