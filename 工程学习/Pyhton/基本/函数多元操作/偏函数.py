from functools import partial
#创建一个偏函数
int2 = partial(int, base=2)

def int_to_base(x, base):
    return int(x, base)

#把下面两种形式进行比较
print(int2('1000000'))
print(int_to_base('1000000', 2))  # 64