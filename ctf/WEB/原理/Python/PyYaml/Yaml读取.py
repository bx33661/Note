import yaml

yaml_str = """
- Apple:
    Model: iPhone 12
    Color: Black
    Storage: 128GB
- Samsung:
    Model: Galaxy S21
    Color: Silver
    Storage: 256GB
- Xiaomi:
    Model: Mi 11
    Color: Blue
    Storage: 128GB
"""

data0 = yaml.safe_load(yaml_str)

# 从文件加载
with open('demo.yaml', 'r',encoding="utf-8") as file:
    data = yaml.safe_load(file)

print(data0)
print(data)