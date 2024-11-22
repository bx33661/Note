## [BJDCTF2020]Easy MD5

进入题目页面：发现只有一个输入框，根据提示我们输入万能密码

![image-20240603172648128](https://gitee.com/bx33661/image/raw/master/path/image-20240603172648128.png)

> `ffifdyop`

![image-20240603172851687](https://gitee.com/bx33661/image/raw/master/path/image-20240603172851687.png)

```html
<!--
$a = $GET['a'];
$b = $_GET['b'];

if($a != $b && md5($a) == md5($b)){
    // wow, glzjin wants a girl friend.
-->
```

我们利用数组绕过这个md5检测：

![image-20240603173158946](https://gitee.com/bx33661/image/raw/master/path/image-20240603173158946.png)

```php
<?php
error_reporting(0);
include "flag.php";

highlight_file(__FILE__);

if($_POST['param1']!==$_POST['param2']&&md5($_POST['param1'])===md5($_POST['param2'])){
    echo $flag;
}
```

![image-20240603173448331](https://gitee.com/bx33661/image/raw/master/path/image-20240603173448331.png)

利用post传参，得到flag