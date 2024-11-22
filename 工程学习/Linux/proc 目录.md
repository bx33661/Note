### /proc 目录

> 网上介绍：
>
> 在Linux系统中，`/proc`目录是一个虚拟文件系统，它提供了内核和进程的运行时信息。这个目录中的文件和子目录不是存储在磁盘上的实际文件，而是由内核动态生成的

![image-20240915144147544](https://gitee.com/bx33661/image/raw/master/path/image-20240915144147544.png)

```bash
cat cpuinfo
```

![image-20240915144629556](https://gitee.com/bx33661/image/raw/master/path/image-20240915144629556.png)

给出了很多信息

很多的以数字直接命名的文件夹，查看一个`1`

![image-20240915144712987](https://gitee.com/bx33661/image/raw/master/path/image-20240915144712987.png)

> 查了一下：
>
> /proc 目录中包含许多以数字命名的子目录，这些数字表示系统当前正在运行进程的进程号(PID)，里面包含对应进程相关的多个信息文件：



/proc 蕴含很多有用信息

- cmdline

启动该进程的命令行

![image-20240915145141458](https://gitee.com/bx33661/image/raw/master/path/image-20240915145141458.png)

- cwd

指向该进程的当前工作目录的符号链接

![image-20240915145229748](https://gitee.com/bx33661/image/raw/master/path/image-20240915145229748.png)

- environ

该进程的环境变量

![image-20240915145345482](https://gitee.com/bx33661/image/raw/master/path/image-20240915145345482.png)