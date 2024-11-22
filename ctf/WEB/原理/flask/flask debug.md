## Flask debug和pin码

从一个小实验进行学习：

我这里是采用pycharm新建一个flask项目，app.py内容如下，里面有一个错误

```python
#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    1/0    
    return '<b>hello world</b>'

if __name__ == '__main__':
    app.run(debug = True)
```

如果我们不开启debug模式，那么浏览器回应如下：

![image-20240918115632871](https://gitee.com/bx33661/image/raw/master/path/image-20240918115632871.png)

我们开启`denbug` 模式---

这个`FLASK_DEBUG=0`

![DDSS](https://gitee.com/bx33661/image/raw/master/path/image-20240918113751926.png)

但需要注意的是pycharm中还需要进行设置，需要打开FLASK_DEBUG

![image-20240918113624533](https://gitee.com/bx33661/image/raw/master/path/image-20240918113624533.png)

再次运行观察到：这个`FLASK_DEBUG=1`

![image-20240918113703363](https://gitee.com/bx33661/image/raw/master/path/image-20240918113703363.png)

同时控制台会输出：

```python
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 109-411-626
```

提示我们Debug模式已经启动，同时我们还获得了**PIN** 码！

![image-20240918115142110](https://gitee.com/bx33661/image/raw/master/path/image-20240918115142110.png)

点击右侧的终端按钮进入调试

会弹出需要pin码的东西，我们输入我们获得的pin码

![image-20240918115249628](https://gitee.com/bx33661/image/raw/master/path/image-20240918115249628.png)

之后就会出现类似于终端的东西，我们可以查询变量，执行函数，来判断哪里出现问题

![image-20240918115839444](https://gitee.com/bx33661/image/raw/master/path/image-20240918115839444.png)



### debug开启的几种方式

1. 在app.run()传递参数

```python
if __name__ == '__main__':
    app.run(debug = True)
```

2. 配置app.deubg=True
3. 配置config.py文件

> [`config`](https://dormousehole.readthedocs.io/en/latest/api.html#flask.Flask.config) 实质上是一个字典的子类，可以像字典一样操作
>
> 具体看：https://dormousehole.readthedocs.io/en/latest/config.html

![image-20240918121230567](https://gitee.com/bx33661/image/raw/master/path/image-20240918121230567.png)



### Pin码

查看源码：(我的实在conda里，路径如下)

**C:\anconda\pkgs\werkzeug-2.2.3-py311haa95532_0\Lib\site-packages\werkzeug\debug\__init__.py**

这个文件⬇️有一个`def get_pin_and_cookie_name()`函数

```python
    probably_public_bits = [
        username,
        modname,
        getattr(app, "__name__", app.__class__.__name__),
        getattr(mod, "__file__", None),
    ]
    private_bits = [str(uuid.getnode()), get_machine_id()]
    #一共六个参数
```

一共六个参数，只要参数一样就可以生成相同pin码

> 但是具体这些参数怎么获得，我没有具体尝试



网上生成代码：

```python
import hashlib
from itertools import chain
probably_public_bits = [
    'Administrator',# username
    'flask.app',# modname
    'Flask',# getattr(app, '__name__', getattr(app.__class__, '__name__'))
    'C:\\Users\\Administrator\\PycharmProjects\\securritystudy\\venv\\lib\\site-packages\\flask\\app.py' # getattr(mod, '__file__', None),
]

private_bits = [
    '106611682152170',# str(uuid.getnode()),  /sys/class/net/ens33/address
    b'6893142a-ab05-4293-86f9-89df10a4361b'# get_machine_id(), /etc/machine-id
]

h = hashlib.md5()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv =None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```

