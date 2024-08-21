# web课第一节

---

> 作者：张博翔（bx33661）

## 第一题：bugku-GET

进入页面：

```php
$what=$_GET['what'];
echo $what;
if($what=='flag')
echo 'flag{****}';
```

分析：要求使用get方法传入一个`what`值，`what`的值等于**flag** 时候输出flag

- 可以采用直接在url后直接传入参数
- 可以使用hackbar load传参
- 可以bp抓包在包名后修改url

```
得到flag：flag{bc27baf6f936797ea872031e49bd6e0f}
```

![image-20240803164248227](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240803164248227.png)

## 第二题 bugku-Post

```php
$what=$_POST['what'];
echo $what;
if($what=='flag')
echo 'flag{****}';
```

跟上一题基本思路一样，但是是post方法

- 使用hackbar中的`post data`模块

![image-20240803164800553](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240803164800553.png)

- 采用bp抓包

修改get为post头，添加

```
Content-Type: application/x-www-form-urlencoded
```

修改后的请求头：

```http
POST / HTTP/1.1
Host: 114.67.175.224:18478
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: Hm_lvt_c1b044f909411ac4213045f0478e96fc=1722081512,1722167716; _ga=GA1.1.47055084.1722081512; _ga_F3VRZT58SJ=GS1.1.1722167716.2.1.1722168007.0.0.0
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Length: 11
Content-Type: application/x-www-form-urlencoded

what=flag
```

最后得到flag

## bugku-本地管理员

进入网站，发现是一个登录系统，在代码中发现

```python
dGVzdDEyMw== #看着像bs64编码
#base64解码之后
test123
#感觉是密码，由题目猜测账号是admin
```

提示：==IP禁止访问，请联系本地管理员登陆，IP已被记录.==

在bp中向表头添加----X-Forwarded-For ：127.0.0.1

得到flag：==flag{67cbc02c922177bad0e998e9fea42b5e}==



## bugku--bp

进入页面发现标题是：intruder（爆破），我们得知此题是需要爆破的

![image-20240804090446980](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240804090446980.png)

根据提示我们知道，是z开头6位密码，我尝试在网上寻找这一类的目录

![image-20240804091051425](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240804091051425.png)

开始爆破，这里测试了好几个目录

找到`zxc123`

![image-20240808210021262](C:/Users/lenovo/Desktop/%E7%B4%A0%E6%9D%90%E5%BA%93/%E7%B4%A0%E6%9D%90/image-20240808210021262.png)

> 分析一下，这道题主要是利用bp中的intruder功能实现爆破得到密码