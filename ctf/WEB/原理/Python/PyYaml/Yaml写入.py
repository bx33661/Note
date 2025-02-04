import yaml
data = {
    'name': 'Kobe',
    'age': 40,
    'address': {
        'street': 'Laker',
        'city': 'Zhengzhou'
    },
    'hobbies': ['coding', 'basketball']
}

# 写入到文件
with open('output.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

# 转换为YAML字符串
yaml_string = yaml.dump(data, default_flow_style=False)
print(yaml_string)
