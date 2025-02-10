### Bytes编码

```python
a = "hello".encode()
print(list("hello"))
print(list(a))
```



可以使用以下脚本

```python
def to_bytes(content: str) -> list:
    return list(content.encode())

def from_bytes(byte_list: list) -> str:
    return bytes(byte_list).decode('utf-8')

def format_byte_list(byte_list: list) -> str:
    return f"[{','.join(map(str, byte_list))}]"


original_content = 'hello'
byte_list = to_bytes(original_content)
formatted_byte_list = format_byte_list(byte_list)
print(f"Byte list: {formatted_byte_list}")
    
decoded_content = from_bytes(byte_list)
print(f"Decoded content: {decoded_content}")

```

--->

```python
Byte list: [104,101,108,108,111]
Decoded content: hello
```

