# Redis

---

## 踩坑

> 本地连接远程服务器redis的话

首先确保服务器防火墙放行端口6379

修改`/etc/redis`目录下的`redis.conf`

1. 注释掉bind 127.0.0.1

![image-20241207143855050](https://gitee.com/bx33661/image/raw/master/path/image-20241207143855050.png)

2. 修改 protected-mode yes 为 protected-mode no

```bash
root@VM-0-9-ubuntu:/etc/redis# sudo systemctl restart redis
root@VM-0-9-ubuntu:/etc/redis# sudo systemctl status redis
```

