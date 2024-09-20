### HTTP是什么

----

```http
POST /?basectf=we1c%2500me HTTP/1.1
Host: gz.imxbt.cn:20050
Cache-Control: max-age=0
Origin: http://gz.imxbt.cn:20050
x-forwarded-for: 127.0.0.1
Upgrade-Insecure-Requests: 1
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Accept-Encoding: gzip, deflate
Cookie: c00k13=i can't eat it
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: Base
Content-Type: application/x-www-form-urlencoded
User-Agent: Base
Content-Length: 11

Base=fl%40g
```

根据提示，最后有一个302跳转

得到base64数据解码即可