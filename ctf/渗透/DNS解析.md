# DNS解析



> @Author:bx33661
>
> @参考：
>
> [DNS记录类型 | 小菜学网络 (fasionchan.com)](https://fasionchan.com/network/dns/record-types/)

### dig命令

> `dig`（Domain Information Groper）是一个常用的命令行工具，用于查询DNS（域名系统）记录

```bash
dig [@server] [域名] [查询类型] [选项]
```

示例：
```bash
#查询A记录
dig example.com
#查询CNAME记录
dig example.com CNAME
#指定DNS服务器
dig @8.8.8.8 example.com
```

`dig` 输出通常分为几个部分：

1. **Header**：显示查询的基本信息，如查询时间、DNS服务器等。
2. **QUESTION SECTION**：显示你查询的域名和记录类型。
3. **ANSWER SECTION**：显示查询的结果，如返回的IP地址或其他记录。
4. **AUTHORITY SECTION**：显示提供该记录的DNS服务器。
5. **ADDITIONAL SECTION**：可能包含与查询相关的其他信息，如额外的DNS服务器或IP地址

![image-20241129182051540](https://gitee.com/bx33661/image/raw/master/path/image-20241129182051540.png)

![image-20241129182153952](https://gitee.com/bx33661/image/raw/master/path/image-20241129182153952.png)



## 解析类型

示例---腾讯云中常见解析

![image-20241129193116052](https://gitee.com/bx33661/image/raw/master/path/image-20241129193116052.png)

### CNAME记录

**CNAME记录**（Canonical Name Record），用于将一个域名别名指向另一个域名的“规范”名称。

简单来说，CNAME记录就是给其他一个域名起一个别名，所有对该别名的DNS查询都会被重定向到目标域名，从而解析出相应的IP地址。

**基本原理**

当你查询一个CNAME记录时，DNS解析器会执行以下步骤：

1. **查询CNAME记录**：查询目标域名（例如，`www.bx33661.com`）的CNAME记录。
2. **重定向**：如果CNAME记录指向另一个域名（例如，`bx33661.com`），DNS解析器会再次查询该目标域名的A记录（或其他类型的记录），直到最终得到IP地址。
3. **返回最终的IP地址**

![image-20241129193846640](https://gitee.com/bx33661/image/raw/master/path/image-20241129193846640.png)

我们访问这个http://dx.bx33661.com/

成功

### **MX记录**

（Mail Exchange Record，邮件交换记录）是DNS（域名系统）中的一种记录类型，指示邮件服务器用于接收电子邮件的服务器地址。当发送电子邮件时，发送方的邮件服务器通过查询目标域名的MX记录来找出接收邮件的邮件服务器（即邮件主机）。



> GPT:(查了一下这个TTL参数)
> **TTL**（Time To Live）是DNS记录中的一个重要字段，表示该记录在DNS缓存中的存活时间，单位是秒。它控制DNS解析器和其他DNS服务器缓存该记录的时间长度。在TTL到期后，DNS记录会被认为是过时的，需要重新查询原始的DNS服务器以获取最新的记录。
>
> ### TTL的作用
>
> 1. **缓存管理**：TTL决定了DNS记录在缓存中的有效期。在TTL过期后，DNS解析器必须重新向DNS服务器请求更新的记录。TTL的目的是减少DNS查询的次数，从而提高查询效率，降低网络负载。
> 2. **减少DNS查询负担**：通过设置合理的TTL，DNS服务器可以减少因频繁查询导致的负担。多个查询可以在TTL有效期内使用缓存的结果，而不需要每次都向权威DNS服务器发起请求。
> 3. **灵活的更新策略**：TTL值的设置可以影响DNS记录更新的频率。TTL值较低时（例如几秒到几分钟），当DNS记录变化时，变化会较快传播；而TTL值较高时，缓存时间较长，记录更新需要更长的时间才能在全网生效。
>
> ### TTL的工作原理
>
> 1. **DNS查询和缓存**：当DNS解析器（如浏览器或本地DNS服务器）发起查询时，它会首先检查是否有该记录的缓存。如果缓存未过期，解析器会直接返回缓存的结果。如果缓存已过期或没有缓存，解析器会向权威DNS服务器发送查询请求，并将获得的DNS记录缓存一定时间，直到TTL过期。
> 2. **缓存时间**：每个DNS记录都有一个TTL值，表示该记录被缓存的最长时间。例如，如果TTL为3600秒（即1小时），DNS服务器会缓存该记录1小时。超过这个时间，记录就会过期，解析器需要再次查询DNS服务器。
>
> ### 示例
>
> 假设你查询 `example.com` 的A记录，得到以下结果：
>
> ```
> example.com.        3600    IN      A       93.184.216.34
> ```
>
> 这里的 `3600` 表示TTL为3600秒，即1小时。这意味着在接下来的1小时内，任何查询 `example.com` 的DNS解析器都会缓存这个IP地址，直到1小时过后，缓存会过期，必须重新查询。



### TXT记录

这个我的使用来看，就是存一些信息，主要用于验证

站长站用的多