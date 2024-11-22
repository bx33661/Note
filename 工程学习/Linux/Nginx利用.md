Nginx的文件信息：

| 类别             | 路径                                      |
| ---------------- | ----------------------------------------- |
| 配置文件         | `/usr/local/nginx/conf/nginx.conf`        |
| 配置文件存放目录 | `/etc/nginx`                              |
| 主配置文件       | `/etc/nginx/conf/nginx.conf`              |
| 管理脚本         | `/usr/lib64/systemd/system/nginx.service` |
| 模块             | `/usr/lib64/nginx/modules`                |
| 应用程序         | `/usr/sbin/nginx`                         |
| 程序默认存放位置 | `/usr/share/nginx/html`                   |
| 日志默认存放位置 | `/var/log/nginx`                          |



`nginx.conf(/etc/nginx)`

配置文件采用模块化设计，主要包括全局配置、事件模块配置、HTTP 模块配置和邮件模块配置等

内容如下

```nginx
# 指定 NGINX 运行的用户
user  nginx;

# 设置工作进程的数量，auto 表示自动检测 CPU 核心数
worker_processes  auto;

# 定义错误日志文件的位置和日志级别
error_log  /var/log/nginx/error.log notice;

# 定义 PID 文件的位置
pid        /var/run/nginx.pid;

# 事件模块配置
events {
    # 每个工作进程的最大连接数
    worker_connections  1024;
}

# HTTP 模块配置
http {
    # 包含 MIME 类型定义文件
    include       /etc/nginx/mime.types;

    # 设置默认的 MIME 类型
    default_type  application/octet-stream;

    # 定义日志格式
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    # 定义访问日志文件的位置和使用的日志格式
    access_log  /var/log/nginx/access.log  main;
```

更多详细内容看：https://www.cnblogs.com/54chensongxia/p/12938929.html