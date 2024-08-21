# CTFSHOW-WEB-信息搜集

[TOC]

## web-1

直接`CTRL+U`查看网页源代码



## web-2

```bash
view-source:url
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715772994055-cdeeaeb3-7468-4456-b81a-907a35ee913e.png#averageHue=%23e9e9e5&clientId=u4e4b0884-61d4-4&from=paste&height=120&id=u8202b5cc&originHeight=180&originWidth=1003&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=29141&status=done&style=none&taskId=u9b1fb554-b8b3-4e95-9ad7-6ce96179e07&title=&width=668.6666666666666)
点击F12无作用
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715772980031-eb9d6b1f-8257-48c1-a989-fc1f40032763.png#averageHue=%23fafaf9&clientId=u4e4b0884-61d4-4&from=paste&height=512&id=ufc7c0792&originHeight=768&originWidth=1750&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=133322&status=done&style=none&taskId=u786ba3bd-867f-4364-a896-7e3a17eb987&title=&width=1166.6666666666667)

## web-3
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715774364533-e740bbb6-029e-46ff-82e4-db952c341167.png#averageHue=%23eae9e4&clientId=u50145e32-3875-4&from=paste&height=140&id=u23177bee&originHeight=210&originWidth=939&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=31797&status=done&style=none&taskId=ueae07271-3e19-4f4f-8811-8e629ea4ab2&title=&width=626)
F12和查询资源后没用，用bp抓包一下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715774407583-7b945921-8b9c-4789-80d4-39362b4d1c11.png#averageHue=%23fafaf9&clientId=u50145e32-3875-4&from=paste&height=389&id=ubc34705b&originHeight=584&originWidth=1927&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=134007&status=done&style=none&taskId=u53c1a7a4-e47e-4585-a952-50bc031e707&title=&width=1284.6666666666667)
找到flag在返回值里面：
```bash
ctfshow{f8e67d22-4f8f-4454-8893-61b5bd52860e}
```

---

## web-4
扫描，进入 `robots.txt`
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715775508088-769006c2-55b2-4339-917f-dab36ebb9467.png#averageHue=%23eae9e5&clientId=u54147efd-de2d-4&from=paste&height=155&id=u983a5f13&originHeight=232&originWidth=1050&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=36938&status=done&style=none&taskId=ua0971872-ce4a-47d4-939d-d4818393f98&title=&width=700)
按照提示进行下去：
得到flag
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715775573581-37211d5e-dc91-444b-96c4-82788a64ac31.png#averageHue=%23eaeae7&clientId=u54147efd-de2d-4&from=paste&height=142&id=u502cc3b5&originHeight=213&originWidth=1100&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=38846&status=done&style=none&taskId=u3cb335d3-b7f9-4636-bc2c-afdb886655f&title=&width=733.3333333333334)

---

## web-5 phps文件泄露
[CTF学习-PHPS文件泄露-CSDN博客](https://blog.csdn.net/JY_Heart/article/details/129398872?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171577601416800182785041%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171577601416800182785041&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-129398872-null-null.142^v100^pc_search_result_base5&utm_term=phps%E6%96%87%E4%BB%B6%E6%B3%84%E9%9C%B2&spm=1018.2226.3001.4187)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715776292651-3559c1f8-94ef-4333-b748-5501f39210b7.png#averageHue=%23e9e9e4&clientId=u54147efd-de2d-4&from=paste&height=114&id=u3c8d8e10&originHeight=171&originWidth=1177&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=30887&status=done&style=none&taskId=u345cba5b-7aa6-4b88-a890-d10b0e06390&title=&width=784.6666666666666)
输入   --- index.phps
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715776315343-2ff60d23-1b05-4247-88ac-43d74b110d1f.png#averageHue=%23faf9f9&clientId=u54147efd-de2d-4&from=paste&height=93&id=uddac2efb&originHeight=139&originWidth=480&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=9213&status=done&style=none&taskId=u13584e58-956e-4298-bc9a-144ee693333&title=&width=320)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715776334345-c66b6333-2690-4b4a-8e82-1d9340bdf83f.png#averageHue=%23232222&clientId=u54147efd-de2d-4&from=paste&height=477&id=u84d49be4&originHeight=715&originWidth=1115&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=95678&status=done&style=none&taskId=ub9d56c15-713b-4175-9aa9-239a6db3017&title=&width=743.3333333333334)

---

## web-6  www.zip
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715779429303-cd38d4db-243a-4c85-b863-3b78f306dddc.png#averageHue=%23eae9e4&clientId=u54147efd-de2d-4&from=paste&height=137&id=u05b029c8&originHeight=206&originWidth=990&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=33414&status=done&style=none&taskId=ueee995f3-9dd2-4fc2-a8e7-64dbbdd8e18&title=&width=660)
www.zip泄露，url/www.zip
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715779474010-aefeb980-1292-41c5-bbe7-9dedb5238dba.png#averageHue=%23f9f6f4&clientId=u54147efd-de2d-4&from=paste&height=329&id=ua5a5dee0&originHeight=493&originWidth=1760&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=71638&status=done&style=none&taskId=uceb62f84-0b66-4727-bb1a-c05d5b928d0&title=&width=1173.3333333333333)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715779485965-ad13bc89-3f64-477c-9b55-e60d46f77f58.png#averageHue=%23f3f0ed&clientId=u54147efd-de2d-4&from=paste&height=200&id=u5ceafc86&originHeight=300&originWidth=1201&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=22297&status=done&style=none&taskId=uef41bd27-6c9b-4b3e-9ae2-493d0f9db65&title=&width=800.6666666666666)
得到flag

---

## web7：.git泄露
> 用dirsearch扫描发现，.git可以访问

我第一下使用githack但是提示如下:
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715783037863-71e21e02-7c88-4bae-b0ba-eacef73e5f0f.png#averageHue=%23171717&clientId=u256e3f60-df35-4&from=paste&height=107&id=u6a13de17&originHeight=160&originWidth=1687&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=24848&status=done&style=none&taskId=u9ca622f6-3f81-4a27-8b40-4d1d3045488&title=&width=1124.6666666666667)
没有文件可以下载，于是我开始访问`./.git`目录
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715783089411-638cbd57-ba65-477d-ae6b-7c7b10acdea3.png#averageHue=%23e9e8e4&clientId=u256e3f60-df35-4&from=paste&height=139&id=u54dc5b62&originHeight=209&originWidth=1141&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=46024&status=done&style=none&taskId=u9d9bfbb9-3b20-4587-99ce-8d64b97c5ed&title=&width=760.6666666666666)
发现flag

---

## web8：.svn泄露
常规操作查找，使用dirmap或dirsearch扫描端口发现
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715824365608-884b3cff-227a-463a-a359-ad96a4e84302.png#averageHue=%230f0f0f&clientId=u9bcc38df-e3ab-4&from=paste&height=421&id=u2b9b3f80&originHeight=631&originWidth=1693&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=74601&status=done&style=none&taskId=u8d24015d-6914-4bfe-9fb4-d3c5bc0cfd3&title=&width=1128.6666666666667)
于是在浏览器上搜索：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715824385814-9908d589-286f-4388-8c92-fe4736fe9ede.png#averageHue=%23e9e9e5&clientId=u9bcc38df-e3ab-4&from=paste&height=120&id=ue3d2d073&originHeight=180&originWidth=1009&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=41533&status=done&style=none&taskId=ue5370aa0-e532-4f47-b6e4-f303f07fe7f&title=&width=672.6666666666666)

---

## web9：vim
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715827254270-55073497-3416-4b93-814b-0778b1dedb00.png#averageHue=%23fefefe&clientId=uc7ac3868-f378-4&from=paste&height=256&id=ua9d299d8&originHeight=384&originWidth=1138&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=65916&status=done&style=none&taskId=ub72e3a49-7531-4ad6-b269-22b13a15947&title=&width=758.6666666666666)
根据题目提示：
> vim缓存泄露，在使用vim进行编辑时，会产生缓存文件，操作正常，则会删除缓存文件，如果意外退出，缓存文件保留下来，这是时可以通过缓存文件来得到原文件，以index.php来说，第一次退出后，缓存文件名为 .index.php.swp，第二次退出后，缓存文件名为.index.php.swo,第三次退出后文件名为.index.php.swn

![1715827400853_d.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715827404485-c2381d17-ae49-4f03-823a-fbba41736505.png#averageHue=%23282726&clientId=uc7ac3868-f378-4&from=paste&height=71&id=u53e02fc2&originHeight=107&originWidth=1114&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=14323&status=done&style=none&taskId=u1f96dfda-55aa-46c5-81d7-a513c9d5b68&title=&width=742.6666666666666)


---

## web10：cookie泄露
根据提示直接在cookie里面寻找
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715827918278-5fb626f1-83a1-49d7-a57c-c78d559b27a5.png#averageHue=%238d8d8b&clientId=uc7ac3868-f378-4&from=paste&height=474&id=ua9cf1e05&originHeight=711&originWidth=2560&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=135397&status=done&style=none&taskId=uffc69089-78bf-4c35-a151-2166e5d97d9&title=&width=1706.6666666666667)
完成

---

## web11：
利用nslookup

---

## web12：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715866144361-c7311823-5eea-42ac-99a1-c861cf2704f0.png#averageHue=%23fefdfd&clientId=ube4643aa-6a3a-4&from=paste&height=413&id=udac0cc20&originHeight=620&originWidth=1108&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=106846&status=done&style=none&taskId=u84a2ae47-1128-467d-b449-c10b621331c&title=&width=738.6666666666666)
经过提示我们需要在网站上寻找可用资源
先扫描一下，发现robots.txt
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715866470487-04e15520-fb37-43f1-8034-5e20ff773e9d.png#averageHue=%23eaeae6&clientId=u318d9ff5-3e66-4&from=paste&height=245&id=u38e02b56&originHeight=367&originWidth=1166&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=40530&status=done&style=none&taskId=u4cdafcef-319b-4ce5-821d-40a418ef516&title=&width=777.3333333333334)
进入./admin/目录
发现需要输入：
> admin:
password:

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715866538669-b9db0b98-ffe7-4700-a007-5f1ac3e26b07.png#averageHue=%23acabaa&clientId=u318d9ff5-3e66-4&from=paste&height=953&id=u2fce6b19&originHeight=1430&originWidth=2153&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=316928&status=done&style=none&taskId=u8d376776-d0b4-49ac-83d7-025d02f9500&title=&width=1435.3333333333333)
在网站上搜集到信息之后
> admin = admin
> password =[372619038](https://5a7ebed2-0354-4233-bbb6-5857647a73b4.challenge.ctf.show/#)

得到flag
![image.png](https://cdn.nlark.com/yuque/0/2024/png/42994824/1715866600014-fdd36dd5-91cb-4e50-b81f-956227ede97c.png#averageHue=%23e9e9e4&clientId=u318d9ff5-3e66-4&from=paste&height=154&id=u4c7b9cb4&originHeight=231&originWidth=1048&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=39744&status=done&style=none&taskId=u89846e7f-8879-4d50-be03-4aa78e830b4&title=&width=698.6666666666666)
