[TOC]

### PyObject

参考文章

- http://www.lll.plus/zh/blog/content?id=1428
- http://www.lll.plus/zh/blog/content?id=1439

> 主要是了解和记录一下，感觉是比较深奥的，得沉淀一下

CPython中的`object.h`

```c
// object.h
/* Nothing is actually declared to be a PyObject, but every pointer to
 * a Python object can be cast to a PyObject*.  This is inheritance built
 * by hand.  Similarly every pointer to a variable-size Python object can,
 * in addition, be cast to PyVarObject*.
 */
struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    PyTypeObject *ob_type;
};

// pytypedefs.h
typedef struct _object PyObject;
```

> 翻译了一下注释内容：
>
> 实际上并没有声明任何东西为 PyObject，但每个指向 Python 对象的指针都可以转换为 PyObject*。这是手动构建的继承。同样，每个指向可变大小 Python 对象的指针，除了可以转换为 PyVarObject* 之外，还可以转换为 PyVarObject*

--->看一下这个例子，各个类型的继承关系

```python
In [5]: int.__mro__
Out[5]: (int, object)

In [6]: str.__mro__
Out[6]: (str, object)

In [7]: float.__mro__
Out[7]: (float, object)

In [8]: object.__mro__
Out[8]: (object,)
```



```c
// floatobject.h
typedef struct {
    PyObject_HEAD
    double ob_fval;
} PyFloatObject;

// object.h
/* PyObject_HEAD defines the initial segment of every PyObject. */
#define PyObject_HEAD                   PyObject ob_base;
```

其中``PyObject_HEAD` 是一个宏定义

**`double ob_fval`**: 这是一个 `double` 类型的字段，用于存储浮点数的值

再看下面的

```c
#define PyObject_HEAD                   PyObject ob_base;
```

**`PyObject_HEAD`**: 这个宏定义了 `PyObject` 的基本头部。它展开后就是 `PyObject ob_base;`，这意味着 `PyObject_HEAD` 实际上就是 `struct _object` 的定义。

> 在 C 语言中，宏（Macro）是一种预处理指令，用于在编译之前替换代码中的文本。宏通常用于定义常量、简化代码、减少重复代码等

我们可以展开来看：
```c
typedef struct {
    PyObject ob_base;  // 包含引用计数和类型信息
    double ob_fval;    // 浮点数的值
} PyFloatObject;
```

总的来说---> `PyFloatObject` 是一个结构体，它继承了 `PyObject` 的基本结构，并添加了一个 `double` 类型的字段 `ob_fval`，用于存储浮点数的值。这种设计使得 `PyFloatObject` 可以被视为一个 `PyObject`，并且可以通过指针转换来访问其基本属性和方法。



所以说*object是任何类型的父类，或者说，python中的任何一个类都继承自object类，除了object自己外*



### PyTypeObject

```c
// If this structure is modified, Doc/includes/typestruct.h should be updated
// as well.
struct _typeobject {
    PyObject_VAR_HEAD
    const char *tp_name; /* For printing, in format "<module>.<name>" */
    Py_ssize_t tp_basicsize, tp_itemsize; /* For allocation */

    /* Methods to implement standard operations */

    destructor tp_dealloc;
    Py_ssize_t tp_vectorcall_offset;
    getattrfunc tp_getattr;
    setattrfunc tp_setattr;
    PyAsyncMethods *tp_as_async; /* formerly known as tp_compare (Python 2)
                                    or tp_reserved (Python 3) */
    reprfunc tp_repr;

    /* Method suites for standard classes */

    PyNumberMethods *tp_as_number;
    PySequenceMethods *tp_as_sequence;
    PyMappingMethods *tp_as_mapping;

    /* More standard operations (here for binary compatibility) */

    hashfunc tp_hash;
    ternaryfunc tp_call;
    reprfunc tp_str;
    getattrofunc tp_getattro;
    setattrofunc tp_setattro;

    /* Functions to access object as input/output buffer */
    PyBufferProcs *tp_as_buffer;

    /* Flags to define presence of optional/expanded features */
    unsigned long tp_flags;

    const char *tp_doc; /* Documentation string */

    /* Assigned meaning in release 2.0 */
    /* call function for all accessible objects */
    traverseproc tp_traverse;

    /* delete references to contained objects */
    inquiry tp_clear;

    /* Assigned meaning in release 2.1 */
    /* rich comparisons */
    richcmpfunc tp_richcompare;

    /* weak reference enabler */
    Py_ssize_t tp_weaklistoffset;

    /* Iterators */
    getiterfunc tp_iter;
    iternextfunc tp_iternext;

