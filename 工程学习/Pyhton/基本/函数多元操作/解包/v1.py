def add(x,y,z):
    return x+y+z

# 解包元组
nums = (4,6,9)
print(add(*nums))  # 19

# 解包列表
nums = [4,6,9]
print(add(*nums))  # 19

# 解包字典
nums = {"x":4, "y":6, "z":9}
print(add(**nums))  # 19
