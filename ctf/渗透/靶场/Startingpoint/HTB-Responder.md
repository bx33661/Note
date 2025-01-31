# HTB-Responder

---

> 可以ping通说明环境连接正常

```bash
┌──(bx㉿kali)-[~]
└─$ nmap -sV -sC 10.129.95.234
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-01-25 14:55 CST
Nmap scan report for 10.129.95.234
Host is up (0.38s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.52 ((Win64) OpenSSL/1.1.1m PHP/8.1.1)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_http-server-header: Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.72 seconds
```

### 1. 使用 IP 地址访问 Web 服务时，我们被重定向到的域名是什么？

访问一下，被重定向到unika.htb

### 2.服务器上使用哪种脚本语言生成网页？

PHP

### 3. 用于加载网页不同语言版本的 URL 参数名称是什么？

page

![image-20250125152407049](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20250125152407049.png)

###  4.以下哪个`page`参数值是利用本地文件包含（LFI）漏洞的示例："french.html"、"//10.10.14.6/somefile"、"../../../../../../../../windows/system32/drivers/etc/hosts"、"minikatz.exe"

../../../../../../../../windows/system32/drivers/etc/hosts

### 5.以下哪个`page`参数值是利用远程文件包含（RFI）漏洞的示例："french.html"、"//10.10.14.6/somefile"、"../../../../../../../../windows/system32/drivers/etc/hosts"、"minikatz.exe"



6.

New Technology LAN Manager