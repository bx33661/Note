#实现四则运算
def operations(op, *args):
    if op == '+':
        return sum(args)
    if op == '-':
        return args[0] - sum(args[1:])
    if op == '*':
        result = 1
        for i in args:
            result *= i
        return result
    if op == '/':
        result = args[0]
        for i in args[1:]:
            result /= i
        return result
    return None

print(operations('+', 1, 2, 3, 4, 5))  # 15
print(operations('-', 1, 2, 3, 4, 5))  # -13
print(operations('*', 1, 2, 3, 4, 5))  # 120
print(operations('/', 1, 2, 3, 4, 5))  # 0.008333333333333333