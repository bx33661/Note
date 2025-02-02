## `routes` 包

[TOC]

`routes` 包在 Flask 应用中主要负责组织和定义应用程序的各个路由及其对应的视图函数。

```txt
        ├── routes/          # 路由模块
        │   ├── __init__.py
        │   ├── pdf_routes.py    # PDF相关路由
        │   ├── email_routes.py  # 邮件相关路由
        │   ├── find_routes.py   # 文件查找路由
        │   ├── bs_routes.py     # Base64相关路由
        │   ├── network_routes.py # 网络工具路由
        │   └── system_monitor_routes.py # 系统监控路由
```

### `__init__.py`

该文件用于初始化蓝图，并导入其他路由模块。通过将路由模块封装为蓝图，Flask 应用可以更好地组织和管理不同功能的路由。

```python
from flask import Blueprint

# 创建一个名为 'routes' 的 Blueprint 实例
bp = Blueprint('routes', __name__)

# 导入各个子路由模块
from . import pdf_routes, email_routes, find_routes, bs_routes, system_monitor_routes

from .network_routes import bp as network_bp  # 从 network_routes 模块导入名为 bp 的 Blueprint，并重命名为 network_bp

def init_app(app):
    """
    初始化应用程序，注册各个 Blueprint
    """
    app.register_blueprint(network_bp)  # 将 network_bp Blueprint 注册到 Flask 应用中

```

在此文件中，我们创建了一个蓝图对象 `bp`，并将其他路由模块导入其中。这使得这些路由可以在应用程序的主文件（通常是 `app.py`）中注册。

### 独立的路由文件

每个路由文件定义一组相关的路由和视图函数。例如，`bs_routes.py` 文件包含与 Base64 编码和解码相关的所有路由。

#### 示例：`bs_routes.py`

```python
from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template
from utils.bs_utils import encode_base64, decode_base64

# 创建一个名为 'bs_routes' 的蓝图实例，URL 前缀为 '/base'
bp = Blueprint('bs_routes', __name__, url_prefix='/base')

# 根路由，渲染 'bs.html' 模板
@bp.route('/', methods=['GET'])
def bs_index():
    return render_template('bs.html')

# 编码路由，接受 POST 请求，返回编码后的 Base64 字符串
@bp.route('/encode', methods=['POST'])
def encode():
    data = request.json  # 获取 JSON 请求数据
    input_string = data.get('input_string', '')  # 获取 'input_string'，默认为空字符串
    if not input_string:
        flash('请输入有效的字符串进行编码')  # 显示错误消息
        return redirect(url_for('bs_routes.bs_index'))  # 重定向到根路由
    encoded_string = encode_base64(input_string)  # 编码字符串
    return jsonify({'encoded_string': encoded_string})  # 返回 JSON 响应

# 解码路由，接受 POST 请求，返回解码后的字符串
@bp.route('/decode', methods=['POST'])
def decode():
    data = request.json  # 获取 JSON 请求数据
    base64_string = data.get('base64_string', '')  # 获取 'base64_string'，默认为空字符串
    if not base64_string:
        flash('请输入有效的Base64字符串进行解码')  # 显示错误消息
        return redirect(url_for('bs_routes.bs_index'))  # 重定向到根路由
    decoded_string = decode_base64(base64_string)  # 解码 Base64 字符串
    return jsonify({'decoded_string': decoded_string})  # 返回 JSON 响应
```

#### 路由解析

- **根路由 (`/base/`)**: 渲染 `bs.html` 模板，供用户进行 Base64 编码和解码操作。
- **编码路由 (`/base/encode`)**: 处理 POST 请求，接收待编码的字符串，返回对应的 Base64 编码字符串。
- **解码路由 (`/base/decode`)**: 处理 POST 请求，接收 Base64 字符串，返回解码后的原始字符串。

#### 功能文件与工具函数

`bs_routes.py` 引用了 `utils.bs_utils` 模块中的 `encode_base64` 和 `decode_base64` 函数，这些函数负责执行 Base64 编码和解码的具体操作。

```python
# utils/bs_utils.py

import base64

def encode_base64(input_string):
    """编码字符串为 Base64"""
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_base64(base64_string):
    """解码 Base64 字符串"""
    decoded_bytes = base64.b64decode(base64_string)
    return decoded_bytes.decode('utf-8')
```

这些工具函数简洁而高效地处理了编码和解码的核心逻辑。

### 蓝图模式

Flask 中的蓝图（Blueprint）是一种将应用程序的不同组件组织在一起的机制。在上面的例子中，每个功能模块（如 Base64 编码、电子邮件相关路由等）都有一个对应的蓝图实例。通过这种方式，我们可以避免把所有的路由放到一个文件中，从而提升代码的可维护性和可扩展性。

- `bs_routes.py` 是 `base` 路由模块的蓝图，URL 前缀为 `/base`，意味着该模块内所有的路由都会以 `/base` 为前缀。
- `pdf_routes.py`、`email_routes.py` 和 `find_routes.py` 等文件也有各自独立的蓝图实例，分别处理与 PDF、邮件和搜索相关的功能。



### `network_routes`示例

**创建 Blueprint 实例：**

```python
bp = Blueprint('network_routes', __name__)
```

- 创建一个名为 `'network_routes'` 的 Blueprint，用于组织网络相关的路由。

**定义路由和视图函数：**

- **网络首页路由：**

  ```py
  @bp.route('/network/index')
  def network_index():
      return render_template('network.html')
  ```

  - 渲染 `network.html` 模板，作为网络监控的主页。

