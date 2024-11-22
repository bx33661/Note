## PHP

### 16和8进制

十六进制：`0x开头`

 八进制 ： `0开头`

```php
<?php
$orgin_num = 3366;
$eight_num = 06446;
$sixteen_num = 0xd26;
var_dump($orgin_num == $eight_num);
//bool(true)
var_dump($orgin_num == $sixteen_num);
//bool(true)
```



### intval()

```php
intval(mixed $value, int $base = 10): int
```

(PHP-manual)

如果 `base` 是 0，通过检测 `value` 的格式来决定使用的进制：

- 如果字符串包括了 "0x" (或 "0X") 的前缀，使用 16 进制 (hex)；否则，
- 如果字符串以 "0b" (或 "0B") 开头，使用 2 进制 (binary)；否则，
- 如果字符串以 "0" 开始，使用 8 进制(octal)；否则，
- 将使用 10 进制 (decimal)。



### strpos()

`strpos('01234', 0)` 返回的结果是 0 对应的索引 0, 也就是 false

如果是 `!strpos()` 这种则会返回 true

代码使用了 `if(!strpos($str, 0))` 对八进制进行过滤, 可以在字符串开头加空格绕过

strpos() 遇到数组返回 null

strrpos() stripos() strripos() 同理



### is_numeric()

> (PHP 4, PHP 5, PHP 7, PHP 8)
>
> is_numeric — 检测变量是否是数字或数字字符串

```php
is_numeric(mixed $value): bool
```



### SHA1()--哈希

```
string sha1(string $str [, bool $raw_output = false ])
```

![94f37cfe4e0e38af06cf18450b189b2](https://gitee.com/bx33661/image/raw/master/path/94f37cfe4e0e38af06cf18450b189b2.png)
