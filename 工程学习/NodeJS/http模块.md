### http模块

```javascript
var http = require('http');
http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(req.url);
    res.end();
}).listen(8080);
```

`http.createServer` 函数的回调函数有两个参数：`req` 和 `res`。它们的作用如下：

1. **`req`（请求对象）**：
   - 代表客户端发来的请求。
   - 包含有关请求的信息，如请求方法（GET、POST等）、请求头、请求 URL 等。
   - 你可以通过 `req.url` 获取请求的 URL，或者使用其他属性来获取更多信息。

2. **`res`（响应对象）**：
   - 代表服务器将要发送给客户端的响应。
   - 你可以使用 `res.writeHead()` 设置响应的状态码和头部信息。
   - 使用 `res.write()` 向响应体中写入数据。
   - 使用 `res.end()` 结束响应，告诉服务器已经完成了对该请求的处理。

**示例**

```javascript
http.createServer(function (req, res) {
    console.log(req.method); // 打印请求方法
    console.log(req.url);    // 打印请求的 URL

    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<h1>Hello, World!</h1>'); // 返回 HTML 内容
    res.end();
}).listen(8080);
```

在这个示例中，`req` 用于获取请求的信息，而 `res` 用于构建和发送响应给客户端。