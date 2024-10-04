## R!!C!!E!!

![image-20240822154309075](https://gitee.com/bx33661/image/raw/master/path/image-20240822154309075.png)

进入页面，提示需要找一些信息

使用目录扫描，发现`.git`泄露，这里使用`GitHack-master`直接下载下来，有两个文件

- bo0g1pop.php
- index.php

```php
<?php
highlight_file(__FILE__);
if (';' === preg_replace('/[^\W]+\((?R)?\)/', '', $_GET['star'])) {
    if(!preg_match('/high|get_defined_vars|scandir|var_dump|read|file|php|curent|end/i',$_GET['star'])){
        eval($_GET['star']);
    }
}
```

发现   RCE  