真实IP是指互联网上某个设备或服务器的实际网络地址，通常用于标识和定位该设备。与真实IP相对的是代理IP或CDN IP（内容分发网络IP），后者可能会隐藏或掩盖真实IP，以提高安全性和性能。

## 真实IP的特点

- **唯一性**：每个真实IP在网络上是唯一的，能够直接与其他设备进行通信。
- **可识别性**：通过真实IP，网络管理员可以追踪设备的地理位置、网络提供商等信息。
- **直接访问**：真实IP允许用户直接访问设备或服务，而不经过中介或代理。

## 真实IP的获取方法

在某些情况下，用户可能需要绕过CDN或其他保护机制来获取目标网站的真实IP。以下是一些常见的方法：

1. **查询历史DNS记录**：通过工具查询域名的历史解析记录，可以找到使用CDN之前的真实IP。
2. **利用子域名**：一些网站可能只对主域名使用CDN，而子域名未使用。通过查询子域名，可以找到其对应的真实IP。
3. **邮件服务器查询**：如果Web和邮件服务器在同一台机器上，可以通过邮件功能（如注册确认邮件）获取真实IP。
4. **使用国外DNS解析**：国内的CDN可能在国外没有覆盖，通过国外DNS解析可能获取到真实IP。
5. **利用漏洞**：某些Web应用漏洞（如XSS、SSRF）可以被利用来获取服务器的真实IP。
6. **Censys等搜索引擎**：通过查询SSL证书等信息，可能找到与目标域名相关的真实IP。

## 结论

了解和获取真实IP对于网络安全、渗透测试和系统管理等领域都非常重要。尽管有多种方法可以尝试获取真实IP，但应确保遵循法律法规，并尊重他人的隐私和安全。

Citations:
[1] https://www.cnblogs.com/zhaoyunxiang/p/17744170.html
[2] https://www.cnblogs.com/qi-yuan/p/14066806.html
[3] https://juejin.cn/post/7259195948772425784
[4] https://xie.infoq.cn/article/1b1d530f772e33b669f6cbedf
[5] https://blog.csdn.net/shadow20112011/article/details/104235905
[6] https://blog.csdn.net/lady_killer9/article/details/135047935
[7] https://www.tencentcloud.com/zh/document/product/627/47817
[8] https://blog.csdn.net/itworld123/article/details/122906262