    /* Attribute descriptor and subclassing stuff */
    PyMethodDef *tp_methods;
    PyMemberDef *tp_members;
    PyGetSetDef *tp_getset;
    // Strong reference on a heap type, borrowed reference on a static type
    PyTypeObject *tp_base;
    PyObject *tp_dict;
    descrgetfunc tp_descr_get;
    descrsetfunc tp_descr_set;
    Py_ssize_t tp_dictoffset;
    initproc tp_init;
    allocfunc tp_alloc;
    newfunc tp_new;
    freefunc tp_free; /* Low-level free-memory routine */
    inquiry tp_is_gc; /* For PyObject_IS_GC */
    PyObject *tp_bases;
    PyObject *tp_mro; /* method resolution order */
    PyObject *tp_cache;
    PyObject *tp_subclasses;
    PyObject *tp_weaklist;
    destructor tp_del;

    /* Type attribute cache version tag. Added in version 2.6 */
    unsigned int tp_version_tag;

    destructor tp_finalize;
    vectorcallfunc tp_vectorcall;
};
```

读了文章和使用copilot,学习到了

`tp_name`：类型名称

- **作用**：定义类型的名称，用于打印、错误提示等。

- **示例**：

  ```c
  // 定义一个新的类型对象
  PyTypeObject MyType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "mymodule.MyType", // 类型名称
    .tp_basicsize = sizeof(MyObject),
    // 其他字段...
  };
  ```

  **在 Python 中的效果**：

  ```python
  >>> obj = MyType()
  >>> print(type(obj))
  <class 'mymodule.MyType'>
  ```

`tp_methods`:对象方法列表

> 我的理解就是：就是定义新的类型时，告诉程序这个类型拥有哪些方法的一个列表

- 代码原型

  ```c
  // 定义方法函数
  static PyObject *MyObject_hello(MyObject *self, PyObject *args) {
      printf("Hello from MyType!\n");
      Py_RETURN_NONE;
  }
  
  // 定义方法列表
  static PyMethodDef MyObject_methods[] = {
      {"hello", (PyCFunction)MyObject_hello, METH_NOARGS, "Say hello"},
      {NULL}  // 哨兵，表示列表结束
  };
  
  // 定义类型对象
  PyTypeObject MyType = {
      PyVarObject_HEAD_INIT(NULL, 0)
      .tp_name = "mymodule.MyType",        // 类型名称
      .tp_basicsize = sizeof(MyObject),    // 对象大小
      .tp_methods = MyObject_methods,      // 对象方法列表
      // 其他字段...
  };
  ```

​	**`PyTypeObject`结构**：定义新的Python类型的核心数据结构。

​	字段解释

​		`PyVarObject_HEAD_INIT(NULL, 0)`：初始化类型对象的头部。

​		`.tp_name = "mymodule.MyType"`：类型的全名，通常是`模块名.类型名`格式。

​		`.tp_basicsize = sizeof(MyObject)`：对象的基本大小，用于内存分配。

​		`.tp_methods = MyObject_methods`：将之前定义的方法列表关联到类型上。

​	实现过程

1. 定义了方法`MyObject_hello`，该方法在被调用时输出一行文本并返回`None`。
2. 将方法添加到`MyObject_methods`方法列表中，以供类型使用。
3. 定义`PyTypeObject MyType`类型对象，设置基本信息并关联方法列表。

- python中的效果

```python
>>> obj = MyType()
>>> obj.hello()
Hello from MyType!
```



就看了这两个，这两个相对好懂一些

> 1. **`PyTypeObject` 内部定义了三大类型的结构体**
>
>    - 三大类型
>
>      - **`number`（数值类型）**
>      - **`sequence`（序列类型）**
>      - **`mapping`（映射类型）**
>
>    - 含义
>
>      ：每个结构体都代表了一类最基本的行为集合。它们定义了对应类型需要实现的方法和操作。
>
>      - **`PyNumberMethods`**：定义数值类型的操作，如加减乘除、取模等。
>      - **`PySequenceMethods`**：定义序列类型的操作，如索引、切片、长度计算等。
>      - **`PyMappingMethods`**：定义映射类型的操作，如键值访问、长度计算等。



### **IPython更好的交互体验**

项目地址：https://github.com/ipython/ipython

```python
pip install ipython
#使用
ipython
```

同时了解到了一个小彩蛋

```python
import this
```

![image-20241030113259436](https://gitee.com/bx33661/image/raw/master/path/image-20241030113259436.png)





**探究bulitins**

```python
dir(__builtins__)
```

--->包含了Python中的内置异常、内置常量、内置函数和内置类型

```python
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```



**内置常量**

| 常量名称        | 描述                      |
| --------------- | ------------------------- |
| --------------- | ------------------------- |
| Ellipsis        | 省略符号 ...              |
| False           | 布尔值 False              |
| None            | 空值 None                 |
| NotImplemented  | 未实现                    |
| True            | 布尔值True                |





### python链

```python
>>> ().__class__
<class 'tuple'>
>>> "".__class__
<class 'str'>
>>> [].__class__
<class 'list'>
```

我们在ssti中经常使用的`""`,和`（）`，我的理解就是创建一个空元组或者空字符串为入口，一切皆对象的方式，来访问其他内置函数





在 Python 中导入模块的方法通常有三种（xxx 为模块名称）：

1. `import xxx`
2. `from xxx import *`
3. `__import__('xxx')`

示例：

```python
my_package = __import__("os")
my_package.system("dir")
```





**pip**

```python
pip list
```

![image-20241029210807455](https://gitee.com/bx33661/image/raw/master/path/image-20241029210807455.png)

```python
pip show jinjia2
```

![image-20241029205719603](https://gitee.com/bx33661/image/raw/master/path/image-20241029205719603.png)

```python
pip show jinjia2
pip show os
```

![image-20241029210914840](https://gitee.com/bx33661/image/raw/master/path/image-20241029210914840.png)

> 由于os是内部模块，不饿那个输出信息





### **python 域**

> 在 Python 中，**作用域**（Scope）是指变量、函数、类等名称在代码中可见和可访问的范围。理解作用域对于编写清晰、可维护的代码非常重要。Python 的作用域规则遵循 LEGB 规则，即：

1. **Local (局部作用域)**
2. **Enclosing (闭包作用域)**
3. **Global (全局作用域)**
4. **Built-in (内置作用域)**

(以前老是不知道老用的`__bulitins__`为啥叫这)

局部和这个全局都比较熟悉，

- Enclosing (闭包作用域)

闭包作用域是指嵌套函数中，外部函数的变量对于内部函数来说是可见的，但不是全局的。

```python
def outer_function():
    y = 20  # y 是外部函数的局部变量

    def inner_function():
        print(y)  # 内部函数可以访问外部函数的变量

    inner_function()

