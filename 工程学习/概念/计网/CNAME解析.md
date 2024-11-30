CNAME（Canonical Name）记录是一种DNS记录类型，用于将一个域名别名指向另一个“规范”的（正式的）域名。这意味着当DNS解析请求一个CNAME记录时，DNS服务器会将请求重定向到另一个域名进行解析。

### 具体例子
假设有以下两条DNS记录：
1. `www.example.com` 可能是一个CNAME记录，指向 `example.com`
2. `ftp.example.com` 可能是一个CNAME记录，指向 `example.com`

当你访问 `www.example.com` 或 `ftp.example.com` 时，DNS解析器会将这些请求解析到 `example.com`，然后继续解析实际的IP地址。

### 工作原理
1. 用户请求一个域名（如 `www.example.com`）。
2. DNS服务器看到这个域名有CNAME记录，并查找它指向的目标域名（如 `example.com`）。
3. DNS解析器继续对目标域名进行解析，最终返回IP地址。

### 特点
- **简化管理**：CNAME记录可以将多个域名指向同一个IP地址，只需维护一个目标域名的A记录或其他解析。
- **限制**：一个CNAME记录不能与其他类型的记录（如A记录、MX记录等）共存于同一域名下。
- **递归解析**：使用CNAME时，DNS解析器可能需要进行多次查询，直到最终找到目标域名的IP地址。

CNAME记录广泛用于负载均衡、域名重定向、子域名管理等场景。