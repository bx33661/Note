### md5绕过欸

----

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
require 'flag.php';

if (isset($_GET['name']) && isset($_POST['password']) && isset($_GET['name2']) && isset($_POST['password2']) ){
    $name = $_GET['name'];
    $name2 = $_GET['name2'];
    $password = $_POST['password'];
    $password2 = $_POST['password2'];
    if ($name != $password && md5($name) == md5($password)){
        if ($name2 !== $password2 && md5($name2) === md5($password2)){
            echo $flag;
        }
        else{
            echo "再看看啊，马上绕过嘞！";
        }
    }
    else {
        echo "错啦错啦";
    }

}
else {
    echo '没看到参数呐';
}
?> 
```

直接采用数组绕过！

```
http://gz.imxbt.cn:20086/?name[]=1&name2[]=2

password[]=2&password2[]=1
```

