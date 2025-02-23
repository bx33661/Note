在网络安全领域，**web挖洞打点**是指通过识别和利用Web应用程序中的漏洞来获取系统权限的过程。这一过程通常包括信息收集、漏洞选择、漏洞利用等步骤，目的是为了最终获得目标系统的控制权。

## 打点的主要目标

- **获取权限**：通过利用漏洞获得Web应用程序的访问权限，通常是为了执行恶意代码或获取敏感信息。
- **扩大攻击面**：在成功获取初步权限后，攻击者可能会寻找其他漏洞以进一步渗透系统。

## 常见的漏洞类型

在web打点中，攻击者通常关注以下几种漏洞：

1. **SQL注入**：
   - SQL注入是最常见的攻击方式之一，攻击者通过向数据库发送恶意SQL查询来操控数据库。
   - 利用工具如sqlmap可以自动化检测和利用SQL注入漏洞，从而获取数据库中的敏感信息或执行命令[1]。

2. **文件上传漏洞**：
   - 文件上传漏洞允许攻击者将恶意文件上传到服务器，并通过访问这些文件来执行恶意代码。
   - 这种漏洞通常出现在允许用户上传文件的Web应用程序中，例如头像上传或文档提交功能[1]。

3. **其他漏洞**：
   - 还包括反序列化漏洞、逻辑错误、跨站脚本（XSS）等，这些漏洞虽然不一定直接导致权限获取，但可以作为辅助手段来实现更复杂的攻击[1][3]。

## 信息收集与打点流程

在进行web打点时，信息收集是至关重要的一步。攻击者通常会：

- **识别目标**：通过域名查询、WHOIS信息、DNS记录等方式识别目标网站及其相关资产。
- **探测服务**：使用端口扫描工具探测开放的服务和可能存在的漏洞。
- **收集技术栈信息**：了解目标使用的操作系统、Web服务器、中间件和数据库等，以便选择合适的攻击手段[2][3]。

## 防御措施

为了防止web打点攻击，组织可以采取以下措施：

- **输入验证与过滤**：确保所有用户输入经过严格验证，以防止SQL注入和文件上传漏洞。
- **使用Web应用防火墙（WAF）**：部署WAF可以帮助检测和阻止恶意请求。
- **定期安全审计与渗透测试**：定期对Web应用进行安全审计和渗透测试，以发现并修复潜在的安全漏洞。

总之，web挖洞打点是一种复杂且技术性强的攻击方式，通过对Web应用程序中的各种漏洞进行识别和利用，攻击者能够实现对目标系统的控制。加强防护措施和提高安全意识是抵御此类攻击的有效手段。

Citations:
[1] https://www.cnblogs.com/Xiaoming0/p/13923341.html
[2] https://www.cnblogs.com/gao79135/p/17848142.html
[3] https://www.eet-china.com/mp/a160150.html
[4] https://www.cnblogs.com/piaomiaohongchen/p/17044530.html
[5] https://www.anquanke.com/post/id/289490
[6] https://blog.csdn.net/m0_73803866/article/details/127085799
[7] https://www.sangfor.com.cn/news/633bc9eebc1a463684cc9f2a5dd5a738
[8] https://blog.gm7.org/%E4%B8%AA%E4%BA%BA%E7%9F%A5%E8%AF%86%E5%BA%93/01.%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/08.%E6%94%BB%E9%98%B2%E6%BC%94%E7%BB%83/01.%E6%89%93%E7%82%B9%E6%80%9D%E8%B7%AF.html