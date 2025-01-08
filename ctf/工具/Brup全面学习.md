# BP补充学习

> Brupsuite官网：https://portswigger.net/burp

[TOC]

### Brupsuite工作原理

初始模式：本机127.0.0.1上开启了一个浏览器，浏览器访问某个网页时，会从一个随机端口发送流量出去。  
使用Burpsuite之后：本机127.0.0.1上开启了一个浏览器，在127.0.0.1:8083端口作为浏览器的代理。所有从本机浏览器上面发出的流量包都会经过代理（127.0.0.1:8083），所有回向本机浏览器的流量包也会经过代理（127.0.0.1:8083）。Burpsuite Listener则和代理（127.0.0.1:8083）是一个串联模式，Burpsuite Listener可以拦截所有通过代理的网络流量，主要是拦截HTTP和HTTPS协议的流量。通过拦截，Burpsuite可以以中间人的身份对客户端的请求数据、服务端的返回数据做各种的修改。

*一般情况下我们是不能获取明文可读的HTTPS包的，但是通过Brup这个中间人我们可以去抓取brup这个包*



## 技巧

- Bp中一些路径配置需要使用全英路径

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



### 快捷修改请求方式

GET和POST请求快速切换

![image-20250108114941499](https://gitee.com/bx33661/image/raw/master/path/image-20250108114941499.png)



### 全局搜索(search)

可以查找bp中所有东西

![image-20250108122101484](https://gitee.com/bx33661/image/raw/master/path/image-20250108122101484.png)



## 模块介绍

### Target模块

- Site map

这站点地图，开启漏扫之后可以，自动爬取站点地图

可以大致看到网站结构

![image-20250108112025622](https://gitee.com/bx33661/image/raw/master/path/image-20250108112025622.png)

- Issue definitions

这里面就是漏洞仓库，提供bp被动扫描

![image-20250108111804368](https://gitee.com/bx33661/image/raw/master/path/image-20250108111804368.png)

- Scope

算一个过滤功能

上面是添加希望看到的

下面是希望移除的

![image-20250108114217786](https://gitee.com/bx33661/image/raw/master/path/image-20250108114217786.png)







### 利用bp漏洞扫描

> 只是作为了解bp，展示一下这个功能，但是实际使用不多
>
> bp扫描的能力不是很强
>
> 采用测试站：http://testphp.vulnweb.com/

在dashboard界面内新建一个扫描目标

![image-20250108112905934](https://gitee.com/bx33661/image/raw/master/path/image-20250108112905934.png)

填写扫描目标

![image-20250108112953778](https://gitee.com/bx33661/image/raw/master/path/image-20250108112953778.png)

选择扫描方式，爬虫深度

一共四种选项，每一个时间不同，深度不同

![image-20250108113021301](https://gitee.com/bx33661/image/raw/master/path/image-20250108113021301.png)



具体结果在仪表盘

![image-20250108113216181](https://gitee.com/bx33661/image/raw/master/path/image-20250108113216181.png)

然后呢在Target模块的sitemap下的Crawl...

原本没有东西，但是我们主动扫描之后会发现，给出存在问题以及具体情况和url

![image-20250108113442963](https://gitee.com/bx33661/image/raw/master/path/image-20250108113442963.png)



### collaborator模块

BP的外带模块

![image-20250108115412723](https://gitee.com/bx33661/image/raw/master/path/image-20250108115412723.png)

如果使用可以先进行一个`run health check`

去检查一下功能是否

![image-20250108115513416](https://gitee.com/bx33661/image/raw/master/path/image-20250108115513416.png)

查看是否正常

![image-20250108115802992](https://gitee.com/bx33661/image/raw/master/path/image-20250108115802992.png)

```(空)
utr96icgoeo2w5da3lvzprhs8jea20qp.oastify.com
```

我们就可以获得一个DNSlog

我们尝试访问一下

![image-20250108120034690](https://gitee.com/bx33661/image/raw/master/path/image-20250108120034690.png)

回到模块界面

![image-20250108120019006](https://gitee.com/bx33661/image/raw/master/path/image-20250108120019006.png)



### Decoder模块

编解码模块，可以使用常用的编码和解码

![image-20250108121454375](https://gitee.com/bx33661/image/raw/master/path/image-20250108121454375.png)



### Comparer模块

![image-20250108120951676](https://gitee.com/bx33661/image/raw/master/path/image-20250108120951676.png)

- Words对比

![image-20250108121024594](https://gitee.com/bx33661/image/raw/master/path/image-20250108121024594.png)

- Bytes对比

![image-20250108121034632](https://gitee.com/bx33661/image/raw/master/path/image-20250108121034632.png)



### Organizer模块

主要记录，比如说发现了什么，最后才需要记录统计，防止忘记先发到这个模块做一个记录

在Notes中可以写一些东西什么的

![image-20250108121643446](https://gitee.com/bx33661/image/raw/master/path/image-20250108121643446.png)



## 问题解决

#### Bp光标不对

需要修改一个合适默认的字体

![image-20250108120432707](https://gitee.com/bx33661/image/raw/master/path/image-20250108120432707.png)
