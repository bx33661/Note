## express 和 pm2

---

### express

> Express 是一个基于 Node.js 的快速、非侵入式、极简的 Web 应用程序框架。它提供了一组强大的功能，用于构建各种类型的 Web 应用程序和 API。Express 是 Node.js 生态系统中最流行的 Web 框架之一，广泛用于构建服务器端应用程序。

由介绍可以知道，express就是一个web框架

```bash
#安装
npm install express
#检查是否安装成功
npm list express
```

测试,创建一个ex.js文件

```javascript
// 引入express框架
const express = require('express');
// 创建网站服务器
const app = express();

app.get('/' , (req, res) => {
    // send()
    // 1. send方法内部会检测响应内容的类型
    // 2. send方法会自动设置http状态码
    // 3. send方法会帮我们自动设置响应的内容类型及编码
    res.send('Hello. Express');
})

app.get('/list', (req, res) => {
    res.send({name: '张三', age: 20})
})

// 监听端口
app.listen(3000);
console.log('网站服务器启动成功');
```

启动服务，正常启动

```bash
node ex.js
#访问http://localhost:3000/
```



### 使用pm2

> `pm2` 是一个用于 Node.js 应用程序的生产进程管理器，它可以帮助你管理和监控你的应用程序。`pm2` 提供了许多有用的功能，如自动重启、负载均衡、日志管理、监控等，使得在生产环境中运行 Node.js 应用程序变得更加简单和可靠。

```
pm2 start ex.js
```

回显如下：

```
                        -------------

__/\\\\\\\\\\\\\____/\\\\____________/\\\\____/\\\\\\\\\_____
 _\/\\\/////////\\\_\/\\\\\\________/\\\\\\__/\\\///////\\\___
  _\/\\\_______\/\\\_\/\\\//\\\____/\\\//\\\_\///______\//\\\__
   _\/\\\\\\\\\\\\\/__\/\\\\///\\\/\\\/_\/\\\___________/\\\/___
    _\/\\\/////////____\/\\\__\///\\\/___\/\\\________/\\\//_____
     _\/\\\_____________\/\\\____\///_____\/\\\_____/\\\//________
      _\/\\\_____________\/\\\_____________\/\\\___/\\\/___________
       _\/\\\_____________\/\\\_____________\/\\\__/\\\\\\\\\\\\\\\_
        _\///______________\///______________\///__\///////////////__


                          Runtime Edition

        PM2 is a Production Process Manager for Node.js applications
                     with a built-in Load Balancer.

                Start and Daemonize any application:
                $ pm2 start app.js

                Load Balance 4 instances of api.js:
                $ pm2 start api.js -i 4

                Monitor in production:
                $ pm2 monitor

                Make pm2 auto-boot at server restart:
                $ pm2 startup

                To go further checkout:
                http://pm2.io/


                        -------------

[PM2] Spawning PM2 daemon with pm2_home=C:\Users\lenovo\.pm2
[PM2] PM2 Successfully daemonized
[PM2] Starting E:\gitproject\nodejs\express初体验\ex.js in fork_mode (1 instance)
[PM2] Done.
```

![image-20240921233338755](https://gitee.com/bx33661/image/raw/master/path/image-20240921233338755.png)

#### 查看日志

```bash
pm2 log
```

```shell
PS E:\gitproject\nodejs\express初体验> pm2 logs
[TAILING] Tailing last 15 lines for [all] processes (change the value with --lines option)
C:\Users\lenovo\.pm2\pm2.log last 15 lines:
PM2        | 2024-09-21T23:31:57: PM2 log: PM2 version          : 5.4.2
PM2        | 2024-09-21T23:31:57: PM2 log: Node.js version      : 20.11.1
PM2        | 2024-09-21T23:31:57: PM2 log: Current arch         : x64
PM2        | 2024-09-21T23:31:57: PM2 log: PM2 home             : C:\Users\lenovo\.pm2
PM2        | 2024-09-21T23:31:57: PM2 log: PM2 PID file         : C:\Users\lenovo\.pm2\pm2.pid
PM2        | 2024-09-21T23:31:57: PM2 log: RPC socket file      : \\.\pipe\rpc.sock
PM2        | 2024-09-21T23:31:57: PM2 log: BUS socket file      : \\.\pipe\pub.sock
PM2        | 2024-09-21T23:31:57: PM2 log: Application log path : C:\Users\lenovo\.pm2\logs
PM2        | 2024-09-21T23:31:57: PM2 log: Worker Interval      : 30000
PM2        | 2024-09-21T23:31:57: PM2 log: Process dump file    : C:\Users\lenovo\.pm2\dump.pm2
PM2        | 2024-09-21T23:31:57: PM2 log: Concurrent actions   : 2
PM2        | 2024-09-21T23:31:57: PM2 log: SIGTERM timeout      : 1600
PM2        | 2024-09-21T23:31:57: PM2 log: ===============================================================================
PM2        | 2024-09-21T23:31:57: PM2 log: App [ex:0] starting in -fork mode-
PM2        | 2024-09-21T23:31:57: PM2 log: App [ex:0] online

C:\Users\lenovo\.pm2\logs\ex-error.log last 15 lines:
C:\Users\lenovo\.pm2\logs\ex-out.log last 15 lines:
0|ex       | 网站服务器启动成功
```

#### 监控

```
pm2 monit
```

![image-20240921234253592](https://gitee.com/bx33661/image/raw/master/path/image-20240921234253592.png)

#### 查看程序状态

```
pm2 list
```

#### 停止服务

```
pm2 stop ex.js
```

![image-20240921235929000](https://gitee.com/bx33661/image/raw/master/path/image-20240921235929000.png)