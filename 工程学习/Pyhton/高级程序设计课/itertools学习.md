> 整理于deepseek

`itertools` 是 Python 标准库中的一个模块，提供了许多用于操作迭代器的工具函数。这些函数可以帮助你生成各种组合、排列、笛卡尔积等，非常适合用于解决涉及组合数学的问题。

以下是一些常用的 `itertools` 函数及其用途：

### 1. `itertools.combinations(iterable, r)`
生成 `iterable` 中所有长度为 `r` 的组合。组合是无序的，即 `(a, b)` 和 `(b, a)` 被认为是相同的组合。

```python
import itertools

# 从 'ABCD' 中生成所有长度为 2 的组合
combinations = itertools.combinations('ABCD', 2)
for combo in combinations:
    print(combo)
```

输出：
```plaintext
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'C')
('B', 'D')
('C', 'D')
```

### 2. `itertools.permutations(iterable, r)`
生成 `iterable` 中所有长度为 `r` 的排列。排列是有序的，即 `(a, b)` 和 `(b, a)` 被认为是不同的排列。

```python
import itertools

# 从 'ABCD' 中生成所有长度为 2 的排列
permutations = itertools.permutations('ABCD', 2)
for perm in permutations:
    print(perm)
```

输出：
```plaintext
('A', 'B')
('A', 'C')
('A', 'D')
('B', 'A')
('B', 'C')
('B', 'D')
('C', 'A')
('C', 'B')
('C', 'D')
('D', 'A')
('D', 'B')
('D', 'C')
```

### 3. `itertools.product(*iterables, repeat=1)`
生成多个 `iterables` 的笛卡尔积。`repeat` 参数用于指定重复次数。

```python
import itertools

# 生成 'AB' 和 '12' 的笛卡尔积
product = itertools.product('AB', '12')
for prod in product:
    print(prod)
```

输出：
```plaintext
('A', '1')
('A', '2')
('B', '1')
('B', '2')
```

### 4. `itertools.chain(*iterables)`
将多个 `iterables` 连接成一个迭代器。

```python
import itertools

# 将 'ABC' 和 'DEF' 连接成一个迭代器
chain = itertools.chain('ABC', 'DEF')
for item in chain:
    print(item)
```

输出：
```plaintext
A
B
C
D
E
F
```

### 5. `itertools.groupby(iterable, key=None)`
根据 `key` 函数对 `iterable` 进行分组。

```python
import itertools

# 根据字符长度对字符串进行分组
data = ['aa', 'bb', 'ccc', 'dd', 'eee']
grouped = itertools.groupby(data, key=len)
for key, group in grouped:
    print(key, list(group))
```

输出：
```plaintext
2 ['aa', 'bb']
3 ['ccc', 'dd', 'eee']
```

### 6. `itertools.islice(iterable, start, stop[, step])`
对 `iterable` 进行切片操作，类似于列表的切片。

```python
import itertools

# 对 'ABCDEFG' 进行切片操作
sliced = itertools.islice('ABCDEFG', 2, 5)
for item in sliced:
    print(item)
```

输出：
```plaintext
C
D
E
```

### 7. `itertools.cycle(iterable)`
无限循环 `iterable` 中的元素。

```python
import itertools

# 无限循环 'ABC'
cycle = itertools.cycle('ABC')
for _ in range(10):
    print(next(cycle), end=' ')
```

输出：
```plaintext
A B C A B C A B C A 
```

### 8. `itertools.repeat(object[, times])`
重复生成 `object`，重复次数由 `times` 指定。

```python
import itertools

# 重复生成 'A' 5 次
repeat = itertools.repeat('A', 5)
for item in repeat:
    print(item, end=' ')
```

输出：
```plaintext
A A A A A 
```

这些只是 `itertools` 模块中的一部分函数，它们可以帮助你高效地处理各种迭代器操作。通过组合使用这些函数，你可以解决许多复杂的组合数学问题。