

### 知识

makefile里面可以用$(shell {cmd})执行命令





```(空)
PATH 环境变量被显式地设定为空。这段 Makefile 的逻辑检查了 PATH 是否未定义，如果未定义则设为空，如果已定义也重设为空。由于 PATH 被设置为空，shell 将无法定位到除内置命令之外的任何外部命令的位置。

Bash 内建命令

这些命令是由Bash自身提供，而不是独立的程序：

alias - 定义或显示别名。
cd - 改变当前目录。
echo - 输出参数到标准输出。
exit - 退出当前shell。
export - 设置或显示环境变量。
history - 显示命令历史记录。
pwd - 打印当前工作目录的路径。
read - 从标准输入读取一行数据。
set - 设置或取消设置shell选项和位置参数。
type - 显示一个命令的类型。
unset - 删除变量或函数的定义。
```



### 题目

#### EzMake

```(空)
$(shell ls)
```

![image-20250117123719520](https://gitee.com/bx33661/image/raw/master/path/image-20250117123719520.png)

```(空)
$(shell cat flag)
```

