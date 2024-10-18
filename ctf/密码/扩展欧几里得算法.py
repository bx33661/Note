import sys
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

sys.stdout.reconfigure(encoding='utf-8')
# 示例
a = 35
b = 15
gcd, x, y = extended_gcd(a, b)
print(f"对于 a = {a} 和 b = {b}:")
print(f"最大公约数 gcd = {gcd}")
print(f"x = {x}, y = {y}")
print(f"验证: {a} * {x} + {b} * {y} = {gcd}")
