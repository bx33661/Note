**Python字节码**

字节码的生成过程

1. **源代码**: 你编写的 Python 代码（`.py` 文件）。
2. **编译**: Python 解释器会将源代码编译成字节码。这个过程通常是隐式的，当你运行 Python 代码时，解释器会自动进行编译。
3. **字节码**: 编译后的字节码存储在 `.pyc` 文件中（在 Python 3.2 及更高版本中，通常存储在 `__pycache__` 目录下）。
4. **执行**: 解释器执行字节码，完成程序的运行。

```python
import py_compile
#确保存在一个py文件，为bytecode.py
py_compile.compile('bytecode.py')
```

然后在当前目录下会多出一个`__pycache__`目录

生成了`bytecode.pyc`





```python
>>> import dis
>>> def f(x):print('hello',x)
>>> f.__code__.co_code
b'\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01|\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00'
>>> dis.dis(f)
  1           0 RESUME                   0
              2 LOAD_GLOBAL              1 (NULL + print)
             14 LOAD_CONST               1 ('hello')
             16 LOAD_FAST                0 (x)
             18 PRECALL                  2
             22 CALL                     2
             32 POP_TOP
```

大致分为四列：

源码的行号（即当前字节码对应的源码所在的行数），字节码偏移量，操作码（具体的字节码指令），操作数（字节码指令的参数）。

> 这里简单学习分析一下：
>
> 1. **RESUME**: 这是 Python 3.8 引入的新指令，用于恢复协程或生成器的执行。`0` 表示从第 0 行开始执行。
> 2. **LOAD_GLOBAL**: 加载全局变量。这里加载的是 `print` 函数。`1` 是操作数，表示在全局变量表中的索引。
> 3. **LOAD_CONST**: 加载常量。这里加载的是字符串 `'hello'`。`1` 是操作数，表示在常量表中的索引。
> 4. **LOAD_FAST**: 加载局部变量。这里加载的是局部变量 `x`。`0` 是操作数，表示在局部变量表中的索引。
> 5. **PRECALL**: 准备调用函数。`2` 表示有 2 个参数（`'hello'` 和 `x`）。
> 6. **CALL**: 调用函数。这里调用的是 `print` 函数，参数是 `'hello'` 和 `x`。
> 7. **POP_TOP**: 弹出栈顶元素。这里弹出的是 `print` 函数的返回值（通常是 `None`）。
> 8. **RETURN_VALUE**: 返回值。这里返回的是 `None`。

![image-20241030153445428](https://gitee.com/bx33661/image/raw/master/path/image-20241030153445428.png)

等于说无论我们的代码有多长，最终都是由字节码堆积而成