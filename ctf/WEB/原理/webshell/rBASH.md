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


## 绕过方法
参考：
[Linux rbash 限制绕过 | Yongz 丶](https://www.yongz.fun/posts/49dbd3aa.html)
...

## Linux中的ln
`ln` 命令是 Linux 中一个非常重要的命令，它的功能是为一个文件在另外一个位置建立一个链接。当需要在不同的目录使用相同的文件时，不需要在每个目录下都放置一个相同的文件，只需要在一个固定的目录放置该文件，然后在其他目录下用 `ln` 命令链接它即可，这样可以节省磁盘空间。

**链接的类型：**

Linux 文件系统中的链接分为两种：

- **硬链接（Hard Link）：** 可以理解为一个文件拥有多个文件名。所有硬链接都指向相同的 inode（索引节点），inode 中包含文件的元数据（如权限、所有者、数据块位置等）。因此，无论通过哪个硬链接访问文件，访问的都是相同的数据。
- **符号链接（Symbolic Link，也称为软链接）：** 可以理解为 Windows 中的快捷方式。符号链接是一个特殊的文件，它包含指向目标文件的路径。当访问符号链接时，系统会重定向到目标文件。

**`ln` 命令的语法：**
```
ln [选项] 源文件 目标文件
```
**常用选项：**
- `-s`：创建符号链接。如果没有指定 `-s` 选项，则创建硬链接。
- `-f`：强制创建链接。如果目标文件已存在，则覆盖它。
- `-v`：显示详细的链接创建过程。

**硬链接：**

- **创建硬链接：**    
    ```
    ln 源文件 目标文件
    ```
    
    例如：
    ```
    ln file1.txt file1_hardlink.txt
    ```
    
    这会在当前目录下创建一个名为 `file1_hardlink.txt` 的硬链接，它指向 `file1.txt`。
    
- **硬链接的特点：**
    
    - 硬链接和源文件拥有相同的 inode，因此它们是完全等价的。
    - 修改其中任何一个文件，其他所有硬链接都会受到影响。
    - 删除源文件或任何一个硬链接，其他硬链接仍然可以访问文件内容。只有当所有指向该 inode 的链接都被删除时，文件才会被真正删除。
    - 硬链接不能跨文件系统创建，也不能链接目录。

**符号链接：**

- **创建符号链接：**
    ```
    ln -s 源文件 目标文件
    ```
    
    例如：    
    ```
    ln -s file1.txt file1_softlink.txt
    ```
    
    这会在当前目录下创建一个名为 `file1_softlink.txt` 的符号链接，它指向 `file1.txt`。
    
- **符号链接的特点：**
    
    - 符号链接是一个独立的文件，拥有自己的 inode，其内容是指向目标文件的路径。
    - 修改源文件会影响符号链接访问的内容，但修改符号链接本身不会影响源文件。
    - 如果删除源文件，符号链接将失效（变成“断链”），因为其指向的目标文件不存在了。
    - 符号链接可以跨文件系统创建，也可以链接目录。

**示例：**

1. **创建硬链接：**

    ```bash
    touch original_file.txt  # 创建一个空文件
    ln original_file.txt hard_link.txt
    ls -li  # 查看 inode 信息
    ```
    
    你会发现 `original_file.txt` 和 `hard_link.txt` 的 inode 号相同。
    
2. **创建符号链接：**
    
    ```bash
    ln -s original_file.txt soft_link.txt
    ls -li  # 查看 inode 信息
    ```
    
    你会发现 `original_file.txt` 和 `soft_link.txt` 的 inode 号不同，并且 `soft_link.txt` 的文件类型为 `l`（表示链接）。
    
3. **链接目录：**
    
    ```bash
    mkdir my_directory
    ln -s my_directory my_directory_link
    ```
    
    这会创建一个名为 `my_directory_link` 的符号链接，它指向 `my_directory` 目录。
    

**总结：**

| 特性    | 硬链接                       | 符号链接        |
| ----- | ------------------------- | ----------- |
| inode | 共享同一个 inode               | 拥有不同的 inode |
| 文件类型  | 普通文件                      | 链接文件（l）     |
| 跨文件系统 | 不能                        | 可以          |
| 链接目录  | 不能                        | 可以          |
| 删除源文件 | 其他硬链接仍然有效，直到所有链接都被删除才释放空间 | 链接失效（断链）    |
