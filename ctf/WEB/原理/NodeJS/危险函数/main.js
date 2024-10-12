var express = require("express");
var app = express();

app.get('/eval',function(req,res){
    res.send(eval(req.query.q));
    console.log(req.query.q);
})

var server = app.listen(8888, function() {
    console.log("应用实例，访问地址为 http://127.0.0.1:8888/");
})