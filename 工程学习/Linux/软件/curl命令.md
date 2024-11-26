`curl` 是一个用于传输数据的命令行工具，广泛应用于与各种协议（HTTP、HTTPS、FTP 等）交互。它功能强大，适用于测试、自动化脚本、调试网络请求等。

以下是关于 `curl` 的详细介绍：

---

## **基本语法**

```bash
curl [options] [URL]
```

---

## **常见功能与选项**

### 1. **发送 GET 请求**

GET 是 HTTP 请求的默认方法。

```bash
curl https://example.com
```

这会下载指定 URL 的内容并打印到终端。

---

### 2. **发送 POST 请求**

发送数据到服务器。

```bash
curl -X POST -d "key=value&key2=value2" https://example.com
```

- `-X POST`：指定 HTTP 方法为 POST。
- `-d` 或 `--data`：提供请求体数据。

如果你想发送 JSON 格式的数据：

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' https://example.com
```

---

### 3. **自定义请求头**

可以通过 `-H` 指定 HTTP 请求头。

```bash
curl -H "Authorization: Bearer <token>" https://api.example.com
```

---

### 4. **下载文件**

使用 `-O` 将文件保存为其默认文件名：

```bash
curl -O https://example.com/file.zip
```

如果要自定义文件名：

```bash
curl -o custom_name.zip https://example.com/file.zip
```

---

### 5. **上传文件**

使用 `-F` 上传文件（通常用于 multipart/form-data 表单提交）。

```bash
curl -X POST -F "file=@path/to/file" https://example.com/upload
```

---

### 6. **处理 HTTPS 请求**

如果目标服务器使用了自签名证书，`curl` 默认会报错。可以跳过 SSL 验证：

```bash
curl -k https://self-signed.example.com
```

**⚠️ 注意**：跳过验证存在安全风险，仅限测试使用。

---

### 7. **保存和恢复 Cookies**

#### 保存 Cookies 到文件：

```bash
curl -c cookies.txt https://example.com
```

#### 使用 Cookies：

```bash
curl -b cookies.txt https://example.com
```

---

### 8. **跟踪重定向**

默认情况下，`curl` 不会自动跟随 HTTP 重定向。可以用 `-L` 实现跟踪：

```bash
curl -L https://short.url
```

---

### 9. **设置超时**

- 连接超时：`--connect-timeout`
- 请求总超时：`--max-time`

```bash
curl --connect-timeout 5 --max-time 10 https://example.com
```

---

### 10. **代理设置**

通过 HTTP 代理发送请求：

```bash
curl -x http://proxy.example.com:8080 https://example.com
```

通过 SOCKS 代理发送请求：

```bash
curl --socks5-hostname 127.0.0.1:1080 https://example.com
```

---

## **一些高级功能**

### 1. **获取 HTTP 响应头**

使用 `-I` 或 `--head`：

```bash
curl -I https://example.com
```

---

### 2. **显示详细信息**

`-v` 或 `--verbose` 显示请求和响应的完整交互过程：

```bash
curl -v https://example.com
```

如果需要更详细的调试信息，可以使用 `--trace` 或 `--trace-ascii`：

```bash
curl --trace trace.log https://example.com
```

---

### 3. **并发请求**

`curl` 本身不支持直接的并发请求，但可以结合工具（如 `xargs` 或 `&`）模拟：

```bash
echo "https://example1.com https://example2.com" | xargs -n 1 -P 2 curl -O
```

`-P 2` 表示最多同时运行 2 个请求。

---

### 4. **模拟浏览器**

通过设置 `User-Agent` 模拟不同浏览器：

```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36" https://example.com
```

---

## **实战场景示例**

### 1. 测试 RESTful API

发送一个带有身份认证的 GET 请求：

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://api.example.com/data
```

### 2. 批量下载文件

结合 `bash` 脚本：

```bash
for url in https://example.com/file1 https://example.com/file2; do
    curl -O $url
done
```

### 3. 检查网站是否在线

使用 `-o` 丢弃输出，用 `-w` 格式化输出：

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.com
```

返回的 HTTP 状态码可以用于监控网站状态。

---

## **常用选项总结表**

|选项|描述|
|---|---|
|`-X`|指定请求方法（GET、POST、PUT 等）。|
|`-d`|发送请求数据。|
|`-H`|添加自定义请求头。|
|`-o/-O`|保存响应内容到文件。|
|`-I`|获取 HTTP 响应头。|
|`-L`|跟踪 HTTP 重定向。|
|`-c/-b`|保存或发送 Cookies。|
|`-k`|跳过 SSL 验证。|
|`-v`|显示详细的调试信息。|
|`--max-time`|设置总超时时间。|

如果需要更多帮助，使用 `curl --help` 查看完整的选项列表。

---
### **学习资源**
- [curl 官方文档](https://curl.se/docs/)
- [curl GitHub 仓库](https://github.com/curl/curl)