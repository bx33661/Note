主要记录一下wget的命令，方便查询


>`wget` 是一个非常强大的命令行工具，用于从网络上下载文件。它支持 HTTP、HTTPS 和 FTP 协议，并且可以递归地下载整个网站。以下是关于 `wget` 的详细说明，包括其基本用法、常用选项和一些高级功能。

下载wget
```bash
# debian/ubuntu
sudo apt update
sudo apt install wget

# CentOS
sudo yum update
sudo yum install wget

#windows
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

choco install wget

# Mac

```


### 基本用法
#### 下载单个文件
```bash
wget http://example.com/file.zip
```

#### 下载文件并指定保存路径
```bash
wget -O /path/to/save/file.zip http://example.com/file.zip
```

### 常用选项

1. **指定输出文件名**
   ```bash
   wget -O output_filename http://example.com/file.zip
   ```

2. **后台下载**
   ```bash
   wget -b http://example.com/file.zip
   ```
   这会在后台下载文件，并将日志输出到 `wget-log` 文件中。

3. **显示详细输出**
   ```bash
   wget -v http://example.com/file.zip
   ```

4. **静默模式**
   ```bash
   wget -q http://example.com/file.zip
   ```

5. **继续下载**
   ```bash
   wget -c http://example.com/file.zip
   ```
   如果下载中断，可以使用 `-c` 选项继续下载。

6. **限制下载速度**
   ```bash

      ```
   限制下载速度为 200KB/s。

7. **递归下载**
   ```bash
   wget -r http://example.com/
   ```
   递归下载整个网站。

8. **限制递归深度**
   ```bash
   wget -r -l 2 http://example.com/
   ```
   递归下载深度为 2。

9. **排除某些文件**
   ```bash
   wget -r --exclude-directories=dir1,dir2 http://example.com/
   ```
   排除 `dir1` 和 `dir2` 目录。

10. **包含某些文件**
    ```bash
    wget -r --accept=jpg,gif,png http://example.com/
    ```
    仅下载 `.jpg`、`.gif` 和 `.png` 文件。

11. **使用代理**
    ```bash
    wget -e use_proxy=yes -e http_proxy=http://proxy.example.com:8080 http://example.com/file.zip
    ```
    使用代理服务器进行下载。

12. **设置超时时间**
    ```bash
    wget --timeout=10 http://example.com/file.zip
    ```
    设置超时时间为 10 秒。

### 高级功能

1. **断点续传**
   ```bash
   wget -c http://example.com/file.zip
   ```
   如果下载中断，可以使用 `-c` 选项继续下载。

2. **使用 HTTP 头**
   ```bash
   wget --header="User-Agent: Mozilla/5.0" http://example.com/file.zip
   ```
   设置自定义的 HTTP 头。

3. **下载多个文件**
   ```bash
   wget -i file_list.txt
   ```
   其中 `file_list.txt` 包含要下载的 URL 列表。

4. **限制带宽**
   ```bash
   wget --limit-rate=200k http://example.com/file.zip
   ```
   限制下载速度为 200KB/s。

5. **递归下载并转换链接**
   ```bash
   wget -r -k http://example.com/
   ```
   递归下载并转换链接，使其在本地可以正常访问。

6. **使用 HTTPS**
   ```bash
   wget https://example.com/file.zip
   ```
   支持 HTTPS 协议。

### 示例

#### 下载单个文件并指定保存路径
```bash
wget -O /home/user/downloads/file.zip http://example.com/file.zip
```

#### 递归下载整个网站并限制深度
```bash
wget -r -l 2 http://example.com/
```

#### 使用代理下载文件
```bash
wget -e use_proxy=yes -e http_proxy=http://proxy.example.com:8080 http://example.com/file.zip
```

#### 设置超时时间并限制下载速度
```bash
wget --timeout=10 --limit-rate=200k http://example.com/file.zip
```