- **Ping 测试路由：**

  ```python
  @bp.route('/network/ping', methods=['POST'])
  def ping_test():
      host = request.form.get('host')
      try:
          param = '-n' if platform.system().lower() == 'windows' else '-c'
          command = ['ping', param, '4', host]
          result = subprocess.run(command, capture_output=True, text=True, timeout=10)
          return jsonify({'success': True, 'result': result.stdout})
      except Exception as e:
          return jsonify({'success': False, 'error': str(e)})
  ```

  - 接收 POST 请求，获取要 ping 的主机名或 IP。
  - 根据操作系统选择 `ping` 命令的参数（Windows 使用 `-n`，其他系统使用 `-c`）。
  - 执行 `ping` 命令并捕获输出。
  - 返回 JSON 格式的结果，包含 ping 命令的输出或错误信息。

- **端口扫描路由：**

  ```python
  @bp.route('/network/port', methods=['POST'])
  def port_scan():
      host = request.form.get('host')
      port = int(request.form.get('port'))
      try:
          sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          sock.settimeout(2)
          result = sock.connect_ex((host, port))
          sock.close()
          
          status = '开放' if result == 0 else '关闭'
          return jsonify({'success': True, 'result': f'端口 {port} 状态: {status}'})
      except Exception as e:
          return jsonify({'success': False, 'error': str(e)})
  ```

  - 接收 POST 请求，获取要扫描的主机和端口。
  - 创建一个 TCP 套接字并设置超时时间。
  - 尝试连接指定主机和端口，判断端口是否开放。
  - 返回 JSON 格式的结果，指示端口的状态或错误信息。

- **DNS 查询路由：**

  ```python
  @bp.route('/network/dns', methods=['POST'])
  def dns_lookup():
      host = request.form.get('host')
      try:
          ip = socket.gethostbyname(host)
          return jsonify({'success': True, 'result': f'域名 {host} 解析到 IP: {ip}'})
      except Exception as e:
          return jsonify({'success': False, 'error': str(e)})
  ```

  - 接收 POST 请求，获取要解析的域名。
  - 使用 `socket.gethostbyname` 执行 DNS 查询，将域名解析为 IP 地址。
  - 返回 JSON 格式的结果，包含解析后的 IP 或错误信息。

这个主要是靠json数据与前端互联

--->network_html

```javascript
<script>
// 为 Ping 测试表单添加提交事件监听器
document.getElementById('pingForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // 阻止表单的默认提交行为
    const formData = new FormData(this); // 创建 FormData 对象，包含表单中的数据
    const result = document.getElementById('pingResult'); // 获取显示结果的 HTML 元素
    
    try {
        // 使用 fetch API 发送 POST 请求到 '/network/ping' 路由
        const response = await fetch('/network/ping', {
            method: 'POST',
            body: formData // 将表单数据作为请求体
        });
        const data = await response.json(); // 解析响应数据为 JSON 格式
        
        result.style.display = 'block'; // 显示结果区域
        if (data.success) {
            result.textContent = data.result; // 显示成功返回的结果
        } else {
            result.textContent = '错误: ' + data.error; // 显示返回的错误信息
        }
    } catch (error) {
        // 捕获请求错误，显示错误信息
        result.style.display = 'block';
        result.textContent = '请求失败: ' + error;
    }
});

// 为端口扫描表单添加提交事件监听器
document.getElementById('portForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // 阻止表单的默认提交行为
    const formData = new FormData(this); // 创建 FormData 对象，包含表单中的数据
    const result = document.getElementById('portResult'); // 获取显示结果的 HTML 元素
    
    try {
        // 使用 fetch API 发送 POST 请求到 '/network/port' 路由
        const response = await fetch('/network/port', {
            method: 'POST',
            body: formData // 将表单数据作为请求体
        });
        const data = await response.json(); // 解析响应数据为 JSON 格式
        
        result.style.display = 'block'; // 显示结果区域
        if (data.success) {
            result.textContent = data.result; // 显示成功返回的结果
            result.className = 'alert alert-info'; // 为结果设置样式
        } else {
            result.textContent = '错误: ' + data.error; // 显示返回的错误信息
            result.className = 'alert alert-danger'; // 设置错误样式
        }
    } catch (error) {
        // 捕获请求错误，显示错误信息
        result.style.display = 'block';
        result.textContent = '请求失败: ' + error;
        result.className = 'alert alert-danger'; // 设置错误样式
    }
});

// 为 DNS 查询表单添加提交事件监听器
document.getElementById('dnsForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // 阻止表单的默认提交行为
    const formData = new FormData(this); // 创建 FormData 对象，包含表单中的数据
    const result = document.getElementById('dnsResult'); // 获取显示结果的 HTML 元素
    
    try {
        // 使用 fetch API 发送 POST 请求到 '/network/dns' 路由
        const response = await fetch('/network/dns', {
            method: 'POST',
            body: formData // 将表单数据作为请求体
        });
        const data = await response.json(); // 解析响应数据为 JSON 格式
        
        result.style.display = 'block'; // 显示结果区域
        if (data.success) {
            result.textContent = data.result; // 显示成功返回的结果
            result.className = 'alert alert-info'; // 为结果设置样式
        } else {
            result.textContent = '错误: ' + data.error; // 显示返回的错误信息
            result.className = 'alert alert-danger'; // 设置错误样式
        }
    } catch (error) {
        // 捕获请求错误，显示错误信息
        result.style.display = 'block';
        result.textContent = '请求失败: ' + error;
        result.className = 'alert alert-danger'; // 设置错误样式
    }
});
</script>

```



### 总结

- 每个功能模块都使用独立的蓝图进行管理。
- 通过蓝图机制，可以将不同的路由分开，提升项目结构的清晰度。
- 路由文件可以引入工具函数来处理特定的业务逻辑，保证代码的简洁和复用性。
- `__init__.py` 用于初始化和导入所有路由模块，确保它们能够被主应用程序注册。

