var http = require('http模块');
var dt = require('./mymodule')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write("The date and time are currently: " + dt.myDateTime());
    res.end();
}).listen(8080);

console.log("Hello, World!");