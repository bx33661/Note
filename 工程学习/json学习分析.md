# json学习分析

---

> JavaScript 对象表示法（JSON）是用于将结构化数据表示为 JavaScript 对象的标准格式
>
> 虽然它是基于 JavaScript 语法，但它独立于 JavaScript

## 一个初步的json解析器

### Token

```python
class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
```

### Lexer

```python
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def string(self):
        result = ""
        self.advance()  # 跳过初始的双引号
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # 跳过结束的双引号
        return result

    def number(self):
        result = ""
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        return float(result) if '.' in result else int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '"':
                value = self.string()
                return Token('STRING', value)

            if self.current_char.isdigit() or self.current_char == '-':
                value = self.number()
                return Token('NUMBER', value)

            if self.current_char == 't' and self.text[self.pos:self.pos+4] == 'true':
                self.pos += 4
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token('TRUE', True)

            if self.current_char == 'f' and self.text[self.pos:self.pos+5] == 'false':
                self.pos += 5
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token('FALSE', False)

            if self.current_char == 'n' and self.text[self.pos:self.pos+4] == 'null':
                self.pos += 4
                self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
                return Token('NULL', None)

            if self.current_char == '{':
                self.advance()
                return Token('LCURLY', '{')

            if self.current_char == '}':
                self.advance()
                return Token('RCURLY', '}')

            if self.current_char == '[':
                self.advance()
                return Token('LBRACKET', '[')

            if self.current_char == ']':
                self.advance()
                return Token('RBRACKET', ']')

            if self.current_char == ':':
                self.advance()
                return Token('COLON', ':')

            if self.current_char == ',':
                self.advance()
                return Token('COMMA', ',')

            raise Exception(f"Unexpected character: {self.current_char}")

        return Token('EOF')
```

### Parser

```python
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type}")

    def value(self):
        if self.current_token.type == 'STRING':
            token = self.current_token
            self.eat('STRING')
            return token.value
        elif self.current_token.type == 'NUMBER':
            token = self.current_token
            self.eat('NUMBER')
            return token.value
        elif self.current_token.type == 'TRUE':
            self.eat('TRUE')
            return True
        elif self.current_token.type == 'FALSE':
            self.eat('FALSE')
            return False
        elif self.current_token.type == 'NULL':
            self.eat('NULL')
            return None
        elif self.current_token.type == 'LCURLY':
            return self.object()
        elif self.current_token.type == 'LBRACKET':
            return self.array()

    def array(self):
        self.eat('LBRACKET')
        elements = []
        while self.current_token.type != 'RBRACKET':
            elements.append(self.value())
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
            else:
                break
        self.eat('RBRACKET')
        return elements

    def object(self):
        self.eat('LCURLY')
        obj = {}
        while self.current_token.type != 'RCURLY':
            key = self.current_token.value
            self.eat('STRING')
            self.eat('COLON')
            value = self.value()
            obj[key] = value
            if self.current_token.type == 'COMMA':
                self.eat('COMMA')
            else:
                break
        self.eat('RCURLY')
        return obj

    def parse(self):
        result = self.value()
        self.eat('EOF')
        return result
```



测试一个例子（就用mdn上的那个数据）

```json
{'squadName': 'Super Hero Squad', 'homeTown': 'Metro City', 'formed': 2016, 'secretBase': 'Super tower', 'active': True, 'members': [{'name': 'Molecule Man', 'age': 29, 'secretIdentity': 'Dan Jukes', 'powers': ['Radiation resistance', 'Turning tiny', 'Radiation blast']}, {'name': 'Madame Uppercut', 'age': 39, 'secretIdentity': 'Jane Wilson', 'powers': ['Million tonne punch', 'Damage resistance', 'Superhuman reflexes']}, {'name': 'Eternal Flame', 'age': 1000000, 'secretIdentity': 'Unknown', 'powers': ['Immortality', 'Heat Immunity', 'Inferno', 'Teleportation', 'Interdimensional travel']}]}
```

然后这里用json库美化一下输出结果

```python
import json
```



```python
{
    "squadName": "Super Hero Squad",
    "homeTown": "Metro City",
    "formed": 2016,
    "secretBase": "Super tower",
    "active": true,
    "members": [
        {
            "name": "Molecule Man",
            "age": 29,
            "secretIdentity": "Dan Jukes",
            "powers": [
                "Radiation resistance",
                "Turning tiny",
                "Radiation blast"
            ]
        },
        {
            "name": "Madame Uppercut",
            "age": 39,
            "secretIdentity": "Jane Wilson",
            "powers": [
                "Million tonne punch",
                "Damage resistance",
                "Superhuman reflexes"
            ]
        },
        {
            "name": "Eternal Flame",
            "age": 1000000,
            "secretIdentity": "Unknown",
            "powers": [
                "Immortality",
                "Heat Immunity",
                "Inferno",
                "Teleportation",
                "Interdimensional travel"
            ]
        }
    ]
}
```

