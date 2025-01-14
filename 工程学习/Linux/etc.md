### etc目录

---

"/etc" 目录用于存储系统配置文件。

- /etc/passwd（用户账户信息）
- /etc/shadow（加密的密码信息）
- /etc/fstab（文件系统表）
- /etc/hosts（主机名和IP地址映射）
- /etc/network/（网络配置）



#### /etc/passwd文件

> /etc/passwd 是 Linux 系统中存储用户账户信息的重要文件。它包含了系统中所有用户的基本信息。

所有用户可读，只有root用户可以修改,每行代表一个用户,使用冒号(:)分隔不同字段。格式如下:

```
username:password:UID:GID:comment:home_directory:shell
```

- username: 用户登录名
- password: 通常显示为 'x',实际密码存储在 /etc/shadow 中
- UID: 用户ID,0 通常代表 root 用户
- GID: 用户主组ID
- comment: 用户全名或描述
- home_directory: 用户主目录路径
- shell: 用户登录后使用的 shell

![image-20240917135007763](https://gitee.com/bx33661/image/raw/master/path/image-20240917135007763.png)

获取/etc/passwd可以获取很多信息，比如说知道这个服务器使用了哪些服务，哪些用户，比如说mysql等

```
ftp:x:108:65534::/srv/ftp:/usr/sbin/nologin
mysql:x:109:114:MySQL Server,,,:/nonexistent:/bin/false
```



找到了一篇文章，分享了几个案例：

https://blog.csdn.net/weixin_46356409/article/details/135276965