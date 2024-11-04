# 用于合并两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [*list1, *list2]
print(list3)  # [1, 2, 3, 4, 5, 6]

list4 = list1 + list2
print(list4)  # [1, 2, 3, 4, 5, 6]

# 用于合并两个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
