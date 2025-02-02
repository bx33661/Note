## app.py说明

---

> `app.py` 是Flask Web应用的主入口文件。它负责初始化和配置Flask应用，注册多个功能模块的路由蓝图，设置日志记录，定义错误处理机制。
>
> 应用集成了多个模块，提供PDF处理、邮件服务、系统监控和网络功能等。

### 注册路由

这六个主要是六个功能模块，采用蓝图开发的方案

```python
app.register_blueprint(pdf_routes.bp)
app.register_blueprint(email_routes.bp)
app.register_blueprint(find_routes.bp)
app.register_blueprint(bs_routes.bp)
app.register_blueprint(system_monitor_routes.bp)
app.register_blueprint(network_routes.bp)
```

### 全局错误处理

当应用报错`404`和`500`时候响应，最后渲染调用error.html

![image-20241206164904905](https://gitee.com/bx33661/image/raw/master/path/image-20241206164904905.png)

到时候采用模板插入错误就行

```python
# 全局错误处理
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Internal server error'), 500
```



### 跟路由

由于采用蓝图方式开发，所以这里只定义根路由就行

端口设置在5000，并且对所有网络开放

```python
# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```



### **日志配置解析**

1. **配置 RotatingFileHandler**

   ```python
   file_handler = RotatingFileHandler('logs/btools.log', maxBytes=10240, backupCount=10)
   ```

   - `RotatingFileHandler` 是 Python 标准库 `logging` 中的一种日志处理方式，适用于日志文件滚动（log rotation）。当日志文件达到一定大小时，它会被轮替（滚动）成备份文件。
   - `logs/btools.log` 指定了日志文件的路径和名称，所有的日志信息将保存在这个文件中。
   - `maxBytes=10240` 设置日志文件的最大大小为 10MB（10240 字节）。一旦文件大小超过此限制，`RotatingFileHandler` 会自动创建一个新的日志文件。
   - `backupCount=10` 设置最多保留 10 个备份文件。也就是说，最多保存 10 个滚动文件，旧的日志文件会被删除或覆盖。

2. **设置日志格式**

   ```Python
   file_handler.setFormatter(logging.Formatter(
       '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
   ))
   ```

   - `setFormatter` 方法设置日志消息的格式。这里使用了 `logging.Formatter` 来定义格式。
   - `%(asctime)s` 会输出日志记录的时间戳。
   - `%(levelname)s` 会输出日志的级别（例如：INFO、DEBUG、ERROR）。
   - `%(message)s` 会输出日志的具体消息。
   - `%(pathname)s` 输出日志记录发生的文件路径。
   - `%(lineno)d` 输出日志记录发生的行号。



具体代码如下

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from routes import pdf_routes, email_routes, find_routes, bs_routes,system_monitor_routes,network_routes
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

app = Flask(__name__)

# 从环境变量获取密钥，如果没有则使用默认值
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'bx33661')

# 配置日志
if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/btools.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('BTools startup')

# 注册路由
app.register_blueprint(pdf_routes.bp)
app.register_blueprint(email_routes.bp)
app.register_blueprint(find_routes.bp)
app.register_blueprint(bs_routes.bp)
app.register_blueprint(system_monitor_routes.bp)
app.register_blueprint(network_routes.bp)

# 全局错误处理
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Internal server error'), 500

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 启动应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

