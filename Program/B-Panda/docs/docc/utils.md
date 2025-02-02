## `utils` 包

`utils` 文件夹包含了一些常用的工具函数模块，帮助实现项目的核心功能。这些工具函数被分为多个文件，每个文件专注于处理特定的业务逻辑。为了便于管理，所有的工具模块在 `__init__.py` 中进行了统一导入。

```txt
├── utils/
│   ├── __init__.py
│   ├── pdf_utils.py
│   ├── email_utils.py
│   ├── find_utils.py
│   └── bs_utils.py
```

### `__init__.py`

该文件用于将所有工具模块统一导入，使得在其他地方导入 `utils` 时，可以直接访问所有的工具函数。

```python
from .pdf_utils import *
from .email_utils import *
from .find_utils import *
from .bs_utils import *
```

### 示例：`bs_utils.py`（Base64 编码和解码）

我们以 `bs_utils.py` 为例，来看一下如何实现 Base64 编码和解码的工具函数。这个模块包括了两个函数：`encode_base64` 和 `decode_base64`，分别用于将字符串编码为 Base64 和将 Base64 字符串解码为原始字符串。

#### 1. **`encode_base64` 函数**

```python
import base64

def encode_base64(input_string):
    """
    将字符串编码为 Base64
    :param input_string: 需要编码的字符串
    :return: Base64 编码后的字符串
    """
    try:
        # 将字符串编码为字节
        byte_data = input_string.encode('utf-8')
        # 使用 base64 编码
        base64_bytes = base64.b64encode(byte_data)
        # 将字节转换回字符串
        base64_string = base64_bytes.decode('utf-8')
        return base64_string
    except Exception as e:
        return f"编码错误: {str(e)}"
```

- **功能**: 该函数将输入的字符串 `input_string` 编码为 Base64 格式。

- 实现步骤

  :

  1. 首先将字符串转换为字节。
  2. 然后使用 `base64.b64encode` 对字节数据进行编码。
  3. 最后，将编码后的字节数据解码为字符串并返回。

- **异常处理**: 如果编码过程中出现任何错误，会捕获并返回错误信息。

#### 2. **`decode_base64` 函数**

```python
def decode_base64(base64_string):
    """
    将 Base64 字符串解码为原始字符串
    :param base64_string: Base64 编码的字符串
    :return: 解码后的原始字符串
    """
    try:
        # 将 Base64 字符串编码为字节
        base64_bytes = base64_string.encode('utf-8')
        # 使用 base64 解码
        byte_data = base64.b64decode(base64_bytes)
        # 将字节转换回字符串
        decoded_string = byte_data.decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"解码错误: {str(e)}"
```

- **功能**: 该函数将 Base64 编码的字符串 `base64_string` 解码回原始字符串。
- 实现步骤:
  1. 将 Base64 字符串转换为字节。
  2. 使用 `base64.b64decode` 对字节数据进行解码。
  3. 最后，将解码后的字节数据转换为字符串并返回。
- **异常处理**: 如果解码过程中出现任何错误，同样会捕获并返回错误信息。

### 代码中的错误处理 🛠️

在这两个函数中，我们都使用了 `try-except` 语句来捕获可能的异常。这确保了函数在遇到错误时不会崩溃，而是返回一个包含错误信息的字符串：

- **编码错误**: 如果输入的数据无法正确编码为 Base64，将返回 `编码错误: <错误信息>`。
- **解码错误**: 如果输入的 Base64 字符串无效，无法正确解码，则返回 `解码错误: <错误信息>`。

### 总结 🎯

- 工具函数：

  ```
  bs_utils.py
  ```

   中提供了两个核心功能：

  - `encode_base64`：将字符串转换为 Base64 编码。
  - `decode_base64`：将 Base64 字符串解码回原始字符串。

- **异常处理**：通过 `try-except` 捕获编码或解码过程中可能出现的错误，确保函数的稳定性。

- **通用性**：这两个函数可以广泛用于需要 Base64 编码或解码的场景，例如文件上传、图片处理、数据传输等。

