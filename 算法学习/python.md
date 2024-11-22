

# python

*总结一些在leecode上做题所学习到的一些知识---from bx*

[TOC]



## 数据类型

`break`直接终止操作Python 中有多种内置数据类型，它们用于表示和处理不同类型的数据。以下是一些常见的Python数据类型：

1. **整数（int）：** 用于表示整数值，如 1、-5、100。
2. **浮点数（float）：** 用于表示带有小数点的数值，如 3.14、-0.5、2.0。
3. **字符串（str）：** 用于表示文本数据，如 "Hello, World!"、'Python'。
4. **布尔值（bool）：** 用于表示真（True）或假（False）。
5. **列表（list）：** 有序的数据集合，允许包含不同类型的元素。例如，[1, 2, 'three']。
6. **元组（tuple）：** 有序的不可变数据集合，一旦创建，不能被修改。例如，(1, 2, 3)。
7. **集合（set）：** 无序的数据集合，用于存储唯一的元素。例如，{1, 2, 3}。
8. **字典（dict）：** 键-值对的数据结构，用于存储和检索数据。例如，{'name': 'Alice', 'age': 30}。
9. **字节串（bytes）：** 用于存储字节数据，通常用于处理二进制数据。
10. **字节数组（bytearray）：** 与字节串类似，但是可变的。
11. **空值（None）：** 表示一个空对象或变量。
12. **范围（range）：** 用于生成一系列数字。
13. **复数（complex）：** 用于表示复数，如 3+2j。

这些是Python中的一些常见数据类型，每种类型都有特定的属性和方法，用于执行不同的操作。Python还允许用户创建自定义数据类型，以满足特定的需求。数据类型的选择取决于您要处理的数据和任务的性质。



### `Optional[ListNode]` 

是一个类型注解，通常用于 Python 中的类型提示或类型检查。它表示一个具有两种可能取值的数据类型：

1. `None`：表示空值或缺失值。
2. `ListNode` 类型的对象：表示一个链表节点。

通常，`Optional[X]` 表示一个可以是类型 `X` 的对象，也可以是 `None` 的对象。在这种情况下，`Optional[ListNode]` 表示一个可以是链表节点 `ListNode` 的对象，也可以是 `None` 的对象，用于表示可能为空的链表。

例如，如果您要声明一个变量，它可以是链表节点，也可以是空值，可以这样做：

```
 codefrom typing import Optional

node: Optional[ListNode] = None  # 可以是链表节点，也可以是None
```

这有助于在类型提示中明确表达变量的可能取值，以提高代码的可读性和类型安全性。

***



## 操作学习

`return True`返回true
`return False`返回false
`.lower()`将大写变小写
`.upper()`将小写变大写
`.append()`添加数
`.remove()`添加数
`sum()`求和数组
`max()`找出（）内最大数并返回
`min()`找出（）内最小数并返回

***



## replace()函数

`str.replace(old, new, count)` 方法用于在字符串中替换特定子字符串。其中的参数如下：

- `old`: 要被替换的子字符串。
- `new`: 要替换为的新字符串。
- `count`（可选参数）：表示替换的最大次数。如果指定了 `count`，则只会替换前 `count` 次出现的 `old`。

例如，代码片段 `t = t.replace(i, "", 1)` 表示将字符串 `t` 中的第一个匹配的子字符串 `i` 替换为空字符串 `""`。

这将从字符串 `t` 中删除第一个匹配的 `i`。如果 `i` 在 `t` 中多次出现，只有第一个匹配会被替换，其余不会受到影响。

如果需要替换所有匹配的 `i`，可以省略 `count` 参数，或将其设置为更大的值，或使用循环来重复调用 `replace` 方法，直到没有更多匹配的子字符串为止。

>给定两个字符串 s 和 t ，它们只包含小写字母。
>字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
>请找出在 t 中被添加的字母。
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            t=t.replace(i,"",1)
        return t
```

***



## ord()与char()----ASCLL码

`ord()` 函数是Python的内置函数，用于将字符转换为其对应的ASCII码值。它的基本语法如下：
```python
ord(character)
```
`chr()`函数，将ASCLL码值转化为对应字符，基本语法如下：
```python
ascii_value = 65
char = chr(ascii_value)
print(f"字符为 {char}，对应的ASCII码值为 {ascii_value}")
```

***



## 反转数字



```python
orgin_x = x    #由于之后的x值将会被改变所以在一开始保留一个原始的值

reverse_x = 0 #记录反转的值
#开始执行反转
while x< 0:
    dight = x%10
    reverse_x = reverse_x*10 +dight
    x//=10
```

***



## 反向遍历

```python
def ce_last(s):
    a=0
    n=len(s)
    for i in reversed(range(n)):#reversed()函数用于反向遍历!!!!
        if s[i]==' ':
            return a
        else:
            a+=1
