# Jinja2语法

---

以下是 Jinja2 模板引擎的 **全面语法指南**，包含代码示例和最佳实践：

---

### 一、基础语法结构
#### 1. 变量输出
```jinja2
{# 基本输出 #}
{{ user.name }}

{# 安全输出原始HTML（需确保内容可信） #}
{{ html_content|safe }}

{# 未定义变量处理 #}
{{ var|default('默认值') }}
```

#### 2. 注释
```jinja2
{# 单行注释 #}

{#
  多行
  注释
#}
```

#### 3. 控制结构
```jinja2
{# if判断 #}
{% if user.is_admin %}
  <p>管理员面板</p>
{% elif user.is_guest %}
  <p>游客模式</p>
{% else %}
  <p>普通用户</p>
{% endif %}

{# for循环 #}
{% for item in items %}
  <li>{{ loop.index }}. {{ item.name }}</li>
{% else %}
  <p>暂无数据</p>
{% endfor %}

{# loop变量说明 #}
loop.index0  # 当前迭代索引（从0开始）
loop.revindex  # 反向迭代索引
loop.first     # 是否是第一个元素
loop.last      # 是否是最后一个元素
```

---

### 二、模板组合
#### 1. 模板继承
```jinja2
{# base.html #}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}默认标题{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>

{# child.html #}
{% extends "base.html" %}

{% block title %}子页面标题{% endblock %}

{% block content %}
  <h1>主要内容区域</h1>
  {{ super() }}  {# 继承父模板内容 #}
{% endblock %}
```

#### 2. 包含（Include）
```jinja2
{% include 'header.html' %}
<main>主体内容</main>
{% include 'footer.html' ignore missing %}  {# 忽略模板不存在错误 #}
```

#### 3. 宏（Macro）
```jinja2
{# 定义宏 #}
{% macro input(name, type='text', value='') -%}
  <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{%- endmacro %}

{# 使用宏 #}
{{ input('username') }}
{{ input('password', type='password') }}
```

---

### 三、过滤器（Filters）
#### 1. 内置常用过滤器
```jinja2
{{ text|capitalize }}      {# 首字母大写 #}
{{ list|join(', ') }}      {# 列表转字符串 #}
{{ html|escape }}          {# HTML转义 #}
{{ value|default('N/A') }} {# 默认值 #}
{{ num|round(2) }}         {# 四舍五入 #}
{{ date|datetimeformat('%Y-%m-%d') }} {# 时间格式化 #}
```

#### 2. 链式调用
```jinja2
{{ "  HELLO WORLD  "|trim|lower }}
{# 输出："hello world" #}
```

#### 3. 自定义过滤器
```python
# Python代码注册过滤器
def reverse_filter(s):
    return s[::-1]

app.jinja_env.filters['reverse'] = reverse_filter

{# 模板中使用 #}
{{ 'abcd'|reverse }}  {# 输出：dcba #}
```

---

### 四、全局函数与变量
#### 1. 内置全局函数
```jinja2
{{ range(5)|list }}          {# 生成列表[0,1,2,3,4] #}
{{ dict(key='value') }}      {# 创建字典 #}
{{ cycler('odd', 'even') }}  {# 轮换值生成器 #}
```

#### 2. 自定义全局函数
```python
# 注册全局函数
def format_price(amount):
    return f"¥{amount:.2f}"

app.jinja_env.globals['format_price'] = format_price

{# 模板中使用 #}
{{ format_price(99.8) }}  {# 输出：¥99.80 #}
```

---

### 五、测试函数（Tests）
#### 1. 内置测试
```jinja2
{% if var is defined %}      {# 变量是否定义 #}
{% if num is even %}         {# 是否为偶数 #}
{% if str is string %}       {# 是否为字符串 #}
{% if none is none %}        {# 是否为None #}
```

#### 2. 自定义测试
```python
# 注册测试函数
def is_adult(age):
    return age >= 18

app.jinja_env.tests['adult'] = is_adult

{# 模板中使用 #}
{% if user.age is adult %}
  允许访问
{% endif %}
```

---

### 六、高级特性
#### 1. 上下文控制
```jinja2
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

#### 2. 空白控制
```jinja2
{# 去除左侧空白 #}
{%- for item in list -%}
  {{ item }}
{%- endfor %}

{# 去除右侧空白 #}
{{ value -}}
```

#### 3. 沙箱模式（安全执行）
```python
# 配置沙箱环境
from jinja2.sandbox import SandboxedEnvironment
env = SandboxedEnvironment()
```

---

### 七、安全实践
1. **自动转义配置**
```python
app.jinja_env.autoescape = True  # Flask默认开启
```

2. **手动控制转义**
```jinja2
{# 关闭自动转义区块 #}
{% autoescape false %}
  {{ raw_html }}
{% endautoescape %}

{# 手动转义 #}
{{ user_input|e }}
```

3. **禁用危险特性**
```python
# 禁用某些功能
app.jinja_env.policies.update({
    'compiler.ascii_str': True,       # 强制使用ASCII字符串
    'json.dumps_kwargs': {
        'ensure_ascii': False         # 允许非ASCII字符
    }
})
```

---

以上内容已覆盖 Jinja2 的 **核心语法要素** 和 **安全实践**，适用于 Web 开发、自动化脚本生成等多种场景。