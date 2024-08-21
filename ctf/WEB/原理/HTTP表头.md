# HTTP表头



## Referer

在HTTP（超文本传输协议）中，`Referer`（注意：这是一个历史拼写错误，正确的英文单词应该是 “referrer”，但由于广泛使用，这个拼写错误被保留了下来）是一个请求头字段，它包含了当前请求页面的来源页面的地址。换句话说，当用户点击一个链接或者提交一个表单从一个网页跳转到另一个网页时，浏览器通常会在HTTP请求中包含一个`Referer`头部，这个头部会告诉服务器用户是从哪个页面发起的这次请求。

以下是一个HTTP请求头的例子，其中包含了`Referer`字段：

```http
GET /page.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Referer: http://www.previouspage.com/index.html
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
```

在这个例子中，`Referer`字段告诉`www.example.com`服务器，用户的请求是从`http://www.previouspage.com/index.html`页面发起的。

`Referer`头部有几个用途：

1. **追踪流量来源**：网站管理员可以通过分析`Referer`头部来了解用户是如何到达他们网站的，这对于SEO（搜索引擎优化）和营销活动分析非常有用。
2. **防止盗链**：服务器可以使用`Referer`头部来决定是否允许资源（如图片或视频）的请求。如果请求不是从允许的域名发起的，服务器可以拒绝这个请求。
3. **增强安全性**：某些网站使用`Referer`头部作为CSRF（跨站请求伪造）攻击的防御机制，通过检查请求的来源是否是预期的来源。
4. **个性化内容**：网站可以根据用户来自的页面定制响应内容。

需要注意的是，出于隐私考虑，用户可以通过浏览器设置或者使用插件来控制是否发送`Referer`头部，而且某些敏感信息的URL可能不会完整地包含在`Referer`头部中。