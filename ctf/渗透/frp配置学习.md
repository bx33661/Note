## frp配置学习

> https://gofrp.org/zh-cn/docs/overview/
>
> https://ukfc.twilightly.top:4333/p/frp%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%E7%AE%80%E5%8D%95%E6%90%AD%E5%BB%BA%E6%95%99%E7%A8%8B/
>
> 

![image-20241130160452535](https://gitee.com/bx33661/image/raw/master/path/image-20241130160452535.png)

主要是两端配置

### 服务端配置

![image-20241130162141635](https://gitee.com/bx33661/image/raw/master/path/image-20241130162141635.png)

下载到服务器先解压

> 之前记录过这个解压命令
>
> https://github.com/bx33661/Note/blob/main/%E5%B7%A5%E7%A8%8B%E5%AD%A6%E4%B9%A0/Linux/%E5%91%BD%E4%BB%A4/%E6%89%93%E5%8C%85%E5%92%8C%E5%8E%8B%E7%BC%A9%E5%91%BD%E4%BB%A4.md

```(空)
tar -zxvf ....
```

![image-20241130163335895](https://gitee.com/bx33661/image/raw/master/path/image-20241130163335895.png)

服务器主要作为这个服务端，我们配置这个frps.toml

```(空)
bindAddr = "0.0.0.0"
bindPort = 7100
kcpBindPort = 7100

webServer.addr = "0.0.0.0"
webServer.port = 7500
webServer.user = "user"
webServer.password = "password"


log.to = "/frpslog/frps.log"
log.level = "info"
log.maxDays = 3

auth.method = "token"
auth.token = "tokentoken"

allowPorts = [
{ start = 6000, end = 7000},
]
```

同时也要去这个安全组去把这个端口开一下

![image-20241130163458828](https://gitee.com/bx33661/image/raw/master/path/image-20241130163458828.png)

```
webServer.user = "user"
webServer.password = "password"
```

这个就是设置web控制台的账密

```(空)
auth.method = "token"
auth.token = "tokentoken"
```

这个就是验证系统，需要两端保持一致才行

设置`systemd`

```(空)
cd /etc/systemd/sysytem

#创建一个服务
vim frps.service

#启动服务
systemtcl start frps.service

#查看状态
systemtcl status frps.service
```

![image-20241130160452535](https://gitee.com/bx33661/image/raw/master/path/image-20241130160452535.png)

> 我之前记录过这个systemtcl 命令
>
> https://github.com/bx33661/Note/blob/main/%E5%B7%A5%E7%A8%8B%E5%AD%A6%E4%B9%A0/Linux/systemctl.md

此时我们访问我们服务器这个7500端口

![image-20241130164111437](https://gitee.com/bx33661/image/raw/master/path/image-20241130164111437.png)

![image-20241130164045650](https://gitee.com/bx33661/image/raw/master/path/image-20241130164045650.png)

这样就差不多了



### 客户端配置

配置这个frpc.toml

```(空)
# 服务器地址
serverAddr = ""

# 服务器端口
serverPort = 7100

# 登录失败时退出
loginFailExit = true

# 日志配置
[log]
to = "./frpc.log"
level = "info"
maxDays = 3

# 认证方法和令牌
[auth]
method = "token"
token = "tokentoken"

# 代理配置
[[proxies]]
name = "test"
type = "http"
localIP = "127.0.0.1"
localPort = 5000
customDomains = ["bx33661.com"]
```

