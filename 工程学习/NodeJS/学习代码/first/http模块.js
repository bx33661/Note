// 引入http模块
var http = require('http');

// 创建一个服务器
http.createServer(function (req, res) {
    //添加 HTTP 标头, HTTP 状态值: 200: OK
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World\n');
}).listen(1337, '127.0.0.1');// 监听端口