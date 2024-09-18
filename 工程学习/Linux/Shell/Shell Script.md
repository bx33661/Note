# Shell Script

---

> 参考：
>
> - https://blog.csdn.net/w918589859/article/details/108752592
> - https://github.com/qinjx/30min_guides/blob/master/shell.md
> - https://github.com/huyubing/books-pdf/blob/master/Shell%E8%84%9A%E6%9C%AC%E5%AD%A6%E4%B9%A0%E6%8C%87%E5%8D%97.pdf

开始第一个例子，先创建一个文件夹📂开始学习

```bash
root@cloud:~# mkdir shlearn
root@cloud:~# cd shlearn
root@cloud:~/shlearn# vim test.sh

root@cloud:~/shlearn# test.sh
test.sh: command not found

root@cloud:~/shlearn# ls
test.sh

root@cloud:~/shlearn# ./test.sh
-bash: ./test.sh: Permission denied

root@cloud:~/shlearn# chmod +x test.sh
root@cloud:~/shlearn# ./test.sh
hello world
```

这里有一点需要注意的是跟Windows-cmd一样：

注意，一定要写成./test.sh，而不是test.sh，运行其它二进制的程序也一样，直接写test.sh，linux系统会去`PATH`里寻找有没有名称为test.sh的，

而只有Python，/bin, /sbin, /usr/bin，/usr/sbin等在PATH里，你的当前目录通常不在PATH里，所以写成test.sh是会找不到命令的，就会提示`test.sh: command not found`

要用./test.sh告诉系统说，就执行当前目录下的`./test.sh`

```bash
#另一种执行方式：
bash test.sh
```



## 基本语法

### 变量

```bash
root@cloud:~/shlearn# bx = 3366
bx: command not found
root@cloud:~/shlearn# $bx=3366
=3366: command not found
root@cloud:~/shlearn# $ bx=3366
$: command not found

#正确方式
root@cloud:~/shlearn# bx=3366
root@cloud:~/shlearn# echo bx
bx
```

> 单引号和双引号：
>
> ```bash
> root@cloud:~# name=bx
> root@cloud:~# echo '$name'
> $name
> root@cloud:~# echo "$name"
> bx
> ```
>
> **双引号能够识别变量，双引号能够实现转义**

#### 变量删除

```
unset 变量名
```



> 可以利用以下两个命令去查看变量`set`  `env`
>
> **set命令可以查看所有变量，而env命令只能查看环境变量。**

```bash
#!/bin/bash
$name=bx
$age=18
$num=17
echo "hello world"
echo "shell脚本本身的名字: $0"
echo "传给shell的第一个参数: $1"
echo "传给shell的第二个参数: $2"
echo "所有：$@"
echo "个数：$#"
```

```
root@cloud:~/shlearn# ./test.sh 1 2 3 4
./test.sh: line 2: =bx: command not found
./test.sh: line 3: =18: command not found
./test.sh: line 4: =17: command not found
hello world
shell脚本本身的名字: ./test.sh
传给shell的第一个参数: 1
传给shell的第二个参数: 2
所有：1 2 3 4
个数：4
```

几个参数，例子：

```shell
#!/bin/bash
for i in "$*"
do
    echo "The parameters is: $i"
done

x=1
for y in "$@"
do
    echo "The parameter$x is: $y"
    x=$((x + 1))
done

```

```bash
 ~  vim demo2.sh                                           
 ~  bash demo2.sh 1 2 5 9 3 4                      
The parameters is: 1 2 5 9 3 4
The parameter1 is: 1
The parameter2 is: 2
The parameter3 is: 5
The parameter4 is: 9
The parameter5 is: 3
The parameter6 is: 4
```



*预定义参数：*

| $?   | 最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行;如果这个变量的值为非О(具体是哪个数，由命令自己来决定），则证明上一个命令执行不正确了。 |
| ---- | ------------------------------------------------------------ |
| $$   | 当前进程的进程号（PID)                                       |
| $!   | 后台运行的最后一个进程的进程号(PID)                          |







**反引号：**（``）

执行命令 （`$()`也可以）

```bash
root@cloud:~# echo ls
ls
root@cloud:~# echo `ls`
shlearn snap
root@cloud:~# echo $(ls)
shlearn snap
```



### 注释
- 单行注释 `#`
- 多行注释 `#`
没有专门的语句，只能一行一行的添加