outer_function()  # 输出 20
```

-  Built-in (内置作用域)

内置作用域包含 Python 内置的函数和变量，如 `print`、`len`、`range` 等。这些名称在任何地方都是可见的。

```python
print(len([1, 2, 3]))  # 使用内置函数 len
```

作用域规则示例

```python
# 内置作用域
import builtins

# 全局作用域
global_var = 100

def outer_function():
    # 闭包作用域
    enclosing_var = 200

    def inner_function():
        # 局部作用域
        local_var = 300
        print(local_var)  # 输出 300
        print(enclosing_var)  # 输出 200
        print(global_var)  # 输出 100
        print(dir(builtins))  # 查看所有内置名称

    inner_function()

outer_function()
```



还有一个有趣的示例：
```python
import builtins

#全局变量
x  = 1

def f():
    #局部变量
    x = 2
    print(x)
    print(globals()['x'])
    print(locals()['x'])
    print(builtins.__dict__['x'])

f()
```

输出结果如下：
```
2
1
2
Traceback (most recent call last):
  File "E:\py\py-demo\bu.py", line 14, in <module>
    f()
  File "E:\py\py-demo\bu.py", line 12, in f
    print(builtins.__dict__['x'])
          ~~~~~~~~~~~~~~~~~^^^^^
KeyError: 'x'
```

> `KeyError: 'x'` 错误是因为 `builtins.__dict__` 中并没有名为 `'x'` 的键。`builtins.__dict__` 包含了 Python 内置的所有函数和变量，但 `x` 并不是内置的名称。



**`locals()`函数**

这个可以帮助我们调试，所处环境中的变量，这个字典包含了当前作用域中所有局部变量和它们的值。

```
x  = 1
my_name = "bx33661"
def f():
    #局部变量
    x = 2
    my_name = "dx33661"
    #print(builtins.__dict__['x'])
    print(locals())

f()
print(locals())
```

看一下结果

```python
{'x': 2, 'my_name': 'dx33661'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001BFA0CD5F90>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'E:\\py\\py-demo\\bu.py', '__cached__': None, 'builtins': <module 'builtins' (built-in)>, 'x': 1, 'my_name': 'bx33661', 'f': <function f at 0x000001BFA0DAD120>}
```



