>RBASH 是 Restricted Bash 的缩写，中文译为“受限的 Bash”。它实际上是 Bash Shell 的一个受限版本，通过限制某些操作和功能来增强安全性。管理员可以通过配置用户的登录 Shell 为 RBASH，从而限制该用户在系统上的操作权限。

RBASH的限制一般是：
- **目录切换：** 禁止使用 `cd` 命令更改当前工作目录。
- **环境变量修改：** 禁止设置或取消设置 `SHELL`、`PATH`、`ENV` 或 `BASH_ENV` 等环境变量的值。这意味着用户无法轻易修改命令搜索路径或 Shell 的行为。
- **命令执行：** 命令名称中不能包含斜杠 `/`，这有效地阻止了用户执行任意路径下的命令。例如，用户不能直接执行 `/bin/ls`，而只能执行在受限环境中允许的命令。
- **输出重定向：** 在某些情况下，RBASH 可能会限制输出重定向，例如使用 `>` 或 `>>` 将命令输出重定向到文件。
- **内置命令参数：** 限制将包含斜杠的文件名指定为内置命令的参数，例如 `hash` 命令的 `-p` 选项。

## 设置RBASH
我这里学习一下如何设置RBASH：
先看一下自己环境有没有bash，并且创建一个测试账号
![image.png](https://gitee.com/bx33661/image/raw/master/path/20250113121049.png)
然后设置账户基本信息
![image.png](https://gitee.com/bx33661/image/raw/master/path/20250113121257.png)
最后设置这个用户的bash为rbash
```bash
sudo usermod -s /bin/rbash linuxdemo
```
![image.png](https://gitee.com/bx33661/image/raw/master/path/20250113121513.png)
```bash
sudo mkdir /home/linuxdemo/bin
```

登录到linuxdemo这个账号
可以测试一些命令，发现无法执行
![image.png](https://gitee.com/bx33661/image/raw/master/path/20250113122302.png)
