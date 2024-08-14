# 攻防世界-php2

----

进入页面首先发现的就是这个，ctrl+u并没发现什么东西

![image-20240803101405026](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240803101405026.png)

进行目录扫描发现

- index.php
- index.phps

> “.phps”是PHP文件的一种特殊扩展名，它通常用于显示PHP源代码的语法高亮版本。相比于标准的“.php”文件，`.phps`文件不会在服务器上执行PHP代码，而是将PHP代码以格式化的方式展示出来。
>
> 通常情况下，当你在服务器上访问`.phps`文件时，服务器会将文件内容以HTML格式输出，并包含语法高亮。它主要用于代码示例展示、调试或教学目的。如果你想在服务器上启用这种功能，需要在服务器配置文件中指定如何处理`.phps`扩展名，通常是在Apache服务器中通过配置`.htaccess`文件或在PHP的配置文件中进行设置。

```php
<?php
if("admin"===$_GET[id]) {
  echo("<p>not allowed!</p>");
  exit();
}

$_GET[id] = urldecode($_GET[id]);
if($_GET[id] == "admin")
{
  echo "<p>Access granted!</p>";
  echo "<p>Key: xxxxxxx </p>";
}
?>
```

进行代码分析：----我们要绕过第一个检测

这里我们采用`%61dmin`来绕过第一个检测后就可以得到结果

但是值得注意的是，浏览器在接受url时会再进行解码，所以我们采用二次编码

`%2561dmin`最后得到flag