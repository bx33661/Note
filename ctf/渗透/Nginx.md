## Nginx

---

```bash
#更新系统软件包
sudo apt update

#安装nginx
sudo apt install nginx -y 
# -y 选项用于自动确认所有提示

#检查安装和版本
nginx -v
# ubuntu@VM-0-9-ubuntu:~$ nginx -v
# nginx version: nginx/1.18.0 (Ubuntu)
```

这里再记录一下`systemctl`命令

> systemctl 是 systemd 系统和服务管理器的主要命令行工具。systemd 是 Linux 系统中用于初始化和管理系统服务的系统和服务管理器。它取代了传统的 SysV init 系统，提供了更高效、更灵活的服务管理功能。
>
> 这里采用nginx为示例

1. **启动 Nginx 服务**
   
   ```bash
   sudo systemctl start nginx
   ```
   
2. **停止 Nginx 服务**
   ```bash
   sudo systemctl stop nginx
   ```

3. **重启 Nginx 服务**
   ```bash
   sudo systemctl restart nginx
   ```

4. **重新加载 Nginx 配置**
   ```bash
   sudo systemctl reload nginx
   ```

5. **启用 Nginx 开机自启动**
   ```bash
   sudo systemctl enable nginx
   ```

6. **禁用 Nginx 开机自启动**
   ```bash
   sudo systemctl disable nginx
   ```

7. **查看 Nginx 服务状态**
   ```bash
   sudo systemctl status nginx
   ```

8. **查看 Nginx 服务日志**
   ```bash
   sudo journalctl -u nginx
   ```

![image-20241126171251293](https://gitee.com/bx33661/image/raw/master/path/image-20241126171251293.png)

可以查看某个服务的情况

- 名称
- 位置
- 状态  ...

`.service`文件是system服务单元

`nginx.service`文件如下：

```bash
[Unit]
Description=A high performance web server and a reverse proxy server
Documentation=man:nginx(8)
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
PIDFile=/run/nginx.pid
ExecStartPre=/usr/sbin/nginx -t -q -g 'daemon on; master_process on;'
ExecStart=/usr/sbin/nginx -g 'daemon on; master_process on;'
ExecReload=/usr/sbin/nginx -g 'daemon on; master_process on;' -s reload
ExecStop=/bin/kill -s TERM $MAINPID

[Install]
WantedBy=multi-user.target

```

- **[Unit] 部分**

描述服务的基本信息和依赖关系。

- **[Service] 部分**

定义服务的行为和属性

- **[Install] 部分**

定义服务的安装行为，主要用于设置开机启动





Nginx常用命令：

```bash
nginx -s stop       快速关闭Nginx，可能不保存相关信息，并迅速终止web服务。
nginx -s quit       平稳关闭Nginx，保存相关信息，有安排的结束web服务。
nginx -s reload     因改变了Nginx相关配置，需要重新加载配置而重载。
nginx -s reopen     重新打开日志文件。
nginx -c filename   为 Nginx 指定一个配置文件，来代替缺省的。
nginx -t            不运行，仅仅测试配置文件。nginx 将检查配置文件的语法的正确性，并尝试打开配置文件中所引用到的文件。
nginx -v            显示 nginx 的版本。
nginx -V            显示 nginx 的版本，编译器版本和配置参数。
```

