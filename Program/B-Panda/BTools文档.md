

## BTools文档

[[TOC]]

### 项目概述

本项目是一个基于 Flask 的 Web 应用，提供了 PDF 操作、邮件操作和文件查找功能。用户可以通过 Web 界面执行各种操作，如合并 PDF 文件、添加水印、发送定时邮件、自动回复邮件以及查找文件。

### 目录结构

```python
app/
├── app.py
├── requirements.txt
├── routes/
│   ├── __init__.py
│   ├── pdf_routes.py
│   ├── email_routes.py
│   └── find_routes.py
├── utils/
│   ├── __init__.py
│   ├── pdf_utils.py
│   ├── email_utils.py
│   └── find_utils.py
└── templates/
    ├── index.html
    ├── pdf.html
    ├── email.html
    └── find.html
```


### 依赖项

项目依赖项列在 `requirements.txt` 文件中。使用以下命令安装依赖项：

```bash
pip install -r requirements.txt
```


### 文件说明

#### `app.py`

主应用文件，包含 Flask 应用的初始化和路由注册。

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from routes import pdf_routes, email_routes, find_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 注册路由
app.register_blueprint(pdf_routes.bp)
app.register_blueprint(email_routes.bp)
app.register_blueprint(find_routes.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```


#### `requirements.txt`

列出项目所需的所有依赖包及其版本。

```plaintext
Flask==2.3.2
PyPDF2==3.0.1
reportlab==3.6.10
schedule==1.1.0
```


#### `routes/__init__.py`

初始化路由模块。

```python
from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import pdf_routes, email_routes, find_routes
```


#### `routes/pdf_routes.py`

处理 PDF 操作的路由。

```python
from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.pdf_utils import merge_pdfs, add_watermark, extract_text, split_pdf, encrypt_pdf, rotate_pdf, crop_pdf, compress_pdf, extract_pages

bp = Blueprint('pdf_routes', __name__, url_prefix='/pdf')

@bp.route('/', methods=['GET'])
def pdf_index():
    return render_template('pdf.html')

@bp.route('/', methods=['POST'])
def pdf_operations():
    action = request.form['action']
    input_file = request.files['input_file']
    output_file = request.form['output_file']
    watermark_text = request.form.get('watermark_text')
    password = request.form.get('password')
    degrees = request.form.get('degrees')
    box = request.form.get('box')
    page_range = request.form.get('page_range')
    input_folder = request.form.get('input_folder')
    output_folder = request.form.get('output_folder')

    if action == 'merge':
        if not input_folder:
            flash('合并PDF时必须提供输入文件夹')
        else:
            merge_pdfs(input_folder, output_file)
            flash('PDF文件已合并')
    elif action == 'add_watermark':
        if not watermark_text:
            flash('添加水印时必须提供水印文本')
        else:
            add_watermark(input_file.filename, output_file, watermark_text)
            flash('水印已添加')
    elif action == 'extract_text':
        extract_text(input_file.filename, output_file)
        flash('文本已提取')
    elif action == 'split':
        if not output_folder:
            flash('拆分PDF时必须提供输出文件夹')
        else:
            split_pdf(input_file.filename, output_folder)
            flash('PDF文件已拆分')
    elif action == 'encrypt':
        if not password:
            flash('加密时必须提供密码')
        else:
            encrypt_pdf(input_file.filename, output_file, password)
            flash('PDF文件已加密')
    elif action == 'rotate':
        if not degrees:
            flash('旋转时必须提供旋转角度')
        else:
            rotate_pdf(input_file.filename, output_file, int(degrees))
            flash('PDF文件已旋转')
    elif action == 'crop':
        if not box:
            flash('裁剪时必须提供边界')
        else:
            box = [float(x) for x in box.split(',')]
            crop_pdf(input_file.filename, output_file, box)
            flash('PDF文件已裁剪')
    elif action == 'compress':
        compress_pdf(input_file.filename, output_file)
        flash('PDF文件已压缩')
    elif action == 'extract_pages':
        if not page_range:
            flash('提取页面时必须提供页面范围')
        else:
            extract_pages(input_file.filename, output_file, page_range)
            flash('PDF文件的特定页面已提取')

    return redirect(url_for('pdf_routes.pdf_index'))
```


#### `routes/email_routes.py`

处理邮件操作的路由。

```python
from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.email_utils import send_weekly_report, auto_reply

bp = Blueprint('email_routes', __name__, url_prefix='/email')

@bp.route('/', methods=['GET'])
def email_index():
    return render_template('email.html')

@bp.route('/', methods=['POST'])
def email_operations():
    action = request.form['action']
    from_email = request.form['from_email']
    password = request.form['password']
    if action == 'send':
        send_email_time = request.form['send_email_time']
        # schedule.every(int(send_email_time)).minutes.do(send_weekly_report, from_email, password)
        flash('定时发送报告任务已启动')
    elif action == 'reply':
        keywords = request.form['keywords']
        reply_body = request.form['reply_body']
        # schedule.every(30).seconds.do(auto_reply, from_email, password, reply_body, keywords)
        flash('自动回复邮件任务已启动')
    return redirect(url_for('email_routes.email_index'))
```


#### `routes/find_routes.py`

处理文件查找的路由。

```python
from flask import Blueprint, request, flash, redirect, url_for, render_template
from utils.find_utils import search_files_by_name, search_files_by_content

bp = Blueprint('find_routes', __name__, url_prefix='/find')

@bp.route('/', methods=['GET'])
def find_index():
    return render_template('find.html')

@bp.route('/', methods=['POST'])
def find_files():
    directory = request.form['directory']
    keyword = request.form['keyword']
    mode = request.form.get('mode', 'name')
    output_file = request.form.get('output_file')

    if mode == 'name':
        results = search_files_by_name(directory, keyword)
    elif mode == 'content':
        results = search_files_by_content(directory, keyword)

    if results:
        flash('找到以下文件包含关键词:')
        for result in results:
            flash(result)
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for result in results:
                    f.write(result + '\n')
            flash(f"结果已保存到: {output_file}")
    else:
        flash('没有找到包含关键词的文件。')

    return redirect(url_for('find_routes.find_index'))
```


#### `utils/pdf_utils.py`

包含 PDF 操作的工具函数。

```python
import os
from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_pdfs(input_folder, output_file):
    pdf_writer = PdfWriter()
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def add_watermark(input_file, output_file, watermark_text):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    watermark_pdf = create_watermark(watermark_text)
    watermark_page = watermark_pdf.pages[0]
    for page in pdf_reader.pages:
        page.merge_page(watermark_page)
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def create_watermark(text):
    c = canvas.Canvas("watermark.pdf", pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 50)
    c.setFillColorRGB(0.5, 0.5, 0.5, 0.5)
    c.rotate(45)
    c.drawString(100, height - 100, text)
    c.save()
    return PdfReader("watermark.pdf")

def extract_text(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write(text)

def split_pdf(input_file, output_folder):
    pdf_reader = PdfReader(input_file)
    for page_num, page in enumerate(pdf_reader.pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(page)
        output_file = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
        with open(output_file, 'wb') as out:
            pdf_writer.write(out)

def encrypt_pdf(input_file, output_file, password):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    pdf_writer.encrypt(password)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def rotate_pdf(input_file, output_file, degrees):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        page.rotate(degrees)
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def crop_pdf(input_file, output_file, box):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        page.cropbox.lower_left = (box[0], box[1])
        page.cropbox.upper_right = (box[2], box[3])
        pdf_writer.add_page(page)
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def compress_pdf(input_file, output_file):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    pdf_writer.compress_content_streams()
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)

def extract_pages(input_file, output_file, page_range):
    pdf_reader = PdfReader(input_file)
    pdf_writer = PdfWriter()
    if '-' in page_range:
        start, end = map(int, page_range.split('-'))
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_reader.pages[page_num])
    else:
        page_num = int(page_range) - 1
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
```


#### `utils/email_utils.py`

包含邮件操作的工具函数。

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from datetime import datetime
import imaplib
import email

def read_report(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_email(subject, body, to_email, from_email, password):
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"发送邮件时出错: {e}")
        return False

def send_weekly_report(from_email, password):
    report_content = read_report("report.txt")
    send_email("Weekly Report", report_content, "recipient@example.com", from_email, password)

def connect_to_imap(from_email, password):
    imap_server = "imap.qq.com"
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(from_email, password)
    mail.select('inbox')
    return mail

def read_unread_emails(mail):
    status, response = mail.search(None, 'UNSEEN')
    unread_msg_nums = response[0].split()
    return unread_msg_nums

def parse_email(msg):
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            return part.get_payload(decode=True).decode('utf-8')
    return ""

def auto_reply(from_email, password, reply_body, keywords):
    mail = connect_to_imap(from_email, password)
    server = smtplib.SMTP(smtp.qq.com, 587)
    server.starttls()
    server.login(from_email, password)
    
    unread_msg_nums = read_unread_emails(mail)
    
    for e_id in unread_msg_nums:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                email_body = parse_email(msg)
                
                for keyword in keywords.split(','):
                    if keyword.strip() in email_body:
                        reply_subject = f"Re: {email_subject}"
                        send_email(reply_subject, reply_body, email_from, from_email, password)
    
    mail.logout()
    server.quit()
```


#### `utils/find_utils.py`

包含文件查找的工具函数。

```python
import os

def search_files_by_name(directory, keyword):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword in file:
                matched_files.append(os.path.join(root, file))
    return matched_files

def search_files_by_content(directory, keyword):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if keyword in f.read():
                        matched_files.append(file_path)
            except (UnicodeDecodeError, FileNotFoundError, PermissionError):
                continue
    return matched_files
```


#### `templates/index.html`

主页，包含导航链接到不同的功能页面。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>PDF和邮件自动化工具</title>
</head>
<body>
    <h1>PDF和邮件自动化工具</h1>
    <ul>
        <li><a href="{{ url_for('pdf_routes.pdf_index') }}">PDF操作</a></li>
        <li><a href="{{ url_for('email_routes.email_index') }}">邮件操作</a></li>
        <li><a href="{{ url_for('find_routes.find_index') }}">文件查找</a></li>
    </ul>
</body>
</html>
```


#### `templates/pdf.html`

PDF 操作页面。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>PDF操作</title>
</head>
<body>
    <h1>PDF操作</h1>
    <form action="/pdf/" method="post" enctype="multipart/form-data">
        <label for="action">操作类型:</label>
        <select name="action" id="action">
            <option value="merge">合并</option>
            <option value="add_watermark">添加水印</option>
            <option value="extract_text">提取文本</option>
            <option value="split">拆分</option>
            <option value="encrypt">加密</option>
            <option value="rotate">旋转</option>
            <option value="crop">裁剪</option>
            <option value="compress">压缩</option>
            <option value="extract_pages">提取页面</option>
        </select>
        <br>
        <label for="input_file">输入文件:</label>
        <input type="file" name="input_file" id="input_file">
        <br>
        <label for="output_file">输出文件:</label>
        <input type="text" name="output_file" id="output_file">
        <br>
        <label for="watermark_text">水印文本:</label>
        <input type="text" name="watermark_text" id="watermark_text">
        <br>
        <label for="password">密码:</label>
        <input type="password" name="password" id="password">
        <br>
        <label for="degrees">旋转角度:</label>
        <input type="number" name="degrees" id="degrees">
        <br>
        <label for="box">裁剪边界:</label>
        <input type="text" name="box" id="box">
        <br>
        <label for="page_range">页面范围:</label>
        <input type="text" name="page_range" id="page_range">
        <br>
        <label for="input_folder">输入文件夹:</label>
        <input type="text" name="input_folder" id="input_folder">
        <br>
        <label for="output_folder">输出文件夹:</label>
        <input type="text" name="output_folder" id="output_folder">
        <br>
        <input type="submit" value="执行操作">
    </form>
</body>
</html>
```

#### `templates/email.html`

邮件操作页面。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>邮件操作</title>
</head>
<body>
    <h1>邮件操作</h1>
    <form action="/email/" method="post">
        <label for="action">操作类型:</label>
        <select name="action" id="action">
            <option value="send">发送定时报告</option>
            <option value="reply">自动回复</option>
        </select>
        <br>
        <label for="from_email">发件人邮箱:</label>
        <input type="email" name="from_email" id="from_email" required>
        <br>
        <label for="password">密码:</label>
        <input type="password" name="password" id="password" required>
        <br>
        <div id="send_options" style="display: none;">
            <label for="send_email_time">发送间隔（分钟）:</label>
            <input type="number" name="send_email_time" id="send_email_time">
        </div>
        <div id="reply_options" style="display: none;">
            <label for="keywords">关键词:</label>
            <input type="text" name="keywords" id="keywords">
            <br>
            <label for="reply_body">回复内容:</label>
            <textarea name="reply_body" id="reply_body" rows="4" cols="50"></textarea>
        </div>
        <br>
        <input type="submit" value="执行操作">
    </form>

    <script>
        document.getElementById('action').addEventListener('change', function() {
            var sendOptions = document.getElementById('send_options');
            var replyOptions = document.getElementById('reply_options');
            if (this.value === 'send') {
                sendOptions.style.display = 'block';
                replyOptions.style.display = 'none';
            } else if (this.value === 'reply') {
                sendOptions.style.display = 'none';
                replyOptions.style.display = 'block';
            }
        });
    </script>
</body>
</html>
```



#### `templates/find.html`

文件查找页面。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>文件查找</title>
</head>
<body>
    <h1>文件查找</h1>
    <form action="/find/" method="post">
        <label for="directory">目录:</label>
        <input type="text" name="directory" id="directory" required>
        <br>
        <label for="keyword">关键词:</label>
        <input type="text" name="keyword" id="keyword" required>
        <br>
        <label for="mode">查找模式:</label>
        <select name="mode" id="mode">
            <option value="name">文件名</option>
            <option value="content">文件内容</option>
        </select>
        <br>
        <label for="output_file">输出文件:</label>
        <input type="text" name="output_file" id="output_file">
        <br>
        <input type="submit" value="查找">
    </form>
</body>
</html>
```



### 功能说明

#### PDF 操作

- **合并 PDF**: 选择一个文件夹，合并其中的所有 PDF 文件。
- **添加水印**: 上传一个 PDF 文件，添加指定的水印文本。
- **提取文本**: 上传一个 PDF 文件，提取其中的文本内容。
- **拆分 PDF**: 上传一个 PDF 文件，拆分到指定的文件夹。
- **加密 PDF**: 上传一个 PDF 文件，使用指定的密码进行加密。
- **旋转 PDF**: 上传一个 PDF 文件，旋转指定的角度。
- **裁剪 PDF**: 上传一个 PDF 文件，裁剪指定的边界。
- **压缩 PDF**: 上传一个 PDF 文件，压缩文件大小。
- **提取页面**: 上传一个 PDF 文件，提取指定的页面范围。

#### 邮件操作

- **发送定时报告**: 定时发送指定的邮件报告。
- **自动回复**: 根据关键词自动回复邮件。

#### 文件查找

- **文件名查找**: 在指定目录中查找包含关键词的文件名。
- **文件内容查找**: 在指定目录中查找包含关键词的文件内容，并可将结果保存到文件中。



### 使用方法

1. **启动应用**:
   ```bash
   python app.py
   ```

2. **访问应用**:
   打开浏览器，访问 `http://127.0.0.1:5000/`。

3. **执行操作**:
   - 选择相应的功能页面（PDF 操作、邮件操作、文件查找）。
   - 填写表单并提交，执行相应的操作。

### 注意事项

- 确保所有依赖项已正确安装。
- 邮件操作需要提供有效的邮箱地址和密码。
- 文件查找功能需要提供有效的目录路径。
