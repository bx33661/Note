### `file`命令

> 下载file
>
> ```bash
> sudo apt update
> sudo apt install file
> ```

`file` 命令是一个在 Unix 和类 Unix 系统（例如 Linux、macOS）中非常实用的工具，用于确定文件的类型。它不依赖于文件扩展名，而是通过检查文件的内部结构（例如文件头部的“魔数”），来准确地判断文件类型。这在处理没有扩展名或者扩展名被错误修改的文件时非常有用。

**基本语法:**

```bash
file [选项] 文件名...
```

**常用选项:**

- `-b` (brief): 简洁输出，只显示文件类型，不显示文件名。
- `-c` (check): 检查被测试文件的标准格式中的语法错误。此选项不检查实际的文件内容。
- `-d` (debug): 输出调试信息。
- `-f <namefile>` (files-from): 从指定的文件中读取要检查的文件名列表，每行一个文件名。
- `-i` (mime-type): 输出 MIME 类型，例如 `text/plain`、`image/jpeg`。这在 Web 开发中很有用。
- `-L` (follow-symlinks): 如果文件是符号链接，则跟随链接并显示链接指向的文件的类型。默认情况下，`file` 会报告符号链接本身。
- `-z` (uncompress): 尝试解压缩压缩文件并检查解压后的内容。

**工作原理:**

`file` 命令主要通过以下三个步骤来判断文件类型：

1. **文件系统检查：** 检查文件是否存在、是否可读等基本属性。
2. **魔数检查：** 检查文件开头的几个字节（称为“魔数”或“幻数”），这些字节是特定文件类型的标识。例如，JPEG 文件的开头通常是 `ffd8ff`。
3. **语言检查：** 如果前两步没有确定文件类型，`file` 还会尝试根据文件内容判断是否是某种编程语言的源代码或文本文件。

**常见的文件类型输出:**

- `ASCII text`: 纯文本文件，只包含 ASCII 字符。
- `UTF-8 Unicode text`: 使用 UTF-8 编码的文本文件。
- `PNG image`: PNG 图像文件。
- `JPEG image`: JPEG 图像文件。
- `gzip compressed data`: gzip 压缩文件。
- `ELF ...`: 可执行文件或共享库文件（Linux 系统）。
- `Mach-O ...`: 可执行文件或共享库文件 (macOS 系统)。
- `directory`: 目录。
- `symbolic link to ...`: 符号链接，后跟链接指向的目标。

**使用示例:**

1. **检查单个文件类型:**

   ```bash
   file myfile.txt
   ```

   输出示例：

   ```
   myfile.txt: UTF-8 Unicode text
   ```

2. **检查多个文件类型:**

   ```bash
   file myfile.txt image.jpg archive.zip
   ```

3. **简洁输出:**

   ```bash
   file -b myfile.txt
   ```

   输出示例：

   ```
   UTF-8 Unicode text
   ```

4. **输出 MIME 类型:**

   ```bash
   file -i image.jpg
   ```

   输出示例：

   ```
   image.jpg: image/jpeg; charset=binary
   ```

5. **跟随符号链接:**

   假设 `mylink` 是一个指向 `myfile.txt` 的符号链接：

   ```bash
   file mylink
   ```

   默认输出：

   ```
   mylink: symbolic link to myfile.txt
   ```

   使用 `-L` 选项：

   ```bash
   file -L mylink
   ```

   输出示例：

   ```
   mylink: UTF-8 Unicode text
   ```

6. **检查压缩文件内部:**

   ```bash
   file -z archive.zip
   ```

![image-20241212102603790](https://gitee.com/bx33661/image/raw/master/path/image-20241212102603790.png)



### 查看压缩包内容

1. 查看压缩文件内容

```bash
unzip -l demo.zip
```

![image-20241212102901885](https://gitee.com/bx33661/image/raw/master/path/image-20241212102901885.png)

2. zipinfo

```bash
zipinfo demo.zip
```

![image-20241212103050446](https://gitee.com/bx33661/image/raw/master/path/image-20241212103050446.png)

3. 7z

> 安装7z
>
> ```bash
> sudo apt update
> sudo apt install p7zip-full 
> ```

```bash
7z l demo.zip
```

![image-20241212103459074](https://gitee.com/bx33661/image/raw/master/path/image-20241212103459074.png)





### md5sum命令

 **完整性检测：计算文件 MD5**

在合并文件后，为了确保合并后的文件内容正确无误，没有发生损坏或篡改，可以计算文件的 MD5 值进行完整性校验。

- **`md5sum` 命令：** 用于计算文件的 MD5 校验和。

  - **基本语法：** `md5sum 文件名`

  - **示例：** 计算 `output.txt` 文件的 MD5 值：

    Bash

    ```
    md5sum output.txt
    ```

    输出类似于：

    ```
    e10adc3949ba59abbe56e057f20f883e  output.txt
    ```

    其中 `e10adc3949ba59abbe56e057f20f883e` 就是 `output.txt` 文件的 MD5 值。

- **比较 MD5 值：** 如果你有合并前各个文件的 MD5 值，可以将它们组合起来，再计算合并后文件的 MD5 值。如果合并后的 MD5 值与组合后的 MD5 值一致（通常是对合并前所有文件内容直接计算一次MD5值），则说明合并过程没有引入错误。

  **注意:** 直接把各个文件的md5值拼接在一起再计算md5值的方法是不正确的，必须把文件内容连接起来后计算md5值。