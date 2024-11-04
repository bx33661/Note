### Python递归

---

```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))
```

这个例子实现阶乘，具体逻辑如下

```(空)
>>> fact(5)
>>> 5*fact(4)
>>> 5*(4*fact(3))
>>> 5*(4*(3*fact(2)))
>>> 5*(4*(3*(2*fact(1)))
>>> 5*(4*(3*(2*(1)))
>>> 5*(4*(3*2))
>>> 5*(4*6)
>>> 5*24
>>> 120
```

这个递归过程的本质在于每一次调用都会等待其下一个调用完成，并利用返回的结果进行后续计算。这就是递归的强大之处，但也正是由于这种等待，递归深度过大会导致栈溢出。

（Stack Overflow）



#### 尾递归

> 尾递归（Tail Recursion）是一种特殊的递归形式，它的特点是在递归调用时没有额外的计算或操作。在尾递归中，递归调用是该函数的最后一步，且递归的返回值直接返回给上一级调用。由于这一特点，尾递归可以被编译器或解释器优化，从而减少函数调用栈的占用，避免递归深度过大导致的栈溢出。

```python
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)

print(factorial_tail(5))  # 120
```

在支持尾递归优化的语言中，尾递归可以将递归调用转换成循环，从而在执行时不会增长调用栈。

```python
>>> factorial_tail(5, 1)
>>> factorial_tail(4, 5)
>>> factorial_tail(3, 20)
>>> factorial_tail(2, 60)
>>> factorial_tail(1, 120)
>>> 120
```

*但在 Python 中，由于没有原生的尾递归优化支持，调用栈会随着递归层数的增加而增长，因此在 Python 中使用尾递归并不会节省内存。*

所以说次数增多同样存在栈溢出问题



### Python偏函数

---

> 偏函数（partial function）是指通过固定一个或多个参数的值，生成一个新的函数。偏函数使得我们可以通过减少函数的参数数量，得到一个更简单、更具体化的函数

基本用法：(**functools**)

```python
from functools import partial

# 原函数
def power(base, exponent):
    return base ** exponent

# 创建偏函数，固定 exponent=2
square = partial(power, exponent=2)

# 使用偏函数
print(square(5))  # 输出：25

```

从这个小例子中我们可以发现：偏函数能帮助代码更简洁、可读性更高



#### 几个例子

- **简化I/O操作**

  ```python
  from functools import partial
  
  # 创建一个偏函数，将文件以只读模式打开
  open_read = partial(open, mode='r')
  
  # 现在我们只需传递文件名即可
  with open_read('example.txt') as f:
      print(f.read())
  ```

  

- **int2函数**

  ```python
  print(int(10))
  res = int(10,base=8)
  print(res)
  //Error
  ```

  *需要注意一点： `int()` 函数在接收两个参数时，第一个参数必须是字符串。正确的用法是将第一个参数写为字符串形式的数字*

  ```python
  from functools import partial
  #创建一个偏函数
  int2 = partial(int, base=2)
  
  def int_to_base(x, base):
      return int(x, base)
  
  #把下面两种形式进行比较
  print(int2('1000000'))
  print(int_to_base('1000000', 2))  # 64
  ```

  从这个小例子中我们可以发现：偏函数能帮助代码更简洁、可读性更高

  