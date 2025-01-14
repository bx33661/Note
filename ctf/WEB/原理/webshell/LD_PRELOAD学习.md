# LD_PRELOAD学习

---

## 一个例子

我是先复现了安全客上一个例子，体会了一下

https://www.anquanke.com/post/id/254388

先新建一个`passwordcheck.c` 文件

```c
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    char passwd[] = "password";
    if (argc < 2) {
        printf("usage: %s <given-password>\n", argv[0]);
        return 0;
    }
    if (!strcmp(passwd, argv[1])) {
        printf("\033[0;32;32mPassword Correct!\n\033[m");
        return 1;
    } else {
        printf("\033[0;32;31mPassword Wrong!\n\033[m");
        return 0;
    }
}
```

编译一下

```bash
gcc passwordcheck.c -o passwordcheck
```

运行一下看一下效果

![image-20250113135933199](https://gitee.com/bx33661/image/raw/master/path/image-20250113135933199.png)

然后创建一个`hook_strcmp.c`文件

```c
#include <stdlib.h>
#include <string.h>
int strcmp(const char *s1, const char *s2) {
    if (getenv("LD_PRELOAD") == NULL) {
        return 0;
    }
    unsetenv("LD_PRELOAD");
    return 0;
}
```

编译成so文件

```bash
gcc -shared -fPIC hook_strcmp.c -o hook_strcmp.so
```

> `.so` 文件是 **共享库文件（Shared Object file）** 的扩展名，常见于 **Linux/Unix 系统**。它在功能上类似于 Windows 系统中的 `.dll` 文件，用于将通用的代码逻辑以动态链接的方式提供给多个程序使用。

然后设置`LD_PRELOAD`

```BASH
export LD_PRELOAD=$PWD/hook_strcmp.so
```

![image-20250113140427930](https://gitee.com/bx33661/image/raw/master/path/image-20250113140427930.png)



### readelf命令

`readelf` 是一个 Linux 下的命令行工具，用于显示 ELF（Executable and Linkable Format，可执行与可链接格式）文件的信息。ELF 是一种用于可执行文件、目标代码、共享库和核心转储的标准文件格式。`readelf` 可以帮助你深入了解这些文件的内部结构，包括文件头、段（segment）头、节（section）头、符号表、重定位表等信息。

**什么是 ELF 文件？**

在深入 `readelf` 之前，先简单了解一下 ELF 文件。ELF 文件是 Linux 系统中可执行文件和库文件的标准格式。它提供了一种灵活且可扩展的方式来组织程序代码、数据和元数据。ELF 文件主要包含以下几个部分：

- **ELF 头（ELF Header）：** 描述文件的基本属性，例如文件类型（可执行文件、共享库等）、目标体系结构、入口点地址等。
- **程序头表（Program Header Table）：** 描述如何将文件加载到内存中执行，定义了不同的段（segment），例如代码段、数据段等。
- **节头表（Section Header Table）：** 描述文件的各个节（section），例如 `.text`（代码节）、`.data`（数据节）、`.bss`（未初始化数据节）等。
- **数据部分：** 包含实际的程序代码、数据和各种元数据。

**`readelf` 命令的基本用法：**

Bash

```
readelf [选项] ELF文件
```

**常用选项：**

`readelf` 提供了大量的选项来控制输出的信息，以下是一些常用的选项：

- `-a` 或 `--all`：显示所有信息，相当于使用所有其他选项。
- `-h` 或 `--file-header`：显示 ELF 文件头信息。
- `-l` 或 `--program-headers` 或 `--segments`：显示程序头表信息。
- `-S` 或 `--section-headers` 或 `--sections`：显示节头表信息。
- `-s` 或 `--syms` 或 `--symbols`：显示符号表信息。
- `-r` 或 `--relocs`：显示重定位表信息。
- `-d` 或 `--dynamic`：显示动态段信息。
- `-e` 或 `--headers`：显示所有头信息（包括 ELF 头、程序头表和节头表）。
- `-W` 或 `--wide`：使用宽格式输出，避免信息被截断。

**示例：**

假设我们有一个名为 `myprogram` 的可执行文件。

1. **显示 ELF 文件头信息：**

   ```bash
   readelf -h myprogram
   ```

   输出会包含诸如文件类型、目标体系结构、入口点地址等信息。

2. **显示程序头表信息：**

   ```bash
   readelf -l myprogram
   ```

   输出会显示各个段的信息，包括段的类型、偏移地址、虚拟地址、大小等。

3. **显示节头表信息：**

   ```
   readelf -S myprogram
   ```

   输出会显示各个节的信息，包括节的名称、地址、大小、类型等。

4. **显示符号表信息：**

   ```
   readelf -s myprogram
   ```

   输出会显示程序中定义的各种符号，包括函数名、变量名等。符号表对于理解程序的链接过程非常重要。

5. **显示所有信息：**

   ```
   readelf -a myprogram
   ```

   这个命令会输出所有可用的信息，内容非常多，通常用于深入分析 ELF 文件。

**`readelf` 的用途：**

- **理解程序结构：** 通过 `readelf` 可以了解可执行文件的内部结构，包括代码、数据在内存中的布局等。
- **调试程序：** 在调试程序时，`readelf` 可以帮助你查看符号表、重定位表等信息，从而更好地理解程序的运行过程。
- **分析库文件：** 可以使用 `readelf` 分析共享库，了解库中提供的函数和符号。
- **逆向工程：** 在逆向工程中，`readelf` 是一个非常有用的工具，可以帮助分析程序的二进制代码。





## 题目学习

### [0CTF]Wallbreaker_Easy

```bash
Imagick is a awesome library for hackers to break `disable_functions`.
So I installed php-imagick in the server, opened a `backdoor` for you.
Let's try to execute `/readflag` to get the flag.
Open basedir: /var/www/html:/tmp/05571ffc0f0ba134f932c75082af160e
```



执行post传参：backdoor=phpinfo();

![](https://gitee.com/bx33661/image/raw/master/path/image-20250113144130150.png)