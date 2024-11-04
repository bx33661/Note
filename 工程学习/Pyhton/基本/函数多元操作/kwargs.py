def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name="Alice", age=25, city="New York")
# 输出：
# name: Alice
# age: 25
# city: New York
