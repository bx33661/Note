简单教程
https://blog.csdn.net/wuqixiufen2/article/details/140186865

### 基本用法

#### 扫描单个目标
afrog.exe -t http://example.com

#### 扫描多个目标
afrog.exe -t http://example1.com,http://example2.com

#### 从文件中读取目标
afrog.exe -T targets.txt

### 使用 PoC 文件或目录
afrog.exe -t http://example.com -P poc_file_or_directory

### 排除特定 PoC
afrog.exe -t http://example.com -ep poc1,poc2

### 输出结果

#### 生成 HTML 报告
afrog.exe -t http://example.com -o report.html

#### 生成 JSON 报告

afrog.exe -t http://example.com -j report.json

### 调整并发和速率限制

afrog.exe -t http://example.com -c 50 -rl 200

### 使用代理

afrog.exe -t http://example.com -proxy http://proxy.example.com:8080

### 调试模式

afrog.exe -t http://example.com -debug

### 示例：综合用法

假设你有一个目标列表文件 targets.txt，并且你希望排除某些 PoC，同时生成 HTML 和 JSON 报告，你可以使用以下命令：

afrog.exe -T targets.txt -ep poc1,poc2 -o report.html -j report.json -c 50 -rl 200

### 示例：使用特定 PoC 文件

假设你有一个特定的 PoC 文件 poc_file.yaml，并且你希望扫描一个目标并生成 HTML 报告，你可以使用以下命令：

afrog.exe -t http://example.com -P poc_file.yaml -o report.html

### 示例：使用代理和调试模式

假设你希望使用代理并开启调试模式，你可以使用以下命令：

afrog.exe -t http://example.com -proxy http://proxy.example.com:8080 -debug

请根据你的具体需求调整这些参数。如果你有更具体的需求或问题，请提供更多细节，我可以进一步帮助你。