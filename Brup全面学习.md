### Brupsuite工作原理
初始模式：本机127.0.0.1上开启了一个浏览器，浏览器访问某个网页时，会从一个随机端口发送流量出去。  
使用Burpsuite之后：本机127.0.0.1上开启了一个浏览器，在127.0.0.1:8083端口作为浏览器的代理。所有从本机浏览器上面发出的流量包都会经过代理（127.0.0.1:8083），所有回向本机浏览器的流量包也会经过代理（127.0.0.1:8083）。Burpsuite Listener则和代理（127.0.0.1:8083）是一个串联模式，Burpsuite Listener可以拦截所有通过代理的网络流量，主要是拦截HTTP和HTTPS协议的流量。通过拦截，Burpsuite可以以中间人的身份对客户端的请求数据、服务端的返回数据做各种的修改。

*一般情况下我们是不能获取明文可读的HTTPS包的，但是通过Brup这个中间人我们可以去抓取brup这个包*



### 抓包杂项过滤
1. 利用ProxyOmage或者火狐proxy过滤
简单的添加了几个比较常见的
```
*.firefox.com
*.firfox.com.cn
*.firefoxchina.cn
*.google.com
*.mozilla.org
*.bitwarden.com
*.qq.com
*.bing.com
*.baidu.com
*.github.com
*.cnblogs.com
*.csdn.net
*.gitee.com
```


HTTPS的证书信息直接通过浏览器查看
![image.png](https://gitee.com/bx33661/image/raw/master/path/20250106212301.png)

