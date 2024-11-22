### 文件描述符

| 文件描述符 | 用途     | stdio 流 |
| :--------- | :------- | :------- |
| 0          | 标准输入 | stdin    |
| 1          | 标准输出 | stdout   |
| 2          | 标准错误 | stderr   |

1. **文件描述符的类型**：
   - **标准输入（Standard Input）**：文件描述符 0，通常用于从用户或程序读取输入。
   - **标准输出（Standard Output）**：文件描述符 1，通常用于输出信息到终端或文件。
   - **标准错误（Standard Error）**：文件描述符 2，通常用于输出错误信息到终端或文件。
   - **其他文件和资源**：文件描述符 3 及以上的数字表示其他打开的文件或 I/O 资源。
2. **文件描述符的属性**：
   - **非负整数**：文件描述符是一个非负整数，通常从 0 开始。
   - **唯一性**：在每个进程中，文件描述符是唯一的，用于标识不同的文件或资源。
   - **资源限制**：每个进程可以打开的文件描述符数量是有限的，可以通过 `ulimit` 命令查看和设置。



### 进程管理

`top`

![image-20241023115717887](https://gitee.com/bx33661/image/raw/master/path/image-20241023115717887.png)



### 环境变量

```bash
#输出环境变量
env
#输出单个环境变量
ehco $PATH
```

![image-20241023221914577](https://gitee.com/bx33661/image/raw/master/path/image-20241023221914577.png)



```bash
set
```

打印出所有本地定义的 shell 变量

![image-20241023222103846](https://gitee.com/bx33661/image/raw/master/path/image-20241023222103846.png)





### procfs文件系统

#### /proc/cmdline

> cmdline 文件存储着启动当前进程的完整命令，但僵尸进程目录中的此文件不包含任何信息

例子：

我们尝试观察Python3.10的cmdline，先获取到了进程号------548

```bash
cat /proc/548/cmdline
```

![image-20241023224019736](https://gitee.com/bx33661/image/raw/master/path/image-20241023224019736.png)

```bash
#格式化输出
cat /proc/548/cmdline | tr '\0' '\n'
```

结果如下：

```bash
python3
/snap/ubuntu-desktop-installer/1286/usr/bin/cloud-init
status
--wait
```

> 问了一下这个命令具体内容：
>
> 1. `python3`
>
> - **解释**: 这是 Python 3 解释器的命令。它用于运行 Python 脚本或模块。
>
> 2. `/snap/ubuntu-desktop-installer/1286/usr/bin/cloud-init`
>
> - **解释**: 这是 `cloud-init` 工具的完整路径。`/snap/ubuntu-desktop-installer/1286` 表示这个 `cloud-init` 工具位于 `ubuntu-desktop-installer` 的 Snap 包版本 1286 中。
>
> 3. `status`
>
> - **解释**: 这是 `cloud-init` 的子命令，用于检查 `cloud-init` 的当前状态。`cloud-init` 是一个用于初始化云实例的工具，它在实例启动时执行一系列配置任务。
>
> 4. `--wait`
>
> - **解释**: 这是一个命令行选项，指示 `cloud-init` 命令在返回状态之前等待 `cloud-init` 处理完成。这意味着命令会阻塞，直到 `cloud-init` 完成所有配置任务。



#### self

但是在解决问题的时候我们不能获得进程号，这时候可以使用`self`

`/proc/self` 表示当前进程目录。

前面通过 `/proc/$pid/` 来获取指定进程的信息。如果我们只关心当前进程的话，就可以不需要获得pid

```bash
ls /proc/self
```

![image-20241023224550050](https://gitee.com/bx33661/image/raw/master/path/image-20241023224550050.png)



我们接着继续了解我们可以获得信息的几个文件

----->



#### cwd

`cwd` 是 "current working directory" 的缩写，表示当前工作目录。在进程上下文中，`cwd` 指的是进程启动时所在的目录。你可以通过查看 `/proc/<pid>/cwd` 链接来确定某个进程的当前工作目录。

```bash
cat /proc/self/cwd
```

![image-20241023224931510](https://gitee.com/bx33661/image/raw/master/path/image-20241023224931510.png)



#### environ

`environ` 是一个环境变量列表，通常用于表示进程启动时的环境变量。在 Unix 和类 Unix 系统（如 Linux）中，每个进程都有一个环境变量列表，这些环境变量可以在进程中被访问和修改。

```bash
cat /proc/self/environ  
```

![image-20241023225135925](https://gitee.com/bx33661/image/raw/master/path/image-20241023225135925.png)

```bash
#格式化一下
cat /proc/self/environ | tr '\0' '\n'
```

![image-20241023225254044](https://gitee.com/bx33661/image/raw/master/path/image-20241023225254044.png)

有时候一些密钥甚至flag就在环境变量里面



#### fd

> `fd` 是文件描述符（File Descriptor）的缩写，它是操作系统用于表示文件或 I/O 资源的一个非负整数。在 Unix 和类 Unix 系统中，每个打开的文件或 I/O 资源都会被分配一个文件描述符。通常，标准输入（stdin）、标准输出（stdout）和标准错误（stderr）会被分配文件描述符 0、1 和 2。

在 Linux 系统中，每个进程的文件描述符信息存储在 `/proc/<pid>/fd` 目录下

```bash
 ls -l /proc/self/fd  
```

![image-20241023225654587](https://gitee.com/bx33661/image/raw/master/path/image-20241023225654587.png)

```bash
lrwx------ 1 root root 64 Oct 23 22:56 0 -> /dev/pts/0
lrwx------ 1 root root 64 Oct 23 22:56 1 -> /dev/pts/0
lrwx------ 1 root root 64 Oct 23 22:56 2 -> /dev/pts/0
lr-x------ 1 root root 64 Oct 23 22:56 3 -> /proc/10714/fd
```

- **`0 -> /dev/pts/0`**:
  - 文件描述符 0 （标准输入）指向 `/dev/pts/0`，这是一个伪终端设备文件，通常用于终端会话的输入。
- **`1 -> /dev/pts/0`**:
  - 文件描述符 1 （标准输出）指向 `/dev/pts/0`，这是伪终端设备文件，用于终端会话的输出。
- **`2 -> /dev/pts/0`**:
  - 文件描述符 2 （标准错误）指向 `/dev/pts/0`，这是伪终端设备文件，用于终端会话的错误输出。
- **`3 -> /proc/10714/fd`**:
  - 文件描述符 3 指向 `/proc/10714/fd`，这意味着该进程打开了另一个进程（PID 10714）的文件描述符目录。这通常用于进程间通信或调试。



注意⚠️的是：
**在 linux 系统中，如果一个程序用open()打开了一个文件但最终没有关闭他，即便从外部（如os.remove(SECRET_FILE)）删除这个文件之后，在 /proc 这个进程的 pid 目录下的 fd 文件描述符目录下还是会有这个文件的文件描述符，通过这个文件描述符我们即可得到被删除文件的内容。**



### 例子

### [网鼎杯 2020 白虎组]PicDown

----

看名字是图片下载，只给了一个输入框，我们随便输入发现

![image-20241023111409888](https://gitee.com/bx33661/image/raw/master/path/image-20241023111409888.png)

发现：`page?url=www.baidu.com`格式

我们尝试`page?url=https://www.baidu.com`，下载下来了图片格式，我们是用`utf-8`格式打开，发现是百度html源码，我们尝试读取内部文件

![image-20241023111612219](https://gitee.com/bx33661/image/raw/master/path/image-20241023111612219.png)

```
page?url=/etc/passwd
```

![image-20241023112007763](https://gitee.com/bx33661/image/raw/master/path/image-20241023112007763.png)

我们还可以通过`/proc/self/cmdline`

![image-20241023112200778](https://gitee.com/bx33661/image/raw/master/path/image-20241023112200778.png)

同时也发现了，这个使用的python2 ，执行的app.py，我们尝试把`app.py`

我尝试读取`/app/app.py` 和 `/home/app/app.py`

```python
from flask import Flask, Response
from flask import render_template
from flask import request
import os
import urllib

app = Flask(__name__)

SECRET_FILE = "/tmp/secret.txt"
f = open(SECRET_FILE)
SECRET_KEY = f.read().strip()
os.remove(SECRET_FILE)


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/page')
def page():
    url = request.args.get("url")
    try:
        if not url.lower().startswith("file"):
            res = urllib.urlopen(url)
            value = res.read()
            response = Response(value, mimetype='application/octet-stream')
            response.headers['Content-Disposition'] = 'attachment; filename=beautiful.jpg'
            return response
        else:
            value = "HACK ERROR!"
    except:
        value = "SOMETHING WRONG!"
    return render_template('search.html', res=value)


@app.route('/no_one_know_the_manager')
def manager():
    key = request.args.get("key")
    print(SECRET_KEY)
    if key == SECRET_KEY:
        shell = request.args.get("shell")
        os.system(shell)
        res = "ok"
    else:
        res = "Wrong Key!"

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

代码审计：

```python
SECRET_FILE = "/tmp/secret.txt"
f = open(SECRET_FILE)
SECRET_KEY = f.read().strip()
os.remove(SECRET_FILE)
```

读取完密钥文件然后删除了，那现在应该是不存在了，

**两个路由：**

- page:这个歌就是我们最开始获取文件的路由
- no_one_know_the_manager：发现可以执行系统命令，但是我们需要密钥

```python
@app.route('/no_one_know_the_manager')
def manager():
    key = request.args.get("key")
    print(SECRET_KEY)
    if key == SECRET_KEY:
        shell = request.args.get("shell")
        os.system(shell)
        res = "ok"
    else:
        res = "Wrong Key!"

    return res
```



学习到-----> 

在 linux 系统中如果一个程序打开了一个文件没有关闭，即便从外部（上文是利用 `os.remove(SECRET_FILE)`）删除之后，在 `/proc` 这个进程的 pid 目录下的 `fd` 文件描述符目录下还是会有这个文件的 `fd`，通过这个我们即可得到被删除文件的内容

```
/page?url=/proc/self/fd/[num]
```

试到三的时候下载出来一个文件

![image-20241023113820569](https://gitee.com/bx33661/image/raw/master/path/image-20241023113820569.png)

```
96cjVfxGDiRJS2ry7LEsFBHLHzi0+NPV26RSEza9Si4=
```

