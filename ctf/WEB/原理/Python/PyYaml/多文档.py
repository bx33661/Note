import yaml

# 多文档字符串，用---隔开
multi_doc = """
--- # 文档1
name: dx
age: 18
---  # 文档2
name: reyna
age: 25
"""

# 读取多个文档
documents = yaml.safe_load_all(multi_doc)
for doc in documents:
    print(doc)

# 写入多个文档
docs = [
    {'name': 'dx', 'age': 30},
    {'name': 'rayna', 'age': 25}
]

with open('multi.yaml', 'w') as file:
    yaml.dump_all(docs, file, default_flow_style=False)