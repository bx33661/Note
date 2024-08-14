# PHP特性与各种函数

## str_replace

> str_replace() 函数以其他字符替换字符串中的一些字符（区分大小写）。
>
> 该函数必须遵循下列规则：
>
> - 如果搜索的字符串是数组，那么它将返回数组。
> - 如果搜索的字符串是数组，那么它将对数组中的每个元素进行查找和替换。
> - 如果同时需要对数组进行查找和替换，并且需要执行替换的元素少于查找到的元素的数量，那么多余元素将用空字符串进行替换
> - 如果查找的是数组，而替换的是字符串，那么替代字符串将对所有查找到的值起作用。
>
> **注释：**该函数区分大小写。请使用 [str_ireplace()](https://www.w3school.com.cn/php/func_string_str_ireplace.asp) 函数执行不区分大小写的搜索。
>
> **注释：**该函数是二进制安全的。

### 语法：

```php
str_replace(find,replace,string,count)
```

### 例子

把字符串 "Hello world!" 中的字符 "world" 替换为 "Shanghai"：

```php
<?php
echo str_replace("world","Shanghai","Hello world!");
?>
```

## strstr()

> strstr() 函数搜索字符串在另一字符串中是否存在，如果是，返回该字符串及剩余部分，否则返回 FALSE。

### 语法

```php
strstr(string,search,before_search)
```

### 例子

```php
<?php
echo strstr("Hello world!","world");  // 输出 world!
?>
```

## strcmp()

在PHP中，`strcmp()` 是一个用于比较字符串的内置函数。它的原型如下：
```php
int strcmp(string $str1, string $str2)
```
这个函数会比较两个字符串 `$str1` 和 `$str2`，并返回以下三种结果之一：
1. 如果 `$str1` 小于 `$str2`，则返回小于0的整数。
2. 如果 `$str1` 等于 `$str2`，则返回0。
3. 如果 `$str1` 大于 `$str2`，则返回大于0的整数。
这种比较是基于ASCII值来进行的，比较是区分大小写的。以下是几个例子：
```php
// 示例1
var_dump(strcmp("Hello", "Hello")); // 输出 int(0)
// 示例2
var_dump(strcmp("Apple", "Banana")); // 输出 int(-1)，因为 "Apple" 在 "Banana" 之前
// 示例3
var_dump(strcmp("Banana", "Apple")); // 输出 int(1)，因为 "Banana" 在 "Apple" 之后
// 示例4
var_dump(strcmp("apple", "Apple")); // 输出 int(1)，因为小写的 "a" 的ASCII值大于大写的 "A"
```
需要注意的是，如果比较的字符串中含有二进制数据，可能会得到不可预料的结果，因为 `strcmp()` 会在遇到 null 字符 (`\0`) 时停止比较。
另外，如果你需要进行不区分大小写的比较，可以使用 `strcasecmp()` 函数。
在使用 `strcmp()` 时，还应确保比较的字符串是有效的，以避免产生任何警告或错误。

> 绕过方法：
>
> 当strcmp比较出错的时候就会为null。null即为0故输出flag。
>
> strcmp(arr,str);
>
> ?test[]=1

## extract

(PHP 4, PHP 5, PHP 7, PHP 8)

extract — 从数组中将变量导入到当前的符号表

### 说明[ ¶](https://www.php.net/manual/zh/function.extract.php)

```php
extract(array &$array, int $flags = EXTR_OVERWRITE, string $prefix = ""): int
```

本函数用来将变量从数组中导入到当前的符号表中。

检查每个键名看是否可以作为一个合法的变量名，同时也检查和符号表中已有的变量名的冲突。

### 例子

```php
<?php

/* 假定 $var_array 是 wddx_deserialize 返回的数组*/

$size = "large";
$var_array = array("color" => "blue",
                   "size"  => "medium",
                   "shape" => "sphere");
extract($var_array, EXTR_PREFIX_SAME, "wddx");

echo "$color, $size, $shape, $wddx_size\n";

?>
```

