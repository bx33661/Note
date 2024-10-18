def fast_power(a, b, m):
    result = 1
    base = a

    while b > 0:
        if b % 2 == 1:  # 如果 b 的最低位为 1
            result = (result * base) % m
        base = (base * base) % m
        b //= 2  # b 右移一位

    return result

# 示例
a = 3
b = 13
m = 11
print(f"{a}^{b} mod {m} = {fast_power(a, b, m)}")
