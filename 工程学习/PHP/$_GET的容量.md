在PHP中，`$_GET` 是一个用于接收通过 URL 查询字符串传递的参数的全局数组，其容量主要受到以下几个因素的限制：

### **1. URL长度限制**

- **Web服务器的限制**：
    
    - 不同的 Web 服务器对 URL 长度有不同的限制。
    - **Apache**：默认支持 **8190 字节**（可以配置）。
    - **Nginx**：默认支持 **4096 字节**，可通过 `large_client_header_buffers` 配置增大。
    - **IIS**：默认支持 **2048 字节**，可通过修改注册表调整。
- **浏览器的限制**：
    
    - 浏览器对 URL 的长度也有限制。
    - 例如：
        - **Internet Explorer**：最多 2083 个字符。
        - **现代浏览器**（如 Chrome、Firefox）：支持更长的 URL，但通常不会超过 8192 个字符。

### **2. PHP 的限制**

- PHP 本身对 `$_GET` 容量没有直接限制，但以下配置可能间接影响：
    - **`max_input_vars`**（默认值：1000）：限制一次请求中可以使用的变量数（包括 `$_GET`、`$_POST` 和 `$_COOKIE`）。
    - **`memory_limit`**：脚本的最大内存使用量（间接影响 `$_GET`）。

### **3. 数据处理影响**

- 查询字符串中，每个键值对都需要分隔符（`&`、`=`）和 URL 编码（如空格被编码为 `%20`），会增加字节数。
- 实际上，`$_GET` 的容量受限于 URL 的最大长度，以及服务端处理能力。

---

### **总结**

1. **理论容量**：受 Web 服务器和浏览器 URL 长度限制，通常在 **2048 字节到 8192 字节之间**。
2. **实际容量**：受 PHP 配置的 `max_input_vars` 和服务器内存的限制。
3. **推荐实践**：避免在 `$_GET` 中传递过多数据，推荐将大数据量通过 `$_POST` 或其他方式传递。

如需调整容量，可：

1. 配置 Web 服务器以支持更长的 URL。
2. 在 `php.ini` 中调整 `max_input_vars` 和 `memory_limit`。