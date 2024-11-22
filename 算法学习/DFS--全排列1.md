# 全排列

---

全排列问题是指给定一组不同元素，要求找出它们所有可能的排列方式。换句话说，全排列就是对一组元素进行重新排列，使得每一种排列都是这些元素的一个全新的顺序。

例如，对于元素集合 {1, 2, 3}，它的全排列包括 {1, 2, 3}、{1, 3, 2}、{2, 1, 3}、{2, 3, 1}、{3, 1, 2} 和 {3, 2, 1} 六种可能的排列方式。

下面是一个基于递归的经典算法来解决全排列问题：

1. 定义一个递归函数 `permute`，它接收两个参数：`nums` 表示待排列的元素列表，`result` 用于存储所有排列结果。
2. 如果 `nums` 的长度为 1，说明只有一个元素，将 `nums` 加入到 `result` 中作为一个排列结果。
3. 否则，遍历`nums`中的每个元素`num`：
   - 将 `num` 从 `nums` 中移除，并保存到一个新列表 `new_nums`。
   - 递归调用 `permute`，传入参数 `new_nums` 和 `result`。
   - 对于返回的每个排列 `p`，将 `num` 插入到 `p` 的不同位置，并将生成的新排列加入到 `result` 中。
4. 返回 `result`，即包含所有排列结果的列表。

通过递归调用，`permute` 函数会不断缩小问题的规模，直到最终处理只有一个元素的情况，然后不断回溯并构建所有可能的排列。

```python
def permute(nums):
    if len(nums) == 1:
        return [nums]

    result = []
    for i in range(len(nums)):
        num = nums[i]
        new_nums = nums[:i] + nums[i+1:]
        sub_permutations = permute(new_nums)
        for p in sub_permutations:
            result.append([num] + p)

    return result

# 示例用法
nums = [1, 2, 3]
permutations = permute(nums)
for p in permutations:
    print(p)
```

> 该示例将输出元素集合 `[1, 2, 3]` 的全排列结果。。
>



**对代码分析：**

```shell
这段代码是一个使用递归实现的全排列算法。让我们逐行进行分析：

定义了一个名为 permute 的函数，它接收一个参数 nums，表示待排列的元素列表。
在函数内部，首先检查 nums 的长度是否为 1。如果是，说明只有一个元素，直接将 nums 作为一个排列结果返回。
如果 nums 的长度大于 1，则创建一个空列表 result，用于存储所有排列结果。
使用 for 循环遍历 nums 中的每个元素，并依次将每个元素作为当前元素 num 进行处理。
在循环内部，创建一个新的列表 new_nums，通过将 num 从 nums 中移除来得到剩余的元素。
使用递归调用 permute 函数，传入参数 new_nums，以获取剩余元素的全排列结果。将返回的结果保存在变量 sub_permutations 中。
使用 for 循环遍历 sub_permutations 中的每个子排列 p。
在循环内部，将当前元素 num 插入到每个子排列 p 的不同位置，并将生成的新排列 [num] + p 添加到 result 列表中。
循环结束后，将 result 列表作为函数的返回值，即包含所有排列结果的列表。
在示例用法部分，给定一个列表 nums = [1, 2, 3]，调用 permute(nums) 函数来获取全排列结果，并将结果存储在变量 permutations 中。
最后，使用 for 循环遍历 permutations，并打印每个排列结果。

运行这段代码将输出元素集合 [1, 2, 3] 的全排列结果。

该算法利用递归和不断缩小问题规模的思想，通过不断交换元素位置和剩余元素的全排列，构建出所有可能的排列结果。
```

> 代码细节描述

```python
nums_new = num[:i] + num[i+1:]
```

*这段代码将获取余下的元素*

---

## 对“ABX”进行全排列

```python
def f(date, k):
    """
    :param date:
    :param k: 当前位置
    :return:
    """
    date = list(date)
    if k ==len(date):
        for i in range(len(date)):
            print(date[i],end="")
        print()
    for i in range(k,len(date)):
        date[i], date[k] = date[k], date[i] #试探
        f(date,k+1)
        date[i], date[k] = date[k], date[i]   #回溯

date = "ABC"
f(date,0)
```



