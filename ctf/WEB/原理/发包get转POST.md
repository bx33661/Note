一般的发转包软件都有自动的方式

get形式转成post形式需要添加几个参数
```http
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
```


```http
POST /PHPl/CTFSHOW/index.php?a=111 HTTP/1.1

Host: localhost:63342

Upgrade-Insecure-Requests: 1

Content-Type: application/x-www-form-urlencoded

Sec-Fetch-User: ?1

Priority: u=0, i

Sec-Fetch-Site: none

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0

Sec-Fetch-Mode: navigate

Referer: http://localhost:63342/PHPl/CTFSHOW/index.php?a=111

Cookie: Webstorm-d080da3=67762b24-a396-4cc4-b0c7-17c8ca2a353c; Hm_lvt_786a6208323fbecfb41d71bfda8daca6=1703079975,1703237097,1703513068; Phpstorm-1737a8ff=ef76d920-41c2-4b7a-a741-93c6dc7be660; Webstorm-d081163=4e3da769-2515-494a-8a20-2b506957100f; Phpstorm-1737acbf=a0671f11-34f4-4388-937d-49670fbaa240; Phpstorm-1737acc0=94384fa8-0a51-46f9-895f-cca51465c274

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Sec-Fetch-Dest: document

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Encoding: gzip, deflate, br, zstd

Origin: http://localhost:63342

Content-Length: 5

  

v=444
```