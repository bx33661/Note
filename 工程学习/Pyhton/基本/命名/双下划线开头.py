class Phone:
    def __init__(self):
        self.__brand = 'Huawei Mete 70'
        self.__price = 8888

obj = Phone()
print(obj.__dict__)  # {'_Phone__brand': 'Huawei Mete 70', '_Phone__price': 8888}
print(obj._Phone__price)  # 8888
print(obj.__price)  # AttributeError: 'Phone' object has no attribute '__price'
print(obj.__brand)  # AttributeError: 'Phone' object has no attribute '__brand'
