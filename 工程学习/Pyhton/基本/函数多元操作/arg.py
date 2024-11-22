def calculate_average(*grades):
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0

print(calculate_average(80, 90, 70))      # 输出：80.0
print(calculate_average(100, 95, 85, 90)) # 输出：92.5
