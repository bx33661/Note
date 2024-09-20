### highlight_file 结合 glob()

----

- `glob()`

```php
array glob ( string $pattern [, int $flags = 0 ] )
```

- `highlight_file`

```php
highlight_file('path/to/your/file.php');
```



`glob()`出的是一个数组类型

```php
<?php
$nums = glob("./*.php");
foreach ($nums as $num) {
    echo "$num\n";
    echo "<br>";
}
```

![image-20240920201037201](https://gitee.com/bx33661/image/raw/master/path/image-20240920201037201.png)

测试

> 如果题目没有过滤掉highlight，我们可以使用这种执行方法获得flag

```
<?php
//测试,由于目录下有好几个以f开头的文件，我们修改下标寻找
highlight_file(glob("./f*")[1]);
```

![image-20240920201414486](https://gitee.com/bx33661/image/raw/master/path/image-20240920201414486.png)