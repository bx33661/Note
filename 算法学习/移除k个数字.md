# 移除k个数字

---

`pop()` 是 Python 列表（List）对象的一个方法，用于移除列表中的指定位置的元素，并返回该元素的值。在这个代码示例中，`pop(-1)` 表示移除列表中的最后一个元素。

```python
class Solution:
    def removeknums(self, nums, k):
        s = []
        nums = list(map(int, nums))
        
        for i in range(len(nums)):
            number = int(nums[i])
            while len(s) != 0 and s[len(s) - 1] > number and k > 0:
                s.pop(-1)
                k -= 1
            if number != 0 or len(s) != 0:
                s.append(number)
        while len(s) != 0 and k > 0:
            s.pop(-1)
            k -= 1
        result = ""

        result = ''.join(str(i) for i in s)

        return result


if __name__ == "__main__":
    S = Solution()
    print(S.removeknums("1432219", 3))
```

---

1. `removeknums` 方法接受两个参数 `nums` 和 `k`，其中 `nums` 是一个表示整数的字符串，`k` 是要移除的数字的数量。
2. 首先，定义一个空列表 `s`，用于存储最终的结果。
3. 将 `nums` 字符串转换为整数列表 `nums`。
4. 然后，通过遍历 `nums` 列表中的每个数字进行以下操作：
   - 如果 `s` 列表不为空，且当前数字小于 `s` 列表中的最后一个数字，并且 `k` 大于 0，则从 `s` 中移除最后一个数字，同时减少 `k` 的值，直到满足条件为止。
   - 如果当前数字不为 0，或者 `s` 列表不为空，则将当前数字添加到 `s` 中。
5. 在遍历完所有数字后，如果 `k` 的值仍大于 0，则继续从 `s` 中移除数字，直到 `k` 减为 0。
6. 最后，将 `s` 中的数字转换为字符串，并返回结果。

在主函数中，创建了 `Solution` 类的一个实例 `S`，并调用了 `removeknums` 方法来测试移除字符串 "1432219" 中的 2 个数字后的结果。

