在 Python 中，`_`、`__` 和 `__xx__` 都用于变量或方法的命名

### 1. 单下划线 `_`
- **命名惯例**：单下划线开头的变量通常用于指示“该变量是内部使用的”。
- **用途**：并没有特别的语言限制，仅作为一种命名惯例，提醒使用者该变量是内部的或不重要的。
  - 例如，在模块或类中定义 `_var` 表示这是一个内部变量，调用时不建议直接访问。
- **交互式模式下的 `_`**：在交互式模式下，单独的 `_` 代表上一次计算的结果。

### 2. 双下划线开头 `__`

> 名称改编只会在类内使用双下划线的变量或方法时发生。在类外部（例如全局变量）使用双下划线前缀并不会触发改编，且 Python 社区不鼓励在类外部使用双下划线开头的命名方式。

- **用途**：用于类中表示“名称改编”（name mangling），避免子类覆盖。例如，`__var` 会在类定义时被改编为 `_ClassName__var`。
- **作用**：可以帮助避免属性名在继承时被意外覆盖。通常用于不希望被外部或子类直接访问的私有属性或方法。

示例：
```python
class MyClass:
    def __init__(self):
        self.__private_var = 42

obj = MyClass()
print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'
print(obj._MyClass__private_var)  # 42，可以通过改编后的名字访问
```

**我的尝试：**

```python
class Phone:
    def __init__(self):
        self.__brand = 'Huawei Mete 70'
        self.__price = 8888

obj = Phone()
print(obj.__dict__)  # {'_Phone__brand': 'Huawei Mete 70', '_Phone__price': 8888}
print(obj._Phone__price)  # 8888
print(obj.__price)  # AttributeError: 'Phone' object has no attribute '__price'
print(obj.__brand)  # AttributeError: 'Phone' object has no attribute '__brand'
```

> `__dict__` 是 Python 中的一个内置属性，用于存储对象的所有可访问属性及其对应的值。这个属性以字典的形式返回对象的实例属性及它们的当前值。



### 3. 双下划线包裹 `__xx__`

- **用途**：这种命名方式用于 Python 的特殊方法或“魔术方法”。
- **作用**：它们是 Python 的内置方法，用于实现一些特殊功能，比如 `__init__` 表示初始化方法，`__str__` 表示转换为字符串的方法等。
- **不建议自己创建**：开发者不应自行创建这样的名称，以避免与 Python 内置方法冲突。

示例：
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

obj = MyClass(10)
print(obj)  # 调用 __str__ 方法，输出 "MyClass with value: 10"
```

### 总结
- `_`：用于标记内部变量，或在交互式模式中表示上一个结果。
- `__`：用于名称改编，避免属性在继承或子类化中被覆盖。
- `__xx__`：特殊方法或魔术方法，用于实现 Python 中的特殊行为和操作。

