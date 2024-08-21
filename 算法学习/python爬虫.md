

# python爬虫

[TOC]

# 爬取

下面学习爬取的操作



## requests库



```python
import requests

r = requests.get('http://wwww.baidu.com/')

print(type(r))
#打印类型

print(r.status_code)
#打印状态码

print(type(r.text))
#打印文本类型

print(r.text)
#打印文本

print(r.cookies)
#打印cookie
```



> ```markdown
> <class 'requests.models.Response'>
> 200
> <class 'str'>
> <!DOCTYPE html>
> <!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
> 
> <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
> 
> ```

```python
r=requests.get('http://www.httpbin.org/get')
print(r.text)
```

> ```
> {
>   "args": {}, 
>   "headers": {
>     "Accept": "*/*", 
>     "Accept-Encoding": "gzip, deflate, br", 
>     "Host": "www.httpbin.org", 
>     "User-Agent": "python-requests/2.31.0", 
>     "X-Amzn-Trace-Id": "Root=1-655484d8-5e762186147fc42a4452c282"
>   }, 
>   "origin": "202.100.214.107", 
>   "url": "http://www.httpbin.org/get"
> }
> ```



## logging库

在Python中，`logging`是一个内置的日志记录库，用于记录应用程序的日志信息。通过使用`logging`库，你可以控制日志的输出、格式化、过滤等。

以下是`logging`库的基本用法和概念：

1. **导入`logging`模块：**

   ```python
   import logging
   
   ```

### logging日志级别

- DEBUG		10
- INFO            20
- WARNING   30
- ERROR         40
- CRITIICAL     50
- 

```python
import logging
#默认的日志级别是warning，所以只有warning及以上级别的日志才会输出
logging.debug("hello world i am bx-debug")
logging.info("hello world i am bx-info")
logging.warning("hello world i am bx-warning")
logging.error("hello world i am bx-error")
logging.critical("hello world i am bx-critical")
```

> 输出结果

![image-20231115225447928](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20231115225447928.png)



**如果想要修改日志输出级别的简单操作**

```python
logging.basicConfig(level=logging.DEBUG)
```

`level`来定义最低输出等级

![image-20231115225951668](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20231115225951668.png)

```python
logging.basicConfig(filename="demo.log",filemode="w",level=logging.DEBUG)
```

---



# 分析与处理

下面学习如何分析代码



## Xpath

xpth 是lxml库的一个强大的功能

```python
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result=etree.tostring(html,encoding='utf-8').decode('utf-8')

m=html.xpath('//li/a/text()')#`text（）`提取其中的内容
print(m)

```

解析这段代码：

- `html = etree.HTML(text)`

  > 将text变量内的内容转化为html形式

- `result=etree.tostring(html,encoding='utf-8').decode('utf-8')`

> `etree.tostring(html, encoding='utf-8')`: 将 `html` 对象转换为一个包含 HTML 内容的字节序列。参数 `encoding='utf-8'` 指定了使用 UTF-8 编码。`.decode('utf-8')`: 对上一步得到的字节序列进行解码，将其转换为 UTF-8 编码的字符串。这个步骤的常见用途是为了在输出或处理时确保字符串是以 UTF-8 编码的。这在处理中文或其他非ASCII字符时很有用，因为UTF-8是一种支持多语言字符的通用编码方式。如果你希望直接使用 UTF-8 编码的字节序列而不是解码为字符串，你可以省略 `.decode('utf-8')` 部分，得到的结果将是一个 bytes 对象



```python
m=html.xpath('//li[@class="item-0"]/a/text()')
m=html.xpath('//li//@href')
```

`[@....]`来直接匹配class----->'属性匹配'

`@....`来匹配这个属性后面的东西（如`href = www.baidu.com`,输出结果就是www.baidu.com）------>'属性获取'



***

## Beautiful Soup

**一个强大的python库，用于解析html内容**

> 下载
>
> `pip3 install beautifulsoup4`

**引用方法**

```python
from bs4 import beautifulsoup
```





```python
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

#print(soup.prettify()) #--->格式化输出(缩进格式)
#print(soup.title.string)

print(soup.p.attrs) #--->获取属性
print(soup.p.attrs['name'])  #--->获取属性中的name
```