```
### reversed()函数
在Python中，`reversed` 是一个内置函数，它用于反转序列（如列表、元组、字符串等）的元素顺序。 `reversed` 函数返回一个反转器对象，您可以将其转换为列表或迭代它来获取反转后的元素。

下面是使用 `reversed` 函数的示例：
```python
original_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original_list))

print(reversed_list)
```

`reverse()` 方法只能用于列表对象，不能用于其他数据结构，如元组、字符串或集合。如果你需要对其他数据结构进行类似的操作，你需要使用相应的方法或函数来实现。

需要注意的是，`reverse()` 方法会修改原始列表，如果你希望保留原始列表并创建一个反转后的副本，可以使用切片操作来完成，如 `reversed_list = my_list[::-1]`。这将创建一个新的列表，包含原始列表的元素，但按相反的顺序排列。

***



## string库

**string 模块**

Python中的 "string" 模块是一个标准库模块，用于提供字符串操作相关的功能和常量。以下是一些常见用法和示例：

1. **访问字符串常量**:

   - 获取所有大写字母:
     ```python
     import string
     uppercase_letters = string.ascii_uppercase
     ```
   - 获取所有小写字母:
     ```python
     import string
     lowercase_letters = string.ascii_lowercase
     ```

   - 获取所有数字字符:
     ```python
     import string
     digits = string.digits
     ```

   - 获取所有标点符号:
     ```python
     import string
     punctuation = string.punctuation
     ```

2. **判断字符串中是否包含特定类型的字符**:
   ```python
   import string
   
   text = "Hello, World!"
   
   # 检查字符串中是否包含数字字符
   has_digits = any(char in string.digits for char in text)

***




## 去掉最低工资和最高工资后的工资平均值
>给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
>请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。
```python
class Solution:
    def average(self, salary: List[int]) -> float:
        ax=max(salary)
        ay=min(salary)
        salary.remove(ay)
        salary.remove(ax)
        return sum(salary)/len(salary)
```

***



## 在区间范围内统计奇数数目

>给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ca = high - low
        if low %2 ==1 or high%2 == 1:
            a = ca//2
            return  a+1
        else:
            a = ca//2
            return a 
```

***



## 棒球问题

>你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。
>比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循>下述规则：
>整数 x - 表示本回合新获得分数 x
>"+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
>"D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
>"C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
>请你返回记录中所有得分的总和。

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i == "+":
                stack.append(stack[-1]+stack[-2])
            elif i =="D":
                stack.append(stack[-1]*2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        return sum(stack)
```

***



## 逆序操作

```
.strip()`清空开头和末尾的空格
`.split()
def length_of_last_word(s):
    # 使用strip()方法去除字符串两端的空格，然后使用split()方法将字符串分割成单词列表
    words = s.strip().split()

    if words:
        # 找到最后一个单词并返回其长度
        return len(words[-1])
    else:
        # 如果字符串中没有单词，返回0
        return 0
```

`word[-1]`倒着取数
```python
在Python中，world[-1]是用来获取字符串 world 中的倒数第一个字符的语法。字符串中的字符可以通过索引来访问，其中第一个字符的索引为0，第二个字符的索引为1，以此类推。倒数索引从-1开始，表示倒数第一个字符，-2表示倒数第二个字符，以此类推。

例如，如果 world 是字符串 "Hello"，那么：

world[0] 将返回 "H"，即第一个字符。
world[1] 将返回 "e"，即第二个字符。
world[-1] 将返回 "o"，即倒数第一个字符。
world[-2] 将返回 "l"，即倒数第二个字符。
在你的情况下，world[-1] 用于获取字符串中的最后一个字符，以便计算最后一个单词的长度。
```

***



## 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j]==0:
                    tmp = nums[j]
                    nums[j] =nums[j+1]
                    nums[j+1]=tmp
        n = len(nums)
        non_zero_index = 0  # 初始化非零元素应该放置的位置

        # 遍历列表
        for i in range(n):
            if nums[i] != 0:
                # 当遇到非零元素时，将它放置到非零元素应该放置的位置
                nums[non_zero_index] = nums[i]
                if non_zero_index != i:
                    # 如果非零元素的位置和当前位置不同，将当前位置设为零
                    nums[i] = 0
                non_zero_index += 1
```

## 2的次幂

> 给你一个整数 `n`，请你判断该整数是否是 2 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。
>
> 如果存在一个整数 `x` 使得 `n == 2x` ，则认为 `n` 是 2 的幂次方。

- 暴力解法---bx

  ```python
  class Solution:
      def isPowerOfTwo(self, n: int) -> bool:
          for i in range(n):
              if 2**i == n or n==1:
                  return True
          else:
              return False
  ```

  

- 官方解法1

  ```python
  class Solution:
  
      BIG = 2**30   #定义一个类级别常量
  
      def isPowerOfTwo(self, n: int) -> bool:
          return n > 0 and Solution.BIG % n == 0
  ```

- 官方解法2

  ```
  ```

  
