## [ACTF2020 新生赛]BackupFile

---

> flag{e421afa0-93df-4a82-aa4f-e5e3419ca3af}

### 1.

进入界面，常规的审查发现什么也没有：

![image-20240603214156642](https://gitee.com/bx33661/image/raw/master/path/image-20240603214156642.png)

根据提示backupfile---->备份文件

使用dirsearch扫描发现了

`./index.php.bak`

下载文件发现：

```php
<?php
include_once "flag.php";

if(isset($_GET['key'])) {
    $key = $_GET['key'];
    if(!is_numeric($key)) {
        exit("Just num!");
    }
    $key = intval($key);
    $str = "123ffwsfwefwf24r2f32ir23jrw923rskfjwtsw54w3";
    if($key == $str) {
        echo $flag;
    }
}
else {
    echo "Try to find out source file!";
}


```

> `==`为弱相等，当整数和字符串类型相比较时。会先将字符串转化为整数然后再进行比较。
>
> 比如a=123和b=123xxx进行`==`比较时只比较b的前面数字部分即b转化成123

所以我们传入参数

```
/?key=123
```

即可得到flag