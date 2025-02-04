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

# default_flow_style=True
print("With default_flow_style=True:")
print(yaml.dump(data,default_flow_style=True))

# default_flow_style=False
print("\nWith default_flow_style=False:")
print(yaml.dump(data, default_flow_style=False))